# Chapter 12 — CS Student Specifics

A CS degree is four years of being told which tools to use by people who mostly assume Windows or macOS, punctuated by courses that assume Linux and are delighted you have it. This chapter is about surviving the first kind and thriving in the second.

## 12.1 Before the semester: the reconnaissance checklist

Do this in the week before classes, for *every* course:

1. **Read the syllabus for software requirements.** Look for: an IDE by name (Visual Studio ≠ VS Code; Eclipse; IntelliJ), a proctoring tool (LockDown Browser, Proctorio, Honorlock, Examplify, ProctorU), a specific OS ("Windows 10 or later"), a VM image (`.ova`, `.vmdk`, Vagrant box), a Docker image, MATLAB/Mathematica/SPSS/Stata, a specific compiler version.
2. **Find the department's environment.** Which distro and version do the lab machines and grading servers run? (Almost always Ubuntu LTS — 22.04 or 24.04 in 2026, some moving to 26.04.) What `gcc`/`python3`/`java` versions? Your submissions must work *there*.
3. **Ask the TA or course forum** if anything is unclear. "Does the autograder run on Ubuntu 24.04?" is a normal question.
4. **Check the exam format.** In-person on paper: no constraint. In-person on lab machines: no constraint. Online proctored: **hard constraint** — see §12.2.
5. **Check eduroam and VPN instructions** on the IT website — they'll have Linux steps or a CAT installer.

Ten minutes per course saves a panicked evening later.

## 12.2 Proctoring software: the immovable object

As of 2026, **no major exam-proctoring or lockdown tool officially supports Linux**, and none can be made to work reliably:

| Tool | Platforms | Linux? | VM? |
|---|---|---|---|
| **Respondus LockDown Browser** (+ Monitor) | Windows, macOS, iPadOS, ChromeOS | No | Detects and refuses |
| **Proctorio** | Chrome extension — Windows 10+, macOS 11+, ChromeOS | Officially no; sometimes runs in Chrome on Linux, not supported, may fail mid-exam | Detects |
| **Honorlock** | Chrome extension — Windows, macOS, ChromeOS | Officially no; same story as Proctorio | Detects |
| **ExamSoft Examplify** | Windows, macOS, iPad | No | Detects |
| **ProctorU / Meazure** | Windows, macOS | No | Detects |
| **Pearson VUE OnVUE** | Windows, macOS | No | Detects |
| **Safe Exam Browser** | Windows, macOS, iOS | No (open source, but no Linux build) | — |

They detect virtualization (CPUID, DMI strings, timing, device names) and refuse to run; spoofing is possible in principle, unreliable in practice, against every institution's academic-integrity policy, and *not worth the risk of an integrity violation over an OS preference*.

**Your realistic options:**

1. **Dual-boot Windows.** The standard answer. Costs ~40–60 GB of disk and a reboot before exams. Keep Windows minimal: updates, browser, the proctoring tool, nothing else. Details in Chapter 17. If your laptop shipped with Windows, the licence is in firmware and reactivates automatically.
2. **A second cheap device.** A used Windows laptop (~$150–250), a Chromebook (LockDown Browser and Proctorio both support ChromeOS), or a family member's machine. Many students prefer this — it keeps the Linux machine pristine and avoids boot-order dance.
3. **Campus resources.** Most universities have loaner laptops or testing centres with managed machines. Ask disability/accessibility services and the library; you don't need a disability to ask what's available.
4. **Windows-to-Go on a USB SSD.** Boot Windows from an external drive without touching the internal disk. Works; performance depends on the drive; some firmware fights it. A niche but valid option.

Decide before the first exam, not the night before. If *no* course uses proctoring — increasingly common as universities return to in-person exams — you can skip all of this.

## 12.3 Matching the department's environment

Your code must compile and run on the grader. Two ways to guarantee it:

**Run their distro in a container.**

```bash
# Distrobox: department runs Ubuntu 24.04
distrobox create --name cs --image ubuntu:24.04
distrobox enter cs
sudo apt update && sudo apt install build-essential gdb valgrind python3 openjdk-21-jdk
# Now compile and test here; your $HOME is shared, so edit with your host editor.
```

Or plain Docker/Podman with a bind mount, or a devcontainer if the course provides one (some do). This is *the* answer to "the TA says it compiles but my newer `gcc` gives different warnings" or "the autograder uses Python 3.12 and I have 3.14." It also means your *host* distro can be anything — Fedora, Arch, NixOS — while your *course* environment is exactly Ubuntu 24.04.

**Or run Ubuntu LTS as your host.** If you'd rather not think about it, install the same Ubuntu LTS the department uses. Zero translation. This is the strongest argument for Ubuntu in this guide, and it's a good one for students specifically.

Either way: **test your submission in the target environment before submitting.** `-Wall -Wextra -Werror` behaviour, `make` versions, shell differences (`sh` is `dash` on Ubuntu, not `bash`), line endings — all bite at the worst time.

## 12.4 Course-by-course

**Intro programming (Python, Java, C++, sometimes Racket/Scheme).** Trivial on Linux. Use `uv` for Python (match the course's version), SDKMAN for Java. If the course mandates an IDE: IntelliJ/PyCharm (Toolbox), Eclipse (works), VS Code (Microsoft's repo). **If the course mandates Visual Studio (the Windows IDE, for C# or C++), that's a Windows requirement** — dual boot, or negotiate with the instructor to submit via `dotnet` CLI/CMake (many accept it).

**Systems programming / C.** Linux's home turf. `gcc`, `clang`, `gdb` (with `pwndbg`/`gef` for niceties), `valgrind`, `strace`, `ltrace`, `perf`, `make`, `cmake`, AddressSanitizer/UBSan (`-fsanitize=address,undefined`). The course was probably designed on Linux; the instructor's Mac users are the ones suffering. Match the grader's `gcc` version via container if warnings matter.

**Computer architecture / assembly.** x86-64 assembly: `nasm`/`gas`, `gdb`. RISC-V (the modern teaching ISA): `gcc-riscv64-unknown-elf` / `riscv64-linux-gnu-gcc` (packaged on Ubuntu, Fedora, Arch, Nix), `qemu-system-riscv64`, **Venus** or **RARS** (Java simulators), **Ripes** (visual pipeline simulator, AppImage). ARM: `gcc-aarch64-linux-gnu` + QEMU. Logisim-evolution (Java) for digital logic; Verilator/Icarus/GTKWave for HDL. All packaged everywhere.

**Operating systems (xv6, Pintos, JOS, a custom kernel).** These need QEMU, a cross-compiler (xv6-riscv wants `riscv64-unknown-elf-gcc`; Pintos wants ancient x86 tooling), and `gdb` with target support. **Use the course's Docker image or a VM if provided** — Pintos in particular is notorious for needing a specific old toolchain. If you're building your own kernel, KVM acceleration (`-enable-kvm`) makes QEMU fast; make sure you're in the `kvm` group. This is also the course where an **atomic distro's read-only host is a mild annoyance** (you'll do everything in a Distrobox, which is fine) and where **NixOS shines** (a `flake.nix` with the exact cross toolchain).

**Networks.** Wireshark (add yourself to the `wireshark` group to capture without root), `tcpdump`, `iperf3`, `nmap`, `scapy` (Python), `netcat`, `socat`. **Mininet** is Ubuntu-native and fiddly elsewhere — run it in an Ubuntu VM (the course probably provides one) or a privileged Ubuntu container. GNS3/Packet Tracer for Cisco courses: Packet Tracer has a Linux `.deb`; GNS3 is Linux-native.

**Databases.** PostgreSQL, MySQL/MariaDB, SQLite, MongoDB, Redis — run every one in a container (`docker run -e POSTGRES_PASSWORD=x -p 5432:5432 postgres:17`), never on the host. DBeaver (Flatpak/`.deb`), pgAdmin, DataGrip (JetBrains). MS SQL Server: Microsoft ships a Linux container image. MS Access: no; the course will have to accept SQLite or LibreOffice Base.

**Machine learning / AI.** The one course where hardware dictates distro:

- **You have an NVIDIA GPU:** Ubuntu LTS (NVIDIA's documentation target), Pop!_OS NVIDIA ISO, or Fedora + RPM Fusion. Install the *driver* from the distro; install **CUDA-enabled PyTorch via `uv`** (`uv pip install torch --index-url https://download.pytorch.org/whl/cu128` or whatever the current tag is) — the wheel bundles the CUDA runtime; you do *not* need the system CUDA toolkit unless you compile CUDA C++. `nvidia-smi` should show the driver; `torch.cuda.is_available()` should be `True`.
- **You have an AMD GPU:** ROCm. Ubuntu 26.04 packages it (`apt install rocm`); PyTorch has ROCm wheels. Works on RDNA 3/4 discrete cards and select APUs; check AMD's support matrix — consumer GPU support is narrower than NVIDIA's.
- **You have Intel or no dGPU:** train on the department's cluster, Google Colab, Kaggle, or a cloud GPU. Your laptop runs Jupyter and edits code; the GPU is elsewhere. This is what most students end up doing regardless.
- **Apple M1/M2 under Asahi:** no GPU compute (the Metal-like APIs aren't exposed to Linux); CPU-only or remote.

Jupyter, `uv`, `ruff`, VS Code's notebook support or JupyterLab — all fine. Anaconda is heavy and slow; `uv` or `pixi` (conda-compatible, fast) are better in 2026.

**Compilers / programming languages.** OCaml (`opam`), Haskell (`ghcup`), Racket/Scheme (distro or Racket's installer), Rust (`rustup`), LLVM (distro `llvm-dev`/`llvm-devel` or the LLVM apt repo), ANTLR (Java), flex/bison. All straightforward.

**Software engineering / team projects.** Git, GitHub/GitLab, CI (GitHub Actions runs on Ubuntu — your Ubuntu-or-container setup matches), Docker, devcontainers. Linux is the natural habitat.

**Mobile.** Android Studio is Linux-native and works well (`kvm` group for the emulator; `adb` needs a udev rule or the `android-udev` package). **iOS requires Xcode requires macOS**; no workaround exists that's worth your time. If the course is iOS-specific, you need a Mac (borrow, lab, or cloud Mac rental for the semester).

**Graphics / game development.** OpenGL/Vulkan development is excellent on Linux (Mesa's debug tooling, RenderDoc, `vulkan-tools`). Godot: native, first-class. Unity: Linux editor exists, lower priority than Windows/mac, occasionally broken; workable. Unreal Engine: Linux builds exist (compile from source or download from Epic's GitHub), heavy, workable. Blender: excellent. If the course mandates Unity/Unreal and you have issues, a Windows dual-boot is the fallback.

**HCI / design.** Figma (web), Penpot (native/web), Inkscape, GIMP, Krita. Adobe: no (Photopea in a browser covers some cases; Wine + old Photoshop is a hobby). Balsamiq (web).

**Security / CTF.** Ghidra (Java), Burp Suite (Java), `pwntools`, `gdb` + `pwndbg`, `radare2`/Cutter, `binwalk`, Wireshark, Docker for challenge environments. **Do not install Kali as your daily OS.** Run Kali in a VM/container, or install the individual tools (Arch's BlackArch repo, Fedora's security lab packages, or `apt` on any Debian-family distro). Some CTF tooling is 32-bit or ancient; a Docker container per challenge is the clean pattern.

**Theory / math / writing.** LaTeX via **TeX Live** (the full scheme is ~7 GB; `texlive-latex-extra` + `texlive-fonts-extra` is usually enough) with TeXstudio, VS Code + LaTeX Workshop, or Overleaf (web). **Typst** is the modern alternative — fast, sane syntax, tiny install; increasingly accepted for assignments. Pandoc for Markdown → PDF. Zotero (native, `.deb`/Flatpak/AUR) for references. Obsidian/Logseq/Joplin for notes. SageMath, Jupyter, R/RStudio (RStudio has `.deb`/`.rpm`), MATLAB (Linux-native installer, works well; license via your school), Mathematica (Linux-native), SPSS (Linux-native, ugly), Stata (Linux-native).

## 12.5 Campus infrastructure

**eduroam.** NetworkManager handles 802.1X. The **eduroam CAT installer** (cat.eduroam.org) provides a Python script per institution that configures everything including the CA certificate — use it rather than hand-entering settings. If configuring manually: WPA2/WPA3 Enterprise, PEAP or TTLS (as your IT specifies), MSCHAPv2 inner auth, *always set the CA certificate* and domain match (leaving "no CA certificate is required" is a security hole and newer NetworkManager refuses it), identity `user@institution.edu`, anonymous identity `anonymous@institution.edu`.

**VPN.** Cisco AnyConnect → **OpenConnect** (`openconnect --protocol=anyconnect vpn.school.edu`; NetworkManager plugin `network-manager-openconnect-gnome` / `NetworkManager-openconnect`). Cisco Secure Client's *own* Linux build exists too and works. Palo Alto GlobalProtect → `openconnect --protocol=gp` or `gpclient`/`GlobalProtect-openconnect`. Fortinet → `openfortivpn`. WireGuard/OpenVPN → native. Ivanti/Pulse → `openconnect --protocol=pulse`. **Device-posture agents** (Cisco ISE posture, some Zscaler configurations) that require a Linux client may not exist — ask IT; sometimes there's a web-based exception path.

**Printing.** Campus print servers are usually CUPS/IPP (add via `ipp://print.school.edu/printers/name`), a web upload portal (PaperCut, Pharos), or "email it to the printer." All work. Some use PaperCut's client for authentication — it's Java and runs on Linux.

**Storage and collaboration.** OneDrive (most universities): web interface, `onedriver` (FUSE, on-demand), or `rclone` (sync). Google Drive: GNOME Online Accounts mounts it; `rclone` syncs it. Box: `rclone`. Institutional Git: fine. Teams: PWA (`teams.microsoft.com` installed as an app from Chromium/Edge/Firefox) or the community "Teams for Linux" Electron wrapper; both do calls and screen-share on Wayland. Zoom: native.

**Lockdown and MDM.** Some universities require device management (Intune, Jamf) for certain networks or services. Intune has a Linux agent (Ubuntu and RHEL only, officially). If your school requires enrolment for WiFi access and only supports Windows/mac, that's another dual-boot argument — but ask; usually there's a "BYOD/guest" tier that doesn't.

## 12.6 Budget and hardware for students

- **Used ThinkPads** (T480/T490/T14 Gen 1–3, X1 Carbon Gen 6–10, X13) — $200–500, excellent Linux support, upgradeable RAM on many T-series, matte screens, great keyboards. The canonical student Linux laptop.
- **Used Dell Latitude 7x00 / HP EliteBook 8x0 G6–G9** — similar story, slightly less community documentation.
- **Framework 13** if you can afford new and want it to last the degree (upgradeable mainboard).
- **M1 MacBook Air** (used, ~$400–500) with Fedora Asahi Remix — genuinely excellent, if you can live with the caveats (Chapter 10) and no x86 proprietary Linux software.
- **Avoid:** Chromebooks for a main machine (Crostini Linux containers are okay for light coding, but the hardware's storage/RAM is usually too small), Snapdragon X laptops, anything with soldered 8 GB.
- **RAM:** 16 GB. VMs for OS class and a browser with 40 tabs will not fit in 8 GB comfortably.
- **Disk:** 512 GB if dual-booting (Windows 60 GB + Linux 100 GB + your stuff), 256 GB is survivable for Linux-only.

Many universities have hardware grants, laptop loan programs, or student discounts (Framework, Lenovo, Dell all have education pricing). Ask.

## 12.7 Which distro for a student, specifically?

Pulling the threads together:

- **Default: Ubuntu 26.04 LTS** (or Kubuntu). Matches the department, matches the tutorials your classmates share, matches CI, has the smoothest NVIDIA/CUDA path, five years of support covers the whole degree. Remove snaps if they bother you. This is the *lowest-risk* choice for a student.
- **If you want fresher software and a bit more polish: Fedora** (Workstation or KDE), with an Ubuntu Distrobox for coursework that must match the department. Yearly upgrade is a 30-minute task during a break.
- **If you want zero maintenance during term: Bluefin DX / Aurora DX** (or Bazzite if you game). Course toolchains in Distrobox. Rollback if anything goes wrong. The atomic host is a mild nuisance only in the OS course.
- **If you're the tinkering kind and it's not a heavy semester: Arch via EndeavourOS or CachyOS**, with an LTS kernel fallback and Snapper snapshots. Learn a lot; accept the attention cost.
- **If someone else set it up for you and you just want it to work: Linux Mint.**
- **Regardless of distro: plan for proctoring** (§12.2), **match the grader** (§12.3), and **back up your coursework** (git for code; a synced folder or `restic` for everything else — Chapter 14).

---

### Key takeaways

- **Reconnaissance before the semester**: syllabus software requirements, the department's distro/toolchain versions, exam format, eduroam/VPN docs.
- **Proctoring software does not run on Linux and cannot be made to.** Dual-boot Windows, keep a cheap second device, or use campus machines. Decide before the first exam.
- **Match the grader**: run the department's Ubuntu in a Distrobox/Docker container, or run Ubuntu LTS as your host. Test submissions in the target environment.
- Nearly every CS course is Linux-friendly; the exceptions are Visual Studio proper, Xcode/iOS, Adobe, MS Access, and Unity/Unreal edge cases — all Windows/macOS requirements, not distro choices.
- **ML with a GPU**: NVIDIA + Ubuntu/Pop!_OS/Fedora with distro driver and `uv`-installed CUDA PyTorch; AMD + Ubuntu 26.04 ROCm; otherwise use the cluster/Colab.
- eduroam (CAT installer), campus VPNs (OpenConnect and friends), printing and OneDrive/Teams all work on Linux.
- Used ThinkPads are the student's best hardware; 16 GB RAM; 512 GB if dual-booting.
- **Student default: Ubuntu LTS.** Fedora for freshness, Bluefin/Aurora DX for zero maintenance, Arch-family for tinkerers in a light semester, Mint for hands-off.
