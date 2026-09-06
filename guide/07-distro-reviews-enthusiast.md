# Chapter 7 — Distro Reviews: Enthusiast and Rolling

These distributions assume you're willing to learn how your system works, read documentation, and occasionally intervene. In exchange they offer the newest software, the broadest package selection, or a specific philosophy. Same review structure and scoring as Chapter 6; same persona.

---

## 7.1 Arch Linux

**Identity and governance.** Founded 2002 by Judd Vinet; led by a small team of elected developers and a larger body of Trusted Users/package maintainers; volunteer, donation-funded, with Valve sponsoring infrastructure and build-service work since 2024 (SteamOS is Arch-based, and Valve's money has funded signed packages, reproducible builds and a build service). The Arch Way: **simplicity** (no unnecessary additions or modifications — packages are shipped as upstream released them), **modernity** (rolling, current), **pragmatism** (proprietary software in the repos where useful), **user-centrality** (the user is expected to be competent and in control), and **versatility**.

**Release model.** Pure rolling. Packages move from `testing` to `core`/`extra` in hours to days. Monthly ISO snapshots exist only as install media. The **Arch news feed** announces the handful of updates per year that require manual intervention; reading it before updating is the whole discipline. Chapter 4 quantified the maintenance load: roughly 10–20 hours a year for an attentive user, more with NVIDIA, less if you stay near defaults.

**Packaging.** `pacman` — fast, terse, no undo. The official repos are large and current. The **AUR** is the killer feature: ~90,000 user-submitted `PKGBUILD` recipes covering essentially every piece of software that exists for Linux — proprietary apps (Slack, Zoom, Spotify, JetBrains IDEs, Chrome, 1Password), niche developer tools, git-master builds of anything, fonts, themes, obscure drivers. An AUR helper (`paru`, `yay`) makes installing from it a single command. The discipline: skim the PKGBUILD diff the helper shows you; AUR packages are *unsupported* by Arch and are exactly as trustworthy as their maintainer. Binary rebuilds of the AUR exist (**Chaotic-AUR**) for people who don't want to compile.

**Desktop.** None by default — you install what you want. All of them are packaged: GNOME, Plasma, COSMIC, Cinnamon, Xfce, Budgie, every tiling compositor, every display manager. Because Arch ships them unpatched and current, Arch is often the best place to run the *newest* GNOME or Plasma. `archinstall` (4.x, since March 2026 with a new Textual-based TUI) offers desktop profiles that get you a working system in fifteen minutes; the manual install via the wiki takes an hour the first time and teaches you a great deal.

**Hardware.** Current kernel always, so new hardware works as soon as Linux supports it. Firmware packaged. **NVIDIA:** in December 2025 Arch switched its primary packages to the **open kernel modules** (`nvidia-open`, `nvidia-open-dkms`, `nvidia-lts-open`) for Turing and newer, dropped the proprietary `nvidia-dkms` from the repos, and moved Pascal/Maxwell to the AUR's `nvidia-580xx-dkms` legacy branch. The pre-built `nvidia-open` for the stock `linux` kernel is smooth; anything else is DKMS. Keep `linux-lts` + `nvidia-lts-open` installed as a fallback boot entry. **Secure Boot:** not supported out of the box; either disable it or use `sbctl` to enroll your own keys and sign the kernel (the wiki walks you through it; ~20 minutes once).

**Developer experience.** Arguably the best of any conventional distro, *if* you accept the maintenance. Newest compilers and runtimes always; the AUR for everything else; the ArchWiki as documentation for every tool you'll ever use. Docker/Podman, every language, every editor, every version manager — packaged and current. Because nothing is patched, upstream documentation matches what you have. The system stays exactly as lean as you made it. Many kernel, compiler and toolchain developers run Arch because it's closest to upstream.

**Daily-driver polish.** Whatever you build. A GNOME or Plasma install from `archinstall` is as polished as Fedora's after you install codecs (one `pacman -S` — no legal squeamishness), fonts (`noto-fonts`, `ttf-liberation`), a firewall, printing (`cups`), Bluetooth (`bluez`), and Flatpak if you want it. The gaps are all *defaults*: nothing is configured for you, and forgetting one piece (a polkit agent, `xdg-desktop-portal-gnome`, `power-profiles-daemon`) produces a subtly broken desktop that a Fedora user would never see. Snapshots: install `snapper` or `timeshift` yourself, on Btrfs you chose yourself.

**Security defaults.** None to speak of: no firewall, no MAC, no encryption unless you set it up (the wiki's LUKS + Btrfs + systemd-boot setup is excellent and widely followed). Security *updates* are the fastest of any distro — you get the upstream fix within hours. Reproducible builds (Valve-funded) are progressing.

**Documentation and community.** **The ArchWiki is the best Linux documentation in existence**, full stop, and every Linux user regardless of distro benefits from it. The forums and subreddit are knowledgeable and famously blunt: post without having read the wiki and you'll be told to read the wiki. This is off-putting to some and exactly what others want.

**Governance risks.** Low. Volunteer-run for 24 years with stable leadership; Valve's sponsorship is infrastructure, not control. The risk is *you* — an unmaintained Arch install decays.

**Who should pick it.**
- Developers who want the newest everything and enjoy owning their system.
- People who install a lot of niche software (the AUR).
- People who want to understand Linux deeply and will treat the install as a course.
- Tiling WM users (Arch is their natural habitat).
- Anyone who has run Linux for a year and wants to graduate.

**Who should not.**
- First-time Linux users, unless they have unusual patience and a spare machine.
- Students in a heavy semester who can't afford a broken morning.
- People who want to update once a month and never read a changelog.
- People who need Secure Boot without configuring it, or NVIDIA on a non-stock kernel without DKMS attention.
- Anyone who wants the OS to be invisible.

**Verdict: 7.5/10 for our persona** — and **9/10 for the "enjoys administering" subset**. The best desktop Linux experience available for people who want to run it; the wrong choice for people who want to be run by it. The gap between those two scores *is* Arch.

---

## 7.2 EndeavourOS

**What it is.** Arch Linux with a graphical Calamares installer, a curated set of sane defaults, a Welcome app, and a warm community. Founded 2019 by former Antergos community members; volunteer-run; donations.

**How it differs from Arch.** It uses **Arch's repositories directly** (plus a tiny EndeavourOS repo for its own tools and theming), so it *is* Arch in every way that matters — same packages, same news feed, same AUR. The installer offers GNOME, Plasma, Xfce, Cinnamon, MATE, Budgie, LXQt, i3, Sway, Hyprland, or a bare install, each with light, tasteful theming and the obvious pieces (fonts, codecs, `yay`, `firewalld`, `reflector` for mirror ranking) pre-installed. NVIDIA driver installation via the boot menu's "nvidia" option. Btrfs with optional Snapper via the community `btrfs-assistant` recipe. No Secure Boot by default (same as Arch).

**Why choose it over Arch.** You get a working desktop in ten minutes without missing a polkit agent, and the forum is the friendliest in the Arch world — genuinely welcoming to newcomers, which the Arch forums are not. You lose nothing.

**Why choose Arch over it.** Purity, or you want the learning experience of the manual install, or you dislike *any* theming. `archinstall` has closed most of the convenience gap.

**Verdict: 8/10 for our persona.** The recommended way to run Arch for most people. Same maintenance profile as Arch, minus the setup mistakes, plus a community that will help you.

---

## 7.3 CachyOS

**What it is.** An Arch-based distribution focused on **performance**, founded 2021 by Peter Jung (ptr1337) and a small team; donation-funded. Currently the most-viewed distro on DistroWatch (since August 2025), the fastest-growing Linux distro in Steam's hardware survey, and the darling of the gaming and enthusiast communities in 2025–2026.

**How it differs from Arch.**
- **Its own repositories** of core packages rebuilt with **x86-64-v3** and **x86-64-v4** (AVX-512) optimisations and LTO, auto-selected by CPU at install. Measurable single-digit gains in CPU-bound work; more in some media/compression workloads; near zero in typical desktop use.
- **A patched kernel** (`linux-cachyos`) with the **BORE** scheduler, `sched-ext` support, various latency and throughput patches, and options for `linux-cachyos-lts`, `-rt`, `-hardened`, etc. Perceptibly snappier under load for some; benchmarks show modest gains.
- **Calamares installer** with excellent defaults: Btrfs with Snapper snapshots and boot entries (via Limine or GRUB), zram, `paru` pre-installed, choice of ~15 desktops, NVIDIA driver selection, systemd-boot/GRUB/Limine/rEFInd choice, optional Secure Boot with `sbctl` — the most complete installer in the Arch family.
- **CachyOS Hello** app for post-install tasks; `cachyos-settings` with tuned sysctls; **CachyOS Browser** (a hardened Firefox fork); optional gaming meta-packages; Proton-CachyOS builds.
- Tracks Arch **in near-real-time** — not delayed like Manjaro. The AUR works normally because the base is current.

**Concerns.** Small team maintaining a large custom repo — a sustainability question, not a current problem. The optimisation gains are oversold by fans (they're real but small). Some users report edge-case regressions from the kernel patches (fixed quickly). Being popular brings less-experienced users who then hit ordinary Arch realities. The DistroWatch ranking measures interest, not install base; CachyOS's real-world share is meaningful (Steam survey ~4% of Linux users) but well behind Ubuntu/Mint/Fedora/Arch itself.

**Verdict: 8/10 for our persona**, **8.5 for gamers**. The most polished "Arch, installed the way an expert would" experience available, with a bonus of measurable-if-modest performance work. Same maintenance profile as Arch. If you want Arch and you game, pick this; if you want Arch and want the smallest deviation from upstream, pick EndeavourOS.

---

## 7.4 Manjaro

**What it is.** Arch-based, with its own repositories that **hold Arch's packages for ~2 weeks** of additional testing, a Calamares installer, several official editions (Plasma, GNOME, Xfce; community: others), a graphical package manager (Pamac) that also handles AUR/Flatpak/Snap, and a hardware detection tool (`mhwd`) for drivers. Manjaro GmbH & Co. KG is a German company; the distro is long-established (2011) and was the most popular Arch derivative for years.

**The problem.** The two-week delay applies to Manjaro's repos, but **the AUR builds against current Arch**. So an AUR package that needs a library version Arch shipped yesterday fails on Manjaro until the delay catches up — the AUR breaks *more* on Manjaro than on Arch. Manjaro's answer is "don't use the AUR," which removes the main reason to be Arch-based. Beyond the design flaw, Manjaro has a track record of self-inflicted incidents: letting its SSL certificate expire (multiple times, 2015–2021, with a "set your clock back" workaround suggested), a Pamac bug that hammered the AUR servers, treasurer/governance disputes in 2020, shipping Plasma updates that broke systems, and an experience-of-support culture that discourages criticism. Individually minor; collectively a pattern that experienced users cite when steering newcomers to EndeavourOS or CachyOS.

**In fairness.** Manjaro works fine for a lot of people, especially if they stay on official repos and Flatpak. `mhwd` is genuinely convenient for NVIDIA and hybrid graphics. Pamac is a decent GUI. The Manjaro kernel manager lets you pick from many kernel series. The team has stabilised since 2021. And popularity means lots of help exists.

**Verdict: 6/10 for our persona.** Not bad, but dominated: EndeavourOS gives you real Arch with an easy installer; CachyOS gives you real Arch with great defaults; Fedora gives you "curated freshness" with far better engineering. Manjaro's niche has been eaten.

---

## 7.5 Garuda Linux

Arch-based, gaming-and-aesthetics focused: heavily themed Plasma "Dr460nized" edition (neon, blur, Latte-style dock), Btrfs + Snapper + automatic pre-update snapshots, a `garuda-update` wrapper that handles keyring/mirror issues, Chaotic-AUR pre-enabled (binary AUR), the `linux-zen` kernel, performance tweaks, and a Garuda Assistant/Gamer GUI for one-click gaming stacks. Tracks Arch directly (no delay). Fine engineering under a *lot* of visual opinion; resource-hungry by default. Small team.

**Verdict: 6.5/10 for our persona.** Great if you love the look and want everything gaming-related preconfigured; the heavy theming and RAM use are a poor fit for a work laptop, and CachyOS covers the "tuned Arch for gamers" niche with less bling.

---

## 7.6 Artix, Omarchy, and other Arch relatives

- **Artix Linux** — Arch without systemd (choice of OpenRC, runit, s6, dinit). For people with a philosophical objection to systemd. Works; expect friction with anything that assumes `logind`/systemd units (a fair amount of desktop software). **6/10** for our persona, higher if systemd-avoidance is a hard requirement.
- **Omarchy** — DHH's (of Ruby on Rails) opinionated Arch + Hyprland setup script/ISO that went viral in 2025: a curated, keyboard-driven, beautifully themed tiling desktop with sane defaults for web developers (Neovim/LazyVim, Alacritty/Ghostty, Chromium web apps, 1Password, Docker, mise), installed in minutes. It's Arch underneath, so maintenance is Arch's; the value is a complete, coherent WM setup you didn't have to build. Strongly opinionated (DHH's tools, DHH's keybindings). **7.5/10 for the "wants tiling, doesn't want to configure it" developer**; not for everyone.
- **ArcoLinux** (retired 2025), **Antergos** (retired 2019), **RebornOS**, **BigLinux** (Brazilian, Manjaro-based, surprisingly polished), **Archcraft** (WM-focused aesthetics) — niche or gone.

---

*(Continued: openSUSE Tumbleweed / Leap / Slowroll, Gentoo, Void, Alpine, Solus, Slackware, and the summary table.)*
