# Chapter 3 — Requirements: What a SWE, a CS Student, and a Daily Driver Actually Need

Before evaluating candidates, write down the requirements. This sounds obvious; almost nobody does it. They pick a distro on vibes and then discover, three weeks in, that their networking course needs a kernel module the distro doesn't ship, or that the exam software has never heard of Linux.

This chapter enumerates the needs of each of the three roles, notes where they agree and where they fight, and ends with a ranked criteria list that later chapters use to score distributions.

## 3.1 The software engineer

### Non-negotiables

**Toolchain availability and currency.** You need compilers, runtimes and SDKs — often *specific versions*, and often *several versions at once* (the project at work is on Python 3.11 and Node 20; your side project is on 3.13 and 24). No distribution's repositories solve this well; it's a job for language version managers (`uv`, `mise`/`asdf`, `rustup`, `fnm`, `sdkman`, `ghcup`) and containers. What the distro *does* affect is whether the base toolchain (system `gcc`, `glibc`, `cmake`, `git`, `openssl`) is new enough to build these tools and their native extensions. An LTS with a three-year-old `gcc` occasionally bites (a Rust crate needs a newer `clang`; a Python wheel needs a newer `glibc`); a rolling distro never has this problem but occasionally has the opposite one (a new `gcc` breaks an old project's build).

**Containers, first-class.** Docker or Podman, running natively (not through a VM as on macOS/Windows — a genuine Linux advantage for performance and simplicity). Rootless mode. Compose. Possibly a local Kubernetes (kind, minikube, k3s). Every distro does this; Fedora/RHEL family push Podman, Debian/Ubuntu default to Docker via Docker's own repo, and atomic distros build their entire dev story around containers.

**Editors and IDEs.** VS Code (Microsoft ships `.deb`/`.rpm` and a repo; also a Flatpak and Snap, both with sandbox friction around terminals and toolchains), JetBrains (Toolbox app, distro-agnostic), Neovim/Emacs/Helix (everywhere), Zed (native Linux builds), Cursor/Windsurf and other VS Code forks (AppImage or `.deb`). All work on all distros; the only friction is Flatpak sandboxing for people who insist on Flatpak IDEs.

**Terminal-centric workflow.** A good terminal emulator, a shell you like, `tmux`/`zellij`, `ssh`, `git`. Trivially available everywhere; this is Linux's home turf.

**Stability during work hours.** If you're paid to ship, an update that breaks your display driver at 9 a.m. on release day costs real money. This argues for: point releases over rolling, or rolling *with* a snapshot/rollback mechanism, or an atomic distro. It also argues for *not* updating the day of a big milestone. Discipline matters more than distro here, but the distro determines how bad the failure mode is.

**Multi-monitor, HiDPI, docking.** A modern laptop workflow — dock, two external monitors at mixed DPI, hot-plug. This is a *desktop environment* concern (GNOME and KDE on Wayland handle it well; per-monitor fractional scaling is stable in both) and a *GPU driver* concern (AMD/Intel: flawless; NVIDIA: fine since the 590 series on Wayland, occasional glitches with some docks).

**Corporate integration (for the employed).** VPNs (WireGuard, OpenVPN, OpenConnect for Cisco AnyConnect and GlobalProtect all work; some proprietary VPN clients ship only `.deb`), SSO (browser-based, fine), device management/compliance agents (if your employer requires Intune, CrowdStrike, Jamf-equivalents — check what they support; usually it's Ubuntu LTS and RHEL only, sometimes Fedora), Zoom/Teams/Slack (Chapter 13). **If your employer publishes a list of supported Linux distros, that list is your shortlist.** Almost always it's Ubuntu LTS.

### Strongly desired

- **Reproducible dev environments** — devcontainers, Nix shells, Distrobox. Nix has the strongest story; everything else is convention plus Docker.
- **Fast package manager and short update times** — matters when you update daily. `pacman` and `dnf5` are quick; `apt` is fine; `nix` rebuilds can be slow.
- **Good documentation to search when stuck** — ArchWiki (applies to every distro), Ubuntu's sheer volume of Q&A, Fedora's docs and Ask Fedora, NixOS's wiki (improving but scattered).
- **A sane, predictable filesystem layout** — matters for tools that assume FHS paths. NixOS violates FHS (no `/usr/bin/python3`, no `/lib64/ld-linux-x86-64.so.2`), which breaks pre-compiled binaries downloaded from the internet unless you use `nix-ld` or `steam-run`. Atomic distros keep FHS but make `/usr` read-only. Everything else is standard.
- **GPU compute** for the growing number of engineers doing local ML: CUDA (NVIDIA), ROCm (AMD — Ubuntu 26.04 packages it natively; Fedora has partial packaging; elsewhere it's AMD's repos), or oneAPI (Intel).

### Nice to have

- Aesthetics you enjoy looking at for ten hours a day.
- Tiling window management (if you're that kind of person).
- Low idle resource usage (matters less than people think on 16+ GB machines; matters a lot on 8 GB).

## 3.2 The CS student

Students have every need above, at lower intensity, plus a set of *constraints* that professionals don't face.

### The hard constraints

**Proctoring and lockdown software.** Respondus LockDown Browser, Proctorio, Honorlock, ExamSoft Examplify, Pearson VUE OnVUE, ProctorU. As of 2026 **none of them support Linux**, and the ones that are browser extensions (Proctorio, Honorlock) officially list Windows/macOS/ChromeOS only even though Chrome-on-Linux sometimes works. They detect virtual machines and refuse to run in one. **This is the single most consequential constraint for students, and no distro choice fixes it.** Your options:

1. Dual-boot Windows on the same machine (most common; costs ~40 GB and some boot-order annoyance).
2. Keep a second, cheap device — an old laptop or a Chromebook — for exams.
3. Use university-provided lab machines or loaner laptops for proctored exams (ask; many schools have them).
4. A Windows VM with heavy anti-detection tweaks — unreliable, against the terms of service, and can get you accused of cheating. **Don't.**

Find out *before the semester* which of your courses use proctoring. If none do, you're free. If some do, plan for option 1, 2 or 3 now.

**Department-mandated software.** Some courses require specific tools: MATLAB (Linux-native, works well, license via your school), Mathematica (Linux-native), Autodesk/SolidWorks (Windows only — mostly engineering, not CS), Visual Studio proper (Windows only; VS Code is not the same thing and some intro courses in C# or C++ assume the real one), Xcode (macOS only — iOS courses), Adobe Creative Suite (no Linux; relevant to HCI/design-adjacent courses), Microsoft Access (no), specific Java IDEs (all Linux-native), Android Studio (Linux-native and excellent), Unity (Linux editor exists, less polished than Windows/mac), Unreal (Linux builds exist, you compile from source, heavy), Godot (native). Check each syllabus.

**Department-mandated *distros*.** Many CS departments run their lab machines and grading servers on a specific distro — usually Ubuntu LTS, sometimes Debian, RHEL, or Fedora. Your code must compile and run *there*. This does not mean you must run the same distro (Docker or Distrobox reproduces it exactly), but it makes Ubuntu LTS the path of least surprise, and it means you should know how to test against the department's toolchain versions regardless of your desktop distro.

**Campus network.** **eduroam** (802.1X/WPA2-Enterprise with certificate validation) works on every distro through NetworkManager; the eduroam CAT installer is a Python script that runs on Linux. Campus VPNs are usually Cisco AnyConnect (→ `openconnect`, in every repo, works), GlobalProtect (→ `openconnect --protocol=gp` or `gpclient`), or FortiClient (→ `openfortivpn`). Campus printing is usually IPP/CUPS with a print server or a web upload — fine. Some universities require a "device posture" agent (Cisco Secure Client posture module, Ivanti) that may be Windows/mac only — check.

**Office documents and collaboration.** You will be sent `.docx` and `.pptx` files and expected to return them without mangling. LibreOffice handles this well but not perfectly (complex formatting, tracked changes, and fonts drift). OnlyOffice's rendering is closer to MS Office. **Microsoft 365 web** works fully in Firefox/Chromium and is the safest route for anything a professor will grade. Google Docs works. OneDrive has no official client; `onedriver` and `rclone` work. Fonts: install `ttf-mscorefonts-installer` (Ubuntu) or the metric-compatible Liberation/Carlito/Caladea fonts (installed by default on most distros) to keep layouts from shifting.

**Budget hardware.** Students often run older or cheaper machines: 8 GB RAM, integrated graphics, a used ThinkPad. This favours lighter desktops (Xfce, LXQt, Cinnamon, or GNOME/KDE with restraint), ext4 or Btrfs without heavy compression, and distros that don't preload much. It also *favours Linux itself* — a 2018 laptop runs Fedora far better than Windows 11.

### Coursework-specific technical needs

| Course type | What it needs | Distro implications |
|---|---|---|
| Intro programming (Python/Java) | Interpreter/JDK, an IDE | Any distro. Use `uv`/`sdkman` rather than distro packages so your versions match the course. |
| Systems programming (C/C++) | `gcc`/`clang`, `gdb`, `valgrind`, `make`/`cmake`, sanitizers, `perf` | Any. Newer `gcc` on rolling distros may emit *different warnings* than the grader's — test in a container matching the department's distro. |
| Computer architecture / assembly | RISC-V or ARM cross-toolchains, QEMU, Verilator, sometimes Logisim | Arch/AUR and Nix have the widest cross-toolchain packaging; Ubuntu has `gcc-riscv64-unknown-elf`. All fine. |
| Operating systems (xv6, Pintos, own kernel) | QEMU, cross-compilers, `gdb` with target support, sometimes a specific old toolchain version | Same as above. Pintos in particular assumes ancient tooling; use the course's Docker image. |
| Networks | Wireshark (needs `usermod -aG wireshark`), Mininet (Ubuntu-centric; VM recommended), `iperf`, `tcpdump`, `scapy` | Ubuntu LTS is Mininet's native home; a VM works from any host. |
| Databases | PostgreSQL, MySQL/MariaDB, SQLite, MongoDB, DBeaver | Any; run DBs in containers. |
| Machine learning / AI | Python, Jupyter, PyTorch/JAX/TensorFlow, **CUDA** (NVIDIA) or **ROCm** (AMD) | **The GPU driver is the decision.** NVIDIA: Ubuntu LTS is what NVIDIA documents first; Fedora + RPM Fusion works; Arch works; Pop!_OS NVIDIA ISO is the lowest-friction. ROCm: Ubuntu 26.04 native packages. Or use the cloud/lab GPUs and keep the laptop simple. |
| Compilers | OCaml, Haskell, Racket, or LLVM | All packaged everywhere; `opam`/`ghcup` are distro-agnostic. |
| Mobile (Android) | Android Studio, emulator (needs KVM: `/dev/kvm` access) | Any distro; add yourself to the `kvm` group. |
| Mobile (iOS) | Xcode | macOS only. No distro helps. |
| Graphics / game dev | OpenGL/Vulkan dev libs, Godot, Blender, possibly Unity/Unreal | AMD/Intel Mesa drivers are excellent for graphics dev; NVIDIA fine. Unity/Unreal Linux editors work but are second-class. |
| HCI / UX | Figma (web), Penpot (native/web), Inkscape, GIMP; Adobe = no | Any distro. |
| Theory / math | LaTeX (TeX Live), Typst, Sage, Jupyter, Mathematica, MATLAB, R | TeX Live is huge (~7 GB full); Typst is small and modern. All distro-agnostic. |
| Security / CTF | Burp, Ghidra, `pwntools`, `gdb-peda`/`pwndbg`, Docker for challenges, Kali tools | Kali is *not* a daily driver; use Kali in a VM/container or install tools individually. Arch's AUR / BlackArch repo has everything. |

**Notice:** almost every row says "any distro." The student's needs push toward *Ubuntu LTS for compatibility with course materials* and toward *whatever runs CUDA cleanly* for ML — and otherwise don't discriminate.

### Soft needs specific to students

- **Time.** You have less of it than you think. A distro that eats a weekend per month in maintenance is a bad trade during term.
- **Peer support.** If your classmates run Ubuntu, Ubuntu-specific advice ("run `sudo apt install ...`") will be what circulates in the group chat. Translating is easy once you know the mapping (Chapter 11 has one), but it's friction.
- **Resume value.** Marginal. "Comfortable with Linux" on a CV is the same whether it was Fedora or Gentoo. What matters is that you *are* comfortable — knowing systemd, containers, shell, SSH and one package manager well.

## 3.3 The daily driver

Everything a person expects from a computer, none of which has anything to do with programming.

- **Web browsing** with DRM video (Widevine for Netflix/Spotify/Prime — Firefox and Chromium both ship it on x86-64; 1080p max on most services regardless of distro; 4K is not available on Linux browsers), hardware video decode (works in Firefox and Chromium on AMD/Intel with VA-API; NVIDIA needs an extra library), and extensions/password managers.
- **Media codecs.** H.264/H.265/AAC playback. Ubuntu/Mint/Arch/Debian: works out of the box or with a single "restricted extras" package. Fedora and openSUSE: legal caution means you enable RPM Fusion (Fedora) or Packman (openSUSE) and swap `ffmpeg` — a 2-minute, well-documented step that trips up newcomers.
- **Gaming.** Steam + Proton runs the majority of the Windows game catalogue (ProtonDB tracks it). Blockers are kernel-level anti-cheat games whose publishers opt out (a subset of competitive multiplayer titles) — no distro fixes that. Linux was 4–5% of Steam users in 2026. AMD GPUs are the smoothest; NVIDIA fine; distro matters little except that Bazzite and CachyOS pre-tune everything.
- **Video calls.** Zoom (native `.deb`/`.rpm`/Flatpak; screen-share works on Wayland via portal), Teams (PWA in browser; the "Teams for Linux" client is community), Google Meet (browser), Slack/Discord (native/Flatpak; Wayland screen-share works with modern versions). Webcam support is universal *except* Intel IPU6 MIPI webcams on some 2022–2024 laptops, which need extra firmware and work best on new kernels.
- **Office.** Covered above; LibreOffice/OnlyOffice/web.
- **Printing and scanning.** Driverless IPP Everywhere / AirPrint printers "just work" via CUPS on every distro. Old USB printers may need a vendor driver (HP: `hplip`, packaged everywhere; Brother: `.deb`/`.rpm` from Brother; Canon: mixed). Scanning via SANE, `simple-scan`/`skanpage`.
- **Bluetooth audio.** PipeWire handles LDAC/AAC/aptX/SBC-XQ. Multipoint headphones and AirPods work (basic profiles). Microphone quality on Bluetooth headsets is poor on *every* OS (HFP codec) — mSBC helps; LE Audio is arriving.
- **Phone integration.** KDE Connect (KDE and, via GSConnect, GNOME) does notifications, file transfer, clipboard, remote input, SMS from an Android phone. iPhone: very limited on every non-Apple platform.
- **Cloud storage.** Nextcloud (first-class), Dropbox (official client, works), Google Drive (GNOME Online Accounts mounts it; `rclone` for sync), OneDrive (`onedriver`, `rclone`, or web), iCloud (web only, painful).
- **Display niceties.** Fractional scaling (stable in GNOME 50 and Plasma 6), VRR (stable), HDR (Plasma 6 has it; GNOME 50 has the plumbing and it's arriving), night light, mixed-DPI multi-monitor.
- **Power management.** Sleep/resume reliability (mostly a firmware and kernel-version issue), battery life (Linux is typically 10–25% behind Windows on the same laptop; `power-profiles-daemon` or TLP close some of the gap; AMD laptops fare better than Intel lately), hibernate (works with setup; unreliable on some firmware).
- **Fonts and rendering.** Fine everywhere; Ubuntu and Fedora ship good defaults; Arch requires you to install fonts.
- **Backups.** Time Machine-like tooling: Déjà Dup (GNOME), Kup/Pika Backup, Btrfs snapshots (Snapper/Timeshift), `borg`/`restic` for the terminal-inclined.
- **Accessibility.** GNOME leads; Orca screen reader got a major overhaul in GNOME 50.

The daily-driver dimension favours **polished, integrated, popular** distros — the kind with a large user base reporting and fixing the thousand small papercuts. It disfavours niche distros regardless of their technical elegance.

## 3.4 Where the roles agree

- **Wayland-native modern desktop** — everyone benefits; the debate is over.
- **Containers** — the engineer needs them; the student needs them to match course environments; the daily driver benefits indirectly (Distrobox for weird apps).
- **Flatpak for GUI apps** — nice sandboxing, always current, distro-independent.
- **Current-ish kernel** — new hardware, better power management, better GPU drivers. Everyone wants this unless they're on a five-year-old machine that's already fully supported.
- **Btrfs snapshots or atomic rollback** — everyone wants "undo" for the one update a year that goes wrong.
- **Popularity** — more users means more fixed bugs, more Q&A, more vendor testing. This is the underrated argument for Ubuntu and Fedora over technically similar smaller distros.

## 3.5 Where the roles conflict

**Freshness vs. deadline safety.** The engineer wants a recent `gcc`; the student wants nothing to change the week of finals; the daily driver wants the newest Mesa for a game. Resolution: pick a *base* that's stable enough (Fedora, Ubuntu LTS, or atomic), and get freshness from Flatpak, Distrobox, and language managers — *or* pick rolling with snapshots and adopt a personal "no updates in the 72 hours before a deadline" rule.

**Tinkering vs. time.** The engineer's curiosity about NixOS vs. the student's need to finish the OS assignment. Resolution: tinker in a VM or on a second disk; daily-drive something boring during term.

**NVIDIA for CUDA vs. everything else.** ML students and engineers want CUDA, which means NVIDIA, which means the one GPU vendor whose driver is out-of-tree and periodically breaks on kernel updates. Resolution: Ubuntu LTS or Pop!_OS with pre-integrated drivers, or an atomic `-nvidia` image (Bluefin/Bazzite) where the driver is baked into the tested image, or do GPU work remotely and keep the laptop AMD/Intel.

**Proctoring vs. Linux at all.** Irreconcilable. Dual boot or second device.

**Corporate compliance vs. choice.** If IT says Ubuntu 24.04/26.04 LTS, it's Ubuntu. Run whatever you want on a personal machine.

## 3.6 The ranked criteria

Distilling all of the above into criteria we'll actually score against in Chapter 9, weighted by how much they matter to the *combined* SWE + student + daily-driver persona:

| # | Criterion | Weight | Why |
|---|---|---|---|
| 1 | **Hardware support out of the box** (kernel currency, firmware, GPU drivers incl. NVIDIA path, WiFi, webcam, sleep) | ★★★★★ | A machine that doesn't work is worth nothing. |
| 2 | **Stability / low breakage rate of updates** and **quality of the rollback story** | ★★★★★ | Deadlines. Money. Sanity. |
| 3 | **Ecosystem gravity** — third-party software availability, tutorials, vendor support, employer/university compatibility | ★★★★☆ | Removes friction everywhere else. |
| 4 | **Desktop polish and integration** (Wayland, HiDPI, portals, PipeWire, screen sharing, Bluetooth, printing) | ★★★★☆ | Daily-driver quality of life. |
| 5 | **Software freshness** (kernel, Mesa, toolchains, desktop) | ★★★☆☆ | Important, but increasingly solvable outside the distro. |
| 6 | **Package manager & repository breadth** (incl. AUR/nixpkgs/Flathub integration) | ★★★☆☆ | Convenience; Distrobox flattens the difference. |
| 7 | **Maintenance burden** (how many hours/year you spend keeping it running) | ★★★☆☆ | Time is the scarcest resource for students and engineers alike. |
| 8 | **Support lifecycle & upgrade path** (how long before a forced major upgrade; how painful) | ★★★☆☆ | Matters for "install and forget" users. |
| 9 | **Security defaults** (FDE ease, Secure Boot, MAC, firewall, sandboxing) | ★★☆☆☆ | All mainstream distros are acceptable; differences are in defaults. |
| 10 | **Documentation & community quality** | ★★☆☆☆ | When things go wrong. |
| 11 | **Governance & project health** (funding, bus factor, drama) | ★★☆☆☆ | Long-term viability. |
| 12 | **Performance** | ★☆☆☆☆ | Real but small; only gaming and compile-heavy workloads notice. |
| 13 | **Aesthetics / "vibe"** | ★☆☆☆☆ | Fixable in an afternoon. |

Opinionated readers will want to re-weight. That's the point: the framework is more valuable than my weights. Chapter 9 provides the scores and shows how the ranking shifts when you change them.

---

### Key takeaways

- Engineers need: current-enough toolchains (solved mostly by version managers and containers), first-class containers, stability during work hours, good multi-monitor/HiDPI, and whatever their employer's IT supports (usually Ubuntu LTS).
- Students need all that at lower intensity **plus** a Windows/macOS fallback for proctoring software, compatibility with the department's (usually Ubuntu) toolchain, eduroam and campus VPN (fine everywhere), and Office-document round-tripping (use web Office or OnlyOffice for graded work).
- Daily drivers need codecs, DRM, gaming, video calls with screen-share, printing, Bluetooth audio, phone integration, cloud storage, and battery/sleep — all of which favour popular, polished, integrated distros.
- The roles agree on Wayland, containers, Flatpak, a current kernel, snapshots/rollback and popularity. They conflict on freshness vs. deadline safety (solve with a stable base + fresh userland, or rolling + snapshots), tinkering vs. time, NVIDIA for CUDA vs. driver fragility, and proctoring vs. Linux at all.
- Top-weighted criteria: hardware support, update stability/rollback, ecosystem gravity, desktop polish. Performance and aesthetics barely register.
