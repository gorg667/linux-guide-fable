# Chapter 6 — Distro Reviews: The Mainstream

This chapter and the two that follow review every distribution worth considering. Each review follows the same structure so you can compare like with like: **identity and governance; release model; packaging; desktop; hardware; developer experience; daily-driver polish; security defaults; documentation and community; who should pick it; who should not; verdict.**

Scores are out of 10 and reflect fitness for *our* persona — the SWE / CS student / daily driver — not abstract quality. A 6 is a perfectly good distribution that's a worse fit than an 8.

"Mainstream" here means: large user base, corporate or well-funded backing, point-release model, polished installer, and the expectation that a newcomer can install and use it without reading documentation.

---

## 6.1 Ubuntu (Desktop, LTS and interim)

**Identity and governance.** Made by Canonical Ltd (Isle of Man / London), a private company founded by Mark Shuttleworth in 2004, funded by enterprise support, cloud partnerships and Ubuntu Pro subscriptions. Debian-derived. The most widely deployed Linux desktop by every available measure and the default assumption of nearly every tutorial, CI configuration, vendor download page and university lab.

**Release model.** Two tracks:

- **LTS** every two years in April (24.04 "Noble Numbat", **26.04 "Resolute Raccoon"** released 23 April 2026). Five years of standard security updates for the `main` repository; **ten years** with Ubuntu Pro (free for personal use on up to five machines), which also covers the `universe` repo. Hardware Enablement (HWE) stack rolls the kernel and Mesa forward at each interim release point (24.04 went 6.8 → 6.11 → 6.14), so an LTS's hardware support does not stagnate for its first two years.
- **Interim** releases every six months (25.10, 26.10 due October 2026), nine months of support. These are for people who want newer software and are willing to upgrade twice a year; for our persona, **use the LTS**.

**Packaging.** APT/`.deb`, with **APT 3.2** in 26.04 bringing transaction history and rollback (`apt history-undo`). Debian's enormous archive plus Canonical's additions. PPAs for third-party software (variable quality; treat like the AUR — check who maintains it). And **Snap**: Canonical's universal format, pushed hard. Firefox, Thunderbird, Chromium and the App Center itself are snaps; `apt install firefox` installs a transitional package that pulls the snap. Snap's technical merits are real (confinement, auto-updates, CLI tool support), but the proprietary store backend, historically slow first launches, and the *forced* redirection are why it's disliked. In 2026 the Firefox snap performs fine; the annoyance is mostly philosophical and around edge cases (Flatpak-style permission management is clunkier; some snaps can't see files outside `$HOME`). Removing `snapd` and installing Flatpak + Flathub takes ten minutes and is well documented. Ubuntu doesn't ship Flatpak by default (its flavours — Kubuntu, Xubuntu etc. — mostly stopped shipping it in 2023 by Canonical's decision, though a single `apt install flatpak` fixes that).

**Desktop.** GNOME 50 in 26.04, with Canonical's patches and extensions: a persistent dock, app indicators/tray, Yaru theme with accent colours, tiling assistant, triple-buffering (now upstreamed). Wayland-only (GDM X11 removed in GNOME 50). Ptyxis is the default terminal. **Flavours** with other desktops are official and share the same repositories: **Kubuntu** (KDE Plasma — 26.04 LTS ships Plasma 6.5-ish and stays there; the Kubuntu Focus / "Bullet-proof KDE" arrangement means Plasma 6.6 LTS backports are plausible), **Xubuntu** (Xfce), **Lubuntu** (LXQt), **Ubuntu Budgie**, **Ubuntu Cinnamon**, **Ubuntu Studio** (KDE, audio/video production), **Edubuntu**, **Ubuntu Kylin**. **Ubuntu MATE and Ubuntu Unity skipped LTS status for 26.04** owing to contributor shortages — avoid them for a long-term install.

**Hardware.** Excellent and the broadest vendor-tested coverage: Dell, Lenovo, HP and Framework all certify or pre-install Ubuntu. Proprietary drivers and firmware are one click in the installer ("Install third-party software"). **NVIDIA is the smoothest of any distro**: `ubuntu-drivers` installs pre-built, signed kernel modules; Secure Boot is handled with a MOK enrolment prompt; a new kernel never leaves you without a driver. 26.04 improved Wayland-on-NVIDIA and fingerprint reader support. Native **ROCm** packaging (`apt install rocm`) for AMD GPU compute and NVIDIA's own CUDA repository target Ubuntu LTS first. **TPM-backed full-disk encryption** is a stable installer option in 26.04 — currently unique among mainstream desktop installers. x86-64-v3 optimised package variants are available opt-in.

**Developer experience.** The reference platform. If a tool has Linux instructions, they're for Ubuntu. Docker's, Microsoft's (VS Code, .NET, PowerShell), Google's (Chrome, Android Studio), HashiCorp's, NVIDIA's, and every SaaS vendor's `.deb` targets Ubuntu. CI runners (GitHub Actions `ubuntu-latest`) are Ubuntu, so your laptop matches your CI. University CS departments overwhelmingly run Ubuntu LTS. Toolchain ages over the LTS lifetime; use `uv`/`mise`/`rustup`/etc. and Distrobox. The 26.04 base (GCC 15, Python 3.14, kernel 7.0) is fresh in 2026 and fine through 2027; by 2028 you'll lean on version managers. The `sudo-rs` and Rust coreutils swap is invisible in practice; the originals are one package away.

**Daily-driver polish.** Very good. Codecs one checkbox at install. Fonts, printing, Bluetooth, screen sharing all work. GNOME's polish plus Canonical's dock/tray patches make it more approachable than vanilla GNOME. The App Center (snap-first, now shows debs) is mediocre; GNOME Software or the CLI are better. Occasional Canonical-specific quirks: snap auto-refresh at inconvenient moments (configurable), the Ubuntu Pro nag in `apt` output (removable), Firefox-snap-specific bugs with some extensions/native messaging (mostly fixed).

**Security defaults.** AppArmor with a broad profile set; snaps confined; unprivileged user namespace restrictions (since 24.04) that occasionally break Chromium-based Electron apps or dev tools until you add a profile or toggle the sysctl. `ufw` installed but off (few listening services by default). Secure Boot on. LUKS with passphrase or TPM. Livepatch (kernel patching without reboot) via Pro. Timely security updates; Canonical's security team is large.

**Documentation and community.** The largest volume of Q&A on the internet (Ask Ubuntu, forums, blogs). Quality is uneven — a lot of it is outdated and some is wrong — but *something* exists for every problem. Official docs improved with the 2024–2026 Discourse/documentation.ubuntu.com overhaul.

**Governance risks.** Canonical makes unilateral decisions the community dislikes (Unity, Mir, Upstart, snaps, dropping Flatpak from flavours, removing Software & Updates in 26.04) and sometimes reverses them years later. It has also shown willingness to follow its own path on packaging (snap) even where the ecosystem went elsewhere (Flatpak). None of this affects the OS's reliability; it does mean Ubuntu's direction reflects one company's priorities.

**Who should pick it.**
- Anyone whose employer, university, or key software vendor says "Ubuntu."
- NVIDIA owners who want the least driver friction, including CUDA users.
- People who want an LTS with five-to-ten-year support and don't mind a two-year-old desktop by the end.
- Beginners who want the largest pool of help.
- Anyone who wants TPM auto-unlock encryption from the installer.

**Who should not.**
- People who strongly object to snaps and don't want to remove them.
- People who want the newest GNOME/Plasma/Mesa/kernel between LTS releases (Fedora or rolling instead).
- People who dislike Canonical's governance style on principle.

**Verdict: 8.5/10 for our persona.** Ecosystem gravity, hardware/NVIDIA support and LTS stability outweigh snap irritation. The strongest "nobody will blame you" choice. Kubuntu is the same score with Plasma.

---

## 6.2 Fedora Workstation and Fedora KDE Plasma Desktop

**Identity and governance.** The Fedora Project, sponsored by Red Hat (IBM), governed by an elected council and FESCo (engineering steering committee) with meaningful community input. Fedora is the upstream of RHEL — technologies debut here (systemd, Wayland, PipeWire, Btrfs default, dnf5, bootc) two to four years before landing in enterprise. It is *not* a beta for RHEL; it's a complete, polished distro that happens to be ahead of the curve. Red Hat's 2023 decision to restrict RHEL source access angered the clone community but did not affect Fedora.

**Release model.** Every six months (April and October): **Fedora 44** shipped 28 April 2026 (after two one-week slips for blocker bugs — Fedora holds releases until they're right); **Fedora 45** is due late October/November 2026. Each release is supported for ~13 months, so you can skip every other one. Within a release, Fedora **rebases the kernel to new stable versions** (44 shipped 7.0, moved to 7.1 then 7.2), updates Mesa, and takes new Plasma minor releases — making it semi-rolling for hardware while holding GNOME's major version. Upgrades via `dnf system-upgrade` or GNOME Software/Discover are reliable and take ~30 minutes.

**Packaging.** DNF 5 (fast, with history/undo) and RPM. Large, fresh repositories with a strict free-software policy: **no patent-encumbered codecs, no proprietary drivers**. You add **RPM Fusion** (free and nonfree repos, a well-established third party effectively blessed by the community) for full `ffmpeg`, H.264/H.265 hardware decode (`mesa-va-drivers-freeworld` on AMD; Intel similar), NVIDIA drivers (`akmod-nvidia`), Steam and so on. Since Fedora 38 the installer offers a "third-party repositories" toggle that enables a *filtered* set (Steam, NVIDIA, Chrome via Flathub). **Flatpak with Flathub** is preconfigured (the full Flathub since Fedora 38; Fedora's own Flatpak remote is also present and occasionally causes confusion by shadowing Flathub apps — a known papercut, being addressed). **COPR** is Fedora's PPA equivalent for community packages.

**Desktop.** **Workstation** = vanilla GNOME 50, unpatched, as the GNOME designers intended — Fedora is GNOME's reference platform. **KDE Plasma Desktop** = an official Edition (elevated from "spin" in Fedora 42) with the latest Plasma (6.5 at 44's release, updated to 6.6/6.7 within the cycle). Both are Wayland-only. Other **Spins**: Xfce, Cinnamon, MATE, LXQt, Budgie, Sway, i3, COSMIC, Phosh. All share repos.

**Hardware.** Very good for anything less than ~5 years old, because the kernel is always current — Fedora is often the first mainstream distro to work on a brand-new laptop. Firmware via `fwupd` integrated into GNOME Software/Discover (Fedora pioneered this). Framework, Lenovo (some ThinkPads ship with Fedora pre-installed) and Slimbook officially target it. **NVIDIA** works via RPM Fusion's `akmod-nvidia`: the module rebuilds locally after each kernel update (a few minutes; wait before rebooting), and after a *major* kernel bump you should wait a few days for RPM Fusion to catch up — this is the one area where Fedora demands more attention than Ubuntu. Secure Boot signing for akmods requires a one-time key enrolment. **Apple Silicon:** Fedora Asahi Remix is the flagship Asahi distro and its platform packages are now fully upstream in Fedora 44.

**Developer experience.** Excellent. Current toolchains without rolling-release attention. **Podman** (rootless, daemonless, Docker-CLI-compatible) is the default container engine and the best-integrated Podman experience anywhere; Docker itself installs from Docker's repo if you prefer. **Toolbox** (Fedora's Distrobox precursor) and Distrobox are packaged. SELinux enforcing is a *feature* for anyone who'll ever touch RHEL. Python is a first-class citizen (Fedora is where Python packaging changes get tested). GCC/LLVM/Rust/Go are always recent. The one irritation: vendor `.rpm`s occasionally lag their `.deb` siblings, and a few vendors (looking at you, some VPN clients) ship only `.deb`.

**Daily-driver polish.** Very good after the codec step, which is the number-one newcomer trap — a fresh Fedora can't play H.264 in Firefox until you swap `ffmpeg-free` for `ffmpeg` from RPM Fusion. Fedora's docs and every "post-install" guide cover this; it takes two minutes. After that: PipeWire (Fedora shipped it first), Wayland, Flatpak, fractional scaling, HDR-on-Plasma, fwupd, printing — all excellent. Btrfs with transparent zstd compression by default; snapshots are *not* configured by default (a five-minute Snapper/BTRFS Assistant setup fixes that).

**Security defaults.** **SELinux enforcing** with a well-tuned targeted policy — most users never see a denial; when they do, `sealert` explains it. `firewalld` on by default. Btrfs + LUKS from the installer (passphrase; TPM unlock via `systemd-cryptenroll` after install). Secure Boot on. Very prompt security updates. Fedora's policy of shipping only redistributable software also means fewer supply-chain surprises.

**Documentation and community.** Good official docs (docs.fedoraproject.org), Fedora Magazine, Ask Fedora (Discourse), an active Matrix. Smaller volume than Ubuntu's, higher average quality. The ArchWiki applies to most Fedora problems too.

**Governance risks.** Red Hat/IBM's priorities shape Fedora's roadmap (it's why Fedora leads on bootc, Wayland, PipeWire, SELinux). If IBM ever deprioritised Fedora the project would survive but slow. The 13-month support window is short: you *must* upgrade at least yearly. Fedora also occasionally ships a change before the ecosystem is ready (early Wayland, early PipeWire, X11 session removal) — you're on the leading edge, which cuts.

**Who should pick it.**
- Developers who want current toolchains and kernels without rolling-release maintenance.
- Anyone with a modern (< 5 years) AMD/Intel machine.
- People who'll work with RHEL/CentOS Stream/Podman professionally.
- GNOME users who want GNOME as designed; Plasma users who want current Plasma on a stable base.
- Apple Silicon Mac owners (via Asahi Remix).

**Who should not.**
- People who want five-plus years without a major upgrade.
- NVIDIA users who want zero driver thought (Ubuntu or a Universal Blue `-nvidia` image are smoother; Fedora is *fine*, just less hands-off).
- People whose employer or university requires Ubuntu/Debian specifically.
- People who resent the codec step on principle.

**Verdict: 9/10 for our persona.** The best balance of freshness, stability, polish and upstream alignment for a developer's daily driver in 2026. Workstation and KDE Edition score identically; pick by desktop preference. Docked half a point each for the codec ritual and the NVIDIA akmod attention tax.

---

*(Continued in the next section: Debian, Linux Mint, Pop!_OS, Zorin, elementary.)*
