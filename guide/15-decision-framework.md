# Chapter 15 — The Decision Framework

Everything before this chapter was evidence. This chapter is the verdict — or rather, the procedure that produces *your* verdict. It has three parts: a **decision tree** you can walk in five minutes, **twelve personas** with a specific recommendation each, and **the default answer** for when you still can't decide.

## 15.1 The decision tree

Start at the top. Each question eliminates options. Stop at the first leaf you reach — it's your primary recommendation; the "also consider" is your second choice.

```
START
│
├─ Q0. Is there a hard external mandate?
│   (employer/university says "X"; software only supports "X")
│   ├─ YES → Use X. (It's almost always Ubuntu LTS.) Run anything else in a VM or on a second machine. STOP.
│   └─ NO  → continue
│
├─ Q1. What is your hardware?
│   ├─ Apple Silicon M1/M2 → Fedora Asahi Remix. STOP.
│   ├─ Apple Silicon M3/M4/M5 → macOS + Linux VM/remote; revisit in 2027. STOP.
│   ├─ Snapdragon X → Windows + WSL2. STOP.
│   ├─ NVIDIA GPU (Turing or newer) → set NVIDIA=yes, continue
│   ├─ NVIDIA GPU (Pascal or older) → set NVIDIA=legacy, continue (and plan a GPU upgrade)
│   ├─ Laptop released < 6 months ago → set NEW_HW=yes, continue
│   └─ AMD/Intel, ≥ 6 months old → continue
│
├─ Q2. Will you need to run proctoring software (LockDown Browser, Proctorio, Examplify…)?
│   ├─ YES → Plan a Windows dual-boot or second device NOW. Continue for the Linux side.
│   └─ NO / DON'T KNOW → continue (find out before the first exam)
│
├─ Q3. How do you feel about administering your own computer?
│   ├─ "I want it to be an appliance. Update itself, never break, I never think about it."
│   │   → go to APPLIANCE
│   ├─ "I'm happy to do occasional maintenance; I want a normal, mutable system."
│   │   → go to CONVENTIONAL
│   └─ "I enjoy it. I want to understand and control everything."
│       → go to ENTHUSIAST
│
├─ APPLIANCE
│   ├─ Do you do kernel/driver/low-level systems work, or an OS course this year?
│   │   ├─ YES → the atomic host will fight you; go to CONVENTIONAL instead
│   │   └─ NO  → continue
│   ├─ GNOME or KDE? (try both live — Chapter 5)
│   │   ├─ GNOME → Bluefin (Bluefin DX if you're a developer)
│   │   ├─ KDE   → Aurora (Aurora DX if developer); Bazzite if you game a lot
│   │   └─ Don't care → Aurora DX / Bazzite
│   ├─ NVIDIA=yes → pick the `-nvidia` image variant
│   └─ STOP. Also consider: Ubuntu LTS (long support, conventional) if the atomic model worries you.
│
├─ CONVENTIONAL
│   ├─ Q4. Freshness vs. quiet: which sentence is more you?
│   │   ├─ "I want current kernel/toolchains/desktop; I'm fine upgrading yearly."
│   │   │   → go to FRESH
│   │   └─ "I want it to stay the same for years; I'll get new tools via containers/version managers."
│   │       → go to STABLE
│   │
│   ├─ FRESH
│   │   ├─ NVIDIA=yes and you want zero driver thought → Ubuntu 26.04 LTS (see STABLE) or Pop!_OS NVIDIA ISO
│   │   ├─ Prefer a rolling release with a safety net → openSUSE Tumbleweed (Snapper rollback built in)
│   │   ├─ Otherwise → Fedora Workstation (GNOME) or Fedora KDE Plasma Desktop
│   │   │   (NVIDIA=yes: add RPM Fusion akmod-nvidia; wait a few days after kernel majors)
│   │   └─ STOP. Also consider: Tumbleweed ↔ Fedora as each other's alternates.
│   │
│   └─ STABLE
│       ├─ Is this for a newcomer / non-technical user / "make it feel like Windows"?
│       │   ├─ YES → Linux Mint (Cinnamon). STOP. Also consider: Zorin OS.
│       │   └─ NO → continue
│       ├─ GNOME or KDE?
│       │   ├─ GNOME → Ubuntu 26.04 LTS
│       │   ├─ KDE   → Kubuntu 26.04 LTS
│       │   └─ Don't care → Ubuntu 26.04 LTS
│       ├─ Object to snaps? → remove snapd + add Flathub (10 min), or pick Mint / Debian instead
│       ├─ Want volunteer governance and maximum conservatism? → Debian 13 (add backports kernel if NEW_HW)
│       ├─ NVIDIA=yes → Ubuntu's driver checkbox handles it; you're done
│       └─ STOP. Also consider: Fedora if the two-year staleness starts to bite.
│
└─ ENTHUSIAST
    ├─ Q5. Do you want declarative/reproducible configuration above all?
    │   ├─ YES → Have you used Nix on another OS for a few months?
    │   │   ├─ YES → NixOS. STOP.
    │   │   └─ NO  → Install Nix + Home Manager on Fedora/Arch first; revisit NixOS in six months.
    │   └─ NO → continue
    ├─ Q6. Arch it is. How much hand-holding?
    │   ├─ None; I want the manual install as a learning experience → Arch Linux (wiki install)
    │   ├─ Installer + sane defaults, minimal deviation from Arch → EndeavourOS
    │   ├─ Installer + snapshots + performance tuning + gaming → CachyOS
    │   ├─ Pre-built tiling desktop, opinionated → Omarchy
    │   └─ No systemd → Artix (Arch) or Void (independent)
    ├─ NVIDIA=yes → `nvidia-open` + `linux-lts` fallback; NVIDIA=legacy → `nvidia-580xx-dkms` (AUR)
    ├─ Set up Snapper/Timeshift + an LTS kernel before anything else.
    ├─ Heavy semester or critical work deadline this term? → consider Fedora/Tumbleweed instead and come back.
    └─ STOP. Also consider: openSUSE Tumbleweed (the "grown-up rolling") or Fedora as the fallback.
```

A Mermaid rendering of the same tree is in `guide/assets/decision-tree.mmd` for people who like diagrams.

## 15.2 Twelve personas

Each is a real pattern I've seen many times. Find the one closest to you.

### 1. The first-time switcher from Windows
*"I'm tired of Windows. I want something that works, looks vaguely familiar, and won't make me learn a new way to do everything. I'll write code, browse, watch stuff, maybe game."*

**Pick: Linux Mint (Cinnamon).** Second: Kubuntu 26.04 LTS. Third: Zorin OS.
Why: Mint's defaults, Update Manager with Timeshift, Driver Manager, and no-snap Ubuntu base produce the fewest surprises. Cinnamon looks like Windows 7 grew up. Everything Ubuntu applies.
Watch out for: wanting HDR/gestures/new-desktop features (Mint is conservative); a brand-new laptop (wait for a point release or use Kubuntu). Add Flathub apps freely. If you find yourself wanting more after six months, Fedora KDE is the natural next step.

### 2. The macOS refugee
*"I've used a Mac for years. I like coherence, gestures, and things just working. I don't want to tinker. I might miss iMessage."*

**Pick: Fedora Workstation (GNOME).** Second: Bluefin. Third: Ubuntu 26.04 LTS.
Why: GNOME's workflow (Super key, overview, gestures, minimal chrome) is the closest to macOS's spirit; Fedora ships it pristine on a current kernel with excellent trackpad support. Bluefin is the same with even less to manage and a Mac-like dock out of the box.
Watch out for: no iMessage/FaceTime/AirDrop — nothing fixes this; use KDE Connect (via GSConnect) if you have an Android phone, and accept the gap otherwise. Fractional scaling is fine. Install `gnome-tweaks` for the minimise button if you must.

### 3. The NVIDIA owner who games and codes
*"RTX 4070, I play a lot, I also do web dev and some Python. I want the games to run and the driver not to break."*

**Pick: Bazzite (`-nvidia` image) if you like the appliance model; Ubuntu 26.04 LTS or Pop!_OS NVIDIA ISO if you want conventional.** Third: CachyOS (its installer handles NVIDIA; tuned kernel; more maintenance).
Why: Bazzite bakes the driver into a tested image and preconfigures Steam/Proton/gamescope/HDR; Ubuntu and Pop pre-build and sign the driver so kernel updates never strand you. Fedora is fine but adds akmod attention. Arch is fine but adds news-reading.
Watch out for: Secure Boot (off on Pop; enrol keys on Bazzite; automatic on Ubuntu); anti-cheat holdouts (check the list).

### 4. The ML student with a GPU laptop
*"Laptop with an RTX 4060, taking deep learning courses, need CUDA to work, also need to submit assignments that match the department's Ubuntu."*

**Pick: Ubuntu 26.04 LTS.** Second: Pop!_OS NVIDIA ISO. Third: Fedora + RPM Fusion.
Why: NVIDIA documents Ubuntu first; the department is probably Ubuntu; CI is Ubuntu. Install the driver from `ubuntu-drivers`, install PyTorch with `uv` (bundled CUDA runtime), done. Hybrid graphics: Pop!_OS is smoother; Ubuntu is fine with `prime-select`.
Watch out for: installing the system `cuda` toolkit when you don't need it; letting the driver and PyTorch's expected CUDA version drift (pin PyTorch's wheel index); proctoring (this persona almost always has some — plan the dual boot).

### 5. The systems programmer / kernel hacker
*"I write C, Rust, and sometimes kernel modules. I compile kernels. I use eBPF, perf, QEMU. I want the newest toolchains and full control of the host."*

**Pick: Arch Linux (or EndeavourOS/CachyOS) or Fedora Workstation.** Second: openSUSE Tumbleweed. Third: Debian testing.
Why: you need a mutable host with current toolchains and headers; atomic distros will fight you. Arch gives you newest-everything and the AUR for odd tools; Fedora gives you nearly-newest with less attention and the best `perf`/eBPF/SELinux tooling (it's where Red Hat's kernel people live). NixOS is a legitimate alternative if you're happy to package your tools.
Watch out for: nothing much — this persona knows what they're doing. Keep an LTS kernel installed.

### 6. The cloud/web/application developer
*"TypeScript, Go, Python, Kubernetes, Docker, VS Code, a browser. My code runs in containers. I want the laptop to be boring."*

**Pick: Bluefin DX or Aurora DX.** Second: Fedora (Workstation or KDE). Third: Ubuntu 26.04 LTS.
Why: your work never touches the host; the atomic model gives you zero maintenance and guaranteed rollback; DX ships Docker, Podman, VS Code, JetBrains Toolbox, devcontainer tooling. Fedora/Ubuntu are fine if you want conventional.
Watch out for: the workflow shift (Homebrew/Flatpak/Distrobox instead of `dnf install`) — a week of adjustment; VirtualBox if you need it (use KVM).

### 7. The reproducibility enthusiast
*"I have three machines. I want them identical. I want to `git clone` my life onto new hardware. I'm not afraid of a language."*

**Pick: NixOS** (after a trial of Nix on your current distro). Second: Universal Blue custom image (fork Bluefin, add your packages, let CI build it). Third: Fedora + chezmoi + Ansible.
Why: nothing else reproduces a whole system from a text file. Home Manager extends it to dotfiles. Flakes pin everything.
Watch out for: the learning curve (weeks), non-FHS binaries (`nix-ld`), fragmented docs, and the temptation to spend the semester perfecting the config instead of using the machine.

### 8. The minimalist / tiling WM devotee
*"I want Hyprland or niri, a bar, a launcher, and nothing else. Every process on my machine should be one I chose."*

**Pick: Arch Linux (manual install) or EndeavourOS with a WM profile.** Second: NixOS (declarative WM configs are a sweet spot). Third: Omarchy (if you want it pre-built) or Void.
Why: Arch's repos + AUR have every compositor and every piece of the stack current; the wiki documents all of it. NixOS lets you declare the whole WM setup.
Watch out for: screen-sharing portals, polkit agents, and the other glue (Chapter 5) — set up a fallback DE session; don't rice during term.

### 9. The old-laptop owner
*"2015 ThinkPad, 8 GB RAM, i5, integrated graphics. I want it to be fast and useful again."*

**Pick: Linux Mint Xfce or Linux Mint Cinnamon.** Second: Debian 13 with Xfce/LXQt. Third: Fedora Xfce Spin or Xubuntu.
Why: light desktops, LTS stability, everything from that era is fully supported by any kernel. Mint's tooling makes it pleasant.
Watch out for: 8 GB is fine for browsing/coding, tight for VMs and Electron-heavy workflows; use zram; avoid Flatpak-everything (disk and RAM). A cheap RAM upgrade to 16 GB (if the model allows) transforms it.

### 10. The Apple Silicon Mac owner
*"M1/M2 MacBook Air/Pro. I want Linux on it."*

**Pick: Fedora Asahi Remix (KDE or GNOME).** That's the list.
Why: the Asahi team's own distro; platform packages upstream in Fedora 44; the best GPU/audio/display support; dual-boots alongside macOS.
Watch out for: no Touch ID login, higher sleep drain, arm64-only (proprietary x86 Linux software won't run; Steam via FEX works), no CUDA/Metal compute. M3/M4: not yet.

### 11. The corporate engineer on managed IT
*"My company supports Ubuntu 24.04/26.04 LTS on laptops, requires disk encryption, a compliance agent, and the corporate VPN."*

**Pick: whatever IT supports — Ubuntu LTS.** Full stop.
Why: the compliance agent, VPN client, and support desk all assume it. Fighting this costs you political capital and possibly network access.
Watch out for: snaps (live with them; corporate Firefox policies work with the snap); use Distrobox/containers for anything IT's image lacks. Run your preferred distro on a personal machine.

### 12. The person installing Linux for someone else
*"Setting up my parent's / partner's / sibling's laptop. They browse, email, video call, print, watch things. I'll be tech support."*

**Pick: Linux Mint (Cinnamon)** if they came from Windows; **Bluefin or Aurora** if you want it to update itself forever without your intervention; **Zorin OS** if they want it to look exactly like Windows 11.
Why: Mint has the gentlest defaults and the most forgiving update tooling; Universal Blue images never need you to log in and fix anything.
Watch out for: their printer (check it's IPP), their video-call app (all work), any Windows-only software they can't live without (discover this *before* wiping Windows). Set up Timeshift or rely on atomic rollback. Turn on automatic updates.

## 15.3 The default answer

If you've read this far and still can't decide — because several personas fit, or none do — here is the default, in order:

1. **Fedora Workstation** (GNOME) or **Fedora KDE Plasma Desktop** (try both live for an hour; pick the one that felt right; if neither, KDE). Modern AMD/Intel hardware. This is the best-balanced daily driver for a developer in 2026: current, stable, polished, upstream-first, and what you learn transfers everywhere.
2. **If you have NVIDIA, need CUDA, or want five years without a major upgrade: Ubuntu 26.04 LTS** (or Kubuntu). Remove snaps if they bother you; otherwise don't bother.
3. **If you want never to maintain anything: Bluefin DX / Aurora DX** (or Bazzite for gaming).
4. **If you want the newest everything and enjoy the work: CachyOS or EndeavourOS.**
5. **If you're installing for a newcomer: Linux Mint.**

Pick one. Install it. Use it for a full semester or quarter. **Do not distro-hop in the first three months** — most dissatisfaction in that window is unfamiliarity, not a bad fit, and fixing problems in place teaches you more than reinstalling.

## 15.4 When to deviate from the default

Deviate toward **Ubuntu LTS** when: a mandate exists; NVIDIA/CUDA; you want TPM auto-unlock from the installer; you want to match tutorials verbatim; you're risk-averse about yearly upgrades.

Deviate toward **Universal Blue** when: you never install host packages; you want automatic updates; you have NVIDIA and want it baked in; you're setting up for someone else.

Deviate toward **openSUSE Tumbleweed** when: you want rolling with the best safety net; you love KDE; you want Btrfs/Snapper configured for you.

Deviate toward **Arch-family** when: you want the AUR; you want newest-everything; you enjoy administration; you're a WM person; it's not a heavy semester.

Deviate toward **NixOS** when: reproducibility is your top value and you've trialled Nix.

Deviate toward **Debian** when: you want the most conservative, volunteer-run base and know how to add freshness on top.

Deviate toward **Mint** when: familiarity and calm matter more than modernity.

Deviate toward **Pop!_OS** when: NVIDIA laptop with hybrid graphics, or you want COSMIC's tiling and don't need Secure Boot.

## 15.5 If the first choice doesn't work out

Sometimes it won't. The signals and the moves:

| Symptom | Diagnosis | Move |
|---|---|---|
| Hardware doesn't work (WiFi, webcam, sleep) | Kernel too old, or a genuinely unsupported component | Try a fresher distro (Fedora/Arch-family/Tumbleweed) before blaming Linux; check the ArchWiki page for your laptop; consider a WiFi card swap |
| Updates keep breaking things | You're on rolling and not reading the news, or NVIDIA + DKMS | Add snapshots and an LTS kernel; or move to Fedora/Tumbleweed/atomic |
| "It's too old" — you keep fighting for newer tools | LTS staleness | Use version managers/Homebrew/Distrobox first; if still frustrated, move to Fedora |
| You hate the desktop | Wrong DE, not wrong distro | Install the other DE alongside (or reinstall with the other edition); don't change distro for this |
| You never touch the host and resent maintenance | Should be on atomic | Bluefin/Aurora/Bazzite |
| The atomic host is fighting you | You do host-level work | Fedora Workstation/KDE — same base, mutable |
| You're spending more time configuring than working | Arch/NixOS/WM rabbit hole during a busy term | Fedora or Ubuntu for now; return to the hobby in the break |
| Nothing is wrong but you're bored | Distro-hopping urge | Resist for three months; then try the alternate in a VM first |

Switching costs an afternoon if your `$HOME` is backed up and your dotfiles are in git (Chapters 11 and 14). Make sure they are, and the cost of a wrong first choice stays small.

---

### Key takeaways

- **Walk the tree:** mandate? → hardware? → proctoring? → appliance / conventional / enthusiast → GNOME or KDE → fresh or stable. Five minutes, one answer.
- **Twelve personas** map common situations to specific picks: Mint for switchers, Fedora for Mac refugees, Bazzite/Ubuntu/Pop for NVIDIA gamer-devs, Ubuntu for ML students and corporate engineers, Arch/Fedora for systems programmers, Bluefin/Aurora DX for cloud developers, NixOS for reproducibility, Arch/NixOS for WM minimalists, Mint Xfce for old laptops, Fedora Asahi for M1/M2, Mint/Bluefin for someone else's machine.
- **The default: Fedora** (Workstation or KDE) on modern AMD/Intel hardware; **Ubuntu LTS** for NVIDIA/CUDA/mandates/long support; **Bluefin/Aurora DX** for zero maintenance; **CachyOS/EndeavourOS** for enthusiasts; **Mint** for newcomers.
- Commit for a semester; don't hop in the first three months; fix in place.
- If it doesn't work out, the symptom tells you the move — and with `$HOME` backed up and dotfiles in git, switching costs an afternoon.
