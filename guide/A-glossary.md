# Appendix A — Glossary

Terms as used in this guide. Alphabetical.

**akmods** — Fedora/RPM Fusion's mechanism for automatically rebuilding out-of-tree kernel modules (e.g. NVIDIA) against each new kernel. Analogous to DKMS.

**AppArmor** — A path-based mandatory access control (MAC) system used by Ubuntu, Debian, Mint, Pop!_OS. Confines specific programs with per-program profiles.

**AppImage** — A single-file, self-contained application bundle that runs without installation and without a sandbox.

**Atomic (image-based) distro** — A distribution whose base OS is a versioned, read-only image; updates replace the whole image and the previous one remains bootable. Fedora Silverblue/Kinoite, Universal Blue, openSUSE Aeon, Vanilla OS.

**AUR (Arch User Repository)** — Community-submitted build recipes (`PKGBUILD`s) for ~90,000 packages not in Arch's official repos. Unsupported by Arch itself; built locally by an AUR helper.

**AUR helper** — A tool (`paru`, `yay`) that automates searching, downloading, building and installing AUR packages alongside `pacman`.

**Backports** — A repository of newer package versions rebuilt for a stable release (Debian backports, Ubuntu backports). Used to get a newer kernel on Debian stable.

**bootc** — "Bootable containers": a system where the OS image is a standard OCI container image, pulled and booted like a container image. The successor to rpm-ostree's image handling; used by Fedora Atomic and Universal Blue.

**Btrfs** — A copy-on-write filesystem with snapshots, checksums, compression and subvolumes. Default on Fedora, openSUSE, CachyOS.

**bubblewrap (bwrap)** — The low-level sandboxing tool Flatpak uses to isolate applications via Linux namespaces.

**Codecs** — Software for encoding/decoding audio and video formats (H.264, H.265, AAC). Some are patent-encumbered, so Fedora and openSUSE ship them via third-party repos (RPM Fusion, Packman).

**Compositor** — On Wayland, the program that is simultaneously the display server and the window manager (Mutter for GNOME, KWin for KDE, Hyprland, Sway, niri…).

**COPR** — Fedora's community build service for third-party repositories; analogous to Ubuntu PPAs.

**COSMIC** — System76's Rust-based desktop environment, default on Pop!_OS 24.04+, with native tiling.

**CUDA** — NVIDIA's proprietary GPU compute platform, required by most deep-learning frameworks for GPU acceleration on NVIDIA hardware.

**Declarative distro** — A distribution whose entire configuration is described in files and built to match (NixOS, Guix System). Changing the description and rebuilding produces a new bootable "generation."

**Desktop environment (DE)** — A complete graphical shell: compositor/WM, panel, launcher, settings, file manager, core apps. GNOME, KDE Plasma, Cinnamon, COSMIC, Xfce, MATE, LXQt, Budgie, Pantheon.

**Devcontainer** — A project-defined development environment (`.devcontainer/devcontainer.json`) that IDEs build and attach to as a container.

**Distrobox** — A tool for running any distro's userland in a container with your home directory and GUI/audio shared, and exporting its apps to the host. Fedora's **Toolbox** is a simpler sibling.

**DKMS (Dynamic Kernel Module Support)** — A framework that rebuilds out-of-tree kernel modules automatically when a new kernel is installed.

**dnf / dnf5** — Fedora's package manager (dnf5 is the fast C++ rewrite, default since Fedora 41).

**Dual boot** — Two operating systems installed on one machine, chosen at boot time.

**eduroam** — The international academic WiFi roaming federation; 802.1X/WPA-Enterprise authentication.

**ESP (EFI System Partition)** — The small FAT32 partition UEFI firmware reads bootloaders from.

**ext4** — The conservative default Linux filesystem; mature, fast, no snapshots.

**FDE (Full-disk encryption)** — Encrypting the whole disk (via LUKS on Linux) so data is unreadable without the key.

**FHS (Filesystem Hierarchy Standard)** — The conventional Linux directory layout (`/usr/bin`, `/lib`, `/etc`…). NixOS deliberately does not follow it.

**Flakes** — Nix's mechanism for pinning all inputs of a build to exact git revisions; officially "experimental" but the de facto standard.

**Flatpak** — The dominant universal application format on the Linux desktop; sandboxed, with shared runtimes; distributed mainly via **Flathub**.

**Flatseal** — A GUI for viewing and editing Flatpak application permissions.

**fwupd / LVFS** — The firmware update daemon and the Linux Vendor Firmware Service it pulls from; integrated into GNOME Software and KDE Discover.

**GRUB** — The traditional Linux bootloader; handles multi-boot, LUKS, and Btrfs snapshot boot entries.

**Home Manager** — A Nix tool for declaratively managing a user's dotfiles and packages; works on NixOS and on any other distro with Nix installed.

**Homebrew (Linuxbrew)** — The macOS package manager ported to Linux; installs current CLI tools under `/home/linuxbrew` independent of the distro.

**HWE (Hardware Enablement)** — Ubuntu's practice of shipping newer kernels and graphics stacks to an LTS release at each interim release point.

**Hybrid graphics** — A laptop with both an integrated (Intel/AMD) and a discrete (usually NVIDIA) GPU; the OS routes work between them (PRIME offload).

**Init system** — PID 1, the first process; manages services. systemd on all mainstream distros; runit, OpenRC, s6, dinit on a few.

**IPU6** — Intel's image processing unit used for MIPI webcams on some 2022–2024 laptops; historically needed out-of-tree drivers.

**Kernel** — The core of the OS (Linux proper); manages hardware, processes, memory, filesystems, networking.

**KVM/QEMU/libvirt** — Linux's native virtualization stack: KVM (kernel), QEMU (emulator/VMM), libvirt (management API). Front-ends: virt-manager, GNOME Boxes.

**LTS (Long-term support)** — A release supported for years (Ubuntu LTS: 5–10; Debian: 5; kernel LTS branches: 2–6). Also the KDE Plasma 6.6 "Bullet-proof" branch.

**LUKS** — The Linux standard for block-device encryption.

**MAC (Mandatory access control)** — Kernel-enforced access policies beyond Unix permissions: SELinux, AppArmor.

**Mesa** — The open-source OpenGL/Vulkan implementation for AMD (RADV/RadeonSI), Intel (ANV/Iris), and Nouveau/NVK. Newer Mesa = better gaming on those GPUs.

**MOK (Machine Owner Key)** — A user-enrolled Secure Boot key used to sign third-party kernel modules (NVIDIA, VirtualBox) so they load with Secure Boot on.

**musl** — A small, standards-focused C library used by Alpine and optionally Void/Gentoo; proprietary glibc binaries don't run on it.

**Nix / nixpkgs / NixOS** — Nix is a functional package manager and language; nixpkgs is its >120,000-package collection; NixOS is the declarative distro built on them.

**nix-ld** — A NixOS compatibility layer allowing pre-built binaries that expect an FHS dynamic linker to run.

**nvidia-open** — NVIDIA's open-source kernel modules (default since driver 560 for Turing+); the userland (CUDA, Vulkan, display) remains proprietary.

**OBS (Open Build Service)** — openSUSE's community package-building infrastructure; analogous to PPA/COPR/AUR.

**openQA** — openSUSE's automated integration-testing system that gates every Tumbleweed snapshot.

**OSTree / rpm-ostree** — A "git for filesystem trees" and Fedora's hybrid image/package system built on it; being succeeded by bootc.

**pacman** — Arch Linux's package manager.

**Packman** — openSUSE's third-party repository for codecs and multimedia; enabled via `opi codecs`.

**PipeWire** — The modern Linux audio/video routing server; replaced PulseAudio and JACK; handles Bluetooth codecs and screen capture.

**Point release** — A distro model where a versioned snapshot receives only bug/security fixes for its lifetime; new software arrives in the next release.

**Portal (xdg-desktop-portal)** — The mechanism by which sandboxed and Wayland apps request file pickers, screen sharing, screenshots, settings.

**PPA (Personal Package Archive)** — An Ubuntu third-party repository hosted on Launchpad.

**PRIME** — The Linux mechanism for hybrid-graphics render offload (`prime-run`, `__NV_PRIME_RENDER_OFFLOAD`).

**Proctoring software** — Exam-lockdown/monitoring tools (Respondus LockDown Browser, Proctorio, Honorlock, Examplify, ProctorU). None support Linux.

**Proton** — Valve's Wine-based compatibility layer for running Windows games via Steam. **Proton-GE** is a community build with extra fixes.

**Rolling release** — A distro model with no versions; packages update continuously (Arch, Tumbleweed, Void, Gentoo).

**ROCm** — AMD's open GPU compute platform; Ubuntu 26.04 packages it natively.

**RPM Fusion** — Fedora's essential third-party repository for codecs, NVIDIA drivers, Steam and other software Fedora can't ship.

**s2idle / S3** — Modern Standby (software-controlled low-power idle) vs. traditional deep sleep. Most new laptops only implement s2idle.

**sbctl** — A tool for creating and enrolling your own Secure Boot keys and signing binaries; the Arch-family way to enable Secure Boot.

**Secure Boot** — UEFI feature that only runs signed bootloaders/kernels. Supported out of the box by Ubuntu, Fedora, openSUSE, Debian, Mint, Universal Blue via **shim**.

**SELinux** — A label-based MAC system used by Fedora, RHEL, and openSUSE (Leap 16 / Tumbleweed since 2025).

**Semi-rolling** — Informal term for a point-release distro that updates the kernel and some stacks within a release (Fedora), or a rolling distro with delays (Manjaro, Slowroll).

**Snap** — Canonical's universal package format and proprietary store; default on Ubuntu, used almost nowhere else.

**Snapper / Timeshift** — Tools for scheduling and managing Btrfs (or rsync) system snapshots; openSUSE and CachyOS ship Snapper preconfigured; Mint ships Timeshift.

**systemd** — The init system and service manager used by all mainstream distros; also provides journald, logind, timers, resolved, and more.

**systemd-boot** — A minimal UEFI boot manager; used by Pop!_OS, many Arch installs, and bootc systems.

**systemd-cryptenroll** — Tool for binding a LUKS volume to a TPM2 (or FIDO2 key) for automatic unlock.

**TPM (Trusted Platform Module)** — A secure chip that stores keys and boot measurements; enables passphrase-less FDE unlock that still protects against disk theft.

**UEFI** — Modern PC firmware; replaced BIOS; boots from the ESP; supports Secure Boot.

**UKI (Unified Kernel Image)** — Kernel + initramfs + command line bundled into one signed EFI binary.

**Universal Blue** — A community project publishing opinionated bootc images on Fedora Atomic: Bluefin (GNOME), Aurora (KDE), Bazzite (gaming).

**uutils / sudo-rs** — Rust rewrites of GNU coreutils and sudo, default in Ubuntu 26.04.

**uv** — Astral's fast Python package/version/project manager; replaces pip, venv, pyenv, pipx, poetry.

**VA-API** — The Linux hardware video decode/encode API used by browsers and players.

**VRR** — Variable refresh rate (FreeSync/G-Sync); stable on GNOME 50 and Plasma 6 Wayland.

**Wayland** — The modern display protocol replacing X11; GNOME 50 and Plasma 6.8 are Wayland-only.

**WSL2** — Windows Subsystem for Linux: a real Linux kernel in a lightweight VM on Windows; good enough for most development.

**X11 / Xorg** — The legacy display server; still used by Xfce and as **Xwayland** for compatibility inside Wayland sessions.

**x86-64-v3 / v4** — CPU feature levels (AVX2; AVX-512). Some distros (CachyOS; Ubuntu opt-in) ship packages compiled for them for modest performance gains.

**ZFS** — An advanced filesystem with an incompatible licence, shipped as an out-of-tree module; superb for NAS, fragile on rolling desktops.

**zram** — Compressed swap in RAM; the Fedora default; ideal for laptops.

**zypper** — openSUSE's package manager (`zypper dup` on Tumbleweed).
