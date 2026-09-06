# Chapter 17 — Myths, FAQ, and Migration

## 17.1 Myths, examined

**"Arch is unstable."** Arch is *rolling*, which means constantly changing. It is not *unreliable*: a maintained Arch install that follows the news breaks about as often as any other distro — the difference is that the breakage is visible and attributable, rather than a silent unfixed bug you live with for two years. The real cost of Arch is attention, not stability. (Chapter 4.)

**"Ubuntu is bloated / spyware / corporate junk."** Ubuntu's default install is comparable in size to Fedora's. The 2012 Amazon search lens is long gone; current telemetry is opt-in. Snaps are a legitimate annoyance and a legitimate engineering choice; they're removable. Canonical's governance is a fair thing to dislike; it does not make the OS bad. Ubuntu remains the best-supported Linux by third parties, which is worth a lot. (Chapter 6.)

**"Fedora is a beta for RHEL."** Fedora is where technologies debut before RHEL, which is different from being a testing ground *for* RHEL. It has its own release criteria, its own QA, and holds releases for blocker bugs (Fedora 44 slipped two weeks for exactly that). It is a polished, complete distro that happens to be ahead of the curve. (Chapter 6.)

**"Immutable distros can't be used for development."** Bluefin DX is arguably the *best* developer workstation for anyone whose work lives in containers, IDEs and browsers. The atomic model's real limitation is host-level hacking — kernel modules, low-level tooling — not "development." (Chapter 8.)

**"Linux can't game."** Steam's Linux share is 4–5%; the majority of the Windows catalogue runs via Proton; Valve's Steam Deck runs Arch. The genuine exception is a list of kernel-anti-cheat multiplayer titles whose publishers opt out. (Chapter 13.)

**"You need the terminal for everything."** A Mint, Ubuntu, Fedora or Bazzite user can go months without opening one. Developers *want* the terminal — that's different. Most system administration has a GUI (Settings, Software, Discover, Timeshift, Driver Manager, GNOME Disks…). The terminal is a superpower, not a requirement.

**"Wayland isn't ready."** GNOME 50 removed X11. Plasma 6.8 removes X11. Mint's Cinnamon declared Wayland stable. NVIDIA on Wayland works. The residual X11-only cases (some legacy remote-desktop, some accessibility tooling, a few ancient apps) are shrinking monthly. In 2026, "Wayland isn't ready" is a statement about 2021. (Chapter 2.)

**"Linux is more secure by default."** Linux is more *private* by default and its architecture is friendlier to securing, but a default desktop install with no firewall, an unconfined browser, and `curl | sh` habits is not meaningfully safer than a well-configured Windows machine. Do the Chapter 14 basics — FDE, firewall, sandboxing, updates — and *then* it is.

**"Rolling releases are for experts; LTS is for beginners."** Tumbleweed with Snapper and Bazzite/Bluefin are rolling-underneath and among the *easiest* distros to live with. Debian stable is LTS and among the least hand-holding. Release model and difficulty are only loosely correlated. (Chapter 4.)

**"Performance differs a lot between distros."** Same kernel, same Mesa, same compilers → same speed, within run-to-run noise. Exceptions: CPU-optimised rebuilds (CachyOS's x86-64-v3/v4; Ubuntu's opt-in amd64v3) and scheduler patches give single-digit gains in specific workloads; an old kernel/Mesa (Debian stable) can be measurably slower for gaming on new GPUs. For desktop and development work, you will not notice. (Chapter 1.)

**"You have to reinstall to upgrade."** Fedora's `dnf system-upgrade`, Ubuntu's `do-release-upgrade`, Debian's `apt full-upgrade`, and every rolling/atomic/declarative distro upgrade in place. Reinstalling at LTS boundaries is a *preference* some Ubuntu users have; it hasn't been necessary in a decade.

**"NVIDIA doesn't work on Linux."** It works well in 2026 on the 590/6xx series with open kernel modules, on Wayland, with VRR and HDR. What remains true: it's out-of-tree, so choose a distro that pre-builds the module (Ubuntu, Pop!_OS, Universal Blue, Arch `nvidia-open`) or accept a few minutes of DKMS after kernel updates. Pascal and older are now legacy. (Chapter 10.)

**"Linux Mint is only for beginners."** Mint's base is Ubuntu LTS; everything an engineer needs works identically. Its "beginner" reputation comes from excellent defaults, not from missing capability. Plenty of professionals run it because they want a computer that doesn't change.

**"macOS is Unix so it's the same as Linux for development."** Same shell, mostly. Different userland (BSD `sed`/`grep`/`find` flags), different filesystem semantics (case-insensitive by default), containers in a VM with slow file I/O, arm64 vs. the x86 servers your code runs on, no native `systemd`/`perf`/eBPF. Close enough for web development; a source of Friday-afternoon bugs for systems work.

**"Distro X is dying."** Every year someone declares Ubuntu, Fedora, Debian, Arch or openSUSE dead. All of them have been "dying" since before most readers were born. Actual deaths (Antergos, ArcoLinux, Mandriva, CentOS Linux, Solus's near-death) were small or corporate-driven. Pick from the top of Chapter 9's table and your distro will outlive your laptop.

## 17.2 FAQ

**Q: GNOME or KDE — just tell me.**
Try both live for an hour. If you can't: KDE Plasma. Nothing to unlearn, more features, fewer surprises.

**Q: I have an NVIDIA card. Which distro?**
Ubuntu 26.04 LTS or Pop!_OS if conventional; Bazzite/Bluefin/Aurora `-nvidia` if atomic; Fedora + RPM Fusion if you specifically want Fedora and accept a few minutes of akmod after kernel updates; CachyOS if Arch.

**Q: Should I dual-boot or go all-in?**
Dual-boot if you have *any* Windows-only requirement (proctoring, Adobe, Office desktop, specific games, iTunes/iPhone backups). Otherwise go all-in — you'll learn faster and the dual-boot partition will sit unused.

**Q: Can I try before I commit?**
Yes: **live USB** (Ventoy with several ISOs), **VM** (GNOME Boxes / virt-manager / VirtualBox on your current OS — good for the desktop feel, useless for judging hardware support), or **install to an external SSD** (real hardware, no changes to your internal disk).

**Q: How much disk?**
Linux alone: 40 GB minimum, 100 GB comfortable, more for Steam/ML datasets/VMs. Dual-boot: 100+ GB for Linux, keep Windows ≥ 80 GB.

**Q: Which filesystem?**
Btrfs if the installer offers it (snapshots). ext4 is fine and boring. Not ZFS on a laptop, not bcachefs yet.

**Q: Do I need swap?**
zram (compressed RAM swap; Fedora default) is enough for most. A swap file/partition ≥ RAM only if you want hibernate.

**Q: Snap or Flatpak?**
Flatpak, unless you're on Ubuntu and don't care — then snap is fine for the handful of apps that use it.

**Q: Should I remove snaps from Ubuntu?**
Only if they bother you. Many people don't notice them. If you do remove them, the procedure in Chapter 16 takes ten minutes.

**Q: Is the AUR safe?**
Mostly. Read the PKGBUILD; prefer popular, maintained packages; understand it's unsupported by Arch. Treat it like `npm`.

**Q: How often should I update?**
Rolling: weekly minimum. Point release: auto-security + weekly for the rest. Atomic: it does itself. Never the day before a deadline.

**Q: My laptop's WiFi/webcam/fingerprint doesn't work.**
Search "`<laptop model>` ArchWiki" first — even if you're not on Arch. Then linux-hardware.org. The fix is usually a newer kernel (→ Fedora/Arch-family/Tumbleweed/UBlue), a firmware package, or a known quirk.

**Q: Battery life is worse than Windows.**
Expected: 10–25% worse. `power-profiles-daemon` or TLP (not both), `powertop --auto-tune` to diagnose, check for a stuck process, disable the NVIDIA dGPU when unused. AMD laptops fare better.

**Q: Can I run Windows apps?**
Some: **Wine**/**Bottles**/**Proton** run many games and older apps well; **CrossOver** (paid Wine) adds support; Office 365 web replaces Office desktop; Adobe doesn't work. A Windows VM (GNOME Boxes, quickemu) handles the rest at the cost of RAM.

**Q: Is Linux good for a laptop I'll carry to class?**
Yes, with a supported model (Chapter 10). Sleep, WiFi, Bluetooth, gestures, fractional scaling all work on 2026 desktops. Test suspend on the live USB.

**Q: What about ChromeOS / a Chromebook with Linux?**
Crostini (ChromeOS's Linux container) is fine for light development and *is* the proctoring-compatible device. Chromebook hardware is usually too small (RAM/storage) for a main machine. Some Chromebooks can be converted to run full Linux (MrChromebox firmware) — a hobby.

**Q: Should I learn Arch to "understand Linux"?**
It's one way, and a good one — in a VM or on a second machine. You'll learn as much by running Fedora for a year and fixing things when they break, and you'll have a working laptop the whole time.

**Q: What if my university/employer only supports Windows?**
Run Linux anyway if nothing *technically* requires Windows; keep a Windows fallback for the things that do (proctoring, compliance agents). If IT *mandates* Windows on the device, use WSL2 and run your preferred distro on a personal machine.

**Q: Is NixOS worth it?**
For the person who values reproducibility and enjoys the model: overwhelmingly yes. For everyone else: try Nix on your current distro for a few months first. (Chapter 8.)

**Q: Fedora or Ubuntu?**
Fedora if you like current software and don't mind a yearly 30-minute upgrade. Ubuntu if you want five years of quiet, have NVIDIA/CUDA, or need to match a mandate. Both are excellent; the difference is smaller than the internet suggests.

**Q: Tumbleweed or Arch?**
Tumbleweed if you want rolling with a safety net and less news-reading. Arch if you want the AUR and the ArchWiki's exact match to your system.

**Q: I'm overwhelmed.**
Install Fedora KDE (or Ubuntu if NVIDIA). Use it for a semester. Revisit this guide afterwards; the rest will make sense then.

*(Continued: migration from Windows and macOS, keyboard and app equivalents, dual-boot detail, and when to switch distros.)*
