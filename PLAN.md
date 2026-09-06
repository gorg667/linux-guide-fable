# PLAN.md — Full Outline of the Guide

Working title: **"Choosing a Linux Distribution for Software Engineering, Computer Science Study, and Daily Life — The Definitive Guide (2026 edition)"**

Audience: software engineers (junior→senior), CS students, and anyone who wants one machine for work + study + life. Assumes computer literacy, not Linux literacy.

Thesis (to be argued, not assumed):
1. The "which distro" question is mostly a question about **release model + packaging + desktop + support ecosystem**, not about the brand name.
2. For most people in this audience the answer converges on a small set (Fedora Workstation/KDE, Ubuntu LTS, an Arch derivative, an atomic image like Bluefin/Aurora, or NixOS for the declarative-minded), and the marginal differences among the rest are smaller than internet arguments suggest.
3. The *right* answer depends on a handful of concrete facts about you: hardware (esp. NVIDIA), tolerance for breakage vs. staleness, need for specific proprietary software, desire to tinker, and whether you want your machine to be a hobby.

---

## 00 — Preface
- Who this is for / not for
- How to read (TL;DR box up top; skip paths)
- Honesty statement: opinions labelled as such; date-stamped (Sep 2026)
- The 60-second answer (short recommendation table) so impatient readers get value immediately

## 01 — How to Think About the Choice
- Why "best distro" is a category error; what a distro actually decides for you
- The four axes: (a) release cadence/stability, (b) packaging & software availability, (c) desktop/UX defaults, (d) ecosystem/support/docs/community/corporate backing
- Hidden axis: how much you want to *own* the system vs. have it *managed*
- The cost of switching is low; the cost of a bad first experience is high (churn)
- Common failure modes: chasing benchmarks, choosing by aesthetics screenshots, choosing what your friend uses, choosing the "hardest" to prove something
- Framework preview

## 02 — Foundations: What a Distro Is Made Of
- Kernel (versions, LTS kernels, why kernel version matters for hardware)
- Init/system layer: systemd (and alternatives: runit, OpenRC, s6, dinit) — why systemd is the pragmatic default
- Userland: glibc vs musl, coreutils (incl. Rust uutils in Ubuntu), toolchain versions
- Package management primer (dependency resolution, repos, signing, delta updates)
- Release models: fixed/point, LTS, rolling, semi-rolling, atomic/image-based, declarative
- Desktop stack: display server (Wayland now default; X11 legacy), DE vs WM, portals, PipeWire
- Filesystems: ext4, Btrfs (snapshots), XFS, ZFS (licensing), bcachefs status; LVM; LUKS
- Boot: UEFI, Secure Boot, shim, GRUB vs systemd-boot, TPM
- Security frameworks: SELinux vs AppArmor; sandboxing (Flatpak/bubblewrap)

## 03 — Requirements Analysis
- The SWE's needs: toolchains, containers, reproducibility, low friction, stability during deadlines, corporate VPN/IT compliance, hardware acceleration, multiple monitors
- The CS student's needs: coursework-specific software (specific compiler versions, Java/IDE, MATLAB, LaTeX, VMs for OS class, CUDA for ML), university WiFi (eduroam), proctoring & lockdown browsers (major blocker), Office/OneDrive collaboration, budget hardware
- The daily driver's needs: browser, media/codecs, gaming, video calls, printing, Bluetooth audio, phone integration, battery life, sleep/resume, "it just works"
- Where they conflict: bleeding-edge vs stable; tinkering vs "must work for exam tomorrow"
- Derive ranked criteria list to use for scoring

## 04 — Release Models & Package Management (deep dive)
- Point release (Debian, Ubuntu LTS/interim, Fedora, openSUSE Leap, Mint): pros/cons, actual staleness numbers
- Rolling (Arch, Tumbleweed, Void, Gentoo): what "breaks" really means; the Arch news feed reality; openQA on Tumbleweed
- Semi-rolling/curated (Manjaro, Slowroll, CachyOS)
- Atomic/image-based (rpm-ostree/bootc, Universal Blue, Aeon/Kalpa, Vanilla OS): benefits, friction points (layering, /usr immutability, kernel modules)
- Declarative (NixOS, Guix): reproducibility, learning curve, ecosystem (Home Manager, flakes), when it's worth it
- Package managers compared: apt, dnf5, pacman (+AUR helpers), zypper, xbps, portage, nix, apk
- Universal formats: Flatpak (Flathub) vs Snap vs AppImage — tradeoffs, sandbox, theming, startup, storage
- Developer-oriented layers: Distrobox/Toolbox, devcontainers, Homebrew on Linux, asdf/mise, pipx/uv, language-native managers — "the distro matters less than you think for dev tools"
- Kernel/driver delivery: DKMS vs akmods vs prebuilt; NVIDIA as the canonical pain

## 05 — Desktop Environments & Window Managers
- GNOME (workflow, extensions fragility, Wayland-only, fractional scaling, VRR, HDR)
- KDE Plasma 6.x (flexibility, Wayland, HDR, KDE Connect, Kdenlive ecosystem)
- COSMIC (Rust, System76; status in 2026)
- Xfce, Cinnamon, MATE, LXQt, Budgie, Pantheon (elementary)
- Tiling: Hyprland, Sway, i3, niri, river; when tiling makes devs faster, when it's a time sink
- Impact on distro choice: distro defaults & first-class support (e.g. Fedora KDE Edition, Kubuntu, KDE neon)

## 06 — Distro Reviews: Mainstream
For each: identity & governance; release model; packaging; default DE; hardware support; dev experience; daily-driver polish; security defaults; documentation/community; who should pick it; who should not; verdict score.
- Ubuntu (Desktop LTS 26.04 & interim; flavours: Kubuntu, Xubuntu, Ubuntu MATE, Budgie, Studio; snap controversy; Pro/ESM; Canonical)
- Fedora Workstation & Fedora KDE Plasma Desktop (Red Hat relationship; 13-month support; codecs & RPM Fusion; SELinux)
- Debian (13 Trixie / 14 Forky testing; stable/testing/sid strategy; philosophy)
- Linux Mint (Cinnamon; LMDE; Windows-refugee friendly; Ubuntu base without snaps)
- Pop!_OS (COSMIC; System76 hardware; NVIDIA ISO)
- Zorin OS, elementary OS (brief)

## 07 — Distro Reviews: Enthusiast / Rolling
- Arch Linux (archinstall; wiki; AUR; philosophy; maintenance cost honestly assessed)
- EndeavourOS, CachyOS (performance patches, -v3/-v4 repos), Manjaro (delayed rolling, history of issues), Garuda
- openSUSE Tumbleweed (openQA, snapper+btrfs by default, YaST retirement → Cockpit/Myrlyn), Leap 16, Slowroll
- Gentoo (USE flags, binary packages now available), Void (runit, xbps, musl option), Alpine (musl, for containers mostly), Solus
- Slackware (historical mention)

## 08 — Distro Reviews: Atomic & Declarative
- Fedora Atomic Desktops (Silverblue, Kinoite, Sway/Budgie Atomic), bootc transition
- Universal Blue: Bluefin (GNOME, dev-focused, Bluefin DX), Aurora (KDE), Bazzite (gaming)
- openSUSE Aeon / Kalpa
- Vanilla OS (Orchid, apx)
- NixOS (flakes, home-manager, nixpkgs size, reproducibility, community turbulence, learning curve, when it pays off for devs)
- Guix System (brief)
- Verdict on atomic for SWE/students: pros (unbreakable, rollback) vs cons (kernel modules, some tooling assumptions)

## 09 — Comparison Matrices
- Master table: release model, base, pkg mgr, default DE, init, FS default, security framework, support length, corporate backing, install difficulty, hardware breadth, NVIDIA ease, package freshness (kernel/gcc/python/node/rust versions snapshot), universal pkg default (snap/flatpak), docs quality, community size
- Scoring per persona (SWE / student / daily) with weights; sensitivity discussion

## 10 — Hardware Considerations
- Buy-for-Linux vs. make-it-work; laptops: ThinkPad (T/X1/P), Framework (13/16; AMD/Intel), Dell XPS/Precision developer edition, HP Dev One (discontinued), System76, Tuxedo, Slimbook, Star Labs
- GPUs: AMD (best), Intel (great), NVIDIA (open kernel module, proprietary driver 5xx series, Wayland status, explicit sync, CUDA)
- Apple Silicon: Asahi/Fedora Asahi Remix status; M1/M2 vs newer; limitations
- ARM laptops: Snapdragon X Elite status
- WiFi/Bluetooth chipsets (Intel good, Broadcom bad, MediaTek/Realtek mixed), fingerprint readers, webcams (IPU6), HiDPI, touchpads, sleep (s2idle vs S3), battery (TLP/power-profiles-daemon)
- Desktops: easy; mention Secure Boot + NVIDIA + MOK

## 11 — Developer Workflow on Linux
- Toolchains: C/C++ (gcc/clang, cmake), Rust (rustup), Go, Python (uv, pyenv), Node (fnm/volta), Java (SDKMAN), .NET, Haskell/OCaml, etc. — distro package vs upstream manager
- Containers: Docker vs Podman (rootless), Docker Desktop not needed; k8s local (kind, minikube, k3s)
- VMs: KVM/QEMU/virt-manager, GNOME Boxes; VirtualBox pain on rolling kernels
- Editors/IDEs: VS Code (repo/flatpak caveats), JetBrains Toolbox, Neovim, Zed, Emacs
- Shell & terminal: bash/zsh/fish, starship, tmux/zellij, ghostty/kitty/alacritty/foot
- Dotfiles management: chezmoi, stow, home-manager
- Git/SSH/GPG keys, agents, hardware keys (YubiKey)
- Distrobox for "any distro's packages"
- Comparison with WSL2 and macOS for honesty

## 12 — CS Student Specifics
- Course types & their needs (systems/C, OS with QEMU/xv6, architecture (RISC-V toolchains), networks (Wireshark, Mininet), databases, ML (CUDA/ROCm, Jupyter), compilers, HCI/Android dev, game dev (Unity/Unreal/Godot on Linux))
- Proprietary blockers: MATLAB (works), Mathematica, Autodesk (no), Adobe (no), MS Office (web/alternatives), Respondus/LockDown Browser/Proctorio (Windows/mac only → dual boot or VM/Windows on another machine)
- eduroam setup, VPNs (Cisco AnyConnect → OpenConnect, GlobalProtect), printing on campus
- Writing: LaTeX (TeX Live), Typst, Pandoc, Zotero, Obsidian
- Budget hardware; used ThinkPads
- Dual boot best practices vs Windows VM vs cloud Windows

## 13 — Daily Driver Realities
- Browsers (Firefox, Chromium, DRM/Widevine, hardware video decode)
- Media codecs (Fedora/openSUSE quirks), Spotify, streaming 1080p limits
- Gaming: Steam/Proton, anti-cheat exceptions, Heroic, Lutris; NVIDIA
- Video calls: Zoom, Teams (PWA), Slack, Discord (screen share on Wayland → PipeWire portal)
- Office: LibreOffice, OnlyOffice, MS 365 web, Google Docs; fonts (ms fonts, metric-compatible)
- Printing/scanning (IPP everywhere), Bluetooth audio (LDAC/AAC via PipeWire), phones (KDE Connect, GSConnect), cloud storage (Nextcloud, rclone, OneDrive clients), password managers
- Display: HiDPI, fractional scaling, HDR, VRR, multi-monitor mixed DPI
- Power/battery/sleep

## 14 — Security, Privacy, and Long-Term Maintenance
- Update discipline per release model; unattended upgrades
- Secure Boot & third-party modules (MOK); TPM-backed LUKS
- SELinux vs AppArmor practical impact
- Firewalls (firewalld/ufw), Flatpak permissions (Flatseal)
- Backups: Btrfs snapshots (Snapper/Timeshift), borg/restic, Déjà Dup; dotfiles in git
- Longevity: distro upgrade experiences (Ubuntu do-release-upgrade, Fedora dnf system-upgrade, rolling)
- Telemetry & privacy stances

## 15 — The Decision Framework
- Decision tree (text + mermaid)
- Persona-based recommendations (≈10 personas: first-time switcher from Windows, macOS refugee, NVIDIA gamer-dev, ML student with CUDA, systems programmer, Nix enthusiast, minimalist, old laptop, Apple Silicon owner, corporate SWE on managed IT)
- The "default answer" and when to deviate
- Second-choice and what to try if the first fails

## 16 — Post-Install Playbook
- Universal checklist; then concrete for Fedora Workstation, Ubuntu LTS, Arch/EndeavourOS/CachyOS, Bluefin/Aurora, NixOS (short config)
- Essential tweaks: codecs, Flathub, drivers, firmware (fwupd), fonts, shell, dev tools, backups, snapshots

## 17 — Myths, FAQ, Migration
- Myths: "Arch is unstable", "Ubuntu is bloated", "Fedora is a beta for RHEL", "immutable can't do dev", "Linux can't game", "you need the terminal for everything", "Wayland isn't ready"
- FAQ
- Migration from Windows/macOS; keyboard shortcuts, app equivalents; dual-boot; try-before-you-switch (live USB, VM, Ventoy)
- When to switch distros vs. fix your setup

## 18 — Conclusion

## Appendix A — Glossary
## Appendix B — Sources & Further Reading
