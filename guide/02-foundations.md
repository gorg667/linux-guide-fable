# Chapter 2 — Foundations: What a Distribution Is Made Of

You cannot reason about distributions without a working model of the layers underneath them. This chapter builds that model from the bottom up. If you already know what systemd, glibc, Wayland and Btrfs are, skim the headings and read only the "why it matters for choosing" notes.

## 2.1 The kernel

**Linux** is, strictly, only the kernel: the program that talks to hardware, schedules processes, manages memory, and provides the filesystem and networking stacks. Every distribution ships the same kernel source with, at most, a handful of patches. What differs is the *version* and the *configuration*.

**Why the version matters.** Hardware support lives in the kernel. A laptop released in mid-2026 may have a WiFi chip, a touchpad, a webcam or a GPU whose driver landed in Linux 7.0 or 7.1. A distribution shipping kernel 6.12 (Debian 13 stable, as of its 2025 release) won't have that driver at all, or will have an early, buggy version. This is the single most common cause of "Linux doesn't work on my new laptop" — and it's a *distro choice*, not a Linux limitation.

As of September 2026, the situation is:

| Kernel | Status | Typical shipper |
|---|---|---|
| 7.2 | current stable (released Aug 2026) | Arch, Tumbleweed, CachyOS, Fedora (after a few weeks) |
| 7.1 | end-of-life short-term stable | — |
| 7.0 | shipped in Ubuntu 26.04 LTS (Canonical maintains it for the LTS lifetime) | Ubuntu 26.04 and derivatives (Mint 23, Pop!_OS 26.x) |
| 6.18 | current **long-term support (LTS)** kernel, maintained until ~2028 | NixOS 26.05, some Debian backports |
| 6.12 | previous LTS | Debian 13 "Trixie" |
| 6.6, 6.1, 5.15, 5.10 | older LTS branches | enterprise distros, embedded |

Rule of thumb: **if your hardware is less than about a year old, you want a distro that ships a kernel released after your hardware.** Rolling and six-month distros give you that automatically; LTS distros give you a "hardware enablement" (HWE) kernel some months later (Ubuntu does this well; Debian requires the `backports` repository).

**Kernel flavours.** Some distros offer variants: `linux-lts` on Arch (tracks the LTS branch, for people who want a fallback), `linux-zen` (desktop-tuned scheduler tweaks), CachyOS's BORE-scheduler kernels, real-time kernels for audio. For development and daily use the stock kernel is fine; keep an LTS kernel installed as a fallback on rolling distros.

**Out-of-tree kernel modules.** Some drivers are *not* in the kernel — NVIDIA's proprietary/open GPU driver, VirtualBox, some VPN clients, ZFS. These must be compiled against your exact kernel version, which means every kernel update triggers a rebuild via **DKMS** (Dynamic Kernel Module Support) or the distro's equivalent (Fedora's `akmods`). When that rebuild fails — a new kernel breaks the module's build — you get the infamous black screen. Distributions that ship *pre-built* module packages tied to their kernel (Ubuntu's `linux-modules-nvidia-*`, Arch's `nvidia-open` for the stock kernel) avoid this, at the cost of flexibility. This is why NVIDIA + rolling release is a combination that demands attention.

## 2.2 The init system and service manager

When the kernel finishes booting it starts exactly one program: PID 1, the **init**. Since roughly 2015 that program on almost every distribution is **systemd**, which also manages services, logging (`journald`), device naming, login sessions, timers, network configuration (optionally), and more.

systemd was controversial and remains so among a minority, chiefly because it is large, monolithic in spirit, and replaced a lot of shell-script-based tooling. The pragmatic reality in 2026: **every mainstream distribution uses it**, most desktop software assumes it (GNOME and KDE integrate deeply with `logind` and user services), and knowing `systemctl`, `journalctl`, and unit files is a genuinely useful professional skill because your servers run it too.

Alternatives exist and are worth knowing about for context:

- **runit** (Void Linux), **OpenRC** (Gentoo default, Alpine), **s6**, **dinit** (Chimera Linux, some Artix variants). These are smaller, simpler and arguably more Unix-y. Artix Linux is Arch without systemd; Devuan is Debian without systemd.
- Choosing a non-systemd distro is a philosophical choice with real costs: some desktop features (e.g. GNOME's user session management, some Flatpak portals, `systemd-homed`, TPM-based encryption unlock) either need shims or don't work.

**Why it matters for choosing:** it mostly doesn't, unless you specifically want to avoid systemd, in which case your options narrow to Void, Gentoo, Alpine, Artix, Devuan and Chimera. For everyone else, systemd is a constant across choices and a skill worth having.

## 2.3 The userland: libc, coreutils, shells

Above the kernel sits the **C library** (`libc`), which nearly every program links against. Two choices exist:

- **glibc** — the GNU C library. Used by every mainstream distribution. Large, fast, feature-complete, and the target that all proprietary software (Steam, VS Code, JetBrains, Zoom, CUDA) is built against.
- **musl** — small, clean, static-linking-friendly. Used by Alpine Linux (hence its dominance in container images) and available as an option on Void and Gentoo. Proprietary and pre-compiled software frequently does **not** work on musl systems without a glibc compatibility layer. **For a desktop daily driver, musl is the wrong choice**; it exists here so you know why Alpine is great in a Dockerfile and wrong on your laptop.

**Coreutils** are the small programs everyone uses — `ls`, `cp`, `mv`, `cat`, `grep`. Historically always GNU coreutils; since Ubuntu 25.10/26.04, Canonical ships the Rust rewrite **uutils** by default (with GNU available as a fallback package). Behaviour is deliberately identical for common use; edge cases in obscure flags occasionally differ. Ubuntu also ships `sudo-rs` instead of the classic `sudo`. This is mostly invisible; you'll notice asterisks when typing your sudo password.

**Shells** are per-user choices (bash, zsh, fish), not distro decisions, though the default varies (bash almost everywhere; some distros configure zsh nicely out of the box). Any shell works on any distro.

**Why it matters for choosing:** glibc is a hard requirement for a desktop. Otherwise, userland is identical enough not to influence the choice.

## 2.4 Package management: the heart of the matter

A **package** is an archive of files plus metadata: name, version, dependencies, install scripts. A **repository** is a signed, indexed collection of packages served over HTTP. A **package manager** downloads packages, resolves dependencies, verifies signatures, installs files, and records what it did so it can be undone.

This is where distros genuinely differ — not in *whether* they do this, but in format, tooling ergonomics, repository size, freshness, and philosophy.

### The families

| Family | Format | Low-level tool | High-level tool | Used by |
|---|---|---|---|---|
| Debian | `.deb` | `dpkg` | `apt` (3.x; `apt-get` legacy) | Debian, Ubuntu (+flavours), Mint, Pop!_OS, Zorin, elementary, MX, Kali |
| Red Hat | `.rpm` | `rpm` | `dnf` (v5 as of Fedora 41+) | Fedora, RHEL/CentOS Stream/Alma/Rocky, Nobara |
| SUSE | `.rpm` | `rpm` | `zypper` | openSUSE Tumbleweed/Leap/Slowroll |
| Arch | `.pkg.tar.zst` | — | `pacman` (+ AUR helpers `yay`/`paru`) | Arch, EndeavourOS, CachyOS, Manjaro, Garuda, Artix |
| Nix | store paths | — | `nix` | NixOS (and Nix on any distro) |
| Gentoo | source ebuilds (+binpkgs) | — | `emerge` (Portage) | Gentoo, Funtoo |
| Void | `.xbps` | — | `xbps-install` | Void |
| Alpine | `.apk` | — | `apk` | Alpine, postmarketOS, Chimera |

For daily-driver purposes, the practical differences are:

**Repository size and freshness.** Arch's official repos plus the **AUR** (Arch User Repository — community-maintained build recipes for ~90,000 packages, including nearly every piece of developer tooling, proprietary app and niche utility you can think of) is the broadest "just install it" experience on Linux. **nixpkgs** is actually larger by package count (>120,000) and just as fresh, but with the Nix learning curve. Debian's archive is enormous (~65,000 packages) but versions are older on stable. Fedora is large and fresh but excludes patent-encumbered codecs and proprietary drivers, delegating them to the third-party **RPM Fusion** repo. Ubuntu's repos are Debian's plus Canonical's additions, plus **PPAs** (Personal Package Archives — third-party repos of varying quality). openSUSE has the **Open Build Service** (OBS), a huge community repo system roughly analogous to PPAs/AUR.

**Ergonomics.** All modern managers are fine. `apt` 3.x has a coloured, columnar output and (since 3.2 in Ubuntu 26.04) transaction history with `apt history-undo`/`rollback`. `dnf5` is fast and has had transaction history and rollback for years. `pacman` is terse and fast but its flags (`-Syu`, `-Rns`, `-Qi`) take a week to memorise. `zypper` is verbose and explicit. `nix` is a different paradigm altogether (see §2.6).

**Signing and trust.** All official repos are cryptographically signed. The *third-party* channels differ: AUR packages are user-submitted build scripts you are expected to read before building (in practice most people don't, and it has been abused a handful of times); PPAs are trusted binaries from arbitrary individuals; RPM Fusion and OBS are curated to varying degrees; Flathub (see below) has a review process for new apps.

**Delta/partial updates.** Fedora and openSUSE support delta RPMs (download only the changes). Most others download whole packages. With modern bandwidth this rarely matters.

### Universal package formats

Since about 2018 a second layer has grown on top of distro packaging: **application bundles** that carry their own dependencies and run on any distro.

- **Flatpak** — the community standard, dominant on the desktop. Apps come from **Flathub** (the main store), run sandboxed with permissions (manageable with **Flatseal**), share runtimes (GNOME/KDE/Freedesktop) to save space, and integrate with GNOME Software / KDE Discover. Nearly every distro except Ubuntu ships it or makes it one command away. Good for GUI applications; poor for CLI developer tools and anything that needs deep system access (IDEs work but need extra permission fiddling to see your toolchains and Docker socket).
- **Snap** — Canonical's format. Technically capable (supports CLI tools, daemons, and even kernels), but the store backend is proprietary and Canonical-only, first launch of an app is slow (improving), and Ubuntu forcibly redirects some `apt install` commands (Firefox, Chromium, Thunderbird) to snaps. Outside Ubuntu, nobody uses it. The animosity is real but overstated; Chapter 6 covers how to live with or remove it.
- **AppImage** — a single executable file, no installation, no sandbox, no auto-update unless the app implements it. Convenient for occasional tools; poor as a primary distribution method. Recent versions of many distros no longer ship `libfuse2` by default, which older AppImages need.

For **developers**, a third set of tools matters more than any of these: **Distrobox / Toolbox** (run any distro's userland in a container with seamless access to your home directory — so you can have Ubuntu's `apt` on Fedora, or Arch's AUR on Bluefin), **Homebrew on Linux** (fresh CLI tools in `/home/linuxbrew`, independent of the distro), language version managers (`uv`, `mise`, `rustup`, `fnm`, `sdkman`), and **devcontainers**. Together these have made the distro's own repositories *almost irrelevant for your development toolchain*. This is the most important shift of the past five years and Chapter 4 explores it fully.

**Why it matters for choosing:** the AUR and nixpkgs are compelling reasons to choose Arch-family or NixOS *if you frequently install niche software*. For everyone else, Flatpak + Distrobox + language managers make the base distro's repository size a secondary concern. Snap is a mild negative for Ubuntu that most people learn to tolerate or remove.

## 2.5 Release models

A "release model" is the policy about *when* packages in the repository change. This is the axis that determines your position on the freshness–stability–maintenance triangle. Chapter 4 goes deep; here's the taxonomy.

**Fixed / point release.** A snapshot is cut, tested, released, and then receives only bug and security fixes ("stable updates") for its lifetime. New versions of software arrive with the *next* release. Sub-varieties:
- *Short cycle*: Fedora (every ~6 months, each supported ~13 months), Ubuntu interim releases (every 6 months, supported 9 months), openSUSE Leap (annual-ish).
- *Long-term support (LTS)*: Ubuntu LTS (every 2 years, supported 5 years, 10 with Pro), Debian stable (every ~2 years, ~3 years + 2 LTS), RHEL and clones (10 years). Linux Mint tracks Ubuntu LTS.

**Rolling.** No versions; packages update continuously as upstream releases them, after a short (hours to weeks) testing period. Arch, openSUSE Tumbleweed, Void, Gentoo. Sub-varieties:
- *Curated/delayed rolling*: Manjaro (holds Arch packages ~2 weeks), openSUSE Slowroll (monthly-ish snapshots of Tumbleweed), CachyOS (Arch + its own tuned repos, effectively as fast as Arch).
- *Tested rolling*: Tumbleweed runs every snapshot through **openQA** automated testing before release — the best "fresh and rarely broken" record among rolling distros.

**Atomic / image-based.** The base OS is a single versioned image (an OSTree commit or, increasingly, an OCI container image via **bootc**). Updates download a new image and stage it; you reboot into it; if it fails, you boot the previous one. `/usr` is read-only; you don't install packages *into* the base — you use Flatpaks, containers (Distrobox), Homebrew, or *layer* packages on top (slow, discouraged, but possible). Fedora Silverblue/Kinoite, Universal Blue (Bluefin/Aurora/Bazzite), openSUSE Aeon/Kalpa, Vanilla OS, and (in spirit) SteamOS and ChromeOS. These can be rolling *or* point-release underneath; the atomicity is about *how* updates apply, not how often.

**Declarative.** The entire system — packages, services, users, config files — is described in a configuration file; the tool builds the system to match. Changing the file and rebuilding produces a new "generation"; every previous generation remains bootable. NixOS (Nix language) and Guix System (Scheme). Reproducible to a degree nothing else matches; you can rebuild your exact laptop on new hardware from a git repo. NixOS has both a stable channel (released every 6 months: 25.11, 26.05, next 26.11) and `unstable` (rolling).

**Why it matters for choosing:** this is *the* decision. Ask yourself whether you'd rather have a compiler that's 18 months old and never surprises you, or one that's 18 days old and might. Then ask how you feel about rebooting to roll back vs. fixing things in place.

## 2.6 The desktop stack

### Display server: Wayland has won

For thirty years Linux desktops ran on the **X Window System (X11/Xorg)**. Its replacement, **Wayland**, is a protocol where the compositor (the window manager) talks directly to the kernel's graphics stack, eliminating a layer, improving security (apps can't snoop each other's input), and enabling per-monitor fractional scaling, variable refresh rate, HDR, and tear-free rendering.

The transition is essentially complete as of 2026:

- **GNOME 50** (March 2026) removed the X11 session entirely. Fedora 44 and Ubuntu 26.04 are Wayland-only GNOME.
- **KDE Plasma 6.8** (October 2026) removes the X11 session. Plasma 6.6 is being maintained as a long-term branch until 2029 for those who need X11 longer.
- **Cinnamon** (Linux Mint) declared its Wayland session non-experimental in mid-2026 and will fully support both in Mint 23 (December 2026).
- **COSMIC** was Wayland-only from birth. **Hyprland, Sway, niri, river** are Wayland-native tiling compositors.
- **Xfce** 4.20 has experimental Wayland support; Xfce remains the main holdout still defaulting to X11. **MATE, LXQt** are in transition.

X11 applications still run under Wayland via **Xwayland**, a compatibility server. This works for almost everything. Residual pain points: some screen-sharing and global-hotkey tools written for X11, some remote-desktop setups, a few games with cursor-capture bugs, and accessibility tooling that's still catching up. NVIDIA on Wayland was rough through 2023, acceptable in 2024 after "explicit sync" landed, and is now fine on the 590/6xx driver series with rare regressions.

**Why it matters for choosing:** you will be on Wayland. If you have a hard X11 dependency (rare — check your specific tool), you want Xfce, MATE, or a Plasma 6.6 LTS distro. Otherwise it's a non-issue in 2026 and you should be suspicious of advice that still says "Wayland isn't ready."

### Desktop environments vs. window managers

A **desktop environment (DE)** is a full suite: compositor/window manager, panel, launcher, settings app, file manager, notifications, session management, and usually a family of applications. GNOME, KDE Plasma, Cinnamon, COSMIC, Xfce, MATE, LXQt, Budgie, Pantheon.

A **window manager (WM)** or standalone **compositor** is just the part that arranges windows. Hyprland, Sway, i3, niri, river, dwm. You assemble the rest (bar, launcher, notification daemon, lock screen) yourself. Tiling WMs — where windows automatically fill the screen in a grid and you navigate by keyboard — have a devoted following among developers because they minimise mouse use and window-fiddling.

Chapter 5 is devoted to this choice. The short version: **GNOME and KDE Plasma are the two first-class citizens** that every distro supports well and every application is tested against. Cinnamon is a mature, conservative third. COSMIC is the promising newcomer (1.x since December 2025). Tiling WMs are a fantastic productivity tool for the subset of people who enjoy configuring them and a time sink for everyone else.

### Portals, PipeWire, and the plumbing

Two pieces of plumbing you'll bump into:

- **XDG Desktop Portals** — the mechanism by which sandboxed apps (Flatpaks, and everything on Wayland) request things like "open a file", "share my screen", "take a screenshot". Screen sharing in Zoom/Discord/Slack on Wayland goes through the portal and PipeWire. It works well on GNOME and KDE; on niche WMs you need to install and configure a portal backend yourself (`xdg-desktop-portal-wlr`, `-hyprland`, etc.).
- **PipeWire** — the audio and video routing server that replaced PulseAudio and JACK. Universal now. Handles Bluetooth codecs (LDAC, AAC, aptX via `libfreeaptx`), pro-audio low latency, and screen capture. Good on every mainstream distro.

## 2.7 Filesystems, disks, and encryption

The installer will ask you about these, and some choices are annoying to change afterwards.

**ext4** — the conservative default (Debian, Ubuntu, Mint, Arch's guided install, Pop!_OS). Mature, fast, boring. No built-in snapshots or checksumming.

**Btrfs** — copy-on-write filesystem with cheap instant snapshots, transparent compression, checksumming of data and metadata, and subvolumes. Default on Fedora (since 33), openSUSE (with automated **Snapper** snapshots you can boot into from GRUB — the best out-of-box "undo my last update" experience on Linux), and CachyOS. Historically had a bad reputation for RAID 5/6 (still not recommended) and some corruption stories from the early 2010s; single-disk and RAID 1 have been solid for years. **For a laptop, Btrfs with snapshots is the pragmatic choice** — it turns "the update broke my system" from a crisis into a 30-second rollback.

**XFS** — fast, mature, excellent for large files; no snapshots (without LVM). RHEL default. Fine, rarely chosen on desktops.

**ZFS** — technically superb (snapshots, checksums, send/receive, RAID-Z). License (CDDL) is incompatible with the kernel's GPL, so it ships as an out-of-tree module — DKMS pain on rolling kernels. Ubuntu ships it in-tree-ish and its installer once offered root-on-ZFS (deprioritised in recent releases). Fantastic for NAS; overkill and slightly fragile for a laptop.

**bcachefs** — the newest CoW filesystem, merged in 6.7, then marked "externally maintained" in 6.17 after governance disputes and removed from mainline entirely in 6.18 (late 2025); it now lives as an out-of-tree DKMS module. Not for daily driving yet.

**LVM** (Logical Volume Manager) — a layer for resizable volumes across disks. Common under ext4 in Ubuntu/RHEL installs. Adds flexibility; also adds a layer. Btrfs subvolumes make it mostly unnecessary.

**Full-disk encryption (FDE) with LUKS** — every serious installer offers it. **Turn it on for any laptop.** The performance cost is negligible on any CPU with AES instructions (all of them). Two unlock styles:
- *Passphrase at boot* — classic, works everywhere.
- *TPM-backed automatic unlock* — the disk key is sealed to the TPM 2.0 chip and released only if Secure Boot measurements match, so you boot straight to the login screen with no passphrase, yet a thief who pulls the drive gets nothing. Ubuntu 26.04 made this a stable first-class installer option; Fedora and others support it via `systemd-cryptenroll` but not through the installer GUI. Caveat: firmware updates and bootloader changes can trip the measurements and you'll need your recovery key, so **write it down**.

**Swap.** Modern defaults use a swapfile or **zram** (compressed RAM swap; Fedora default, excellent for laptops). If you want hibernate, you need a real swap partition/file at least as large as RAM and some setup; hibernate remains the least reliable power state on Linux and many people live without it.

**Why it matters for choosing:** distros that set up Btrfs + snapshots by default (openSUSE, Fedora with a one-time Snapper/BTRFS Assistant setup, CachyOS, Garuda) give you a safety net that ext4 distros (Ubuntu, Mint, Debian) don't unless you configure Timeshift. Encryption is available everywhere; TPM auto-unlock is easiest on Ubuntu 26.04.

## 2.8 Boot: UEFI, Secure Boot, and the bootloader

Modern machines boot via **UEFI** firmware, which reads a small FAT32 **EFI System Partition (ESP)** and runs a bootloader from it. The bootloader loads the kernel and initramfs.

**Secure Boot** is a UEFI feature that only runs bootloaders signed by a trusted key (Microsoft's, in practice). Distros handle it via **shim**, a Microsoft-signed first stage that then verifies the distro's own signed GRUB and kernel. Ubuntu, Fedora, openSUSE, Debian, Mint all boot fine with Secure Boot **on**. Arch does not ship signed binaries; you either disable Secure Boot or enroll your own keys (`sbctl` makes this straightforward but it's a manual step). The wrinkle is **third-party kernel modules**: NVIDIA, VirtualBox and friends must be signed with a key the firmware trusts, which means enrolling a **Machine Owner Key (MOK)** — Ubuntu's driver installer does this for you with a prompt at next boot; Fedora's `akmods` can be configured to auto-sign; on Arch it's DIY. If you have NVIDIA and want the least friction, Ubuntu with Secure Boot on is the smoothest path; otherwise many people simply turn Secure Boot off, which is a defensible trade-off for a personal machine (it protects against a narrow class of bootkit attacks) but worth understanding rather than doing blindly — and some corporate IT and some anti-cheat systems require it on.

**Bootloaders.** **GRUB** is the traditional universal choice — handles dual-boot, LUKS, Btrfs snapshots-in-boot-menu (via `grub-btrfs`). **systemd-boot** is minimal and fast, and is what Pop!_OS, many Arch installs, and the atomic distros' bootc setups favour; it can't read Btrfs directly, so the kernel must live on the ESP. **Unified Kernel Images (UKIs)** bundle kernel+initramfs+cmdline into one signed EFI binary — the direction the ecosystem is heading, especially for TPM-sealed encryption. **rEFInd** is a pretty graphical manager popular for multi-boot. For most people: accept the installer default.

**Dual booting with Windows** is well supported by all mainstream installers (they detect Windows and add it to the menu). Practical tips live in Chapter 17. The main hazards are Windows updates occasionally resetting the boot order, BitLocker demanding its recovery key after you change boot settings, and Windows "Fast Startup" leaving the NTFS partition dirty — disable it.

## 2.9 Security frameworks

Two mandatory-access-control systems exist, and distros pick one:

- **SELinux** (Fedora, RHEL family, openSUSE Leap 16 and Tumbleweed now default). Label-based, extremely powerful, historically hostile to users when something's denied for a non-obvious reason. Fedora's default policy is well-tuned; most desktop users never see it. When you do, `sealert` or `ausearch` tell you what happened, and `setsebool`/`chcon` fix it. It's a genuinely useful thing to understand if you'll ever administer RHEL servers.
- **AppArmor** (Ubuntu, Debian, SUSE historically, Mint, Pop!_OS). Path-based profiles per application. Simpler, easier to write policies for, less comprehensive. Ubuntu uses it to confine snaps and, since 24.04, to restrict unprivileged user namespaces (which occasionally breaks Chromium-based apps and some dev tools until you add a profile).

Arch ships neither by default (both are installable). Both are "fine". Neither should drive your distro choice unless you're specifically learning enterprise Linux (then SELinux via Fedora).

**Application sandboxing** is separate: Flatpak uses **bubblewrap** namespaces regardless of the distro's MAC system, with permissions managed via Flatseal or the desktop's settings app. Snap uses AppArmor.

**Firewall.** Fedora ships **firewalld** enabled; Ubuntu ships **ufw** installed but *disabled* (and has no listening services by default, so it's mostly moot); Arch ships nothing. Enable one on a laptop that connects to public WiFi — it's a two-second change.

## 2.10 Putting the layers together

A distribution, then, is: a kernel version policy + systemd + glibc + a package manager and repository policy + a release model + a chosen desktop (or none) + a set of installer defaults for filesystem, encryption, security framework and bootloader + a support lifecycle + a community and (maybe) a company.

When you compare two distros, compare *those things*. Everything else — the wallpaper, the logo, the "vibe", the Reddit arguments — is noise.

---

### Key takeaways

- All distros share the same kernel, libc (glibc), init (systemd), desktops and applications; they differ in *policy*: version freshness, packaging, release model, defaults, support and ecosystem.
- Kernel version determines hardware support; new hardware needs a new kernel, which means a rolling or six-month distro (or an LTS with HWE kernels).
- Out-of-tree modules (NVIDIA, VirtualBox, ZFS) are the main source of update breakage; prefer distros that pre-build them or handle DKMS/akmods gracefully.
- Package managers are all competent; the AUR and nixpkgs stand out for breadth and freshness; Flatpak, Distrobox and language version managers have made the base distro's repositories far less important for developers.
- Wayland has won; GNOME 50 and Plasma 6.8 are Wayland-only. Only choose X11-centric desktops if you have a specific, verified need.
- Choose Btrfs with snapshots if the installer offers it; always enable LUKS full-disk encryption on a laptop.
- Secure Boot works out of the box on Ubuntu, Fedora, openSUSE, Debian and Mint; Arch requires manual key enrolment or disabling it. NVIDIA + Secure Boot is smoothest on Ubuntu.
- SELinux vs AppArmor is not a reason to pick a distro.
