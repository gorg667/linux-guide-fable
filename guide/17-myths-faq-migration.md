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

## 17.3 Migrating from Windows

**Before you wipe anything:**
1. Inventory the software you actually use (check the Start menu and the taskbar, not your memory). For each: native Linux version? Web version? Good alternative? Wine? Or a hard Windows requirement? The last category decides dual-boot vs. all-in.
2. Export what's locked in: browser bookmarks/passwords (sync or export), Outlook PST files (convert or move to IMAP/web), Sticky Notes, iTunes/iPhone backups, game saves not in the cloud, licence keys, BitLocker recovery key, WiFi passwords.
3. Copy your documents to an external drive or cloud, *and verify the copy*.
4. Disable Fast Startup and (if dual-booting) shrink `C:` from Windows.

**App equivalents:**

| Windows | Linux |
|---|---|
| Edge/Chrome | Firefox, Chromium, Brave, Vivaldi, Edge (Linux build exists) |
| Office | LibreOffice / OnlyOffice / MS 365 web |
| Outlook | Thunderbird, Evolution (best Exchange), Outlook web |
| OneDrive | `onedriver`, `rclone`, web |
| Notepad++ | Kate, GNOME Text Editor, VS Code, Sublime Text (native) |
| Explorer | Files (GNOME), Dolphin (KDE), Nemo (Cinnamon) |
| Photos | Loupe/Gwenview (view), Shotwell/digiKam (manage), darktable (RAW) |
| Paint / Paint.NET | Pinta, Drawing, Krita (heavier) |
| Photoshop | GIMP 3, Krita, Photopea (web) — different tools |
| Premiere | Kdenlive, DaVinci Resolve (native), Shotcut |
| Audacity | Audacity/Tenacity (native) |
| 7-Zip / WinRAR | built into the file manager; `p7zip`, `unrar` |
| Notepad, Calculator, Snipping Tool | all built in (GNOME/KDE equivalents) |
| PowerToys | KDE has most built in; GNOME via extensions; `ulauncher`/`albert` for the launcher |
| Steam / Epic / GOG | Steam (native), Heroic |
| Discord / Slack / Zoom / Teams | native / native / native / PWA |
| WSL | you're on the real thing now |
| PuTTY / WinSCP | `ssh`, `scp`, `rsync`, or Files/Dolphin's built-in SFTP |
| Task Manager | System Monitor / Resources (GNOME), System Monitor (KDE), `btop` |
| Windows Defender | not needed (ClamAV exists for scanning files you'll pass to Windows users) |
| Regedit | `dconf-editor` (GNOME) / `kwriteconfig` (KDE) — you'll rarely need them |

**Habits that transfer and habits that don't:**
- `Ctrl+C/V/X/Z/A/S/F`, `Alt+Tab`, `Alt+F4` (or `Super+Q` on GNOME), `Win`/`Super` key opens the launcher — all the same.
- `Ctrl+Alt+T` opens a terminal on most desktops.
- **Drive letters** are gone: everything hangs off `/`. Your files live in `/home/you`. External drives appear under `/run/media/you/` or `/media/`.
- **File extensions don't determine executability**; the permission bit does. Case matters (`Report.pdf` ≠ `report.pdf`).
- **Installing software**: from the software center or package manager, not from downloaded `.exe`s. If a website tells you to download an installer, look for the distro package or Flatpak first.
- **No reboot after most updates** (only for kernel/firmware/some system libraries); no "Windows is updating, don't turn off your PC."
- **Antivirus is unnecessary** for normal use; the threat model is different (Chapter 14).
- **The middle-click pastes** the current selection (X11 primary selection, preserved on Wayland) — a delight once you know it.

**Timeline for a comfortable switch:** week 1 — everything is slightly wrong and you miss one app; week 2–4 — muscle memory rewires, you discover the software center and Flathub; month 2–3 — you stop noticing the OS; month 6 — you find Windows strange when you use it.

## 17.4 Migrating from macOS

Mac users have it easier in some ways (a Unix shell, `brew` already familiar) and harder in others (Apple's ecosystem lock-in is deeper).

**What transfers:** the terminal (`zsh`/`bash`, `ssh`, `git`), Homebrew (Linux version exists), most developer tooling, most cross-platform apps (VS Code, JetBrains, Slack, Zoom, Spotify, Firefox/Chrome, Obsidian, 1Password/Bitwarden), keyboard-driven workflows (GNOME's Super-key overview is spiritually close to Spotlight + Mission Control).

**What doesn't:** iMessage, FaceTime, AirDrop, iCloud (web only), Apple Music (web), Photos library (export first), Final Cut / Logic / Xcode, Safari (irrelevant), Time Machine (→ Pika/restic/Déjà Dup), Handoff/Continuity, Apple Watch unlock, Sidecar. If you're deep in these, keep a Mac around or accept the gap consciously.

**App equivalents:**

| macOS | Linux |
|---|---|
| Finder | Files / Dolphin |
| Spotlight | GNOME search (`Super`), KRunner (`Alt+Space`), `ulauncher` |
| Preview | Papers/Okular (PDF), Loupe/Gwenview (images) |
| Pages/Numbers/Keynote | LibreOffice / OnlyOffice; export to Office formats first |
| Notes | Apple Notes web is poor; migrate to Obsidian/Joplin/Standard Notes |
| Mail/Calendar | Thunderbird, Evolution, GNOME Calendar (CalDAV to iCloud works) |
| iTerm2 | Ghostty, Kitty, Ptyxis, Konsole |
| Raycast/Alfred | `ulauncher`, `albert`, KRunner |
| Rectangle/Magnet | built-in tiling in Plasma/GNOME (Tiling Shell) / COSMIC |
| Homebrew | Homebrew on Linux (same formulae for CLI tools) + the distro's package manager |
| Time Machine | Pika Backup / Déjà Dup / `restic` |
| Xcode | nothing — iOS development needs a Mac |
| Final Cut / Logic | Kdenlive/Resolve; Ardour/Reaper/Bitwig |

**Keyboard:** `Cmd` → `Ctrl` for most shortcuts, which is a real adjustment (your thumb wants `Cmd+C`). Options: retrain (two weeks), or remap `Ctrl` and `Super`/`Alt` at the desktop level (`keyd` or `xremap` do Mac-style remapping with per-app rules; Kinto.sh is the packaged solution). GNOME's `Super`-based shortcuts partly ease the transition. External Apple keyboards work (`hid_apple` module options swap `Fn`/`Cmd` behaviour).

**Trackpad:** GNOME on Wayland has the best gestures on Linux and comes closest to macOS; enable "tap to click" and adjust scroll direction. Plasma is good; less gesture-rich.

**Fonts and rendering:** Linux font rendering is good but *different* (no Apple-style heavy hinting/subpixel by default). Inter or SF Pro (if you have it) as the UI font, and confirm grayscale antialiasing with slight hinting, gets you most of the way. It stops being noticeable in a week.

**If you're on Apple Silicon:** Chapter 10 — Fedora Asahi Remix on M1/M2; wait on M3/M4.

## 17.5 Dual-boot decision detail

Chapter 16 §16.10 covers the mechanics. The decision:

| Situation | Recommendation |
|---|---|
| Proctoring software required | Dual-boot (or second device) — no alternative |
| Adobe / MS Office desktop / Autodesk / CAD | Dual-boot; these don't run on Linux |
| Specific anti-cheat games | Dual-boot; check areweanticheatyet.com for your games first |
| "Just in case" | Skip it. You won't boot into it, and it costs disk and complexity. Keep a Windows install USB and your licence for a true emergency. |
| Employer requires Windows on the device | Windows + WSL2 on that device; Linux on yours |
| Unsure | Install Linux to a second disk or external SSD; leave Windows untouched; decide in three months |

If you do dual-boot: separate disks if possible; Fast Startup off; BitLocker key saved; `set-local-rtc 1`; expect Windows to occasionally reset the boot order.

## 17.6 When to switch distros (and when not to)

**Switch when:**
- Hardware support is the problem and a newer kernel/fresher distro would fix it.
- Your needs changed category: you moved from "tinkerer" to "appliance" (→ Universal Blue), or vice versa (→ Arch-family), or you took a job that mandates Ubuntu.
- The distro's direction genuinely conflicts with yours (a governance decision you can't live with).
- You've given it three months and the *fundamental model* (rolling vs. LTS vs. atomic) is wrong for you — not the wallpaper.

**Don't switch when:**
- You dislike the desktop environment. Install the other DE or reinstall with the other edition of the *same* distro.
- A single app is missing. Flatpak/Distrobox/AppImage/Homebrew/a container will get it.
- An update broke something once. Roll back (snapshots!), report or search the bug, and continue. Every distro has this once a year.
- You're bored. Boredom is what a working computer feels like.
- Someone online said your distro is bad. Someone online says every distro is bad.
- You want to "learn Linux." Fix what's in front of you; that's learning Linux.

**The cheap way to scratch the itch:** a VM, a second SSD, or a Distrobox of the other distro. Try it for a month alongside; if you're still using it daily, migrate then.

---

### Key takeaways

- Most distro folklore is out of date: Arch's "instability" is attention cost; Ubuntu's "bloat" is snaps; Wayland is done; immutable distros develop fine; Linux games; NVIDIA works; performance differences are noise.
- FAQ headlines: KDE if you can't choose a DE; Ubuntu/Pop/Bazzite for NVIDIA; dual-boot only for a hard Windows requirement; Btrfs; Flatpak; weekly updates; search "`<laptop>` ArchWiki" for hardware issues; Fedora vs Ubuntu is smaller than the internet thinks.
- **From Windows:** inventory your software honestly, export what's locked in, expect two to four weeks of rewiring, install from the software center not from `.exe`s.
- **From macOS:** the terminal transfers, the ecosystem doesn't; `Cmd`→`Ctrl` is the real adjustment (or remap with `keyd`/Kinto); GNOME's gestures are the closest to home.
- Dual-boot for proctoring, Adobe/Office desktop, CAD, or anti-cheat titles; otherwise skip it.
- Switch distros for hardware, a category change in needs, or a fundamental model mismatch after three months — not for the DE, a missing app, one broken update, or boredom.
