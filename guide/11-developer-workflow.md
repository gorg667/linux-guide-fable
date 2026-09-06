# Chapter 11 — Developer Workflow on Linux

This chapter is about *doing the work* once the distro is installed. Much of it is distro-agnostic by design — that's the point of Chapter 4's argument that the toolchain layer has decoupled from the base system. Where the distro matters, I say so.

## 11.1 The mental model: three layers

Think of your development machine as three layers, each with its own update cadence and its own tooling:

1. **The base system** — kernel, drivers, desktop, system libraries, terminal, shell, `git`, `ssh`, container runtime. Managed by the distro's package manager (or the image, on atomic distros). Changes rarely; when it does, it's the distro's job to keep it coherent.
2. **Your toolchains** — compilers, runtimes, SDKs, language servers, CLI utilities. Managed by *version managers* and *Homebrew*, or by Nix, or inside Distrobox/devcontainers. Changes per project. Should never be the distro's job.
3. **Your projects** — with their own declared dependencies (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, `flake.nix`, `devcontainer.json`). Managed by the project's own tooling.

The most common source of developer misery on Linux is collapsing layers 1 and 2 — `sudo apt install python3-pip` then `sudo pip install` into the system Python, or `sudo npm install -g`, or building a project against the distro's `libssl` and then wondering why it breaks after an upgrade. Keep the layers separate and the distro becomes almost irrelevant to your work.

## 11.2 Toolchains, language by language

The pattern for every language: **install the version manager once (from its upstream), let it manage every version, never use the distro's package for the language itself except as a bootstrap.** Distro packages of `python3`, `nodejs`, `go`, `rustc` exist to build the distro's own software; treat them as read-only.

| Language | Recommended manager (2026) | Notes |
|---|---|---|
| **Python** | **`uv`** (Astral) | Replaces `pip`, `venv`, `pyenv`, `pipx`, `poetry`, `pip-tools` in one fast Rust binary. `uv python install 3.12 3.14`, `uv venv`, `uv run`, `uv tool install ruff`. The 2024–2026 consensus; nothing else is close. Never `pip install` into system Python (PEP 668 will stop you on modern distros anyway). |
| **Node.js** | **`fnm`** or **`volta`** (or `mise`) | Both fast, respect `.nvmrc`/`package.json#engines`. `nvm` works but is slow (shell-function based). Corepack for `pnpm`/`yarn`. |
| **Rust** | **`rustup`** | The only way. `rustup toolchain install stable nightly`, per-project `rust-toolchain.toml`. Distro `rustc` is for building distro packages. |
| **Go** | Official tarball to `/usr/local/go` or `~/go`, **`mise`**, or the distro package | Go's toolchain is self-contained and versioned per-module (`go.mod` `toolchain` directive downloads what's needed). Distro packages are usually fine here. |
| **JVM (Java/Kotlin/Scala)** | **SDKMAN!** or **`mise`** | Multiple JDK vendors (Temurin, GraalVM, Zulu, Corretto) and versions side by side. `jenv` also fine. |
| **.NET** | Microsoft's `dotnet-install.sh` or distro package (`dotnet-sdk-9.0` etc. — Microsoft ships repos for Ubuntu/Debian/Fedora/RHEL) | Ubuntu/Fedora package it natively; fine either way. |
| **Ruby** | **`mise`**, `rbenv` + `ruby-build`, or `chruby` | `rvm` is legacy. |
| **PHP** | distro package for CLI + Docker for apps; `phpenv`/`mise` for multi-version | |
| **Haskell** | **`ghcup`** | Manages GHC, cabal, stack, HLS. |
| **OCaml** | **`opam`** | Switches per project. |
| **Elixir/Erlang** | **`mise`** (via asdf plugins) or `kerl`/`kiex` | |
| **C/C++** | distro `gcc`/`clang` + **CMake** + **Ninja**; `conan`/`vcpkg` for libraries; multiple compiler versions via distro (`gcc-14`, `clang-18`) or Distrobox | The one place the distro's compiler *is* your toolchain by default. On an LTS, newer compilers come via `apt install gcc-15` (Ubuntu toolchain PPA), `dnf install gcc-toolset`, or a container. |
| **Zig** | `zigup`, `mise`, or the tarball | |
| **Polyglot** | **`mise`** (successor to `asdf`, Rust, fast, reads `.tool-versions` and `.mise.toml`, also manages env vars and tasks) | If you juggle many languages, `mise` alone can replace most of the above. |

**Homebrew on Linux** deserves separate mention. Installed to `/home/linuxbrew/.linuxbrew`, it provides thousands of current CLI tools — `ripgrep`, `fd`, `bat`, `eza`, `fzf`, `zoxide`, `lazygit`, `gh`, `jq`, `yq`, `k9s`, `helm`, `terraform`, `neovim` — independent of the distro and identical to macOS. It's the answer to "my LTS has a two-year-old `neovim`." Bluefin ships it by default; anyone can install it. Downsides: it duplicates libraries the distro already has (disk), and a few formulae assume macOS quirks. Distro packages are still preferable for anything that integrates with the system (shells, terminals, `git`, `ssh`).

## 11.3 Containers

**Docker vs. Podman.** Both run OCI containers; both use the same images and the same `Dockerfile`s; both support Compose (`docker compose` / `podman compose` or `podman-compose`). Differences that matter:

- **Docker** — the daemon model (`dockerd` as root; users in the `docker` group have effective root), the reference implementation everyone's docs assume, Docker Desktop *not needed on Linux* (the engine is native and faster than on macOS/Windows). Rootless Docker exists and works. Install from **Docker's own repo**, not the distro's (Ubuntu's `docker.io` package lags and Fedora's `moby-engine` is fine but behind). Debian/Ubuntu/Arch users usually pick Docker.
- **Podman** — daemonless, rootless by default (each container runs as your user via user namespaces), Docker-CLI-compatible (`alias docker=podman` works for 95% of cases), generates systemd units (Quadlet) for services, and is the default on Fedora/RHEL and the atomic distros. Some tools that talk to the Docker socket (Testcontainers, some IDE integrations, some CI runners) need `podman system service` and `DOCKER_HOST` set, or the `podman-docker` compatibility package. Fedora users usually pick Podman.

Either is fine. If your team uses Docker, use Docker. If you're on Fedora/atomic, Podman is smoother. Bluefin DX ships both.

**Local Kubernetes.** `kind` (Kubernetes in Docker/Podman — fastest, most common), `minikube` (VM- or container-based, more features), `k3s`/`k3d` (lightweight real distribution), or Podman's `kube play` for single-manifest testing. All distro-agnostic.

**Distrobox** (and Fedora's **Toolbox**) — covered in Chapter 4. For developers it's the tool that makes the distro choice nearly irrelevant: `distrobox create -i ubuntu:24.04 -n dept` gives you the department's exact Ubuntu with your `$HOME` mounted; `distrobox create -i archlinux -n arch` gives you the AUR on Fedora; `distrobox-export --app code` puts a container's app in your host menu. On atomic distros it's the *primary* way to install CLI tools. Chapter 12 shows the student use case.

**Devcontainers.** A `.devcontainer/devcontainer.json` in the repo declares the image, features (Node, Python, Docker-in-Docker…), extensions and post-create commands. VS Code (Dev Containers extension), JetBrains (Gateway/native), the `devcontainer` CLI, and DevPod all build and attach to it. Onboarding becomes `git clone` + "Reopen in Container." The laptop's distro is irrelevant to the project's build. Strongly recommended for any team project.

## 11.4 Virtual machines

You'll want a VM for: OS-course kernels (QEMU, see Chapter 12), testing installers and other distros, Windows for the occasional tool, and isolating dodgy software.

- **KVM/QEMU + libvirt** — the native Linux hypervisor, in the kernel, fastest, most capable. Front-ends: **virt-manager** (full-featured, slightly dated UI), **GNOME Boxes** (simple, good for "just give me a Windows/Ubuntu VM"), **Cockpit Machines** (web UI), `quickemu` (scripted downloads of Windows/macOS/many Linux ISOs — genuinely convenient). Windows 11 guests work well with virtio drivers and a TPM emulator (`swtpm`). GPU passthrough (VFIO) for gaming VMs is a hobby unto itself. **This is what you should use.**
- **VirtualBox** — familiar from Windows/macOS, works on Linux, but needs out-of-tree kernel modules (DKMS — breaks on new kernels), is slower than KVM, and is essentially impossible on atomic distros. Use only if a course mandates `.ova` appliances (you can convert them: `qemu-img convert`).
- **VMware Workstation** — free for personal use since 2024, out-of-tree modules, similar caveats.
- **Vagrant** — works with libvirt via `vagrant-libvirt`; the VirtualBox provider is the default in many tutorials, so expect to add `--provider=libvirt`.

Enable nested virtualization if you'll run VMs inside VMs (Android emulator inside a VM, etc.). Add yourself to the `libvirt` and `kvm` groups.

## 11.5 Editors and IDEs

All the major editors are first-class on Linux. Installation channel matters more than distro:

| Editor | Best install channel | Notes |
|---|---|---|
| **VS Code** | Microsoft's `.deb`/`.rpm` repo (adds itself on first install), or AUR `visual-studio-code-bin` | Flatpak and Snap versions work but sandbox the integrated terminal and hide host toolchains/Docker socket — avoid unless on an atomic distro (where Bluefin DX puts it in the image instead). **VSCodium** if you want it without telemetry (loses the marketplace by default; Open VSX instead). |
| **Cursor / Windsurf / other VS Code forks** | AppImage or `.deb` from the vendor | Same sandbox caveats if you find a Flatpak. |
| **JetBrains** (IntelliJ, PyCharm, CLion, GoLand, Rider, RustRover…) | **JetBrains Toolbox** app (manages installs/updates in `~/.local/share/JetBrains/Toolbox`) | Distro-agnostic, per-user, no root. Flatpaks exist with the usual sandbox caveats. Increase `fs.inotify.max_user_watches` (the Toolbox prompts you). |
| **Neovim** | distro package if ≥ 0.10, else Homebrew/AppImage/`bob` | Distro versions on LTS lag; Arch/Fedora/Homebrew are current. LazyVim, AstroNvim, NvChad, kickstart.nvim for configs. |
| **Emacs** | distro package (29/30 fine everywhere) | Doom Emacs, Spacemacs. `emacs-pgtk` for native Wayland. |
| **Helix** | distro package or Homebrew | Modal, batteries-included, Rust. |
| **Zed** | official Linux build (`curl | sh` installer) or Flatpak or AUR | Native Linux since 2024, Wayland-native, fast; collaboration features. |
| **Android Studio** | Google's tarball, Flatpak, AUR, or JetBrains Toolbox | Needs `/dev/kvm` access for the emulator (`kvm` group). |
| **Eclipse** | Eclipse Installer or Flatpak | Some university courses still mandate it; works. |
| **Vim/nano** | there already | |

**Wayland note for Electron apps** (VS Code, Cursor, Slack, Discord, Obsidian…): they run under Xwayland by default and can look blurry at fractional scaling. Add `--ozone-platform-hint=auto` (or `--enable-features=UseOzonePlatform --ozone-platform=wayland`) to the `.desktop` file or `~/.config/code-flags.conf` (Arch's package reads this) to run natively. Most distros' packages have started doing this by default in 2025–2026.

*(Continued: terminals, shells, dotfiles, SSH/GPG, distro cheat-sheet, and the honest WSL/macOS comparison.)*
