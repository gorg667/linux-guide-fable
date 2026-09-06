# Chapter 4 — Release Models and Package Management, In Depth

Chapter 2 introduced the taxonomy. This chapter examines each model as it is actually lived: what "stable" and "rolling" mean on a Tuesday afternoon, what really breaks and how often, and how the modern developer-tooling layer has changed the calculus. It ends with the package-manager and universal-format comparisons and a section on the specific misery that is out-of-tree kernel modules.

## 4.1 Point releases, lived

### The promise

A point-release distribution freezes a set of package versions, tests them together for weeks or months, releases, and then changes *only* to fix bugs and security holes. The Firefox you have in month one is the same *major branch* as the Firefox you have in month eighteen (browsers are the usual exception — they get full version bumps because security fixes aren't backported to old branches). Your `gcc`, your `python3`, your kernel, your GNOME — all pinned.

The benefit is that **nothing changes under you**. A script that worked in January works in December. A tutorial written for your release works for the release's whole life. Your muscle memory of where settings live doesn't rot.

### The cost: staleness, quantified

How stale? It depends on where in the cycle you are and how long the cycle is. Concretely, in September 2026:

| Distro / release | Released | Kernel | GCC | Python | GNOME / Plasma | Mesa |
|---|---|---|---|---|---|---|
| Debian 13 "Trixie" | Aug 2025 | 6.12 | 14 | 3.13 | 48 / 6.3 | 25.0 |
| Ubuntu 24.04 LTS | Apr 2024 | 6.8 (HWE → 6.14) | 13 | 3.12 | 46 / 5.27 | 24.0 (HWE newer) |
| Ubuntu 26.04 LTS | Apr 2026 | 7.0 | 15 | 3.14 | 50 / 6.5 | 26.0 |
| Fedora 44 | Apr 2026 | 7.0 → 7.2 (rebased) | 16 | 3.14 | 50 / 6.5→6.6 | 26.x (updated) |
| Arch / Tumbleweed | rolling | 7.2 | 16 | 3.14 | 50 / 6.7 | 26.2 |

(Versions approximate; the point is the *pattern*.)

Two observations:

1. **A fresh LTS is nearly as current as a rolling distro** for about three months. Ubuntu 26.04 in May 2026 was within a hair of Arch. By April 2028, when 28.04 arrives, it will be two years behind on everything except the kernel (HWE) and browsers.
2. **Fedora is the interesting middle.** It releases every six months *and* rebases the kernel to new stable versions throughout a release's life (Fedora 44 shipped 7.0 and moved to 7.1, then 7.2). It also updates Mesa and takes new minor versions of Plasma. Only GNOME is held at the release's major version. This makes Fedora "semi-rolling" in practice: fresh enough for new hardware, frozen enough for a stable desktop.

### What staleness actually costs a developer

Less than it used to, for three reasons:

- **Language version managers** give you any Python/Node/Rust/Go/Java version regardless of what `apt` offers. You should be using them anyway to match project requirements.
- **Containers and Distrobox** give you any distro's userland when a build needs a newer `cmake` or `clang`.
- **Flatpak** gives you current GUI apps (OBS, GIMP, Blender, IDEs) on an old base.

What it *still* costs:

- **Kernel and Mesa** for new hardware and new GPU features. Ubuntu's HWE kernels help (24.04 rolled from 6.8 to 6.14 over its life); Debian's backports help less; enterprise clones don't bother.
- **System libraries** that pre-built binaries link against — chiefly `glibc`. A binary built on a newer distro may refuse to run on an old LTS with `GLIBC_2.39 not found`. This bites people who download tools from GitHub releases. Debian 13/Ubuntu 26.04 are new enough that this is rare for the next year or two; it becomes a real annoyance in the final two years of an LTS.
- **Desktop features.** GNOME 46 (Ubuntu 24.04) vs. GNOME 50 (26.04) is a meaningful jump in HDR, fractional scaling, VRR and accessibility. If you care, a two-year-old desktop feels two years old.
- **Bugs that were fixed upstream a year ago but not backported.** Every LTS user eventually hits one of these. Ubuntu's SRU process and Debian's stable updates are conservative by design.

### The upgrade cliff

Point-release distros defer change; they don't eliminate it. Every N months or years you face a *major upgrade* — a big bang where thousands of packages change at once. Experiences:

- **Fedora:** `dnf system-upgrade` (or GNOME Software's one-click). Twice a year. Robust for over a decade; the Fedora community treats upgrade breakage as a blocker bug. Typically 20–40 minutes. Most users upgrade every release or every other (each release is supported ~13 months, so skipping one is fine).
- **Ubuntu LTS → LTS:** `do-release-upgrade`. Every two years. Generally works; PPAs and third-party repos are disabled and must be re-enabled; snaps carry over. Historically messier than Fedora's, largely because Ubuntu users accumulate more third-party cruft over five years. Many experienced users prefer a clean reinstall at LTS boundaries — it's a 45-minute job if `$HOME` is on its own partition or backed up.
- **Debian stable → stable:** edit `sources.list`, `apt full-upgrade`. Every ~2 years. Excellent track record; Debian's release notes are meticulous about what needs manual attention.
- **Linux Mint:** the "Upgrade Tool" handles point (22.1→22.2) upgrades trivially; major (22→23) upgrades are supported via the tool but Mint's team is candid that a clean install is cleaner.
- **openSUSE Leap:** `zypper dup` with repo changes. Works; Leap 15→16 was a bigger jump than usual because of the rebase onto the SLE 16 codebase.

The upgrade cliff is the hidden maintenance cost of point releases. It's *bursty* rather than continuous — an hour every six months (Fedora) or an afternoon every two years (LTS) — which many people prefer to the rolling model's steady trickle.

## 4.2 Rolling releases, lived

### The promise

New upstream releases flow into the repository after a brief testing period. Arch's is short (typically hours to a few days in `testing`); Tumbleweed's is longer and automated (every snapshot passes openQA's integration test suite before publication). There are no versions to upgrade between; you just update, and you're always current.

The benefit is obvious: **newest kernel, newest drivers, newest compilers, newest desktop**, all the time. The AUR adds *everything else*, also current.

### What "unstable" really means

Arch is famous for being "unstable." This is true in the technical sense (the software changes constantly) and mostly false in the colloquial sense (things break all the time). The realistic experience for a well-maintained Arch install in 2025–2026:

- **Routine:** `pacman -Syu` (or `paru`) daily or weekly; 30 seconds to 5 minutes; nothing happens.
- **Occasionally (several times a year):** a `.pacnew` file appears for a config you edited, and you should merge it. Some AUR package needs a rebuild because a library bumped its soname. A GNOME or Plasma major version arrives and an extension/widget you use stops working until its author updates it.
- **Rarely (once or twice a year):** something needs **manual intervention**, announced on the [Arch news feed](https://archlinux.org/news/). Examples from the last year: the NVIDIA 590 driver dropping Pascal support (December 2025 — users of GTX 10xx cards had to switch to the `nvidia-580xx-dkms` legacy package or lose their display), a package rename requiring `pacman` to be told about the conflict, a filesystem-layout change. **If you read the news before updating — the `informant` AUR package forces you to — you'll never be surprised.** If you don't, you will eventually be.
- **Very rarely:** an actual bug ships. It gets fixed within hours to days. If it affects boot, you use the fallback initramfs or an LTS kernel, or roll back with `downgrade`/a Btrfs snapshot.

The honest summary: **Arch breaks about as often as an LTS hits an unfixed backport bug — but Arch's breakage is visible and attributable to a specific update, while the LTS's is silent and permanent.** Whether that's better depends on your temperament.

Tumbleweed's openQA gate makes actual regressions rarer still; the trade-off is that big transitions (a new GNOME) sometimes take a week or two longer to land while openQA is satisfied.

### The real cost: attention

Rolling releases don't demand more *skill* than point releases. They demand more *attention*. You must update regularly (letting an Arch install sit for six months and then updating is the classic recipe for pain — partial upgrades are unsupported, and the keyring may have rotated). You must read the news. You must notice `.pacnew` files. You must accept that your desktop will occasionally change appearance or behaviour without your asking.

If that attention is a hobby to you, the cost is zero. If it's a tax, it adds up — I'd estimate 10–20 hours a year for an average Arch desktop user who's paying attention, versus 2–5 hours for a Fedora user and 1–3 for an Ubuntu LTS user (excluding the biennial upgrade). Those are rough, personal estimates; your mileage varies with hardware (NVIDIA doubles them) and how many AUR packages you maintain.

### Curated rolling: the compromise that mostly works

**Manjaro** holds Arch packages in its own repos for about two weeks of extra testing. This sounds ideal and is Manjaro's main selling point. The catch is *partial* delay: the AUR is built against current Arch, so AUR packages regularly break on Manjaro's two-week-old libraries — the exact opposite of the intended stability. Manjaro also has a history of self-inflicted problems (expired SSL certificates several times, a DDoS'd AUR incident, team governance drama). It has improved and remains popular, but among experienced users it's the Arch derivative with the worst reputation, and for a good reason: it takes on the risks of rolling without fully delivering the benefits.

**openSUSE Slowroll** snapshots Tumbleweed monthly-ish (plus security fixes). Since it's the same repository frozen, not a separately built one, it avoids Manjaro's AUR-mismatch problem (openSUSE's OBS is per-distro). It's the most sensible "slower rolling" option, though still officially experimental-ish.

**CachyOS** is *not* slower than Arch — it tracks Arch in near-real-time — but adds its own repos with x86-64-v3/v4-optimised rebuilds of the core packages, a patched kernel with the BORE scheduler and other tweaks, and a very good Calamares installer with sane defaults (Btrfs + Snapper snapshots, zram, `paru` pre-installed, Limine or GRUB with snapshot boot entries). It is not "Arch made stable." It is "Arch installed and tuned the way a knowledgeable enthusiast would do it," and its popularity (top of DistroWatch since 2025, the fastest-growing distro in Steam's survey) reflects how many people want exactly that. The x86-64-v3 packages are a measurable but modest win (a few percent in CPU-bound workloads, more in some codecs and compression).

**EndeavourOS** is Arch with a friendly installer, a welcome app, and a handful of sensible defaults, tracking Arch's repos directly. It's the "just install Arch for me and get out of the way" option. Excellent community forum.

## 4.3 Atomic / image-based, lived

### The promise

Your operating system is a single, versioned, read-only image. Updating means downloading the next image and rebooting into it. If the new image doesn't boot or something's wrong, you select the previous one from the boot menu — instant, guaranteed rollback. The base OS is *identical* on every machine running the same image, so bugs are reproducible and the maintainers test what you run.

The implementations:

- **Fedora Atomic Desktops** (Silverblue = GNOME, Kinoite = KDE, Sway Atomic, Budgie Atomic). Built on **rpm-ostree**, transitioning to **bootc** (the OS image is literally an OCI container image you can `podman pull`). Fedora's release cadence; six-month rebases.
- **Universal Blue** — a community project building custom bootc images on top of Fedora Atomic, with the proprietary bits (codecs, NVIDIA drivers, extra firmware) baked in and opinionated defaults. **Bluefin** (GNOME, developer-oriented; **Bluefin DX** adds VS Code, Docker, the JetBrains toolbox and more into the image), **Aurora** (KDE, same idea; Aurora DX), **Bazzite** (gaming: Steam, Proton, controller support, HDR tweaks; also a superb general desktop). Images rebuild daily; you get *tested* updates automatically in the background; a "Bluefin LTS" on a CentOS Stream base exists for people who want an even slower cadence. Universal Blue's insight is that image-based distros let a small team ship a *complete, integrated* system without any of the "install these six things after installing" rituals.
- **openSUSE Aeon** (GNOME) and **Kalpa** (KDE). Built on Tumbleweed with a transactional-update, read-only-root model plus Btrfs snapshots. Rolling base, atomic updates.
- **Vanilla OS** (Orchid). Debian-based; the `apx` tool manages Distrobox containers for any package manager; ABRoot dual-partition atomic updates.
- **NixOS** is atomic *and* declarative — every rebuild is a new bootable generation.

### The friction points, honestly

Atomic desktops are the future for a lot of people, and the Universal Blue images in particular are good enough to recommend broadly. But the model has real friction that advocates gloss over:

1. **You cannot `dnf install` things into the base.** Well, you can *layer* an RPM (`rpm-ostree install foo`), but each layered package makes updates slower and is discouraged. The intended workflow is: GUI apps → Flatpak; CLI dev tools → Homebrew (Bluefin ships it) or a Distrobox container; language toolchains → version managers or containers; things that must be on the host (a VPN client, a kernel module, a udev rule) → layer or, better, build your own image. This is *fine* once you internalise it and *maddening* if you fight it. Many tutorials assume you can just install a package on the host; on an atomic system you must translate.
2. **Kernel modules are hard.** Anything DKMS — a proprietary driver not in the image, VirtualBox, some VPNs — either needs to be in the image (Universal Blue bakes in NVIDIA, v4l2loopback, some others) or you're building a custom image. VirtualBox is the classic casualty; use KVM/virt-manager or GNOME Boxes instead (better anyway).
3. **`/usr` is read-only, `/etc` is a merged overlay, `/opt` and `/usr/local` are symlinks into `/var`.** Software that wants to install into `/usr/local` or `/opt` (some vendor installers) needs coaxing.
4. **Layering + rebases occasionally conflict.** Layered packages can block an image update if their dependencies change. Fedora's tooling has improved here but it's not zero-friction.
5. **Some development tools assume they own the host.** Docker Desktop's Linux build, some kernel-tracing tools, `perf`, certain security tools. Bluefin DX handles Docker/Podman well; other cases need thought.
6. **Debugging is different.** You can't just `apt-get source` and patch something on the host. You *can* build a derived image with your patch (Universal Blue makes this a GitHub Actions template), which is arguably better — but it's a different mental model.

For an **engineer whose work lives in containers, a browser, and an IDE**, and a **daily driver who wants zero maintenance**, atomic is a very strong fit. For a **systems programmer who hacks on the kernel, drivers, or low-level tooling**, or a **student in an OS course** who needs to install odd toolchains on the host, it adds a layer of translation that may not be worth it — a conventional distro with Btrfs snapshots delivers most of the rollback benefit with none of the friction.

## 4.4 Declarative: NixOS, lived

### The promise

Your entire system — packages, kernel, services, users, config files, desktop settings (via Home Manager), even the partition layout (via Disko) — is described in Nix language files, ideally in a git repository. `nixos-rebuild switch` makes the machine match the description. Every rebuild creates a new *generation*; all previous generations are bootable from the menu. Delete the config lines for a package and it's gone — completely, with no orphaned files. Copy your repo to a new laptop, run one command, and you have *your machine*, exactly.

Beyond system configuration, **nixpkgs** is the largest and one of the freshest package collections in existence, and **Nix development shells** (`nix develop`, or `direnv` + `nix-direnv`) give every project its own precise toolchain — the right `gcc`, `python`, `nodejs`, `postgresql` — activated on `cd`, with zero global pollution. For a developer, this last feature is arguably the killer app, and you can use Nix-the-package-manager on *any* distro (or macOS) to get it without committing to NixOS-the-distro.

### The cost

- **You must learn Nix**, a lazy, functional, dynamically typed language with some sharp edges and error messages that have improved but remain cryptic. Two to four weekends to become functional; months to become fluent.
- **Documentation is fragmented.** The official manual, the wiki (community-maintained, now at wiki.nixos.org after a fork of the older unofficial one), Zero to Nix, nix.dev, blog posts and Discourse — you'll consult all of them. The **flakes** feature has been "experimental" for years yet is the de facto standard, which confuses newcomers who see two ways to do everything.
- **It does not follow the FHS.** Nothing lives in `/usr/bin` or `/lib`. Pre-built binaries you download (many CLI tools from GitHub releases, some proprietary software, VS Code's remote server, Python wheels with bundled native libraries) fail with "No such file or directory" because the dynamic linker isn't where they expect. Fixes exist — `nix-ld`, `steam-run`, `buildFHSEnv`, `patchelf` — but every one is a papercut you didn't have elsewhere. This is the number-one practical complaint from developers on NixOS.
- **Community turbulence.** 2024 saw a governance crisis (sponsorship disputes, moderation conflicts, the founder stepping back, several prominent contributors leaving; forks like Lix and Aux emerged). The project has since put a steering committee in place and stabilised, but it's fair to note that NixOS's governance has been rockier than most.
- **Rebuilds can be slow**, especially with Home Manager and many packages; the binary cache helps enormously, but anything with an overlay or override compiles locally.

### When it pays off

- You manage **more than one machine** and want them identical.
- You want **reproducible dev environments** at a level Docker doesn't reach (Docker is reproducible at the image layer; Nix is reproducible at the build-input level).
- You **enjoy** this kind of thing and will treat the learning as an investment. Many who make it through the curve report they can't go back; many who don't report it as the most frustrating month of their computing life.
- You're okay with your friends not being able to help you.

Middle path, strongly recommended for the curious: **use Nix on a conventional distro** for development shells and Home Manager for dotfiles, then decide about NixOS proper after six months.

## 4.5 Package managers, compared

Ergonomics for common operations. Every one of these is perfectly usable; this table is for muscle-memory translation and to show that the differences are cosmetic.

| Task | apt (Debian/Ubuntu) | dnf (Fedora) | pacman (Arch) | zypper (openSUSE) | nix (NixOS) |
|---|---|---|---|---|---|
| Update repo index + upgrade all | `sudo apt update && sudo apt upgrade` | `sudo dnf upgrade` | `sudo pacman -Syu` | `sudo zypper dup` (TW) / `zypper up` (Leap) | `sudo nixos-rebuild switch --upgrade` |
| Install | `sudo apt install foo` | `sudo dnf install foo` | `sudo pacman -S foo` | `sudo zypper in foo` | add to config, rebuild (or `nix profile install nixpkgs#foo`) |
| Remove (+ unneeded deps) | `sudo apt autoremove --purge foo` | `sudo dnf remove foo` | `sudo pacman -Rns foo` | `sudo zypper rm -u foo` | remove from config, rebuild |
| Search | `apt search foo` | `dnf search foo` | `pacman -Ss foo` | `zypper se foo` | `nix search nixpkgs foo` |
| Which package owns a file | `dpkg -S /path` | `dnf provides /path` | `pacman -Qo /path` | `zypper se --provides /path` | (`nix-locate`, via nix-index) |
| List files in package | `dpkg -L foo` | `dnf repoquery -l foo` | `pacman -Ql foo` | `rpm -ql foo` | `ls $(nix path-info nixpkgs#foo)` |
| Transaction history / undo | `apt history-list` / `apt history-undo N` (3.2+) | `dnf history` / `dnf history undo N` | none built-in; use snapshots or `downgrade` | `zypper` has none; use Snapper snapshots | `nixos-rebuild switch --rollback`; boot any generation |
| Community repo | PPAs (`add-apt-repository`) | COPR (`dnf copr enable`) | AUR (via `paru`/`yay`) | OBS (`zypper ar`) | overlays / flake inputs |
| Speed | good | good (dnf5) | very fast | okay | slow to evaluate, fast to switch |

Notes:

- **`apt`** gained history/undo/rollback in 3.2 (Ubuntu 26.04) — a big quality-of-life improvement that closes a long-standing gap with `dnf`.
- **`dnf5`** (Fedora 41+) is a rewrite in C++ that is much faster than the old Python `dnf` and has excellent history/rollback.
- **`pacman`** is fast partly because it does less (no history, no delta updates). The convention on Arch is that snapshots (Snapper/Timeshift on Btrfs) are your undo. CachyOS and EndeavourOS set this up for you; vanilla Arch leaves it to you.
- **AUR helpers** (`paru`, `yay`) wrap `pacman` and build AUR packages. Remember AUR packages are *build scripts submitted by users*; the helpers show you the PKGBUILD diff before building. Read it, at least skim it. Also remember that AUR packages are unsupported by Arch itself — if an update breaks one, that's between you and the AUR maintainer.
- **`zypper`** is verbose and slower but very explicit about what it's doing; openSUSE users generally like it. `zypper dup` (distribution upgrade) is the correct daily command on Tumbleweed, not `up`.

## 4.6 Universal formats, compared

| | Flatpak | Snap | AppImage |
|---|---|---|---|
| Who | Freedesktop community; Flathub is the store | Canonical | Community; no central store (AppImageHub is a directory) |
| Scope | GUI apps (CLI possible, awkward) | Anything: GUI, CLI, daemons, even kernels | Single-file GUI apps mostly |
| Sandbox | bubblewrap namespaces + portals; per-app permissions (Flatseal / desktop settings) | AppArmor confinement; interfaces; "classic" mode = no confinement | None (unless the app does it) |
| Dedup / size | Shared runtimes; first app is big (~1 GB runtime), subsequent apps small | Shared "core"/"gnome" snaps; similar | Each file is self-contained; largest per-app |
| Startup | Near-native | Historically slow first launch (compressed squashfs); improved | Near-native |
| Updates | `flatpak update`, or via software center; delta updates | Automatic, forced (schedulable, refresh can be held) | Manual unless app self-updates; AppImageLauncher helps |
| Theming / integration | Good; uses portals for file dialogs, respects GTK/Qt theme via extensions | Okay; gets better each year | Depends on app |
| Store backend | Open; anyone can host a remote | Proprietary Canonical store only | N/A |
| Distros shipping by default | Fedora, openSUSE, Mint, Pop!_OS, Zorin, elementary, EndeavourOS, CachyOS, all atomic distros | Ubuntu and official flavours only | none |
| Best for | GUI apps on any distro; sandboxing | Ubuntu users; CLI tools with confinement; IoT | one-off tools, portable apps |

**Practical guidance.** Use Flatpak for GUI apps you want current and sandboxed (browsers, chat, media, office, creative). Prefer distro packages for anything CLI or deeply integrated (terminal, shell, `git`, compilers, `docker`). On Ubuntu, either accept snaps (they've improved; the Firefox snap is fine for most people in 2026) or remove `snapd` and add Flathub — a well-documented ten-minute process, though Ubuntu's App Center won't show Flatpaks (install GNOME Software or use the `flatpak` CLI). Avoid AppImages as a primary method.

**A note on IDEs and Flatpak.** VS Code and JetBrains IDEs run as Flatpaks but live in a sandbox that can't see your host toolchains, Docker socket or `~/.ssh` without permission changes, and their integrated terminal is inside the sandbox (use `flatpak-spawn --host` or the Host Shell extension). Most developers are happier with the vendor's native package (Microsoft's `.deb`/`.rpm` repo; JetBrains Toolbox) or, on atomic distros, the Bluefin DX approach (IDE in the image, tools in Distrobox with the IDE's remote-container features).

## 4.7 The developer-tooling layer: why the distro matters less than it used to

This deserves its own section because it inverts a lot of received wisdom.

Ten years ago, "Debian stable is too old for development" was a real complaint: you got Python 2.7 and GCC 4.9 and no easy way to get anything else. Today:

- **Language version managers** — `uv` (Python; also replaces pip/venv/pyenv/poetry), `mise` (polyglot; successor to asdf), `rustup`, `fnm`/`volta`/`nvm` (Node), `sdkman` (JVM), `ghcup` (Haskell), `opam` (OCaml), `g`/`goenv` (Go), `rbenv`. Every one is a `curl | sh` or a single package away, on any distro, and gives you every version of the language independent of the distro.
- **Homebrew on Linux** — the macOS package manager, installed to `/home/linuxbrew/.linuxbrew`, with thousands of fresh CLI tools (ripgrep, fd, bat, lazygit, gh, k9s…) that don't touch the system. Bluefin ships it by default; anyone can install it. It's the answer to "my LTS has an old version of X."
- **Distrobox / Toolbox** — a container with a full distro userland (Ubuntu, Arch, Fedora, Alpine, whatever) whose `$HOME` is your `$HOME`, with GUI and audio passthrough, and whose binaries can be *exported* to appear in your host `$PATH`. Want the AUR on Fedora? `distrobox create -i archlinux` then `paru -S whatever` and `distrobox-export`. Want to test against the department's Ubuntu 24.04? `distrobox create -i ubuntu:24.04`. This single tool removes "which repos does my distro have" as a decision factor.
- **Devcontainers** — a `.devcontainer/devcontainer.json` in the repo defines the exact toolchain; VS Code, JetBrains, and the `devcontainer` CLI build and attach. The distro on your laptop is irrelevant to the project's build.
- **Nix** (on any distro) — per-project shells with exact versions.
- **Docker/Podman** — for services (databases, queues, caches) you'd never install on the host anyway.

The upshot: **for the toolchain, choose whichever distro you like; you'll get the same tools.** The distro still decides your kernel, drivers, desktop, and how the *base* behaves under updates. That's where the choice should focus — which is exactly what the top-weighted criteria in Chapter 3 say.

The one caveat: all of this tooling assumes an FHS-compliant glibc system. NixOS (non-FHS) and Alpine (musl) are the exceptions where `curl | sh` installers and pre-built binaries fail. On NixOS you use Nix for everything instead, which is the point.

## 4.8 Kernel modules and drivers: the recurring pain

Out-of-tree kernel modules are the single most common cause of "my update broke my computer." Understanding the delivery mechanisms helps you choose.

**In-tree** (AMD, Intel, most WiFi/Bluetooth/touchpads, and now the `nova`/Nouveau NVIDIA drivers for basic display): nothing to do; they ship with the kernel.

**Out-of-tree**, delivered as:

| Mechanism | How it works | Failure mode | Who uses it |
|---|---|---|---|
| **Pre-built, kernel-matched packages** | The distro compiles the module against each kernel it ships and publishes both together | Almost none; the module is tested against exactly that kernel | Ubuntu (`linux-modules-nvidia-*`), Arch (`nvidia-open` for `linux`, `nvidia-lts-open` for `linux-lts`), Fedora via RPM Fusion's pre-built `kmod-nvidia` for the current kernel (with akmods as fallback), Universal Blue images (baked in) |
| **DKMS / akmods** | On each kernel update, a hook compiles the module source against the new headers on *your* machine | New kernel breaks the build (API change) → module missing → black screen or missing device until upstream fixes the source | Arch `*-dkms` packages (for custom kernels), Fedora `akmod-*` (RPM Fusion), Debian `*-dkms`, everything on a rolling distro that isn't pre-built |
| **Vendor `.run` installer** | NVIDIA's own script installs everything outside the package manager | Every kernel update breaks it; the package manager doesn't know it exists; **never do this on a desktop** | Nobody who's been burned |

**NVIDIA specifics as of 2026:**

- The **open kernel modules** (`nvidia-open`) have been the default and recommended flavour since the 560 series for Turing (RTX 20xx / GTX 16xx) and newer. Performance parity with the proprietary module; better upstream cooperation. Arch moved its main packages to the open flavour in December 2025 and dropped the proprietary `nvidia-dkms` from the repos; the userland (CUDA, Vulkan, the display driver) remains proprietary.
- The **590 series** (December 2025) dropped support for **Pascal (GTX 10xx) and older**. Those cards live on the **580xx legacy branch**, which gets security fixes only. If you own a GTX 1060/1070/1080 in 2026, you're on legacy drivers and should plan a GPU upgrade or accept that new kernels will eventually outrun the legacy branch (Arch users must use `nvidia-580xx-dkms` from the AUR).
- **Wayland on NVIDIA** is fine on 590+: explicit sync, GAMESCOPE, VRR, and most compositors work. Residual issues: some multi-monitor/VRR edge cases, night light on some setups, occasional flicker regressions in point releases.
- **Secure Boot + NVIDIA** requires signing the module. Ubuntu's `ubuntu-drivers` and Fedora's akmods (with a one-time `kmodgenca` + `mokutil --import`) automate this; Arch requires manual `sbctl` setup. Or disable Secure Boot.
- **CUDA** is version-locked to specific driver ranges; NVIDIA's documentation targets Ubuntu LTS first, then RHEL/Fedora. It works on Arch (`cuda` package) but you get whatever version Arch ships, which may be newer than PyTorch's wheels expect — pin via conda/uv rather than the system package.

**The recommendations that fall out:**

- **AMD or Intel GPU:** any distro; the driver is in-tree; nothing to think about. (This is a real, tangible reason to prefer AMD when buying a Linux machine.)
- **NVIDIA + want minimal friction:** Ubuntu LTS (pre-built modules, Secure Boot handled), Pop!_OS NVIDIA ISO (same, with System76's tuning), or Bazzite/Bluefin/Aurora `-nvidia` images (driver baked into a tested image — the closest to "never think about it").
- **NVIDIA + Fedora:** RPM Fusion's `akmod-nvidia`; works well; you'll wait a few minutes after each kernel update while it builds, and after a new *major* kernel you should wait a few days before updating in case the module needs patching.
- **NVIDIA + Arch:** `nvidia-open` with the stock kernel is pre-built and fine; keep `linux-lts` + `nvidia-lts-open` installed as a fallback; read the news.
- **NVIDIA + atomic non-UBlue (Silverblue/Kinoite):** possible via layering RPM Fusion's akmods but clunky; use Universal Blue's images instead.

---

### Key takeaways

- A fresh LTS is nearly as current as a rolling distro for a few months, then ages; Fedora's six-month cadence with in-release kernel/Mesa rebases makes it "semi-rolling" and is the pragmatic middle for developers.
- Language version managers, Homebrew, Distrobox, devcontainers and Flatpak have made the base distro's repository freshness *almost irrelevant for your toolchain*. Focus the distro choice on kernel/drivers, desktop and update behaviour instead.
- Rolling releases don't demand more skill, they demand more *attention*: update regularly, read the news, handle `.pacnew`. Budget roughly 10–20 hours/year on Arch vs. 2–5 on Fedora vs. 1–3 on Ubuntu LTS (NVIDIA roughly doubles these).
- Manjaro's delayed-repos-plus-live-AUR model is a design flaw; prefer EndeavourOS or CachyOS for "easy Arch," or Slowroll for "slower Tumbleweed."
- Atomic distros deliver genuine unbreakability and are the best "appliance" option — especially Universal Blue's Bluefin/Aurora/Bazzite — but require adopting the Flatpak/Homebrew/Distrobox workflow and struggle with out-of-image kernel modules and host-level hacking.
- NixOS is uniquely reproducible and rewards investment, but its non-FHS layout and learning curve are real costs; try Nix on another distro first.
- All package managers are competent; `apt` 3.2 finally has undo; `pacman` relies on snapshots for rollback. Use Flatpak for GUI apps, distro packages for CLI/system pieces, and avoid AppImages as a primary channel.
- Out-of-tree kernel modules (chiefly NVIDIA) are the top cause of update breakage; prefer pre-built, kernel-matched module packages (Ubuntu, Arch `nvidia-open`, Universal Blue images) over DKMS on a daily driver, and buy AMD/Intel if you can.
