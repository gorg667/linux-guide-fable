# Chapter 8 — Distro Reviews: Atomic and Declarative

These distributions change *how the operating system is managed*, not just which packages it ships. Chapter 4 explained the models; this chapter reviews the implementations. Same structure and persona as Chapters 6–7.

A framing note: atomic and declarative systems are the two serious answers to the question "how do I make an update never break my machine?" Atomic answers with *rollback* (boot the previous image). Declarative answers with *reproducibility* (rebuild the exact same thing from a text description, and also roll back). Both are correct; they suit different temperaments.

---

## 8.1 Fedora Atomic Desktops (Silverblue, Kinoite, and friends)

**What they are.** Fedora's official image-based variants: **Silverblue** (GNOME), **Kinoite** (KDE Plasma), **Sway Atomic**, **Budgie Atomic**, and a **COSMIC Atomic** spin. Built on **rpm-ostree** (a hybrid image/package system on top of OSTree, a "git for filesystem trees") and, since Fedora 41–44, increasingly on **bootc**, where the OS image is a standard OCI container image you can inspect, `podman pull`, and derive from with a `Containerfile`. Fedora's six-month cadence; the same packages as Fedora Workstation, delivered as an image.

**The experience.** Install looks like Fedora. The desktop looks like Fedora. Then you try `dnf install` and are told to use `rpm-ostree install` instead — which works, but stages the change for the next boot and slows future updates. The intended workflow: GUI apps from Flathub (preconfigured); CLI tools in a **Toolbox** or **Distrobox** container (`toolbox enter` drops you into a Fedora container that shares your home directory — `dnf install` works normally there); language toolchains via version managers inside the toolbox or Homebrew; and a small number of host-level layers for things that truly need to be on the host (a VPN client, `libvirt`, a shell). Updates happen silently in the background; you reboot when convenient; the previous deployment is always one boot-menu entry away; `rpm-ostree rollback` makes it permanent.

**Strengths.** Genuine unbreakability. Identical base across every install (so bugs are reproducible and fixes are universal). Clean separation between "the OS" and "my stuff." Rebasing between variants (Silverblue → Kinoite) or to a completely different image (a Universal Blue image) is a single command and a reboot. Fedora's quality and currency underneath.

**Weaknesses.** The stock Fedora Atomic images carry Fedora's free-software policy — **no codecs, no NVIDIA** — and adding them means layering RPM Fusion packages, which works but is clunky and slow, and NVIDIA via layered `akmod-nvidia` is fragile at image rebases. The toolbox workflow has a learning curve and some tutorials will confuse you by assuming a mutable host. Kernel modules (VirtualBox, some VPNs) are hard. Fedora's own documentation for the Atomic variants is thinner than for Workstation. In practice, **most people who want Fedora Atomic are better served by Universal Blue's images**, which are Fedora Atomic with all of these problems solved by the image builder.

**Verdict: 7/10 for our persona** in stock form. Technically excellent; practically superseded by Universal Blue for anyone who isn't a purist or building their own images. If you *are* building your own bootc images (a legitimately great workflow for people managing several machines), start here.

---

## 8.2 Universal Blue: Bluefin, Aurora, Bazzite

**Identity and governance.** A community project (founded 2022–2023 by Jorge Castro, a former Canonical and Heptio community lead, with a growing team of maintainers) that builds custom bootc images on top of Fedora Atomic using GitHub Actions and publishes them to GitHub Container Registry. Not a company; donation- and sponsor-funded; very active. The core insight: **because the OS is a container image built in CI, you can bake in everything Fedora's policy won't — codecs, NVIDIA drivers, extra firmware, Homebrew, opinionated defaults — test it, and ship a complete system daily.** Images rebuild automatically from Fedora's packages, so you're always on current Fedora plus the project's additions.

**The three images.**

- **Bluefin** (GNOME). "The next generation Linux workstation, designed for reliability, performance, and sustainability." GNOME with a curated set of extensions (Dash to Dock, AppIndicator, Blur My Shell, Tailscale, etc.) configured tastefully, a Mac-ish dock layout, **Homebrew preinstalled** for CLI tools, Flathub preconfigured with a good default set of apps, Ptyxis terminal with container integration, `ujust` recipes for common tasks (install Steam, enable Tailscale, set up virtualization…), codecs, and automatic background updates for the image, Flatpaks *and* Homebrew. **Bluefin DX** ("developer experience") adds VS Code, Docker (rootful and rootless), Podman, `libvirt`/virt-manager, the JetBrains Toolbox, `devpod`, Kubernetes tooling, Distrobox, and a Fedora-based dev toolbox — "a workstation for cloud-native developers." **Bluefin GTS** ("Grand Touring Support") tracks the *previous* Fedora release for a slower cadence. **Bluefin LTS** (September 2025) is built on CentOS Stream 10 with a newer kernel for a multi-year base. **`-nvidia` and `-nvidia-open`** variants bake in the driver.
- **Aurora** (KDE Plasma). Bluefin's sibling for Plasma users, with the same philosophy, DX variant, GTS/LTS tracks and NVIDIA variants. Slightly smaller team; a few months behind Bluefin on new features, then catches up.
- **Bazzite** (KDE Plasma default; GNOME available). "SteamOS for your PC" — a gaming-optimised image with Steam, Proton-GE, gamescope session (boot to a Steam Deck-like UI on handhelds and HTPCs), Decky Loader, controller and handheld (ROG Ally, Legion Go, GPD) firmware and quirks, HDR, VRR, a patched kernel (`bazzite` kernel with fsync/futex and handheld patches), `-nvidia` variants, and a lot of tuning. **It is also a superb general-purpose desktop** — Bazzite's "desktop" images are Aurora-with-a-gaming-kernel, and a lot of people who don't game much run it because everything works. Bazzite became the most popular Universal Blue image and one of the most-mentioned distros in gaming communities in 2025–2026.

**Release model.** Continuous images tracking Fedora's current release (main), previous release (GTS), or CentOS Stream (LTS). Fedora-version rebases happen a few weeks after Fedora's release once the team validates them; you don't do anything — the image just moves. Bluefin's "Spring 2026" update moved to Fedora 44 in May 2026.

**Packaging.** You don't install packages into the OS. **Flatpak** (Flathub) for GUI apps; **Homebrew** for CLI; **Distrobox**/**Toolbox** (with `ujust` recipes for Ubuntu/Arch/Fedora boxes, and a `bluefin-cli` box with a curated modern shell) for anything else; `rpm-ostree`/`bootc` layering as a last resort. If the workflow doesn't fit, the intended answer is: fork the image on GitHub (there's a template), add your packages to the `Containerfile`, and let CI build your personal OS image — an approach that's genuinely elegant for people managing several machines and overkill for a single laptop.

**Hardware.** Fedora's current kernel (Bazzite's is patched). Firmware, codecs, and **NVIDIA** all baked in and tested — the `-nvidia` images are the closest thing on Linux to "NVIDIA just works and stays working," because the driver is compiled against the exact kernel in the image before you ever download it. Secure Boot works (Universal Blue signs its kernel and NVIDIA modules; you enroll their key once via `ujust enroll-secure-boot-key`). Hybrid graphics supported. Handheld and HTPC support (Bazzite) is unmatched. Apple Silicon: no.

**Developer experience.** *If your work lives in containers, VS Code/JetBrains, a browser, and a terminal* — which describes most web, cloud, and application developers — **Bluefin DX / Aurora DX is arguably the best developer daily driver available**: zero maintenance, current Fedora, every tool preinstalled and updated, devcontainers first-class, Docker and Podman both present and working, `ujust` recipes for the fiddly bits. *If your work touches the kernel, drivers, low-level tooling, or requires installing odd host packages* — systems programmers, OS-course students, embedded developers — the atomic model adds a translation layer (do it in a Distrobox; or layer; or build an image) that a Fedora Workstation or Arch user doesn't face. Homebrew's Linux packages occasionally lag or misbehave compared to distro packages.

**Daily-driver polish.** Excellent — the best out-of-box of anything in this guide except perhaps Mint, and *far* more modern. Everything works on first boot: codecs, Bluetooth codecs, printing, HDR (Plasma), fractional scaling, fingerprint, Tailscale, screen sharing, Steam (Bazzite). Updates are invisible. The curated defaults are tasteful and mostly sensible; if you disagree with one, changing it is easy (they're just GNOME/KDE settings), but you're on a system with *opinions* in a way vanilla Fedora is not.

**Security defaults.** Fedora's (SELinux enforcing, firewalld, LUKS via installer with TPM unlock recipes). The image model itself is a security property — the base is read-only and signed; tampering is detectable. Automatic updates mean you're patched without acting. Universal Blue is a *community* project publishing images you run as your OS — you're trusting their CI pipeline and GitHub org in addition to Fedora. The project is transparent (every image build is public) and has behaved well; it's a different trust surface than a distro foundation and worth knowing about.

**Documentation and community.** Good and growing: docs.projectbluefin.io, docs.bazzite.gg, a Discourse forum, Discord. Smaller than Fedora's; questions about the *base* are Fedora questions. The atomic workflow has its own idioms that take a week to absorb.

**Governance risks.** Young project (three years), volunteer-led, dependent on GitHub infrastructure and Fedora upstream. Rapid growth has been well handled. Bazzite's gaming focus attracts a large, sometimes demanding user base. If Universal Blue vanished, your system would keep working and you could rebase to stock Fedora Atomic with one command — a real advantage of the image model.

**Who should pick it.**
- Developers who want a zero-maintenance workstation and live in containers/IDEs/browsers → **Bluefin DX** or **Aurora DX**.
- Anyone who wants "my laptop updates itself like a phone and never breaks" → **Bluefin/Aurora**.
- NVIDIA owners who never want to think about the driver → any **`-nvidia`** image.
- Gamers, handheld owners, HTPC builders, and honestly anyone who wants a maximally-working Plasma desktop → **Bazzite**.
- People who want Fedora's currency with Ubuntu's "everything preinstalled."

**Who should not.**
- Systems/kernel/driver developers and OS-course students who need to hack the host.
- People who want to install anything with `dnf` and have it just be there.
- People who need VirtualBox specifically (use KVM), or a niche out-of-image kernel module.
- People who dislike opinionated defaults or want a vanilla desktop.
- People uncomfortable trusting a community CI pipeline for their OS image.

**Verdict: Bluefin / Aurora 8.5/10 for our persona; Bluefin DX / Aurora DX 9/10 for the container-native developer subset; Bazzite 8.5/10 (9.5 for gamers).** The most important new option in desktop Linux since Ubuntu. The score is held back from a clean 9 only by the atomic model's friction for low-level work and by the project's youth.

---

## 8.3 openSUSE Aeon and Kalpa

**What they are.** openSUSE's immutable desktops: **Aeon** (GNOME; formerly MicroOS Desktop) and **Kalpa** (KDE Plasma). Built on **openSUSE MicroOS** — Tumbleweed's packages, a read-only root with Btrfs snapshots, and `transactional-update` which applies package changes to a new snapshot that becomes active on reboot. Rolling underneath (Tumbleweed), atomic in application. Aeon is the more mature of the two (it reached release-candidate status in 2024–2025 and is effectively stable); Kalpa lags.

**The experience.** Very GNOME-vanilla (Aeon ships almost no customisation), Flatpak-first (Flathub preconfigured), **Distrobox preconfigured** for CLI work, automatic background updates with automatic reboot-when-idle (configurable), automatic snapshot cleanup. The `tik` installer is minimal and fast (it images the disk rather than installing packages). Full-disk encryption by default with TPM unlock as the *default* path — the most security-forward defaults of any desktop distro. Aeon's maintainer (Richard Brown, a prominent openSUSE figure) is opinionated about *not* offering knobs: Aeon is "the desktop for people who don't want to configure anything," and it means it.

**Strengths.** Tumbleweed's openQA-tested freshness with atomic safety. TPM-encrypted by default. Genuinely zero-maintenance. Lightweight and fast.

**Weaknesses.** Small community and documentation. No NVIDIA support story comparable to Universal Blue's (the proprietary driver is possible but not the intended path — Aeon assumes Intel/AMD). Aeon's deliberate lack of options frustrates tinkerers. Kalpa's maturity lags Aeon's. Codecs require the Packman step even here (via Flatpak, mostly solved).

**Verdict: Aeon 7.5/10 for our persona, Kalpa 6.5/10.** The most disciplined atomic implementation and the best default security; loses to Universal Blue on NVIDIA, community and developer tooling.

---

## 8.4 Vanilla OS

**What it is.** An independent, Debian-Sid-based atomic distro (Orchid, 2.0, released 2024; Vanilla OS 2.x continuing). **ABRoot** provides A/B partition atomic updates; **Apx** is a Distrobox-based tool for installing packages from *any* distro's package manager (`apx install --arch foo`, `--fedora`, `--alpine`, `--nix`…) into managed containers with host integration; Flatpak for GUI apps; a custom installer and first-run experience; vanilla GNOME. The project's identity is "a stock GNOME experience on an unbreakable base, with a universal package layer."

**The experience.** Interesting and ambitious. Apx is a clever idea (a friendlier Distrobox). The Debian Sid base gives currency; the atomic model gives safety. But the project is small, releases have been slow and occasionally rough, documentation is thin, and the community is a fraction of Universal Blue's. It also went through significant architectural rewrites between 1.0 and 2.0, which is a maturity signal.

**Verdict: 6/10 for our persona.** Promising, worth watching, not yet a safe recommendation over Bluefin/Aurora.

---

## 8.5 NixOS

**Identity and governance.** The NixOS Foundation (Netherlands), community-governed; since the 2024 governance crisis (sponsorship disputes, moderation conflicts, prominent departures, the Lix and Aux forks) a **Steering Committee** was elected in late 2024 and the project has stabilised. Funded by donations and corporate sponsors; large, active, opinionated community. **Nix** (the package manager and language, 2003) and **nixpkgs** (the package collection) are used far beyond NixOS — on macOS, on other Linux distros, and in CI — which gives the ecosystem breadth and durability independent of the distro.

**Release model.** **Stable** channels every six months (**26.05 "Yarara"**, 30 May 2026, supported until end of 2026; **26.11** due November 2026), with **unstable** as a rolling channel most enthusiasts actually use. You choose per-system, and can even mix (stable base, unstable for a few packages). Upgrades are `nixos-rebuild switch` with a new channel/flake input — trivial, and rollback is free.

**Packaging.** **nixpkgs** — over 120,000 packages, the largest collection in existence and among the freshest (Repology data consistently ranks nixpkgs-unstable first or second for currency). Every package is built in isolation with declared inputs, stored in `/nix/store` under a hash of its inputs, and never modifies anything outside its path. Multiple versions coexist trivially. **Home Manager** extends the declarative model to user configuration (dotfiles, per-user packages, desktop settings). **Flakes** (still officially "experimental," de-facto standard) pin every input to a git revision for full reproducibility. Flatpak available (declaratively enabled) but less needed. The AUR-equivalent is the **NUR** (community overlays) plus the ease of writing your own derivation.

**Desktop.** Anything — GNOME, Plasma, COSMIC, Hyprland, niri, Sway, Xfce, Budgie, Pantheon — as one line in your configuration. The **Home Manager modules for tiling compositors** (Hyprland, Sway, niri, Waybar, etc.) are excellent and a major reason NixOS is popular in that community. Desktops are vanilla.

**Hardware.** Kernel is configurable (26.05 defaults to 6.18 LTS; `boot.kernelPackages = pkgs.linuxPackages_latest;` gives you 7.2). Firmware via `hardware.enableRedistributableFirmware`. **nixos-hardware** — a community repository of per-machine configuration modules (ThinkPad models, Framework, Dell XPS, Surface…) that enable the right quirks — is genuinely great. **NVIDIA** is *declaratively* configured (`hardware.nvidia.*`), which is elegant, and the module is built against your kernel as part of the rebuild, so it can't get out of sync — but `nixos-rebuild` will fail if the driver doesn't build against a new kernel, and you'll need to pin. Secure Boot via **Lanzaboote** (community, works, manual setup). Apple Silicon via the **nixos-apple-silicon** community project (Asahi kernel on NixOS — works, niche).

**Developer experience.** This is where NixOS is either the best or the most frustrating, depending on you.

*Best:* `nix develop` / `nix-shell` / `direnv` + `nix-direnv` give every project an exact, reproducible toolchain — the right `gcc`, `python`, `node`, `postgresql`, `protobuf`, whatever — activated when you `cd` in, gone when you leave, sharing nothing with the global system, and identical for every collaborator with a `flake.nix`. This is what Docker promised and Nix delivers at finer granularity. Your entire machine — every service, every dotfile — in a git repo you can rebuild on new hardware in an hour. `nixos-rebuild build-vm` to test a config change in a VM before applying. Rollback anything.

*Most frustrating:* Pre-built binaries from the internet fail. VS Code's remote server, downloaded language servers, Python wheels with bundled `.so` files, `npm` packages with native binaries, proprietary tools' installers, GitHub-release tarballs — all assume `/lib64/ld-linux-x86-64.so.2` exists and it doesn't. Workarounds: `nix-ld` (a compatibility shim that makes *most* of this work and is now widely recommended), `steam-run`, `buildFHSEnv`, `patchelf`, or — the Nix way — package it properly. Every developer on NixOS hits this in week one; most settle into `nix-ld` + Distrobox for the stubborn cases. Also: `nix` is a language to learn; error messages are improving but still cryptic; documentation is split across the manual, wiki.nixos.org, nix.dev, Zero to Nix and hundreds of blog posts; and there are two ways to do everything (channels vs flakes; `nix-env` vs `nix profile`; NixOS module vs Home Manager).

**Daily-driver polish.** After configuration, excellent — it's whatever desktop you chose, vanilla. *During* configuration, you'll spend an evening learning where `programs.firefox.enable`, `services.pipewire`, `hardware.bluetooth`, `services.printing` and `fonts.packages` live. The graphical installer (Calamares) produces a working GNOME/Plasma system with a generated `configuration.nix` you then edit forever. Codecs: fine (nixpkgs has no patent policy). Steam, Discord, everything proprietary: one line each.

**Security defaults.** Nothing enforced by default beyond a firewall (on); you declare what you want (AppArmor is available; SELinux isn't practical). LUKS via installer. Reproducibility itself is a supply-chain property. Security updates come via channel updates — fast on unstable, backported on stable.

**Documentation and community.** Large, passionate, helpful on Discourse and Matrix; the wiki is improving; the learning resources are better than they were. Also famously prone to intense internal debate. The ArchWiki is useless to you here — NixOS is different enough that most generic Linux advice needs translation.

**Governance risks.** The 2024 crisis was real; the resolution appears real too. Forks exist but nixpkgs remains the centre of gravity. The `flakes` limbo is a long-running governance failure to make a decision. The project's size and corporate use (Anduril, Shopify, Replit, many others) make it durable.

**Who should pick it.**
- Developers who value reproducibility above convenience and will invest the learning time.
- People managing multiple machines who want them identical.
- Tiling-WM enthusiasts (declarative WM configs are a sweet spot).
- Anyone who has used Nix on another OS for six months and wants more.
- People who find "understand your whole system" motivating rather than exhausting.

**Who should not.**
- First-time Linux users.
- Students in a heavy term who need the machine to just work *this week*.
- People who download pre-built binaries constantly and don't want to fight the FHS issue.
- People who want to Google an error and paste a fix — generic Linux answers don't apply.
- Anyone who wants their friends to be able to help.

**Verdict: 7/10 for our persona blended; 9.5/10 for the subset who make it through the learning curve and value reproducibility.** No distro has a wider gap between "what it does for the right person" and "what it does to the wrong one." Try Nix (the package manager + `nix develop` + Home Manager) on your current distro first. If you love it after a few months, NixOS awaits and will feel inevitable.

---

## 8.6 Guix System

GNU's declarative distro, using **Guix** (Nix's ideas re-implemented in Scheme/Guile) and the **Shepherd** init system (not systemd). Strictly free software by default (no proprietary firmware or drivers — the **nonguix** community channel adds them, and most laptops need it to have WiFi). Smaller package set than nixpkgs, smaller community, slower. Scheme is a nicer language than Nix for many people; the ecosystem is much thinner. Fascinating, principled, and for our persona a **5/10** — a worse practical fit than NixOS on every axis except language elegance and FSF purity.

---

## 8.7 Summary table: atomic and declarative

| Distro | Model | Base | Desktop | NVIDIA | Codecs OOTB | Dev tooling | Maintenance | Score |
|---|---|---|---|---|---|---|---|---|
| **Bluefin DX / Aurora DX** | atomic (bootc) | Fedora | GNOME / Plasma | **baked in** (`-nvidia`) | yes | **excellent** (Docker, Podman, VS Code, JetBrains, devpod, Distrobox, Homebrew) | ~zero | **9** |
| **Bluefin / Aurora** | atomic | Fedora | GNOME / Plasma | baked in | yes | good (Homebrew, Distrobox) | ~zero | **8.5** |
| **Bazzite** | atomic | Fedora | Plasma / GNOME | baked in | yes | good (same base as Aurora) | ~zero | **8.5** (9.5 gaming) |
| **openSUSE Aeon** | atomic (transactional) | Tumbleweed | GNOME | weak | mostly (Flatpak) | good (Distrobox) | ~zero | **7.5** |
| **NixOS** | declarative | — | any | declarative, good | yes | **unique** (nix develop) / frustrating (FHS) | medium (learning) | **7** (9.5 for converts) |
| **Fedora Silverblue / Kinoite** | atomic | Fedora | GNOME / Plasma | layer (clunky) | no (layer/Flatpak) | good (Toolbox) | low | **7** |
| **openSUSE Kalpa** | atomic | Tumbleweed | Plasma | weak | mostly | good | ~zero | **6.5** |
| **Vanilla OS** | atomic (ABRoot) | Debian Sid | GNOME | fair | yes | interesting (Apx) | low | **6** |
| **Guix System** | declarative | — | any | none (nonguix) | via nonguix | unique, thin | high | **5** |

---

### Key takeaways

- **Universal Blue's Bluefin (GNOME) and Aurora (KDE)** are the best "appliance" desktops on Linux: Fedora's currency, everything preinstalled including NVIDIA drivers and codecs, automatic invisible updates, guaranteed rollback. The **DX** variants are arguably the best zero-maintenance developer workstation for anyone whose work lives in containers, IDEs and browsers. **Bazzite** is the same foundation tuned for gaming and is also a superb general desktop.
- The atomic model's real cost is friction for low-level work (kernel modules, host-level hacking, odd host packages); systems programmers and OS-course students should weigh that seriously.
- **Stock Fedora Atomic** is superseded by Universal Blue for most people; it's the right starting point only if you're building your own images. **openSUSE Aeon** has the most security-forward defaults but a weak NVIDIA story and small community. **Vanilla OS** is promising but young.
- **NixOS** offers unmatched reproducibility and the best per-project dev environments in existence, at the price of a language, a non-FHS layout that breaks downloaded binaries, and fragmented docs. Try Nix on your current distro first; if it clicks, NixOS is a 9.5 for you.
- If you want "an update can never break my machine" without learning a new paradigm, Bluefin/Aurora/Bazzite is the answer. If you also want "and I can rebuild my exact machine from a git repo," NixOS is.
