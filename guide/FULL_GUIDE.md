# Choosing a Linux Distribution for Software Engineering, CS Study, and Daily Life

_Generated 2026-09-06 from individual chapter files. See README.md for the table of contents._


---

# Chapter 0 — Preface, and the Sixty-Second Answer

> **Date-stamp.** This guide was written in September 2026. Linux moves quickly; version numbers, driver states and "what's broken this month" all drift. Where a fact is time-sensitive I say so. The *reasoning* is designed to stay useful for years even as the specifics age.

## Who this is for

You are one, two, or all three of the following:

1. **A software engineer** — professional or aspiring — who writes code for a living or wants to, who lives in terminals, editors, containers and browsers, and who needs the machine to get out of the way.
2. **A computer science student** — who has coursework that ranges from "write a shell in C" to "train a model on a GPU" to "submit a PDF built from LaTeX by midnight", who has to use whatever the department mandates, and who occasionally has to run exam-proctoring software that has never heard of Linux.
3. **A person with a life** — who watches video, plays games, joins video calls, prints boarding passes, pairs Bluetooth headphones, edits photos, and expects the laptop to wake from sleep with battery left.

You want *one machine* — or at least one operating system — that serves all of these roles, and you've decided (or are deciding) that it should run Linux. You've discovered that "which Linux?" is a question with several hundred possible answers and a religious war attached to each one.

This guide exists to end that confusion. Not by declaring a single winner — I'll explain why that would be dishonest — but by teaching you enough about how distributions actually differ that you can make the choice yourself in under an hour, and by giving you concrete, opinionated recommendations for the overwhelming majority of cases.

## Who this is *not* for

- Server, embedded, or cloud deployments. Some concepts transfer, but the trade-offs are different.
- People who want a "Windows lookalike" and nothing more. You'll get a recommendation, but most of the depth here won't matter to you.
- People who have already decided and want confirmation. Read anyway; you may change your mind.

## How to read this

It's long — by design. You do not have to read it linearly.

| If you… | Read… |
|---|---|
| have 60 seconds | the table immediately below |
| have 15 minutes | Chapter 0, Chapter 1, Chapter 15 (decision framework) |
| are new to Linux and want to understand the landscape | Chapters 1 → 5 in order, then 15 |
| already run Linux and want to compare specific distros | Chapters 6 → 9 |
| are a student worried about coursework/proctoring | Chapter 12, then 15 |
| are buying a laptop for Linux | Chapter 10 |
| have chosen and want to set up well | Chapter 16 |
| want to argue with me | Chapter 17 (myths) then open an issue |

Each chapter ends with a **Key takeaways** box. If you skim only those, you'll still come away with the gist.

## A note on honesty and opinions

Most "best Linux distro" articles are either (a) affiliate-driven listicles with ten distros and no verdict, or (b) advocacy for whatever the author uses. I try to do neither. Where I give an opinion it is marked as one, and I explain the reasoning so you can disagree with the premises rather than the conclusion. Where the evidence is thin or the situation is changing (COSMIC's maturity, NVIDIA on Wayland, Apple M3/M4 support), I say so instead of pretending certainty.

I also try to respect your time. If the honest answer is "it doesn't matter much", I'll say that rather than inventing distinctions.

---

## The sixty-second answer

If you read nothing else, here it is. These are defaults; the rest of the guide explains when to deviate.

| Your situation | Pick this | Why, in one line |
|---|---|---|
| **"Just tell me what to install."** Modern laptop/desktop, AMD or Intel graphics, you want current software and a clean, well-integrated desktop. | **Fedora Workstation** (GNOME) or **Fedora KDE Plasma Desktop** | Six-month cadence gives you a current kernel and toolchains without rolling-release babysitting; excellent Wayland/PipeWire/Flatpak integration; upstream-first, so what you learn transfers everywhere. |
| **You want the "boring, safe, everyone-supports-it" option**, especially if your employer or university publishes Ubuntu instructions, you use CUDA, or you value 5+ years of support. | **Ubuntu 26.04 LTS** (or **Kubuntu 26.04** for KDE) | The lingua franca of tutorials, CI images, vendor drivers and corporate IT. Two-year LTS cadence with 5 years of standard support (10 with Ubuntu Pro, free for personal use on up to 5 machines). Live with snaps, or switch to Flatpak in ten minutes. |
| **You want it to feel like Windows and never surprise you.** First-time switcher, older or lower-spec hardware, you don't care about the newest anything. | **Linux Mint** (Cinnamon edition) | Ubuntu LTS base without snaps, a traditional desktop, superb defaults, and the best "it just works" record for newcomers. |
| **You want the newest everything and you enjoy understanding your system.** Comfortable in a terminal, willing to read one news post before big updates. | **Arch Linux** (via `archinstall`), or **CachyOS** / **EndeavourOS** if you'd rather skip the manual bits | Rolling release, the AUR, the ArchWiki. Maintenance is real but much smaller than its reputation. CachyOS adds performance tuning and a friendlier installer. |
| **You want a system that cannot be broken by an update and don't want to think about maintenance.** You like the idea of "my laptop is an appliance for running containers and Flatpaks." | **Bluefin** (GNOME) or **Aurora** (KDE) from Universal Blue | Fedora Atomic base; the whole OS is a versioned container image with automatic updates and instant rollback; developer tools via Distrobox/Homebrew/devcontainers. Bluefin DX ships a full dev toolbox. |
| **You want your entire machine defined in a text file** and are willing to invest a few weekends up front. | **NixOS** | Declarative, reproducible, roll-back-anything. Enormous package set. Steep learning curve and a language to learn; extraordinary payoff if you manage multiple machines or value reproducibility. |
| **You have an NVIDIA GPU and want the least friction.** | **Ubuntu 26.04 LTS** or **Pop!_OS** (NVIDIA ISO), or **Fedora + RPM Fusion**, or **Bazzite/Bluefin `-nvidia` images** | Pre-integrated driver stacks. Avoid distros where you must build DKMS modules by hand on a fresh install unless you know what that means. |
| **You're on Apple Silicon (M1/M2).** | **Fedora Asahi Remix** | The only serious option; M1/M2 excellent, M3 early-alpha, M4 not yet. |
| **You're a student who must run LockDown Browser / Proctorio / Examplify.** | Any of the above **plus a Windows fallback** (dual boot, second device, or a school-provided machine) | These proctoring tools do not run on Linux and cannot be made to. Plan for it now; do not discover it on exam day. |

If several rows apply, they're roughly in order of "safest default first." When in genuine doubt: **Fedora Workstation** (or KDE edition) if your hardware is less than ~5 years old and not NVIDIA; **Ubuntu LTS** if it is NVIDIA or you need the widest third-party support; **Linux Mint** if you or the person you're installing this for mainly wants Windows without Windows.

## What you'll learn along the way

- Why the distribution matters *less* than you think for development work (containers, language version managers, and Flatpak have flattened the differences) and *more* than you think for hardware and desktop polish.
- The real trade-off underneath every distro argument: **freshness vs. stability vs. maintenance effort**, and why you can only pick two.
- What "rolling", "LTS", "atomic", and "declarative" actually mean for your Tuesday afternoon.
- Why GNOME vs. KDE is a bigger decision than Fedora vs. Ubuntu.
- How NVIDIA, Secure Boot, and proctoring software constrain your options far more than any distro's philosophy does.
- How to set up whatever you pick so that it stays reliable for years.

Let's begin.

---

### Key takeaways

- This is a long, opinionated, dated (September 2026) guide for engineers, CS students and daily drivers who want one Linux machine.
- The default answers are: Fedora (Workstation or KDE) for most modern hardware; Ubuntu LTS for NVIDIA, CUDA and "everyone supports it"; Linux Mint for newcomers who want familiarity; Arch/CachyOS for tinkerers; Bluefin/Aurora for an unbreakable appliance; NixOS for declarative purists.
- Students who must run proctoring software need a Windows/macOS fallback regardless of distro.
- Read Chapter 1 and Chapter 15 if you only have fifteen minutes.


---

# Chapter 1 — How to Think About the Choice

## "Which distro is best?" is a category error

Ask "which car is best?" and any sensible person replies "for what?" A rally car, a minivan and a delivery truck are all excellent — at different things. Nobody argues that the minivan is *objectively wrong*.

Yet Linux users argue exactly this way about distributions, and newcomers absorb the framing. They arrive believing there is a hidden ranking, that experienced people know it, and that picking wrong is a costly mistake. None of that is true. The differences between the mainstream distributions are real, but they are differences of *trade-off*, not of quality, and the cost of switching later is a Saturday afternoon and a backup you should have anyway.

So the first thing to do is reframe. You are not looking for the best distro. You are looking for the distro whose trade-offs match your situation. To do that you need to know what a distribution actually decides for you — because it's less than most people assume.

## What a distribution actually decides

Every Linux distribution is the *same* kernel, the *same* GNU userland (or a compatible rewrite), the *same* desktop environments, the *same* browsers, the *same* compilers. Firefox on Arch is Firefox on Ubuntu is Firefox on NixOS. GCC 15 produces the same binaries wherever it runs. Your code doesn't know or care.

What the distribution decides is a small set of policy choices layered on top of shared upstream software:

1. **Release model and cadence** — how often you receive new versions of things, and whether they arrive as a trickle (rolling) or a flood every N months/years (point release). This is the single most consequential decision and it determines how "fresh" vs. how "settled" your system is at any moment.
2. **Package format and manager** — `.deb` with APT, `.rpm` with DNF or Zypper, Arch's `pacman`, Nix's store, etc. Mostly a matter of muscle memory and repository size, plus one huge exception (the AUR) and one paradigm shift (Nix).
3. **Default desktop and the level of integration with it** — GNOME, KDE Plasma, Cinnamon, COSMIC, or none. Whether the distro patches the desktop (Ubuntu, Mint, Pop) or ships it vanilla (Fedora, Arch).
4. **Defaults that are annoying to change later** — filesystem (ext4 vs. Btrfs), whether snapshots are set up, encryption, security framework (SELinux vs. AppArmor), bootloader, whether proprietary codecs and drivers are pre-installed or a chore.
5. **Support lifecycle and upgrade path** — how long a version is patched, how painful the jump to the next one is, and whether that jump is a reinstall.
6. **Ecosystem gravity** — how many tutorials, Stack Overflow answers, vendor `.deb`/`.rpm` files, CI Docker images, and corporate IT policies assume your distro. This is under-discussed and matters enormously for students and engineers.
7. **Governance and funding** — corporate (Canonical, Red Hat, SUSE, System76), foundation, or volunteer. Affects long-term stability of the *project*, not the software.

That's it. Notice what's *not* on the list: performance (differences are within noise for desktop work, with the narrow exception of CPU-optimised builds like CachyOS's x86-64-v3 packages, which are worth a few percent in specific workloads), "security" in the abstract (all mainstream distros patch CVEs promptly; the differences are in defaults), and "which one is for programmers" (all of them; the toolchains are identical).

## The fundamental trade-off: pick two

Almost every distribution debate collapses into a triangle:

```
                 FRESHNESS
          (newest kernel, drivers,
           toolchains, desktop)
                  /\
                 /  \
                /    \
               /      \
              /        \
   STABILITY /__________\ LOW MAINTENANCE
 (things don't          (you never have to
  change under you)      intervene or read news)
```

- **Fresh + stable** is impossible without heroic effort. Something that changes daily cannot be guaranteed not to change under you. The closest approximations are openSUSE Tumbleweed (automated testing of every snapshot) and Fedora (six-month rebase with a stabilization period), and even they occasionally regress.
- **Fresh + low maintenance** is what rolling distros with good tooling *try* to offer, and it mostly works — until it doesn't, and you're the one who has to fix it. The atomic/image-based distros (Bluefin, Aurora, Bazzite) are the most serious attempt to genuinely deliver this corner, by making rollback trivial.
- **Stable + low maintenance** is the LTS promise: Ubuntu LTS, Debian stable, Linux Mint, RHEL clones. The price is that your compiler, your kernel and your desktop are frozen in time for years, and you route around it with Flatpaks, containers, language version managers and backport repos.

There is no fourth option. Every "revolutionary" distro is just a different point on this triangle, sometimes with better tooling to soften the compromise. Knowing where you want to sit on the triangle gets you 80% of the way to a decision.

**Where do engineers and students want to sit?** Usually closer to *fresh* than the average user (new language versions, new kernels for new hardware), but with a hard requirement for *stability during deadlines*. This tension is why so many developers end up on Fedora (fresh-ish, stable-ish) or on an LTS base with everything interesting running in containers.

## The hidden axis: how much do you want to own the machine?

There is a second, less-discussed dimension: **do you want to be the administrator of your computer, or do you want it to be administered for you?**

Some people find joy in understanding every service, hand-writing their window manager config, and reading changelogs. For them, Arch, Gentoo, Void and NixOS are *fun*, and the time spent is a hobby, not a cost. Others — including many excellent engineers — regard their laptop as a tool, want to spend zero minutes on it that aren't spent on their actual work, and would rather the OS updated itself silently at night like a phone. For them, the atomic desktops and the polished mainstream distros are correct, and Arch would be a mistake regardless of skill.

Neither attitude is superior. Be honest about which describes you *this year*, not which you aspire to. A common failure mode is a student who installs Arch to "learn Linux", spends the semester fixing the WiFi instead of doing coursework, and concludes that Linux is unusable. Learning Linux deeply is a great goal; do it in a VM, or on a second machine, or after the semester.

## The cost of switching is low; the cost of a bad first experience is high

This asymmetry should shape how you choose.

Switching distros later costs you: a backup, a reinstall (30–60 minutes), reinstalling your applications (an hour, or five minutes if you kept a list or use a dotfiles manager), and re-learning some package manager verbs. That's it. Your `$HOME` directory, your git repositories, your browser profile and your dotfiles carry over untouched. Experienced users switch on a whim.

A *bad first experience*, by contrast, costs you the whole project. If your first week involves a black screen after an NVIDIA update, a WiFi card with no driver, or a broken `pacman -Syu` before an exam, you will — rationally — go back to Windows or macOS and not return for years. Newcomers churn; that's the real risk.

Therefore: **optimise your first choice for a smooth first month, not for where you think you'll be in three years.** You can always move toward the "harder" or "more interesting" distros once you have a working mental model and a machine you trust. The reverse journey — from a broken Arch install back to something that boots — is much less pleasant.

## Common ways people choose badly

I've watched a lot of people choose distros. These are the recurring mistakes.

**Choosing by screenshot.** Every desktop can be themed to look like every other desktop. The r/unixporn aesthetic you liked is a rice job that took someone a weekend and works on any distro. Choose the distro for its substance; make it pretty afterwards.

**Choosing by benchmark.** Phoronix publishes cross-distro benchmarks; the spread between mainstream distros on the same hardware is typically single-digit percent and often within run-to-run variance. Kernel version and compiler flags explain nearly all of it, and both are adjustable. For desktop work you will never notice. (Gaming is the one area where a tuned kernel — CachyOS, Bazzite — gives *measurable* gains, and even there it's modest.)

**Choosing what your friend uses.** This is actually a *good* heuristic if your friend will help you. Local support beats abstract superiority. But make sure it's what they'd recommend for *you*, not what they enjoy for themselves.

**Choosing the hardest to prove something.** Nobody at your job or in your class will be impressed. Prove things by shipping code.

**Choosing by DistroWatch ranking.** DistroWatch's "Page Hit Ranking" measures curiosity, not usage. CachyOS topping it since 2025 reflects genuine interest (and genuine quality), but it doesn't mean most Linux desktops run CachyOS — they don't; Ubuntu, Mint, Fedora, Debian and Arch derivatives dominate real-world telemetry such as the Steam survey and browser user-agent statistics.

**Choosing by "it's what real programmers use."** Real programmers use everything, including macOS and Windows. The distribution is not a credential.

**Over-indexing on one grievance.** "Ubuntu has snaps, therefore never Ubuntu." Snaps are a real annoyance; they're also removable in ten minutes, and the rest of Ubuntu's ecosystem gravity may outweigh them for your situation. Weigh the whole package.

**Ignoring hardware.** People pick a distro first, then discover their NVIDIA GPU, MediaTek WiFi card, or fingerprint reader wants a newer kernel or a proprietary blob. Check hardware *first* (Chapter 10); it constrains the choice more than philosophy does.

## Better heuristics

Instead, work through these questions, roughly in order of how much they constrain you:

1. **What hardware?** NVIDIA GPU? Apple Silicon? Very new laptop (< 6 months)? Very old (> 8 years)? This eliminates or strongly favours some options immediately.
2. **Any hard external requirements?** Employer/university mandates or publishes instructions for a specific distro; software that only ships `.deb` or only supports Ubuntu LTS (some commercial EDA, CAD, and research tools); proctoring software (requires Windows fallback regardless).
3. **Where on the triangle?** Do you need the latest toolchains and kernels, or do you need nothing to change until finals are over — and are you willing to do the maintenance that "fresh" demands?
4. **Admin or appliance?** Do you want to own the machine or have it managed?
5. **GNOME, KDE, or something else?** This decision is more visible day-to-day than the distro is. Try both in a live USB for an hour each.
6. **Ecosystem gravity — how much do you value "everything assumes I have this"?** Ubuntu wins this outright; Fedora and Arch are strong seconds via excellent documentation; niche distros lose.

Chapter 15 turns this into an explicit decision tree. The chapters in between give you the knowledge to answer the questions truthfully.

## A word about "distro-hopping"

There is a phase most Linux users go through — trying a new distribution every few weeks, convinced the next one will finally be *right*. It's harmless and educational, up to a point. But it's usually a symptom of one of two things: either you haven't figured out where you sit on the triangle, or the thing bothering you is not the distro at all (it's the desktop environment, a hardware quirk, or a workflow you haven't set up yet).

The cure is to make a deliberate choice using the framework here, commit to it for a semester or a quarter, and *fix problems in place* rather than by reinstalling. You will learn far more about Linux by debugging one system for six months than by installing twelve.

---

### Key takeaways

- "Best distro" is the wrong question; the right one is "whose trade-offs match my situation."
- A distro decides: release cadence, package manager, default desktop and defaults, support lifecycle, ecosystem gravity, governance. It does *not* meaningfully decide performance, "security", or which programming languages you can use.
- The core trade-off is a triangle — freshness, stability, low maintenance — and you can only pick two. Know where you want to sit.
- Be honest about whether you want to administer your machine or have it administered for you.
- Optimise for a smooth first month; switching later is cheap, but a bad first experience drives people away for years.
- Check hardware and hard external requirements first; they constrain you more than philosophy does.


---

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


---

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


---

# Chapter 4 — Release Models and Package Management, In Depth

Chapter 2 introduced the taxonomy. This chapter examines each model as it is actually lived: what "stable" and "rolling" mean on a Tuesday afternoon, what really breaks and how often, and how the modern developer-tooling layer has changed the calculus. It ends with the package-manager and universal-format comparisons and a section on the specific misery that is out-of-tree kernel modules.

## 4.1 Point releases, lived

### The promise

A point-release distribution freezes a set of package versions, tests them together for weeks or months, releases, and then changes *only* to fix bugs and security holes. The Firefox you have in month one is the same *major branch* as the Firefox you have in month eighteen (browsers are the usual exception — they get full version bumps because security fixes aren't backported to old branches). Your `gcc`, your `python3`, your kernel, your GNOME — all pinned.

The benefit is that **nothing changes under you**. A script that worked in January works in December. A tutorial written for your release works for the release's whole life. Your muscle memory of where settings live doesn't rot.

### The cost: staleness, quantified

How stale? It depends on where in the cycle you are and how long the cycle is. Concretely, in September 2026:

| Distro / release | Released | Kernel | GCC | Python | GNOME / Plasma | Mesa |
|---|---|---|---|---|---|---|
| Debian 13 "Trixie" | Aug 2025 | 6.12 | 14 | 3.13 | 48 / 6.3 | 25.0 |
| Ubuntu 24.04 LTS | Apr 2024 | 6.8 (HWE → 6.14) | 13 | 3.12 | 46 / 5.27 | 24.0 (HWE newer) |
| Ubuntu 26.04 LTS | Apr 2026 | 7.0 | 15 | 3.14 | 50 / 6.5 | 26.0 |
| Fedora 44 | Apr 2026 | 7.0 → 7.2 (rebased) | 16 | 3.14 | 50 / 6.5→6.6 | 26.x (updated) |
| Arch / Tumbleweed | rolling | 7.2 | 16 | 3.14 | 50 / 6.7 | 26.2 |

(Versions approximate; the point is the *pattern*.)

Two observations:

1. **A fresh LTS is nearly as current as a rolling distro** for about three months. Ubuntu 26.04 in May 2026 was within a hair of Arch. By April 2028, when 28.04 arrives, it will be two years behind on everything except the kernel (HWE) and browsers.
2. **Fedora is the interesting middle.** It releases every six months *and* rebases the kernel to new stable versions throughout a release's life (Fedora 44 shipped 7.0 and moved to 7.1, then 7.2). It also updates Mesa and takes new minor versions of Plasma. Only GNOME is held at the release's major version. This makes Fedora "semi-rolling" in practice: fresh enough for new hardware, frozen enough for a stable desktop.

### What staleness actually costs a developer

Less than it used to, for three reasons:

- **Language version managers** give you any Python/Node/Rust/Go/Java version regardless of what `apt` offers. You should be using them anyway to match project requirements.
- **Containers and Distrobox** give you any distro's userland when a build needs a newer `cmake` or `clang`.
- **Flatpak** gives you current GUI apps (OBS, GIMP, Blender, IDEs) on an old base.

What it *still* costs:

- **Kernel and Mesa** for new hardware and new GPU features. Ubuntu's HWE kernels help (24.04 rolled from 6.8 to 6.14 over its life); Debian's backports help less; enterprise clones don't bother.
- **System libraries** that pre-built binaries link against — chiefly `glibc`. A binary built on a newer distro may refuse to run on an old LTS with `GLIBC_2.39 not found`. This bites people who download tools from GitHub releases. Debian 13/Ubuntu 26.04 are new enough that this is rare for the next year or two; it becomes a real annoyance in the final two years of an LTS.
- **Desktop features.** GNOME 46 (Ubuntu 24.04) vs. GNOME 50 (26.04) is a meaningful jump in HDR, fractional scaling, VRR and accessibility. If you care, a two-year-old desktop feels two years old.
- **Bugs that were fixed upstream a year ago but not backported.** Every LTS user eventually hits one of these. Ubuntu's SRU process and Debian's stable updates are conservative by design.

### The upgrade cliff

Point-release distros defer change; they don't eliminate it. Every N months or years you face a *major upgrade* — a big bang where thousands of packages change at once. Experiences:

- **Fedora:** `dnf system-upgrade` (or GNOME Software's one-click). Twice a year. Robust for over a decade; the Fedora community treats upgrade breakage as a blocker bug. Typically 20–40 minutes. Most users upgrade every release or every other (each release is supported ~13 months, so skipping one is fine).
- **Ubuntu LTS → LTS:** `do-release-upgrade`. Every two years. Generally works; PPAs and third-party repos are disabled and must be re-enabled; snaps carry over. Historically messier than Fedora's, largely because Ubuntu users accumulate more third-party cruft over five years. Many experienced users prefer a clean reinstall at LTS boundaries — it's a 45-minute job if `$HOME` is on its own partition or backed up.
- **Debian stable → stable:** edit `sources.list`, `apt full-upgrade`. Every ~2 years. Excellent track record; Debian's release notes are meticulous about what needs manual attention.
- **Linux Mint:** the "Upgrade Tool" handles point (22.1→22.2) upgrades trivially; major (22→23) upgrades are supported via the tool but Mint's team is candid that a clean install is cleaner.
- **openSUSE Leap:** `zypper dup` with repo changes. Works; Leap 15→16 was a bigger jump than usual because of the rebase onto the SLE 16 codebase.

The upgrade cliff is the hidden maintenance cost of point releases. It's *bursty* rather than continuous — an hour every six months (Fedora) or an afternoon every two years (LTS) — which many people prefer to the rolling model's steady trickle.

## 4.2 Rolling releases, lived

### The promise

New upstream releases flow into the repository after a brief testing period. Arch's is short (typically hours to a few days in `testing`); Tumbleweed's is longer and automated (every snapshot passes openQA's integration test suite before publication). There are no versions to upgrade between; you just update, and you're always current.

The benefit is obvious: **newest kernel, newest drivers, newest compilers, newest desktop**, all the time. The AUR adds *everything else*, also current.

### What "unstable" really means

Arch is famous for being "unstable." This is true in the technical sense (the software changes constantly) and mostly false in the colloquial sense (things break all the time). The realistic experience for a well-maintained Arch install in 2025–2026:

- **Routine:** `pacman -Syu` (or `paru`) daily or weekly; 30 seconds to 5 minutes; nothing happens.
- **Occasionally (several times a year):** a `.pacnew` file appears for a config you edited, and you should merge it. Some AUR package needs a rebuild because a library bumped its soname. A GNOME or Plasma major version arrives and an extension/widget you use stops working until its author updates it.
- **Rarely (once or twice a year):** something needs **manual intervention**, announced on the [Arch news feed](https://archlinux.org/news/). Examples from the last year: the NVIDIA 590 driver dropping Pascal support (December 2025 — users of GTX 10xx cards had to switch to the `nvidia-580xx-dkms` legacy package or lose their display), a package rename requiring `pacman` to be told about the conflict, a filesystem-layout change. **If you read the news before updating — the `informant` AUR package forces you to — you'll never be surprised.** If you don't, you will eventually be.
- **Very rarely:** an actual bug ships. It gets fixed within hours to days. If it affects boot, you use the fallback initramfs or an LTS kernel, or roll back with `downgrade`/a Btrfs snapshot.

The honest summary: **Arch breaks about as often as an LTS hits an unfixed backport bug — but Arch's breakage is visible and attributable to a specific update, while the LTS's is silent and permanent.** Whether that's better depends on your temperament.

Tumbleweed's openQA gate makes actual regressions rarer still; the trade-off is that big transitions (a new GNOME) sometimes take a week or two longer to land while openQA is satisfied.

### The real cost: attention

Rolling releases don't demand more *skill* than point releases. They demand more *attention*. You must update regularly (letting an Arch install sit for six months and then updating is the classic recipe for pain — partial upgrades are unsupported, and the keyring may have rotated). You must read the news. You must notice `.pacnew` files. You must accept that your desktop will occasionally change appearance or behaviour without your asking.

If that attention is a hobby to you, the cost is zero. If it's a tax, it adds up — I'd estimate 10–20 hours a year for an average Arch desktop user who's paying attention, versus 2–5 hours for a Fedora user and 1–3 for an Ubuntu LTS user (excluding the biennial upgrade). Those are rough, personal estimates; your mileage varies with hardware (NVIDIA doubles them) and how many AUR packages you maintain.

### Curated rolling: the compromise that mostly works

**Manjaro** holds Arch packages in its own repos for about two weeks of extra testing. This sounds ideal and is Manjaro's main selling point. The catch is *partial* delay: the AUR is built against current Arch, so AUR packages regularly break on Manjaro's two-week-old libraries — the exact opposite of the intended stability. Manjaro also has a history of self-inflicted problems (expired SSL certificates several times, a DDoS'd AUR incident, team governance drama). It has improved and remains popular, but among experienced users it's the Arch derivative with the worst reputation, and for a good reason: it takes on the risks of rolling without fully delivering the benefits.

**openSUSE Slowroll** snapshots Tumbleweed monthly-ish (plus security fixes). Since it's the same repository frozen, not a separately built one, it avoids Manjaro's AUR-mismatch problem (openSUSE's OBS is per-distro). It's the most sensible "slower rolling" option, though still officially experimental-ish.

**CachyOS** is *not* slower than Arch — it tracks Arch in near-real-time — but adds its own repos with x86-64-v3/v4-optimised rebuilds of the core packages, a patched kernel with the BORE scheduler and other tweaks, and a very good Calamares installer with sane defaults (Btrfs + Snapper snapshots, zram, `paru` pre-installed, Limine or GRUB with snapshot boot entries). It is not "Arch made stable." It is "Arch installed and tuned the way a knowledgeable enthusiast would do it," and its popularity (top of DistroWatch since 2025, the fastest-growing distro in Steam's survey) reflects how many people want exactly that. The x86-64-v3 packages are a measurable but modest win (a few percent in CPU-bound workloads, more in some codecs and compression).

**EndeavourOS** is Arch with a friendly installer, a welcome app, and a handful of sensible defaults, tracking Arch's repos directly. It's the "just install Arch for me and get out of the way" option. Excellent community forum.

## 4.3 Atomic / image-based, lived

### The promise

Your operating system is a single, versioned, read-only image. Updating means downloading the next image and rebooting into it. If the new image doesn't boot or something's wrong, you select the previous one from the boot menu — instant, guaranteed rollback. The base OS is *identical* on every machine running the same image, so bugs are reproducible and the maintainers test what you run.

The implementations:

- **Fedora Atomic Desktops** (Silverblue = GNOME, Kinoite = KDE, Sway Atomic, Budgie Atomic). Built on **rpm-ostree**, transitioning to **bootc** (the OS image is literally an OCI container image you can `podman pull`). Fedora's release cadence; six-month rebases.
- **Universal Blue** — a community project building custom bootc images on top of Fedora Atomic, with the proprietary bits (codecs, NVIDIA drivers, extra firmware) baked in and opinionated defaults. **Bluefin** (GNOME, developer-oriented; **Bluefin DX** adds VS Code, Docker, the JetBrains toolbox and more into the image), **Aurora** (KDE, same idea; Aurora DX), **Bazzite** (gaming: Steam, Proton, controller support, HDR tweaks; also a superb general desktop). Images rebuild daily; you get *tested* updates automatically in the background; a "Bluefin LTS" on a CentOS Stream base exists for people who want an even slower cadence. Universal Blue's insight is that image-based distros let a small team ship a *complete, integrated* system without any of the "install these six things after installing" rituals.
- **openSUSE Aeon** (GNOME) and **Kalpa** (KDE). Built on Tumbleweed with a transactional-update, read-only-root model plus Btrfs snapshots. Rolling base, atomic updates.
- **Vanilla OS** (Orchid). Debian-based; the `apx` tool manages Distrobox containers for any package manager; ABRoot dual-partition atomic updates.
- **NixOS** is atomic *and* declarative — every rebuild is a new bootable generation.

### The friction points, honestly

Atomic desktops are the future for a lot of people, and the Universal Blue images in particular are good enough to recommend broadly. But the model has real friction that advocates gloss over:

1. **You cannot `dnf install` things into the base.** Well, you can *layer* an RPM (`rpm-ostree install foo`), but each layered package makes updates slower and is discouraged. The intended workflow is: GUI apps → Flatpak; CLI dev tools → Homebrew (Bluefin ships it) or a Distrobox container; language toolchains → version managers or containers; things that must be on the host (a VPN client, a kernel module, a udev rule) → layer or, better, build your own image. This is *fine* once you internalise it and *maddening* if you fight it. Many tutorials assume you can just install a package on the host; on an atomic system you must translate.
2. **Kernel modules are hard.** Anything DKMS — a proprietary driver not in the image, VirtualBox, some VPNs — either needs to be in the image (Universal Blue bakes in NVIDIA, v4l2loopback, some others) or you're building a custom image. VirtualBox is the classic casualty; use KVM/virt-manager or GNOME Boxes instead (better anyway).
3. **`/usr` is read-only, `/etc` is a merged overlay, `/opt` and `/usr/local` are symlinks into `/var`.** Software that wants to install into `/usr/local` or `/opt` (some vendor installers) needs coaxing.
4. **Layering + rebases occasionally conflict.** Layered packages can block an image update if their dependencies change. Fedora's tooling has improved here but it's not zero-friction.
5. **Some development tools assume they own the host.** Docker Desktop's Linux build, some kernel-tracing tools, `perf`, certain security tools. Bluefin DX handles Docker/Podman well; other cases need thought.
6. **Debugging is different.** You can't just `apt-get source` and patch something on the host. You *can* build a derived image with your patch (Universal Blue makes this a GitHub Actions template), which is arguably better — but it's a different mental model.

For an **engineer whose work lives in containers, a browser, and an IDE**, and a **daily driver who wants zero maintenance**, atomic is a very strong fit. For a **systems programmer who hacks on the kernel, drivers, or low-level tooling**, or a **student in an OS course** who needs to install odd toolchains on the host, it adds a layer of translation that may not be worth it — a conventional distro with Btrfs snapshots delivers most of the rollback benefit with none of the friction.

## 4.4 Declarative: NixOS, lived

### The promise

Your entire system — packages, kernel, services, users, config files, desktop settings (via Home Manager), even the partition layout (via Disko) — is described in Nix language files, ideally in a git repository. `nixos-rebuild switch` makes the machine match the description. Every rebuild creates a new *generation*; all previous generations are bootable from the menu. Delete the config lines for a package and it's gone — completely, with no orphaned files. Copy your repo to a new laptop, run one command, and you have *your machine*, exactly.

Beyond system configuration, **nixpkgs** is the largest and one of the freshest package collections in existence, and **Nix development shells** (`nix develop`, or `direnv` + `nix-direnv`) give every project its own precise toolchain — the right `gcc`, `python`, `nodejs`, `postgresql` — activated on `cd`, with zero global pollution. For a developer, this last feature is arguably the killer app, and you can use Nix-the-package-manager on *any* distro (or macOS) to get it without committing to NixOS-the-distro.

### The cost

- **You must learn Nix**, a lazy, functional, dynamically typed language with some sharp edges and error messages that have improved but remain cryptic. Two to four weekends to become functional; months to become fluent.
- **Documentation is fragmented.** The official manual, the wiki (community-maintained, now at wiki.nixos.org after a fork of the older unofficial one), Zero to Nix, nix.dev, blog posts and Discourse — you'll consult all of them. The **flakes** feature has been "experimental" for years yet is the de facto standard, which confuses newcomers who see two ways to do everything.
- **It does not follow the FHS.** Nothing lives in `/usr/bin` or `/lib`. Pre-built binaries you download (many CLI tools from GitHub releases, some proprietary software, VS Code's remote server, Python wheels with bundled native libraries) fail with "No such file or directory" because the dynamic linker isn't where they expect. Fixes exist — `nix-ld`, `steam-run`, `buildFHSEnv`, `patchelf` — but every one is a papercut you didn't have elsewhere. This is the number-one practical complaint from developers on NixOS.
- **Community turbulence.** 2024 saw a governance crisis (sponsorship disputes, moderation conflicts, the founder stepping back, several prominent contributors leaving; forks like Lix and Aux emerged). The project has since put a steering committee in place and stabilised, but it's fair to note that NixOS's governance has been rockier than most.
- **Rebuilds can be slow**, especially with Home Manager and many packages; the binary cache helps enormously, but anything with an overlay or override compiles locally.

### When it pays off

- You manage **more than one machine** and want them identical.
- You want **reproducible dev environments** at a level Docker doesn't reach (Docker is reproducible at the image layer; Nix is reproducible at the build-input level).
- You **enjoy** this kind of thing and will treat the learning as an investment. Many who make it through the curve report they can't go back; many who don't report it as the most frustrating month of their computing life.
- You're okay with your friends not being able to help you.

Middle path, strongly recommended for the curious: **use Nix on a conventional distro** for development shells and Home Manager for dotfiles, then decide about NixOS proper after six months.

## 4.5 Package managers, compared

Ergonomics for common operations. Every one of these is perfectly usable; this table is for muscle-memory translation and to show that the differences are cosmetic.

| Task | apt (Debian/Ubuntu) | dnf (Fedora) | pacman (Arch) | zypper (openSUSE) | nix (NixOS) |
|---|---|---|---|---|---|
| Update repo index + upgrade all | `sudo apt update && sudo apt upgrade` | `sudo dnf upgrade` | `sudo pacman -Syu` | `sudo zypper dup` (TW) / `zypper up` (Leap) | `sudo nixos-rebuild switch --upgrade` |
| Install | `sudo apt install foo` | `sudo dnf install foo` | `sudo pacman -S foo` | `sudo zypper in foo` | add to config, rebuild (or `nix profile install nixpkgs#foo`) |
| Remove (+ unneeded deps) | `sudo apt autoremove --purge foo` | `sudo dnf remove foo` | `sudo pacman -Rns foo` | `sudo zypper rm -u foo` | remove from config, rebuild |
| Search | `apt search foo` | `dnf search foo` | `pacman -Ss foo` | `zypper se foo` | `nix search nixpkgs foo` |
| Which package owns a file | `dpkg -S /path` | `dnf provides /path` | `pacman -Qo /path` | `zypper se --provides /path` | (`nix-locate`, via nix-index) |
| List files in package | `dpkg -L foo` | `dnf repoquery -l foo` | `pacman -Ql foo` | `rpm -ql foo` | `ls $(nix path-info nixpkgs#foo)` |
| Transaction history / undo | `apt history-list` / `apt history-undo N` (3.2+) | `dnf history` / `dnf history undo N` | none built-in; use snapshots or `downgrade` | `zypper` has none; use Snapper snapshots | `nixos-rebuild switch --rollback`; boot any generation |
| Community repo | PPAs (`add-apt-repository`) | COPR (`dnf copr enable`) | AUR (via `paru`/`yay`) | OBS (`zypper ar`) | overlays / flake inputs |
| Speed | good | good (dnf5) | very fast | okay | slow to evaluate, fast to switch |

Notes:

- **`apt`** gained history/undo/rollback in 3.2 (Ubuntu 26.04) — a big quality-of-life improvement that closes a long-standing gap with `dnf`.
- **`dnf5`** (Fedora 41+) is a rewrite in C++ that is much faster than the old Python `dnf` and has excellent history/rollback.
- **`pacman`** is fast partly because it does less (no history, no delta updates). The convention on Arch is that snapshots (Snapper/Timeshift on Btrfs) are your undo. CachyOS and EndeavourOS set this up for you; vanilla Arch leaves it to you.
- **AUR helpers** (`paru`, `yay`) wrap `pacman` and build AUR packages. Remember AUR packages are *build scripts submitted by users*; the helpers show you the PKGBUILD diff before building. Read it, at least skim it. Also remember that AUR packages are unsupported by Arch itself — if an update breaks one, that's between you and the AUR maintainer.
- **`zypper`** is verbose and slower but very explicit about what it's doing; openSUSE users generally like it. `zypper dup` (distribution upgrade) is the correct daily command on Tumbleweed, not `up`.

## 4.6 Universal formats, compared

| | Flatpak | Snap | AppImage |
|---|---|---|---|
| Who | Freedesktop community; Flathub is the store | Canonical | Community; no central store (AppImageHub is a directory) |
| Scope | GUI apps (CLI possible, awkward) | Anything: GUI, CLI, daemons, even kernels | Single-file GUI apps mostly |
| Sandbox | bubblewrap namespaces + portals; per-app permissions (Flatseal / desktop settings) | AppArmor confinement; interfaces; "classic" mode = no confinement | None (unless the app does it) |
| Dedup / size | Shared runtimes; first app is big (~1 GB runtime), subsequent apps small | Shared "core"/"gnome" snaps; similar | Each file is self-contained; largest per-app |
| Startup | Near-native | Historically slow first launch (compressed squashfs); improved | Near-native |
| Updates | `flatpak update`, or via software center; delta updates | Automatic, forced (schedulable, refresh can be held) | Manual unless app self-updates; AppImageLauncher helps |
| Theming / integration | Good; uses portals for file dialogs, respects GTK/Qt theme via extensions | Okay; gets better each year | Depends on app |
| Store backend | Open; anyone can host a remote | Proprietary Canonical store only | N/A |
| Distros shipping by default | Fedora, openSUSE, Mint, Pop!_OS, Zorin, elementary, EndeavourOS, CachyOS, all atomic distros | Ubuntu and official flavours only | none |
| Best for | GUI apps on any distro; sandboxing | Ubuntu users; CLI tools with confinement; IoT | one-off tools, portable apps |

**Practical guidance.** Use Flatpak for GUI apps you want current and sandboxed (browsers, chat, media, office, creative). Prefer distro packages for anything CLI or deeply integrated (terminal, shell, `git`, compilers, `docker`). On Ubuntu, either accept snaps (they've improved; the Firefox snap is fine for most people in 2026) or remove `snapd` and add Flathub — a well-documented ten-minute process, though Ubuntu's App Center won't show Flatpaks (install GNOME Software or use the `flatpak` CLI). Avoid AppImages as a primary method.

**A note on IDEs and Flatpak.** VS Code and JetBrains IDEs run as Flatpaks but live in a sandbox that can't see your host toolchains, Docker socket or `~/.ssh` without permission changes, and their integrated terminal is inside the sandbox (use `flatpak-spawn --host` or the Host Shell extension). Most developers are happier with the vendor's native package (Microsoft's `.deb`/`.rpm` repo; JetBrains Toolbox) or, on atomic distros, the Bluefin DX approach (IDE in the image, tools in Distrobox with the IDE's remote-container features).

## 4.7 The developer-tooling layer: why the distro matters less than it used to

This deserves its own section because it inverts a lot of received wisdom.

Ten years ago, "Debian stable is too old for development" was a real complaint: you got Python 2.7 and GCC 4.9 and no easy way to get anything else. Today:

- **Language version managers** — `uv` (Python; also replaces pip/venv/pyenv/poetry), `mise` (polyglot; successor to asdf), `rustup`, `fnm`/`volta`/`nvm` (Node), `sdkman` (JVM), `ghcup` (Haskell), `opam` (OCaml), `g`/`goenv` (Go), `rbenv`. Every one is a `curl | sh` or a single package away, on any distro, and gives you every version of the language independent of the distro.
- **Homebrew on Linux** — the macOS package manager, installed to `/home/linuxbrew/.linuxbrew`, with thousands of fresh CLI tools (ripgrep, fd, bat, lazygit, gh, k9s…) that don't touch the system. Bluefin ships it by default; anyone can install it. It's the answer to "my LTS has an old version of X."
- **Distrobox / Toolbox** — a container with a full distro userland (Ubuntu, Arch, Fedora, Alpine, whatever) whose `$HOME` is your `$HOME`, with GUI and audio passthrough, and whose binaries can be *exported* to appear in your host `$PATH`. Want the AUR on Fedora? `distrobox create -i archlinux` then `paru -S whatever` and `distrobox-export`. Want to test against the department's Ubuntu 24.04? `distrobox create -i ubuntu:24.04`. This single tool removes "which repos does my distro have" as a decision factor.
- **Devcontainers** — a `.devcontainer/devcontainer.json` in the repo defines the exact toolchain; VS Code, JetBrains, and the `devcontainer` CLI build and attach. The distro on your laptop is irrelevant to the project's build.
- **Nix** (on any distro) — per-project shells with exact versions.
- **Docker/Podman** — for services (databases, queues, caches) you'd never install on the host anyway.

The upshot: **for the toolchain, choose whichever distro you like; you'll get the same tools.** The distro still decides your kernel, drivers, desktop, and how the *base* behaves under updates. That's where the choice should focus — which is exactly what the top-weighted criteria in Chapter 3 say.

The one caveat: all of this tooling assumes an FHS-compliant glibc system. NixOS (non-FHS) and Alpine (musl) are the exceptions where `curl | sh` installers and pre-built binaries fail. On NixOS you use Nix for everything instead, which is the point.

## 4.8 Kernel modules and drivers: the recurring pain

Out-of-tree kernel modules are the single most common cause of "my update broke my computer." Understanding the delivery mechanisms helps you choose.

**In-tree** (AMD, Intel, most WiFi/Bluetooth/touchpads, and now the `nova`/Nouveau NVIDIA drivers for basic display): nothing to do; they ship with the kernel.

**Out-of-tree**, delivered as:

| Mechanism | How it works | Failure mode | Who uses it |
|---|---|---|---|
| **Pre-built, kernel-matched packages** | The distro compiles the module against each kernel it ships and publishes both together | Almost none; the module is tested against exactly that kernel | Ubuntu (`linux-modules-nvidia-*`), Arch (`nvidia-open` for `linux`, `nvidia-lts-open` for `linux-lts`), Fedora via RPM Fusion's pre-built `kmod-nvidia` for the current kernel (with akmods as fallback), Universal Blue images (baked in) |
| **DKMS / akmods** | On each kernel update, a hook compiles the module source against the new headers on *your* machine | New kernel breaks the build (API change) → module missing → black screen or missing device until upstream fixes the source | Arch `*-dkms` packages (for custom kernels), Fedora `akmod-*` (RPM Fusion), Debian `*-dkms`, everything on a rolling distro that isn't pre-built |
| **Vendor `.run` installer** | NVIDIA's own script installs everything outside the package manager | Every kernel update breaks it; the package manager doesn't know it exists; **never do this on a desktop** | Nobody who's been burned |

**NVIDIA specifics as of 2026:**

- The **open kernel modules** (`nvidia-open`) have been the default and recommended flavour since the 560 series for Turing (RTX 20xx / GTX 16xx) and newer. Performance parity with the proprietary module; better upstream cooperation. Arch moved its main packages to the open flavour in December 2025 and dropped the proprietary `nvidia-dkms` from the repos; the userland (CUDA, Vulkan, the display driver) remains proprietary.
- The **590 series** (December 2025) dropped support for **Pascal (GTX 10xx) and older**. Those cards live on the **580xx legacy branch**, which gets security fixes only. If you own a GTX 1060/1070/1080 in 2026, you're on legacy drivers and should plan a GPU upgrade or accept that new kernels will eventually outrun the legacy branch (Arch users must use `nvidia-580xx-dkms` from the AUR).
- **Wayland on NVIDIA** is fine on 590+: explicit sync, GAMESCOPE, VRR, and most compositors work. Residual issues: some multi-monitor/VRR edge cases, night light on some setups, occasional flicker regressions in point releases.
- **Secure Boot + NVIDIA** requires signing the module. Ubuntu's `ubuntu-drivers` and Fedora's akmods (with a one-time `kmodgenca` + `mokutil --import`) automate this; Arch requires manual `sbctl` setup. Or disable Secure Boot.
- **CUDA** is version-locked to specific driver ranges; NVIDIA's documentation targets Ubuntu LTS first, then RHEL/Fedora. It works on Arch (`cuda` package) but you get whatever version Arch ships, which may be newer than PyTorch's wheels expect — pin via conda/uv rather than the system package.

**The recommendations that fall out:**

- **AMD or Intel GPU:** any distro; the driver is in-tree; nothing to think about. (This is a real, tangible reason to prefer AMD when buying a Linux machine.)
- **NVIDIA + want minimal friction:** Ubuntu LTS (pre-built modules, Secure Boot handled), Pop!_OS NVIDIA ISO (same, with System76's tuning), or Bazzite/Bluefin/Aurora `-nvidia` images (driver baked into a tested image — the closest to "never think about it").
- **NVIDIA + Fedora:** RPM Fusion's `akmod-nvidia`; works well; you'll wait a few minutes after each kernel update while it builds, and after a new *major* kernel you should wait a few days before updating in case the module needs patching.
- **NVIDIA + Arch:** `nvidia-open` with the stock kernel is pre-built and fine; keep `linux-lts` + `nvidia-lts-open` installed as a fallback; read the news.
- **NVIDIA + atomic non-UBlue (Silverblue/Kinoite):** possible via layering RPM Fusion's akmods but clunky; use Universal Blue's images instead.

---

### Key takeaways

- A fresh LTS is nearly as current as a rolling distro for a few months, then ages; Fedora's six-month cadence with in-release kernel/Mesa rebases makes it "semi-rolling" and is the pragmatic middle for developers.
- Language version managers, Homebrew, Distrobox, devcontainers and Flatpak have made the base distro's repository freshness *almost irrelevant for your toolchain*. Focus the distro choice on kernel/drivers, desktop and update behaviour instead.
- Rolling releases don't demand more skill, they demand more *attention*: update regularly, read the news, handle `.pacnew`. Budget roughly 10–20 hours/year on Arch vs. 2–5 on Fedora vs. 1–3 on Ubuntu LTS (NVIDIA roughly doubles these).
- Manjaro's delayed-repos-plus-live-AUR model is a design flaw; prefer EndeavourOS or CachyOS for "easy Arch," or Slowroll for "slower Tumbleweed."
- Atomic distros deliver genuine unbreakability and are the best "appliance" option — especially Universal Blue's Bluefin/Aurora/Bazzite — but require adopting the Flatpak/Homebrew/Distrobox workflow and struggle with out-of-image kernel modules and host-level hacking.
- NixOS is uniquely reproducible and rewards investment, but its non-FHS layout and learning curve are real costs; try Nix on another distro first.
- All package managers are competent; `apt` 3.2 finally has undo; `pacman` relies on snapshots for rollback. Use Flatpak for GUI apps, distro packages for CLI/system pieces, and avoid AppImages as a primary channel.
- Out-of-tree kernel modules (chiefly NVIDIA) are the top cause of update breakage; prefer pre-built, kernel-matched module packages (Ubuntu, Arch `nvidia-open`, Universal Blue images) over DKMS on a daily driver, and buy AMD/Intel if you can.


---

# Chapter 5 — Desktop Environments and Window Managers

Here is a claim that surprises newcomers: **your choice of desktop environment affects your daily experience more than your choice of distribution.** Fedora KDE and Kubuntu feel more alike than Fedora Workstation (GNOME) and Fedora KDE do. The desktop is what you look at, click on, and fight with for eight hours a day; the distro is the plumbing.

Fortunately the desktop choice is (a) mostly independent of the distro — every major DE runs on every major distro — and (b) easy to test: boot a live USB, use it for an hour, form an opinion. Do that before reading Reddit threads.

## 5.1 The two first-class citizens

Two desktops receive the lion's share of development effort, testing and distro integration. Choosing one of them is the low-risk path.

### GNOME

**What it is.** The default desktop of Fedora Workstation, Ubuntu, Debian, Zorin, and the GNOME-flavoured atomic distros (Silverblue, Bluefin, Aeon). Developed by the GNOME Foundation with heavy Red Hat, Canonical, SUSE and Endless involvement. Six-month cadence — GNOME 50 shipped March 2026; 51 is due September 2026.

**The philosophy.** GNOME is *opinionated*. It has a specific workflow — an Activities overview showing windows and workspaces, a top bar, a dock hidden until invoked, dynamic workspaces, minimal window chrome (no minimise button by default), a keyboard-and-gesture-first model — and it expects you to adapt to it rather than the reverse. The Settings app exposes what the designers think you should change and nothing else. Applications follow the GNOME Human Interface Guidelines: header bars, hamburger menus, adaptive layouts, `libadwaita` styling that looks identical everywhere and resists theming.

**The experience.** When you accept the workflow, GNOME is calm, cohesive, fast to navigate with `Super` + type-to-search, and has the best touchpad gestures on Linux (three-finger swipe between workspaces is superb on a laptop). Fractional scaling and VRR are stable as of GNOME 50. Wayland-only since 50 (the X11 session is gone). Accessibility is the best on Linux; the Orca screen reader was overhauled in 50. The core apps — Files (Nautilus), Ptyxis/Console, Text Editor, Loupe, Showtime, Papers, Calendar, Weather, Software — are consistent and pleasant. HDR plumbing has landed in Mutter and is reaching apps.

**The friction.** GNOME's opinions are strong and some are unpopular:

- No system tray by default (an extension restores it; Slack, Discord, Steam and many others expect one).
- No desktop icons, no minimise button, a dock only in the overview (Ubuntu and Zorin patch in a persistent dock; extensions exist).
- **Extensions** fill every gap — Dash to Dock/Panel, AppIndicator, Blur My Shell, Tiling Shell/Forge/Pop Shell for tiling, GSConnect for phone integration, Clipboard Indicator. They're JavaScript against an unstable internal API, so **every six-month GNOME release breaks some of them** until authors update. Heavy extension users on Fedora (new GNOME on day one) live this twice a year; Ubuntu LTS users rarely do (GNOME is frozen two years, and Canonical maintains its own dock/appindicator/tiling extensions). Pick a few well-maintained extensions and resist installing twenty.
- Theming is deliberately hard: libadwaita apps ignore GTK themes; you get accent colours and dark mode.
- Idle memory ~1–1.5 GB — fine on 8 GB+, noticeable below.
- Some settings live in `dconf-editor` or GNOME Tweaks rather than Settings.
- Parts of the GNOME community can be dismissive of requests outside the design vision, which frustrates people who just want a minimise button.

**Best for.** People who like a Mac-ish, keyboard-driven, uncluttered workflow and will adapt to it. Laptop users who value gestures. Anyone who wants the most-tested desktop on the most-tested distros (Fedora Workstation and Ubuntu are both GNOME).

**Avoid if.** You want a Windows-like taskbar/tray/menu layout without extensions, want deep customisation, or dislike being told how to work.

### KDE Plasma

**What it is.** The default of Fedora KDE Plasma Desktop (an official Edition since Fedora 42), Kubuntu, KDE neon, openSUSE (its historical home), CachyOS, Garuda, Nobara, SteamOS desktop mode, Bazzite, Aurora, Kinoite and Kalpa. Developed by the KDE community (KDE e.V., a German non-profit, with funding from Blue Systems, Valve, SUSE and others). Plasma 6 launched February 2024; 6.6 (February 2026) and 6.7 (July 2026) are current; **6.8 (October 2026) removes the X11 session**. Plasma 6.6 is being maintained as a three-year "Bullet-proof KDE" LTS branch until 2029. Roughly three releases a year.

**The philosophy.** "Simple by default, powerful when needed." Plasma ships a familiar layout — bottom panel, launcher, system tray, task manager, desktop icons — and lets you change *everything*: panels anywhere, widgets everywhere, per-window rules, every shortcut, animation and colour. KDE apps (Dolphin, Konsole, Kate, Okular, Gwenview, Spectacle, Kdenlive, Krita, digiKam) are feature-dense in the same spirit.

**The experience.** Plasma 6 on Wayland is fast, polished and feature-complete: fractional scaling, VRR, **HDR** (Plasma had it first and has the most mature implementation on Linux), per-display colour management, excellent multi-monitor handling (per-screen virtual desktops since 6.6), built-in tiling with custom layouts (`Super`+`T`), KRunner as a universal launcher/calculator/converter, KDE Connect for phone integration, Discover for software (Flatpak/Snap/native), a real system tray, and a setting for everything. Memory footprint comparable to GNOME. Wayland stability, once Plasma's weak point, has been excellent since 6.1.

**The friction.**

- Flexibility has a cost: settings sprawl, and there's often more than one way to do things. Liberating to some, exhausting to others. The 6.x series has trimmed a lot.
- Visual consistency is slightly lower than GNOME's — Qt, GTK and Electron apps coexist with more seams (Breeze GTK narrows it).
- Point releases occasionally introduce papercuts (a widget crashes, a shortcut resets). KDE's release frequency means bugs appear *and disappear* faster than GNOME's.
- Default look is "fine" rather than beautiful; five minutes of theming fixes it.

**Best for.** Windows switchers who want a familiar layout; people who want to configure their desktop exactly; gamers (HDR, VRR, Valve's investment); anyone who wants a full-featured desktop without extensions. The safest choice for people who "don't know what they want."

**Avoid if.** You want a fixed, curated workflow with few knobs, or visual uniformity matters more to you than features.

### GNOME vs. Plasma: the honest verdict

Both are excellent and stable in 2026. The difference is temperament:

- **GNOME**: fewer choices, more coherence, better gestures and accessibility, breaks extensions twice a year, fights you if you disagree.
- **Plasma**: more choices, more features (HDR, tiling, KDE Connect, tray), slightly more seams, never fights you, occasionally overwhelms.

Developers split roughly evenly. Newcomers skew toward Plasma because there's nothing to unlearn; long-term GNOME users rarely switch because the workflow becomes second nature. Try both for an hour on a live USB. **If you genuinely can't decide, pick Plasma** — fewer surprises, nothing to unlearn.

**Distro implications.** Both are first-class on Fedora (Workstation vs KDE Edition), Ubuntu (Ubuntu vs Kubuntu), Arch/EndeavourOS/CachyOS, openSUSE, Debian, Universal Blue (Bluefin vs Aurora), Fedora Atomic (Silverblue vs Kinoite), and NixOS. GNOME-only: Zorin, elementary (Pantheon). KDE-first: KDE neon (Ubuntu LTS base + always-latest Plasma — a showcase, not a great daily driver due to base/desktop version mismatch), Garuda, Nobara, Bazzite.

## 5.2 The credible third options

### Cinnamon

Linux Mint's flagship, forked from GNOME 3 in 2011 to preserve a traditional layout. Panel with menu, tray and task list; desktop icons; window buttons; a Settings app that exposes what a normal person wants and nothing more. Mature, conservative, quiet. The team declared the **Wayland session stable in mid-2026**; Mint 23 (December 2026) will fully support both X11 and Wayland, with X11 likely still default for a cycle. Fractional scaling works on Wayland; HDR/VRR are not priorities. Spices (applets/desklets/extensions) use a stable API, so breakage is rare.

**Best for.** Windows switchers, people who want zero surprises, older hardware (lighter than GNOME/Plasma). **Distros:** Linux Mint (the canonical home), LMDE, Ubuntu Cinnamon, Fedora Cinnamon Spin, Arch. Realistically, if you want Cinnamon you want Mint.

### COSMIC

System76's from-scratch desktop in Rust (iced toolkit, Smithay compositor), grown from their Pop Shell GNOME extension. **Epoch 1 (1.0) shipped December 2025** with Pop!_OS 24.04 LTS; point releases have followed rapidly (1.7 by August 2026). Design: a GNOME-like uncluttered look with **first-class tiling** (toggle auto-tiling per workspace, keyboard-driven window management), configurable panel and dock, a settings app with GNOME-style restraint but Plasma-style options, its own apps (Files, Terminal, Text Editor, Store), theming with accent and corner-radius controls, HDR in progress. Wayland-only.

**Status.** Usable as a daily driver and improving monthly, but young: a thinner native app suite (you'll use GNOME/KDE apps for gaps), fewer third-party integrations, occasional rough edges with Xwayland fractional scaling, and a smaller troubleshooting community. System76 has a commercial incentive to keep it moving. Available on Pop!_OS (default), Fedora COSMIC Spin, Arch (`extra`), NixOS, openSUSE and others.

**Best for.** People who want tiling without configuring a WM; developers who like GNOME's aesthetic but want a tray, tiling and more control. **Verdict:** promising, worth trying, not yet the low-risk choice.

### Xfce

The venerable lightweight desktop. Traditional layout, plainly configurable, extremely stable, ~500 MB idle. Slow cadence (4.20 in December 2024; 4.22 expected 2026). **Still X11 by default**; 4.20 introduced incomplete experimental Wayland support. If you have a specific X11 need or a genuinely old/low-RAM machine, Xfce is the answer. Otherwise it feels dated. **Distros:** Xubuntu, Mint Xfce, MX Linux, Fedora Xfce Spin, EndeavourOS, Debian.

### The rest, briefly

- **MATE** — GNOME 2's continuation. Light, stable, slowly moving to Wayland. Ubuntu MATE skipped LTS status for 26.04 for lack of contributors — a sign of a shrinking project.
- **LXQt** — Qt-based, very light, Wayland arriving via labwc/kwin. Lubuntu's desktop. For low-end hardware.
- **Budgie** — elegant, moderately popular, moving to its own stack in Budgie 11. Ubuntu Budgie, Fedora Budgie Spin, Solus. Small team.
- **Pantheon** — elementary OS's macOS-inspired desktop. Beautiful, opinionated, tied to elementary's slow cycle. Wayland since elementary OS 8.
- **Deepin DE** — visually striking; telemetry concerns and slow security updates limit adoption outside China.

## 5.3 Tiling window managers and compositors

A different approach: no desktop environment, just a program that arranges windows — automatically, in tiles — and lets you drive everything from the keyboard. You add a bar (Waybar), launcher (fuzzel, rofi-wayland, wofi), notification daemon (mako, dunst, swaync), lock screen (swaylock, hyprlock), wallpaper tool, screenshot tool, a portal backend for screen sharing, and configure all of it in text files.

**The Wayland compositors:**

- **Hyprland** — by far the most popular in 2026. Dynamic tiling, extremely smooth animations, huge config surface, plugins, very active development with frequent breaking config changes. The r/unixporn darling. The project's leadership has had public controversies (including a 2024 ban from Freedesktop.org infrastructure, since largely resolved).
- **Sway** — the i3-compatible compositor. Manual tiling, rock-stable, boring in the best way, i3's config format. For people who want a tool, not a project.
- **niri** — scrollable tiling (windows on an infinite horizontal strip, like PaperWM). Rust. Rapidly growing, excellent defaults, thoughtful design. My pick for people trying tiling for the first time in 2026.
- **river**, **dwl**, **labwc** (stacking, Openbox-like), **Wayfire**, and others.

X11 window managers (i3, bspwm, dwm, awesome, xmonad, qtile) still work, but new users should start on Wayland — GNOME, KDE and GDM have all abandoned X11.

**Should a developer use a tiling WM?**

*For:* Keyboard-only window management is genuinely faster once learned. Workspace-per-project workflows are natural. Resource use is minimal. You understand every piece of your desktop. Many extremely productive engineers swear by it.

*Against:* You are now the maintainer of your desktop environment. Screen sharing, Bluetooth and network applets, brightness and media keys, lock screen, idle management, lid handling, monitor hot-plug, clipboard manager, notification history, HiDPI for Xwayland apps, dark-mode switching for GTK/Qt apps, file-picker portals — each is something you install, configure, and can break. First setup is a weekend; keeping it working is ongoing. Screen sharing in Zoom/Teams needs `xdg-desktop-portal-wlr`/`-hyprland` and sometimes won't let you pick a window. Nobody else can use your laptop. "Ricing" is a documented productivity sink.

*The pragmatic middle:* Both big DEs tile. **Plasma's built-in tiling** (`Super`+`T` layouts; **Polonium** or **Krohnkite** KWin scripts for dynamic tiling), **GNOME's Tiling Shell / Forge / Pop Shell extensions**, and **COSMIC's native auto-tiling** (the best tiling-in-a-DE experience). You get 80% of the keyboard-driven benefit with 0% of the maintenance. Start there. Move to a dedicated compositor only if you want more — and install it as a *second session* alongside your DE so you always have a fallback at the login screen.

**Distro implications.** Any distro runs any compositor; some make it easier: **Arch/EndeavourOS/CachyOS** (everything in repos/AUR; the wiki documents it all), **Fedora Sway Atomic** and community Hyprland/niri COPRs, **NixOS** (declarative WM configs are a sweet spot; the Home Manager modules for Hyprland/Sway/niri are excellent), **Omarchy** (DHH's opinionated Arch + Hyprland setup that went viral in 2025 — good defaults, very opinionated), and Universal Blue community images. Debian/Ubuntu lag on versions — Hyprland in particular moves too fast for LTS packaging.

## 5.4 Glue you'll meet

- **Display manager (login screen):** GDM (GNOME), SDDM (KDE), LightDM (Xfce/Cinnamon/MATE), `greetd` + `tuigreet`/`regreet` (WM setups). Any DM launches any session; mixing is fine.
- **Portals:** `xdg-desktop-portal-gnome`/`-kde`/`-wlr`/`-hyprland`/`-gtk` handle file pickers, screen sharing and settings for sandboxed apps. DEs configure this automatically; WM users install one.
- **Polkit agent:** the graphical privilege prompt. DEs ship one; WM users install one (`polkit-gnome`, `hyprpolkitagent`).
- **Cross-toolkit theming:** `qt6ct`/Kvantum/`adwaita-qt` for Qt apps on GNOME; `breeze-gtk` + `kde-gtk-config` for GTK on Plasma (automatic). Both DEs handle the other's apps acceptably now.

## 5.5 Making the decision

1. **Download two live ISOs** — one GNOME (Fedora Workstation), one KDE (Fedora KDE or Kubuntu). Write both to one USB with Ventoy.
2. **Spend an hour in each doing real things:** terminal, browser, WiFi, Bluetooth, second monitor, file manager, change a setting, screenshot, launcher.
3. **Notice your emotional reaction.** Calm or constraining? Capable or cluttered? That reaction is your answer.
4. **Curious about tiling?** Use the DE's built-in option for a month first.
5. **Choose the distro *then*** — from those that ship your DE as a first-class option.

---

### Key takeaways

- The desktop environment shapes your day more than the distro, and is independent of it.
- GNOME (opinionated, cohesive, gesture-first, Wayland-only since 50, extension breakage twice a year) and KDE Plasma (flexible, feature-rich, HDR-leading, Wayland-only from 6.8) are the two low-risk choices. Try both live; if undecided, pick Plasma.
- Cinnamon (via Mint) is the mature Windows-familiar third option with Wayland now stable. COSMIC is the promising Rust newcomer with excellent built-in tiling — usable but young. Xfce remains for X11 holdouts and very old hardware.
- Tiling compositors make some developers faster and cost all of them a weekend plus ongoing maintenance. Start with your DE's built-in tiling; graduate only if you want more, keeping the DE as a fallback session.
- Pick the desktop first, then the distro that ships it well.


---

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

## 6.3 Debian

**Identity and governance.** The Debian Project, founded 1993, entirely volunteer-run under a constitution, an elected Project Leader, and the Debian Social Contract and Free Software Guidelines. No company owns it. Ubuntu, Mint, Pop!_OS, Kali, Raspberry Pi OS, Proxmox and hundreds of others are built on it. The archive is the largest in the Linux world and the packaging standards (Debian Policy) are the strictest.

**Release model.** Three branches you can run:

- **Stable** — **Debian 13 "Trixie"**, released 9 August 2025. Roughly two-year cadence; three years of security support from the Security Team plus two more from the LTS team (five total). Frozen: kernel 6.12 LTS, GNOME 48, Plasma 6.3, GCC 14, Python 3.13. Point releases (13.1, 13.2…) roll up fixes every couple of months. The **backports** repository offers newer kernels and selected packages for stable users.
- **Testing** — the next release ("Forky", to become Debian 14 in ~2027). A *de facto rolling* distro with packages that have sat in unstable for ~10 days without release-critical bugs. Fresh, usually fine, but security fixes can lag because the Security Team doesn't cover testing, and during the freeze period before a release it stagnates. Many developers happily daily-drive testing; it's a legitimate choice with caveats.
- **Unstable ("Sid")** — the development branch; packages land here first. Rolling, faster than testing, occasionally broken in ways testing filters out. For contributors and the brave.

**Packaging.** APT 3.0 (Trixie) — the new coloured output and improved solver, but not yet 3.2's history/undo (that's Ubuntu 26.04; Debian will get it in Forky). The largest archive. No snaps. Flatpak available (`apt install flatpak` + Flathub); the GNOME and KDE images don't preconfigure it. Non-free firmware has been included in official installer images since Debian 12 (a big usability fix), and the `non-free`/`non-free-firmware` components are one line in `sources.list`.

**Desktop.** Installer offers GNOME (default), KDE Plasma, Xfce, Cinnamon, MATE, LXQt, LXDE, and no desktop. All as upstream shipped them at freeze time, unpatched. Wayland default for GNOME and Plasma; X11 sessions still present in Trixie's versions.

**Hardware.** Stable's 6.12 kernel is the limitation: hardware newer than roughly early 2025 may have partial support until you install the backports kernel (6.18 LTS is in trixie-backports). Firmware included. NVIDIA via `nvidia-driver` (DKMS, in `non-free`) — works, with the usual DKMS caveats, and the version is frozen at release (Trixie has 550/570-era drivers; newer GPUs like RTX 50-series need backports or NVIDIA's repo). Secure Boot works.

**Developer experience.** Rock-solid base; you *will* use version managers and containers for anything current, and that's fine. Debian is what your production servers and Docker base images probably run, so matching it locally has real value. `.deb` ecosystem gravity is nearly Ubuntu's (most vendor `.deb`s work on Debian, though a few assume Ubuntu-specific paths or versions). Testing gives you a rolling experience with Debian's packaging quality.

**Daily-driver polish.** Good but plain. Debian does not hold your hand: codecs work (no patent worries in Debian's jurisdiction stance), but you'll enable `non-free`, add Flatpak, and possibly the backports kernel yourself. The installer (still the venerable debian-installer, with a Calamares option on live images) is functional and dated-looking. Nothing is broken; nothing is curated. Stable's older GNOME/Plasma means you miss a year or two of desktop improvements.

**Security defaults.** AppArmor enabled. Excellent, conservative security team with a reputation for careful backporting. No firewall active by default (few listening services). Reproducible builds are a Debian flagship effort — 95%+ of the archive builds bit-for-bit reproducibly, a genuine supply-chain security achievement.

**Documentation and community.** Extensive but scattered: the Debian Wiki, the Administrator's Handbook (excellent and free), mailing lists, forums, IRC. Ubuntu Q&A mostly applies. The community is technical and expects you to read; it's less newcomer-oriented than Fedora's or Mint's.

**Governance risks.** Effectively none — no company to lose interest. The risk is *pace*: Debian moves deliberately, sometimes glacially, and consensus processes occasionally produce drama (the systemd vote, the firmware vote) that resolves over years.

**Who should pick it.**
- People who want maximum stability and minimum change, and know how to layer freshness on top.
- Server-minded developers who want their desktop to match their deployment target.
- Users on older hardware (anything pre-2024 is fully supported by 6.12).
- People who prefer volunteer, non-corporate governance on principle.
- Debian **testing** for people who want rolling-ish freshness with Debian's packaging quality and understand the security-lag caveat.

**Who should not.**
- Owners of hardware newer than ~12 months (use backports, or a fresher distro).
- People who want out-of-box curation (Mint gives you Debian-family polish; Ubuntu gives you Debian-family gravity).
- Anyone who needs current GNOME/Plasma features.

**Verdict: 7/10 for our persona** on stable; **7.5** on testing for the experienced. Superb foundation, deliberately unpolished, best when you know exactly why you want it. For most of our readers, Ubuntu or Mint delivers Debian's benefits with less setup; for some, Debian's purity is the point.

---

## 6.4 Linux Mint

**Identity and governance.** An independent project led by Clément Lefebvre since 2006, funded by donations and sponsors, with a small core team. Ubuntu LTS-based (Mint 22.x on Ubuntu 24.04; **Mint 23** on Ubuntu 26.04 due **December 2026**), with a Debian-based sibling (**LMDE 7** on Debian 13) maintained as insurance against Ubuntu going somewhere Mint won't follow.

**Release model.** Tracks Ubuntu LTS: a major release every two years, point releases (22.1, 22.2, 22.3) roughly every six months bringing Cinnamon and Mint-tool updates plus Ubuntu's HWE kernel. Five years of support riding on Ubuntu's. Upgrades between point releases are trivial (Update Manager); between majors via the Upgrade Tool.

**Packaging.** Ubuntu's APT repos with Mint's own additions and **snap disabled by default** (`snapd` is blocked via an apt preference; you can unblock it). **Flatpak preconfigured with Flathub** and integrated into Mint's Software Manager. Firefox and Chromium are shipped as proper `.deb`s (Mint builds Firefox itself under a Mozilla agreement). Mint's own tools — Update Manager (with kernel management and Timeshift integration), Software Manager, Driver Manager, Warpinator (LAN file transfer), Hypnotix (IPTV), Webapp Manager, Sticky Notes — are consistently good and the reason many people stay.

**Desktop.** **Cinnamon** (flagship), plus Xfce and MATE editions. Traditional layout, restrained, familiar. **Cinnamon's Wayland session became non-experimental in mid-2026**; Mint 23 will fully support both, likely defaulting to X11 for one more cycle before the switch. Mint's themes and icon sets are attractive out of the box. X-Apps (Xed, Xviewer, Xreader, Pix, Xplayer) are traditional-UI forks of GNOME apps.

**Hardware.** Ubuntu's, including HWE kernels via the point releases (Mint 22.3 shipped 6.14; Mint 23 will ship 7.0). **Driver Manager** GUI handles NVIDIA (Ubuntu's pre-built packages) and Broadcom WiFi with one click. Excellent on older hardware — Mint's audience skews toward extending the life of existing machines. The new Mint 23 installer adds Secure Boot handling and LVM/LUKS options that were awkward before.

**Developer experience.** Identical to Ubuntu underneath — every Ubuntu instruction works. Slight friction: Mint's Ubuntu version is always the LTS (never the interim), and a few vendor docs check for `lsb_release` saying "Ubuntu" and get confused by "Linux Mint" (rare; easily worked around). No snap means you install VS Code and friends from vendor `.deb`s or Flatpak — arguably better. Cinnamon's traditional multi-window workflow suits developers who came from Windows; its lack of gestures and modest Wayland polish (until 23) matter on laptops.

**Daily-driver polish.** **The best in class for newcomers.** Codecs a checkbox at install. Every tool a normal person needs is present, discoverable and works. Update Manager's Timeshift integration means system snapshots before updates — Mint has had a real "undo" for years. Printing, Bluetooth, media — fine. No telemetry, no nagging, no store pushing anything. The weak spots are all "modern-ness": no HDR, VRR only on Wayland (new), fewer gestures, a desktop that looks like 2015 (deliberately).

**Security defaults.** Ubuntu's AppArmor, `ufw` (Mint's firewall GUI makes enabling it obvious), LUKS from the installer, Secure Boot. Mint's Update Manager historically *de-emphasised* kernel and some critical updates for stability (the "levels" system), which drew criticism; since 2019 it applies all security updates by default. Fine.

**Documentation and community.** The most beginner-friendly forum in Linux. Mint's official user guide is good. Everything written for Ubuntu applies.

**Governance risks.** Small team; a real (if long-standing and so far unrealised) bus-factor concern. The LMDE hedge and Mint's conservative pace mean a disruption would be slow-moving, not sudden. Mint depends on Ubuntu's base decisions it doesn't control.

**Who should pick it.**
- First-time switchers from Windows who want familiarity and zero surprises.
- Anyone installing Linux for a family member.
- Older or lower-spec hardware.
- People who want Ubuntu's ecosystem without snaps and without doing the removal themselves.

**Who should not.**
- People who want GNOME or Plasma (install Ubuntu/Kubuntu/Fedora instead; Cinnamon is the point of Mint).
- People who want cutting-edge desktop features (HDR, gestures, latest Wayland work).
- Owners of brand-new hardware between Mint point releases (HWE lag).

**Verdict: 8/10 for our persona**, and **9/10 if the persona is specifically "newcomer who wants Windows-like."** The gap is entirely about desktop modernity; the fundamentals are excellent. Mint 23's Wayland-stable Cinnamon on the 26.04 base narrows the gap further.

---

## 6.5 Pop!_OS

**Identity and governance.** System76, a Denver hardware company that sells Linux laptops and desktops, created Pop!_OS in 2017 to ship on its machines. Ubuntu LTS-based. Funded by hardware sales. Small but very active engineering team writing a lot of Rust.

**Release model.** Tracks Ubuntu LTS, but System76 held **Pop!_OS 22.04** as current for an unusually long time while building COSMIC. **Pop!_OS 24.04 LTS** with **COSMIC Epoch 1** shipped December 2025; COSMIC point releases (1.1 → 1.7 by August 2026) roll out through the update channel. A 26.04-based release is expected but unannounced as of September 2026. Pop!_OS ships its own **current kernel** (System76 maintains it; 24.04 tracks recent stable kernels, not Ubuntu's HWE cadence) and current Mesa — so it's fresher on hardware than its base suggests.

**Packaging.** APT/`.deb` with Pop's own repos on top of Ubuntu's. **No snap** (removed entirely). **Flatpak with Flathub** preconfigured; the Pop!_Shop (being replaced by COSMIC Store) mixes debs and Flatpaks. Pop's own `.deb`s for the kernel, drivers, COSMIC, and their `system76-power` / `system76-scheduler` tooling.

**Desktop.** **COSMIC** — see Chapter 5. Native tiling, keyboard-first, GNOME-adjacent aesthetics, Rust from top to bottom, Wayland-only. Rapidly maturing. The Pop!_OS 22.04 ISO with the older GNOME + Pop Shell desktop remains downloadable for those who want it, but is on borrowed time.

**Hardware.** Two ISOs: standard (Intel/AMD) and **NVIDIA**, the latter with the proprietary driver pre-installed and tested — the single lowest-friction NVIDIA experience on Linux, because System76 sells NVIDIA laptops and must make it work. Hybrid graphics switching (`system76-power graphics integrated|hybrid|nvidia`) is the best implementation of the genre. Pop's kernel and firmware tooling target System76 hardware first, but it's generic Ubuntu underneath and runs on anything. Secure Boot: **not supported out of the box** (Pop!_OS uses systemd-boot with unsigned kernels; you disable Secure Boot). That's a real limitation for dual-boot with Windows 11 requirements and some corporate settings.

**Developer experience.** Ubuntu's ecosystem, no snaps, current kernel, the best NVIDIA/CUDA laptop experience, and — if you like tiling — a desktop built by and for people who live in terminals and editors. System76's own Rust-heavy stack means the `rustup`/cargo path is well-trodden. COSMIC's youth means occasional desktop bugs that a GNOME/Plasma user wouldn't encounter.

**Daily-driver polish.** Good and improving fast. Codecs included. COSMIC 1.x is usable for everything; its app suite is thinner than GNOME's/KDE's so you'll mix in apps from those ecosystems. Fractional scaling, multi-monitor, hybrid graphics all work. HDR arriving. Recovery partition with a "refresh install" that keeps your home directory is a genuinely great feature nobody else has.

**Security defaults.** Ubuntu's AppArmor. LUKS by default (the installer encrypts unless you opt out — good). systemd-boot. No Secure Boot. Firewall off.

**Documentation and community.** System76 support docs, a friendly subreddit and Mattermost, but far smaller than Ubuntu's; most Ubuntu answers apply. COSMIC-specific troubleshooting resources are still thin.

**Governance risks.** Pop!_OS is one company's product for its hardware; if System76 pivoted, the distro would be at risk (COSMIC the desktop would survive as open source). The long 22.04 hold showed System76 will prioritise its roadmap over release cadence.

**Who should pick it.**
- NVIDIA laptop owners, especially hybrid-graphics, especially for CUDA/ML.
- People who want built-in tiling without a WM project.
- System76 hardware owners (obviously).
- Developers who like the idea of a Rust-native desktop and don't mind being early.

**Who should not.**
- People who need Secure Boot.
- People who want a mature, complete desktop today (GNOME/Plasma) rather than a maturing one.
- People who want a predictable release cadence.

**Verdict: 7.5/10 for our persona**, rising as COSMIC matures. **8.5/10 for the NVIDIA-laptop subset.** The best-in-class NVIDIA story and a genuinely exciting desktop, held back by COSMIC's youth, no Secure Boot, and single-company dependence.

---

## 6.6 Briefly: Zorin OS and elementary OS

**Zorin OS** (Ubuntu LTS base; Zorin 18 on 24.04, a 26.04-based version expected). GNOME heavily customised with "layouts" that mimic Windows 11, macOS, or classic GNOME; strong Windows-app compatibility story (Wine/Bottles integration, a database of "you tried to open an .exe, here's the Linux alternative"). Free "Core" edition and a paid "Pro" edition with extra layouts and support. Polished, pretty, aimed squarely at Windows refugees. Development pace is slow (releases lag Ubuntu LTS by 6–12 months), the team is tiny, and the heavy GNOME modification means GNOME extension breakage is handled by Zorin, for good and ill. **Verdict: 7/10** — a fine Mint alternative for people who specifically want a Windows 11 look and don't mind waiting for releases. For our persona, Mint or Ubuntu do the same job with more momentum.

**elementary OS** (Ubuntu LTS base; elementary OS 8 on 24.04). The **Pantheon** desktop: macOS-inspired, gorgeous, opinionated, with its own curated AppCenter of Flatpaks (pay-what-you-want). Wayland since OS 8. A design-first project with a small team and a history of slow releases and internal turbulence (a 2022 co-founder departure). Beautiful; limited; its own app ecosystem is small and its GNOME-derived stack lags. **Verdict: 6/10** — worth a look if design is your top priority and you don't need much from the desktop; not a great fit for a developer who wants flexibility.

---

## 6.7 Summary table: mainstream

| Distro | Base | Release | Desktop | NVIDIA ease | Freshness | Newcomer polish | Ecosystem gravity | Score |
|---|---|---|---|---|---|---|---|---|
| **Fedora** (Workstation / KDE) | — | 6-mo, 13-mo support | GNOME 50 / Plasma 6.6+ | good (akmods) | ★★★★☆ | ★★★★☆ | ★★★★☆ | **9** |
| **Ubuntu 26.04 LTS** (+Kubuntu) | Debian | 2-yr LTS, 5–10 yr | GNOME 50 / Plasma 6.5 | **best** | ★★★☆☆ (fresh now, ages) | ★★★★☆ | **★★★★★** | **8.5** |
| **Linux Mint 22.x → 23** | Ubuntu LTS | 2-yr, 5 yr | Cinnamon | very good (Driver Mgr) | ★★☆☆☆ | **★★★★★** | ★★★★★ (Ubuntu's) | **8** (9 for newcomers) |
| **Pop!_OS 24.04** | Ubuntu LTS | irregular LTS | COSMIC 1.x | **best** (NVIDIA ISO) | ★★★☆☆ (own kernel) | ★★★☆☆ | ★★★★☆ | **7.5** (8.5 NVIDIA laptop) |
| **Debian 13** stable | — | ~2-yr, 5 yr | GNOME 48 / Plasma 6.3 / others | okay (DKMS) | ★☆☆☆☆ (★★★★ testing) | ★★☆☆☆ | ★★★★☆ | **7** (7.5 testing) |
| **Zorin OS 18** | Ubuntu LTS | lags LTS | GNOME (custom) | very good | ★☆☆☆☆ | ★★★★☆ | ★★★★☆ | **7** |
| **elementary OS 8** | Ubuntu LTS | slow | Pantheon | good | ★☆☆☆☆ | ★★★☆☆ | ★★★☆☆ | **6** |

---

### Key takeaways

- **Fedora** (Workstation or KDE) is the best all-round fit for a developer daily driver in 2026: current, stable, upstream-first, polished after a two-minute codec step. Its costs are a mandatory yearly upgrade and slightly more NVIDIA attention.
- **Ubuntu LTS** wins on ecosystem gravity, NVIDIA/CUDA friction, TPM encryption and long support; snaps are its tax, and it's removable.
- **Linux Mint** is the newcomer's best friend and the safest thing to install for someone else; its only weakness is desktop modernity, and Mint 23 shrinks that.
- **Pop!_OS** is the NVIDIA-laptop specialist with an exciting young desktop; skip if you need Secure Boot or a fully mature DE today.
- **Debian** is the immovable foundation — superb if you know why you want it, under-curated if you don't; **testing** is a legitimate rolling-ish option for the experienced.
- Zorin and elementary are design-led niche picks; fine, but with less momentum than the big four.


---

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

## 7.7 openSUSE Tumbleweed (and Slowroll, Leap)

**Identity and governance.** The openSUSE Project, sponsored by SUSE (a German enterprise Linux company, publicly traded 2021–2023, now private again under EQT). Community-governed via an elected board, with SUSE employees doing much of the engineering. openSUSE is the upstream/testing ground for SUSE Linux Enterprise the way Fedora is for RHEL, but with a twist: **Tumbleweed** is a rolling release, and **Leap** shares its binaries with SLE. The project has been discussing a rename to distance itself from SUSE's trademark; nothing has landed.

**Release model — three options.**
- **Tumbleweed** — rolling, but every snapshot passes **openQA**, an automated integration-testing system that boots the snapshot, installs it, runs the desktops, and checks hundreds of scenarios before publication. Snapshots ship most days. The result is the **most reliable rolling release in existence** — genuinely rare regressions — at the cost of big transitions (new GNOME, new Plasma, new glibc) sometimes taking a week or two longer than Arch while openQA is satisfied. `zypper dup` is the daily command.
- **Slowroll** — Tumbleweed's snapshots released monthly-ish, with security fixes in between. Same repos, frozen, so no Manjaro-style mismatch problem (openSUSE's community repos are built per-distro). Officially still "experimental" but widely used since 2023. The best "rolling but slower" option in Linux.
- **Leap 16.0** — released October 2025, rebased onto SLE 16 / "SUSE Linux Framework One". Point release, ~18-month cadence, several years' support. **YaST is gone** in Leap 16 (replaced by the **Agama** installer, **Cockpit** for system management, and **Myrlyn** as the graphical package manager); **SELinux is the default** MAC (switched from AppArmor). Leap is a fine stable distro but its desktop stack ages quickly and its niche (a free SLE) matters more to sysadmins than to our persona.

**Packaging.** `zypper` (verbose, explicit, slower than pacman/dnf5) and RPM. Solid official repos. **Packman** is the essential third-party repo for full codecs and `ffmpeg` — the equivalent of Fedora's RPM Fusion step, done via `opi codecs` (a one-liner). The **Open Build Service (OBS)** is openSUSE's PPA/COPR/AUR analogue: a massive community build farm where anyone can publish packages for any openSUSE (and other!) distro version; `opi` searches it. Flatpak available and Flathub one command away (KDE Discover/GNOME Software integrate it). Snaps: not shipped.

**Desktop.** Installer offers KDE Plasma (the historical default and openSUSE's pride — openSUSE is a major KDE contributor), GNOME, Xfce, and others. Plasma on Tumbleweed is excellent and current. **YaST is still present on Tumbleweed but deprecated**; its retirement across all openSUSE is a matter of time, and the replacements (Cockpit, Myrlyn) are less integrated than YaST was — a real loss for people who loved the one-stop admin GUI, less relevant to our persona who lives in the terminal.

**Hardware.** Current kernel on Tumbleweed (7.2 as of September 2026). Firmware packaged. **NVIDIA:** the official NVIDIA repository for openSUSE provides pre-built kmp packages that track Tumbleweed's kernel — generally smooth, occasionally a day or two behind after a kernel bump (during which the module may not load; `zypper dup` will warn). Secure Boot supported out of the box, including NVIDIA module signing via the installer-generated MOK. **Btrfs + Snapper by default** with snapshots automatically taken before and after every `zypper` transaction and **bootable from the GRUB menu** — the best out-of-box rollback on any conventional distro, and the reason Tumbleweed users are relaxed about updates.

**Developer experience.** Very good. Current toolchains, `distrobox`/`toolbox` packaged, Podman and Docker available, OBS for anything missing. Slightly smaller mindshare than Arch/Fedora/Ubuntu means fewer "for openSUSE" tutorials, though most Fedora/RPM instructions adapt. The `zypper` vs `dnf` mental translation is trivial. SUSE's enterprise focus shows in excellent container and Kubernetes tooling (Rancher is SUSE's).

**Daily-driver polish.** Excellent after `opi codecs`. Plasma integration is top-tier. Wayland default. Snapper snapshots + the ability to boot into a snapshot and `snapper rollback` is a daily-driver superpower. Installer is thorough and slightly intimidating (Agama on Leap 16 is more modern). Fewer users than Fedora means occasionally a papercut goes unreported longer.

**Security defaults.** **SELinux default on Tumbleweed since 2025** (following Leap 16), AppArmor still installable. `firewalld` on. LUKS from installer, with TPM unlock configurable. Secure Boot on. Very good security response; SUSE's team is large.

**Documentation and community.** Good official docs, an active forum and Reddit, a smaller but expert community. The openSUSE wiki is decent; the ArchWiki fills gaps. The community skews European and professional.

**Governance risks.** SUSE's commercial priorities shape the project, and SUSE has shifted direction more than once (the SLE 16 rebase, dropping YaST). The community is smaller than Fedora's. The persistent "is openSUSE going to be renamed / restructured" discussion creates uncertainty without (so far) consequences.

**Who should pick Tumbleweed.**
- People who want rolling freshness with the least risk — the "I want Arch-level currency but I have a job" crowd.
- Plasma fans who want a distro that treats Plasma as first-class.
- Anyone who wants Btrfs snapshots + bootable rollback configured out of the box.
- Developers who'll work with SUSE/Rancher/Kubernetes professionally.

**Who should not.**
- People who want the largest community/ecosystem gravity (Ubuntu/Fedora/Arch have more).
- People who want the fastest possible updates with zero delay (Arch).
- People who loved YaST and want it to stay (it won't).

**Verdict: Tumbleweed 8.5/10 for our persona.** Criminally underrated. If Fedora is "semi-rolling done right," Tumbleweed is "fully rolling done right," and the Snapper integration is the best safety net in conventional Linux. **Slowroll 8/10** for the same audience wanting fewer updates. **Leap 16: 7/10** — solid, but its stable niche is better served for our persona by Ubuntu LTS or Debian.

---

## 7.8 Gentoo

**What it is.** The source-based meta-distribution (2000; volunteer foundation). **Portage** builds packages from source according to your **USE flags** (feature toggles), compiler flags, and profile — you get exactly the features you want, compiled for your CPU. Since December 2023 Gentoo also offers **binary packages** for the default configurations, which cut install and update time dramatically for anyone not customising USE flags heavily. Choice of init (OpenRC default, systemd supported), libc (glibc/musl), and essentially everything else.

**The experience.** Unmatched control and understanding. The Gentoo Handbook and wiki are superb (second only to Arch's). Updates of large packages (browsers, LLVM, Qt) from source take hours on a laptop unless you use binpkgs; a "world update" after a month away can take a day. You will learn more about how software is built than on any other distro. Rolling; stable and testing keyword tiers.

**For our persona.** The compile times and configuration burden are a poor fit for a daily driver with deadlines, even with binpkgs. The educational value is genuine — an OS or compilers student could learn a lot in a VM. Almost nobody's *first* Linux, and rightly so.

**Verdict: 5/10 for our persona, 8/10 as a learning project in a VM.**

---

## 7.9 Void Linux

**What it is.** Independent (not derived from anything), rolling, with the **runit** init system (no systemd), its own **XBPS** package manager (very fast, with a well-designed source-package system `xbps-src`), a choice of **glibc or musl**, and a small, technically excellent volunteer team. Founded 2008 by a former NetBSD developer; the BSD influence shows in its minimalism and coherence.

**The experience.** Lean, fast, quiet. Fewer packages than Arch (no AUR-equivalent; `xbps-src` templates are the closest) so niche software may need manual work. Rolling but conservative — Void sometimes holds major transitions for testing. runit is simple and pleasant but some desktop software expects systemd (Void patches or provides shims — elogind — for most of it; GNOME works, Plasma works). Excellent for people who find systemd distasteful and want a coherent alternative rather than a bolt-on (Artix).

**For our persona.** Works well as a developer daily driver for a systemd-sceptic who's comfortable with occasional manual work and a smaller package set. The musl variant is for the adventurous (proprietary binaries break). Community is small, competent and friendly. Bus-factor risk (a 2020 domain/infrastructure scare was resolved but illustrated the exposure).

**Verdict: 6.5/10 for our persona**, higher if "no systemd, coherent design" is a strong preference.

---

## 7.10 Alpine, Solus, Slackware, and others

- **Alpine Linux** — musl + BusyBox + OpenRC, tiny, security-oriented, the dominant container base image. As a desktop: possible (GNOME and Plasma are packaged; postmarketOS is Alpine-based), but musl breaks proprietary binaries (Steam, VS Code official builds, JetBrains, Zoom) unless you use Flatpak or a glibc chroot. Fantastic in Dockerfiles; wrong on a laptop for our persona. **4/10 as a daily driver.**
- **Solus** — independent, curated rolling ("cured rolling" with weekly syncs), its own `eopkg` package manager (moving to `moss`), Budgie's original home (Budgie is now independent). Nearly died in 2022–2023 when infrastructure and leadership collapsed; revived under new leadership in 2023 and releasing again (Solus 4.7 in 2025). Polished, small package set, small team, uncertain long-term. **5.5/10.**
- **Slackware** — the oldest surviving distro (1993), one maintainer (Patrick Volkerding), no dependency resolution in the base package tools, a release every ~5 years (15.0 in 2022). Historically important; a purposeful anachronism today. **3/10 for our persona**, with respect.
- **Chimera Linux** — a new (2021) independent distro with a FreeBSD userland, musl, dinit, LLVM toolchain, and `apk`; technically fascinating, in alpha/beta. Not for daily driving yet.
- **NixOS, Guix** — covered in Chapter 8 (declarative).
- **MX Linux** — Debian-stable-based with Xfce/KDE/Fluxbox editions, systemd-shim by default (SysVinit-first), a suite of MX Tools, very popular on DistroWatch, beloved by its users for stability on old hardware. For our persona it's Debian stable with a friendlier face and an unusual init stance. **6/10.**
- **Kali, Parrot, BlackArch** — security distros. **Not daily drivers**; use their tools via a VM, container, or individual packages on your normal distro. Running Kali as your main OS is a well-known beginner mistake.

---

## 7.11 Summary table: enthusiast and rolling

| Distro | Model | Base | Init | Pkg mgr | Snapshots OOTB | Secure Boot OOTB | NVIDIA | Maintenance | Score |
|---|---|---|---|---|---|---|---|---|---|
| **openSUSE Tumbleweed** | tested rolling (openQA) | — | systemd | zypper | **yes** (Snapper, bootable) | yes | good (repo kmp) | low-medium | **8.5** |
| **EndeavourOS** | rolling | Arch | systemd | pacman + yay | optional | no | good | medium | **8** |
| **CachyOS** | rolling, tuned | Arch | systemd | pacman + paru | **yes** (Snapper) | optional (sbctl) | good (installer) | medium | **8** (8.5 gaming) |
| **openSUSE Slowroll** | monthly rolling | TW | systemd | zypper | yes | yes | good | low | **8** |
| **Arch Linux** | rolling | — | systemd | pacman (+AUR) | DIY | DIY (sbctl) | good (nvidia-open) | medium-high | **7.5** (9 for admins) |
| **Omarchy** | rolling | Arch | systemd | pacman | DIY | no | fair | medium | **7.5** (niche) |
| **openSUSE Leap 16** | point, ~18 mo | SLE 16 | systemd | zypper | yes | yes | good | low | **7** |
| **Garuda** | rolling | Arch | systemd | pacman | yes | no | good | medium | **6.5** |
| **Void** | rolling | — | runit | xbps | DIY | no | fair (DKMS) | medium | **6.5** |
| **Manjaro** | delayed rolling | Arch | systemd | pacman/pamac | optional | no | good (mhwd) | medium | **6** |
| **Artix** | rolling | Arch | OpenRC/runit/s6/dinit | pacman | DIY | no | fair | medium-high | **6** |
| **MX Linux** | point | Debian stable | SysV (systemd avail) | apt | yes (Timeshift) | yes | fair | low | **6** |
| **Solus** | curated rolling | — | systemd | eopkg/moss | no | yes | fair | low-medium | **5.5** |
| **Gentoo** | rolling, source | — | OpenRC/systemd | portage | DIY | DIY | fair | high | **5** (8 to learn) |
| **Alpine** | point + edge | — | OpenRC | apk | no | no | poor (musl) | medium | **4** (desktop) |
| **Slackware** | ~5-yr point | — | SysV/BSD-style | pkgtools | no | yes | manual | high | **3** |

---

### Key takeaways

- **Arch** is the best desktop Linux for people who enjoy administering their machine (9/10 for them) and the wrong choice for people who don't (7.5 blended). The AUR and the ArchWiki are its unmatched assets; attention is its price.
- **EndeavourOS** is the recommended way to run Arch for most people; **CachyOS** adds Snapper snapshots, performance tuning and the most complete installer in the Arch family — the pick for gamers and anyone who wants "Arch as an expert would set it up."
- **openSUSE Tumbleweed** is the most reliable rolling release, with openQA-tested snapshots and out-of-box Btrfs/Snapper bootable rollback — a criminally underrated 8.5. **Slowroll** is the best "slower rolling" option.
- **Manjaro's** delayed-repos-plus-live-AUR design and incident history make it dominated by EndeavourOS/CachyOS/Fedora; **Garuda** is CachyOS with heavier makeup; **Artix/Void** are for systemd-sceptics; **Gentoo** is a magnificent learning project and a poor deadline machine.
- **Alpine, Kali and friends are not daily drivers.** Use them in containers and VMs.


---

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


---

# Chapter 9 — Comparison Matrices

Chapters 6–8 reviewed each distribution in prose. This chapter puts them side by side. Three parts: a **master fact table** (what each distro *is*), a **weighted scoring model** (how each fits each persona, with the weights exposed so you can disagree), and a **sensitivity discussion** (what changes the ranking).

All facts as of September 2026. Versions drift; structure doesn't.

## 9.1 Master fact table

| Distro | Base | Release model | Support per release | Pkg format / mgr | Universal pkg default | Default DE (options) | Default FS | Snapshots OOTB | MAC | Firewall OOTB | Secure Boot OOTB | NVIDIA delivery | Codecs OOTB | Init | Backing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ubuntu 26.04 LTS** | Debian | LTS 2-yr (+6-mo interim) | 5 yr (10 w/ Pro) | deb / apt 3.2 | Snap | GNOME 50 (flavours: KDE, Xfce, LXQt, Budgie, Cinnamon…) | ext4 (ZFS/Btrfs opt) | no | AppArmor | ufw off | yes | pre-built, signed | opt-in checkbox | systemd | Canonical |
| **Fedora 44** | — | 6-mo | ~13 mo | rpm / dnf5 | Flatpak (Flathub) | GNOME 50 / Plasma 6.6+ (spins: Xfce, Cinnamon, COSMIC, Sway…) | Btrfs (zstd) | no (easy) | SELinux | firewalld on | yes | RPM Fusion akmod | no (RPM Fusion) | systemd | Red Hat / community |
| **Debian 13** | — | ~2-yr point | 3 + 2 LTS | deb / apt 3.0 | none (Flatpak avail) | GNOME 48 / Plasma 6.3 / many | ext4 | no | AppArmor | none | yes | DKMS (non-free) | yes | systemd | volunteer |
| **Linux Mint 22.x** | Ubuntu LTS | 2-yr (+6-mo point) | 5 yr | deb / apt | Flatpak | Cinnamon 6.x (Xfce, MATE) | ext4 | Timeshift (prompted) | AppArmor | ufw off (GUI) | yes | pre-built (Driver Mgr) | opt-in checkbox | systemd | independent |
| **Pop!_OS 24.04** | Ubuntu LTS | irregular LTS | ~5 yr | deb / apt | Flatpak | COSMIC 1.x | ext4 (LUKS default) | no | AppArmor | off | **no** | pre-installed (NVIDIA ISO) | yes | systemd | System76 |
| **Zorin OS 18** | Ubuntu LTS | lags LTS ~6–12 mo | ~4 yr | deb / apt | Flatpak + Snap | GNOME (custom layouts) | ext4 | no | AppArmor | off | yes | pre-built | yes | systemd | Zorin Group |
| **Arch** | — | rolling | n/a | pkg.tar.zst / pacman | none (Flatpak avail) | none (any) | user choice | DIY | none | none | **no** (sbctl DIY) | nvidia-open pre-built (stock kernel) | yes | systemd | volunteer (+Valve infra) |
| **EndeavourOS** | Arch | rolling | n/a | pacman + yay | none (Flatpak avail) | choice (GNOME, Plasma, Xfce, WMs…) | ext4/Btrfs | optional | none | firewalld on | no | installer option | yes | systemd | volunteer |
| **CachyOS** | Arch | rolling (tuned) | n/a | pacman + paru | none (Flatpak avail) | Plasma default (15+ options) | Btrfs | **Snapper + boot entries** | none | on | optional (sbctl) | installer option | yes | systemd | small team |
| **Manjaro** | Arch (delayed 2 wk) | curated rolling | n/a | pacman / pamac | Flatpak+Snap via pamac | Plasma / GNOME / Xfce | ext4 | optional | none | off | no | mhwd | yes | systemd | Manjaro GmbH |
| **openSUSE Tumbleweed** | — | tested rolling (openQA) | n/a | rpm / zypper | none (Flatpak avail) | Plasma / GNOME / Xfce | **Btrfs + Snapper** | **yes, bootable** | SELinux (since 2025) | firewalld on | yes | NVIDIA repo kmp | no (Packman / `opi codecs`) | systemd | SUSE / community |
| **openSUSE Slowroll** | Tumbleweed | monthly rolling | n/a | zypper | — | same | Btrfs + Snapper | yes | SELinux | on | yes | same | no (Packman) | systemd | community |
| **openSUSE Leap 16** | SLE 16 | ~18-mo point | ~2 yr+ | zypper | — | Plasma / GNOME | Btrfs + Snapper | yes | SELinux | on | yes | NVIDIA repo | no (Packman) | systemd | SUSE |
| **Fedora Silverblue / Kinoite** | Fedora | atomic, 6-mo | ~13 mo | rpm-ostree / bootc | Flatpak | GNOME / Plasma | Btrfs | **image rollback** | SELinux | on | yes | layer akmod (clunky) | no | systemd | Fedora |
| **Bluefin / Aurora (DX)** | Fedora Atomic | atomic, continuous | rolling w/ Fedora | bootc + Flatpak + Homebrew | Flatpak | GNOME / Plasma | Btrfs | image rollback | SELinux | on | yes (enroll key) | **baked in** (`-nvidia`) | yes | systemd | Universal Blue (community) |
| **Bazzite** | Fedora Atomic | atomic, continuous | rolling | bootc + Flatpak + Homebrew | Flatpak | Plasma / GNOME | Btrfs | image rollback | SELinux | on | yes | baked in | yes | systemd | Universal Blue |
| **openSUSE Aeon** | Tumbleweed | atomic (transactional) | rolling | transactional-update | Flatpak + Distrobox | GNOME | Btrfs | yes | SELinux | on | yes | weak | mostly (Flatpak) | systemd | openSUSE |
| **Vanilla OS 2** | Debian Sid | atomic (ABRoot) | rolling-ish | apx (Distrobox) + Flatpak | Flatpak | GNOME | Btrfs | A/B rollback | AppArmor | on | partial | fair | yes | systemd | small team |
| **NixOS 26.05** | — | declarative; 6-mo stable + unstable | 7 mo (stable) | nix / nixpkgs | Flatpak avail | any (config) | any | **generations** | none (AppArmor avail) | on | Lanzaboote (manual) | declarative module | yes | systemd | NixOS Foundation |
| **Void** | — | rolling | n/a | xbps | Flatpak avail | none (any) | any | DIY | none | none | no | DKMS | yes | **runit** | volunteer |
| **Gentoo** | — | rolling, source (+binpkgs) | n/a | portage | Flatpak avail | none (any) | any | DIY | opt (SELinux/AppArmor) | none | DIY | DKMS-like | yes | OpenRC / systemd | Gentoo Foundation |

### Freshness snapshot (September 2026)

Approximate versions of key components. The point is the pattern, not the decimals.

| Distro | Kernel | Mesa | GCC | Python | GNOME | Plasma |
|---|---|---|---|---|---|---|
| Arch / EndeavourOS / CachyOS / Tumbleweed | 7.2 | 26.2 | 16 | 3.14 | 50 | 6.7 |
| Fedora 44 | 7.2 (rebased) | 26.x | 16 | 3.14 | 50 | 6.6/6.7 |
| NixOS 26.05 (stable) | 6.18 LTS (7.x opt) | 26.x | 15/16 | 3.13/3.14 | 50 | 6.6 |
| Bluefin / Aurora / Bazzite | 7.2 (Fedora's / patched) | 26.x | 16 | 3.14 | 50 | 6.7 |
| Ubuntu 26.04 LTS | 7.0 (HWE later) | 26.0 | 15 | 3.14 | 50 | 6.5 |
| Pop!_OS 24.04 | recent (own) | recent | 13 | 3.12 | — (COSMIC 1.7) | — |
| Linux Mint 22.3 | 6.14 (HWE) | 25.x | 13 | 3.12 | — (Cinnamon 6.6) | — |
| Debian 13 | 6.12 (6.18 backports) | 25.0 | 14 | 3.13 | 48 | 6.3 |

Reading it: a fresh Ubuntu LTS is within months of rolling; Mint and Debian stable are one to two years behind; everything else is current. **Freshness only matters if you need it** — for new hardware, for HDR/VRR/fractional-scaling maturity, for a specific new compiler feature. If your laptop is from 2023 and you write Python web services, Debian 13 is not meaningfully "behind" you.

## 9.2 The weighted scoring model

I scored each distribution 1–10 on thirteen criteria, then weighted the criteria differently for five personas. The scores are my judgement, informed by Chapters 6–8; the weights are derived from Chapter 3's ranked criteria. Both are in `build/score.py` in this repository — change them and re-run to get your own ranking.

### Criteria (and what a 10 means)

| Criterion | 10 means… |
|---|---|
| **hardware** | Current kernel, all firmware, NVIDIA painless, new laptops work day one |
| **stability_rollback** | Updates essentially never break; and if they do, rollback is trivial and guaranteed |
| **ecosystem** | Every vendor, tutorial, university, employer and CI image assumes you |
| **polish** | Everything works on first boot; the desktop is integrated and pleasant |
| **freshness** | Newest kernel, Mesa, toolchains and desktop, always |
| **repos** | Anything you can think of is one command away (AUR / nixpkgs tier) |
| **maintenance** | You never have to intervene, read news or fix anything (10 = zero effort) |
| **lifecycle** | Long support windows; upgrades rare and painless |
| **security** | Strong, sane defaults: MAC enforcing, firewall on, FDE easy, Secure Boot works |
| **docs** | When stuck, the answer exists and is correct (ArchWiki tier) |
| **governance** | Project is durable, well-funded or well-organised, low drama |
| **performance** | Measurably faster for real workloads |
| **host_flexibility** | You can install anything on the host, load any module, hack anything — a conventional mutable FHS system |

### Persona weights

| Criterion | Combined | SWE | CS student | Daily/newcomer | Tinkerer |
|---|---|---|---|---|---|
| hardware | 5 | 4 | 4 | 5 | 3 |
| stability_rollback | 5 | 5 | 5 | 4 | 2 |
| ecosystem | 4 | 4 | 5 | 3 | 2 |
| polish | 4 | 3 | 3 | 5 | 2 |
| freshness | 3 | 4 | 2 | 2 | 5 |
| repos | 3 | 3 | 2 | 2 | 5 |
| maintenance | 3 | 3 | 4 | 5 | 1 |
| lifecycle | 3 | 2 | 3 | 4 | 1 |
| security | 2 | 3 | 1 | 2 | 2 |
| docs | 2 | 2 | 3 | 3 | 4 |
| governance | 2 | 2 | 1 | 1 | 2 |
| performance | 1 | 1 | 1 | 1 | 3 |
| host_flexibility | 3 | 3 | 3 | 1 | 5 |

### Raw criterion scores

| Distro | hw | stab | eco | polish | fresh | repos | maint | life | sec | docs | gov | perf | host |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fedora Workstation / KDE | 9 | 8 | 8 | 9 | 8 | 7 | 8 | 6 | 9 | 8 | 8 | 7 | 10 |
| Ubuntu 26.04 LTS / Kubuntu | 9 | 8 | 10 | 8 | 6 | 7 | 9 | 10 | 8 | 8 | 7 | 7 | 10 |
| Linux Mint 22.x | 8 | 8 | 9 | 8 | 4 | 7 | 9 | 9 | 7 | 8 | 6 | 7 | 10 |
| Pop!_OS 24.04 | 9 | 7 | 8 | 7 | 7 | 7 | 8 | 6 | 6 | 6 | 5 | 7 | 10 |
| Debian 13 stable | 6 | 9 | 8 | 6 | 3 | 8 | 9 | 9 | 8 | 7 | 9 | 7 | 10 |
| Zorin OS 18 | 8 | 8 | 8 | 8 | 3 | 7 | 9 | 8 | 7 | 6 | 5 | 7 | 10 |
| Arch Linux | 9 | 6 | 7 | 6 | 10 | 10 | 4 | 7 | 6 | 10 | 8 | 8 | 10 |
| EndeavourOS | 9 | 6 | 7 | 7 | 10 | 10 | 5 | 7 | 6 | 9 | 7 | 8 | 10 |
| CachyOS | 9 | 7 | 7 | 8 | 10 | 10 | 5 | 7 | 6 | 7 | 6 | 9 | 10 |
| Manjaro | 8 | 5 | 6 | 7 | 8 | 7 | 5 | 7 | 6 | 6 | 4 | 7 | 10 |
| openSUSE Tumbleweed | 9 | 9 | 6 | 8 | 9 | 7 | 7 | 7 | 9 | 7 | 7 | 7 | 10 |
| openSUSE Slowroll | 8 | 9 | 6 | 8 | 7 | 7 | 8 | 7 | 9 | 6 | 6 | 7 | 10 |
| Fedora Silverblue / Kinoite | 8 | 10 | 6 | 8 | 8 | 5 | 9 | 6 | 9 | 6 | 8 | 7 | 5 |
| Bluefin / Aurora | 9 | 10 | 7 | 9 | 8 | 6 | 10 | 7 | 9 | 7 | 6 | 7 | 5 |
| Bluefin DX / Aurora DX | 9 | 10 | 7 | 9 | 8 | 7 | 10 | 7 | 9 | 7 | 6 | 7 | 6 |
| Bazzite | 10 | 10 | 7 | 9 | 8 | 6 | 10 | 7 | 8 | 7 | 6 | 8 | 5 |
| openSUSE Aeon | 7 | 10 | 5 | 8 | 9 | 5 | 10 | 7 | 10 | 5 | 6 | 7 | 4 |
| NixOS | 8 | 10 | 5 | 7 | 10 | 10 | 4 | 8 | 7 | 6 | 6 | 7 | 6 |
| Void Linux | 7 | 6 | 4 | 6 | 9 | 6 | 5 | 7 | 6 | 7 | 5 | 8 | 10 |
| Gentoo | 8 | 6 | 4 | 5 | 10 | 9 | 2 | 7 | 7 | 9 | 7 | 8 | 10 |

### Weighted results

| Distro | Combined | SWE | CS student | Daily / newcomer | Tinkerer |
|---|---|---|---|---|---|
| **Ubuntu 26.04 LTS / Kubuntu** | **8.4** | 8.3 | **8.6** | **8.5** | 8.0 |
| **Fedora Workstation / KDE** | 8.2 | 8.2 | 8.1 | 8.1 | 8.2 |
| **Bluefin DX / Aurora DX** | 8.1 | 8.1 | 8.1 | 8.3 | 7.6 |
| **Bazzite** | 8.1 | 8.0 | 8.1 | 8.4 | 7.4 |
| **openSUSE Tumbleweed** | 8.0 | 8.0 | 7.8 | 7.8 | 8.1 |
| **Bluefin / Aurora** | 8.0 | 7.9 | 8.0 | 8.3 | 7.3 |
| Linux Mint 22.x | 7.8 | 7.7 | 8.1 | 8.0 | 7.5 |
| CachyOS | 7.8 | 7.8 | 7.6 | 7.5 | 8.4 |
| EndeavourOS | 7.7 | 7.7 | 7.6 | 7.4 | 8.5 |
| openSUSE Slowroll | 7.7 | 7.7 | 7.6 | 7.6 | 7.6 |
| Arch Linux | 7.7 | 7.7 | 7.5 | 7.3 | **8.6** |
| Debian 13 stable | 7.6 | 7.5 | 7.8 | 7.5 | 7.3 |
| Fedora Silverblue / Kinoite | 7.5 | 7.5 | 7.4 | 7.6 | 6.9 |
| Zorin OS 18 | 7.5 | 7.3 | 7.6 | 7.6 | 7.0 |
| NixOS | 7.4 | 7.5 | 7.1 | 7.2 | 7.6 |
| Pop!_OS 24.04 | 7.4 | 7.3 | 7.5 | 7.3 | 7.4 |
| openSUSE Aeon | 7.3 | 7.4 | 7.2 | 7.6 | 6.7 |
| Gentoo | 6.8 | 6.9 | 6.6 | 6.4 | 8.0 |
| Manjaro | 6.7 | 6.6 | 6.6 | 6.5 | 7.1 |
| Void Linux | 6.5 | 6.5 | 6.4 | 6.3 | 7.1 |

### Reading the table honestly

Three things jump out.

**First, the top six are within 0.4 points of each other.** Ubuntu LTS, Fedora, Bluefin DX/Aurora DX, Bazzite, Tumbleweed and Bluefin/Aurora are all *excellent* for our persona, and the differences between them are smaller than the noise in my scoring. This is Chapter 1's thesis in numbers: the mainstream choices are all good, and the right one depends on which criteria *you* weight most. Anyone telling you one of these is "wrong" for a developer is selling something.

**Second, the model slightly favours Ubuntu over Fedora, whereas my prose verdict in Chapter 6 favoured Fedora (9 vs 8.5).** The difference is `lifecycle` and `ecosystem`, which the model weights and my gut discounts because *I* don't mind a yearly upgrade and don't need vendor `.deb`s. That's exactly the kind of disagreement the model is meant to surface. If you upgrade happily and live in Flatpaks and containers, Fedora is your pick; if you want five years of quiet and the widest vendor support, Ubuntu is. Both are correct.

**Third, the atomic images (Bluefin/Aurora/Bazzite) score at the top for the daily-driver persona and near the top for everyone else, penalised only by `host_flexibility`.** If that criterion doesn't matter to you — if you never load a custom kernel module or install odd host packages — mentally add 0.3 and they lead the table. This is why Chapter 8 called Universal Blue the most important new option in years.

Further down: **Mint** is held back only by freshness and would top the newcomer column if that persona weighted `polish` even more heavily. **CachyOS/EndeavourOS/Arch** dominate the tinkerer column as expected and sit mid-table for everyone else because of maintenance. **NixOS**'s 7.4 blended score hides a bimodal reality (Chapter 8: 9.5 for converts). **Debian** is solid everywhere and exceptional nowhere for this persona. **Manjaro, Void and Gentoo** trail for the reasons given in Chapter 7.

## 9.3 Sensitivity: what moves the ranking

Try these adjustments to `build/score.py` and watch what happens.

| If you… | Weight change | Effect |
|---|---|---|
| **Have an NVIDIA GPU** | hardware ×1.5; penalise DKMS-only distros by 2 | Ubuntu, Pop!_OS, Bazzite/Bluefin `-nvidia` rise; Fedora, Debian, Aeon, NixOS fall a notch; Arch stays okay via `nvidia-open` |
| **Need CUDA specifically** | as above, plus ecosystem ×1.5 | Ubuntu LTS leads clearly; Pop!_OS second |
| **Are in a heavy semester** | maintenance ×2, stability ×1.5, freshness ÷2 | Bluefin/Aurora/Bazzite lead, then Ubuntu, Mint, Tumbleweed; Arch drops to mid-pack |
| **Do kernel / driver / OS-course work** | host_flexibility ×2 | Atomic images drop out of the top six; Fedora, Ubuntu, Tumbleweed, Arch lead |
| **Value reproducibility above all** | add a "reproducibility" criterion at weight 5 with NixOS=10, atomic=7, others=3 | NixOS jumps to the top |
| **Are a first-timer installing for a relative** | polish ×2, maintenance ×2, docs ×1.5 | Mint, Ubuntu, Bazzite lead |
| **Game a lot** | performance ×3, hardware ×1.5 | Bazzite and CachyOS lead |
| **Are on Apple Silicon** | hardware = 10 for Fedora Asahi, 0 for everything else | Fedora (Asahi Remix), end of discussion |
| **Have an employer/university mandate** | ecosystem = 10 for the mandated distro, cap others at 6 | The mandated distro wins; usually Ubuntu LTS |
| **Have a > 8-year-old laptop** | hardware: penalise heavy DEs; freshness ÷2 | Mint Xfce, Debian, Xubuntu rise |

The point of the exercise is that **the ranking is more sensitive to your situation than to distro quality.** Which is exactly why Chapter 15 gives you a decision tree instead of a single answer.

## 9.4 Quick-reference: "which one has…"

| I want… | Best | Also good |
|---|---|---|
| The longest support without upgrading | Ubuntu LTS (5–10 yr) | Debian stable (5 yr), Bluefin LTS |
| The least NVIDIA friction | Pop!_OS NVIDIA ISO, Ubuntu LTS, Bazzite/Bluefin `-nvidia` | Fedora + RPM Fusion, CachyOS installer |
| Out-of-box bootable snapshots | openSUSE Tumbleweed | CachyOS, Garuda, any atomic |
| The newest everything | Arch / EndeavourOS / CachyOS | Tumbleweed, NixOS unstable, Fedora |
| The largest "just install it" catalogue | Arch + AUR | NixOS/nixpkgs, Debian/Ubuntu archive |
| Zero maintenance | Bluefin / Aurora / Bazzite | Aeon, Ubuntu LTS |
| Reproducible whole-system config | NixOS | Universal Blue custom image, Guix |
| Best per-project dev environments | NixOS (`nix develop`) | devcontainers on anything, Distrobox |
| Most Windows-like out of the box | Linux Mint, Zorin | Kubuntu, Fedora KDE |
| Most Mac-like out of the box | elementary, Bluefin | Ubuntu, Fedora Workstation |
| Best tiling without a WM project | Pop!_OS (COSMIC) | Omarchy, Plasma tiling, GNOME + Tiling Shell |
| Vendor/employer/university compatibility | Ubuntu LTS | Debian, Fedora/RHEL |
| Best gaming out of the box | Bazzite | CachyOS, Nobara |
| Best on old/low-spec hardware | Mint Xfce, Debian Xfce/LXQt, Xubuntu | MX Linux, antiX |
| Best security defaults | openSUSE Aeon (TPM FDE by default), Fedora | Ubuntu 26.04 (TPM FDE option), Tumbleweed |
| Apple Silicon | Fedora Asahi Remix | (nixos-apple-silicon for experts) |
| Learning how Linux works | Arch (manual install), Gentoo (in a VM) | NixOS, Void |
| A rolling release that "just doesn't break" | openSUSE Tumbleweed | Slowroll, CachyOS |

---

### Key takeaways

- The **master fact table** shows the structural differences: release model, packaging, defaults, driver delivery. Compare on these, not on branding.
- Under a weighted model built from Chapter 3's criteria, the **top six — Ubuntu LTS, Fedora, Bluefin DX/Aurora DX, Bazzite, Tumbleweed, Bluefin/Aurora — are within 0.4 points**. All are excellent; the choice among them is about your weights.
- **Ubuntu LTS** leads on lifecycle and ecosystem; **Fedora** on the freshness/stability balance; **Universal Blue** on maintenance and rollback (penalised only by host flexibility); **Tumbleweed** on tested rolling with snapshots.
- **Arch and family** dominate the tinkerer column and sit mid-table otherwise; **NixOS** is bimodal; **Mint** would lead the newcomer column with a heavier polish weight.
- The ranking moves more with your situation (NVIDIA, CUDA, semester load, kernel work, Apple Silicon, mandates) than with distro quality. The scoring script is in the repo — re-weight it and see.


---

# Chapter 10 — Hardware Considerations

Hardware constrains the distro choice more than philosophy does. This chapter covers what to buy if you're buying, what to check if you already own it, and which components are the recurring troublemakers. The single most important sentence: **if you can choose, choose AMD or Intel graphics, an Intel WiFi card, and a laptop the vendor ships or certifies with Linux.** Everything after that is detail.

## 10.1 Buy-for-Linux vs. make-it-work

**Buy for Linux.** Choose hardware the manufacturer sells with Linux pre-installed or explicitly certifies. Everything works on day one, firmware updates arrive through `fwupd`, sleep works, the fingerprint reader works, and when something breaks the vendor is on the hook. Costs a small premium or limits selection.

**Make it work.** Buy whatever, install Linux, fix what's broken. Almost always succeeds on mainstream x86 laptops from the last decade — Linux hardware support is far better than its reputation — but "almost" hides a long tail: a MediaTek WiFi card that drops connections until a kernel point release, a webcam behind Intel's IPU6 needing extra firmware, a fingerprint reader with no driver, firmware that implements Modern Standby badly.

For a student or engineer whose machine is a tool, buying for Linux is worth the premium. For an existing machine, "make it work" is the only option and usually fine.

## 10.2 Laptops that work

**Tier 1 — sold with Linux, engineered for it**

- **Framework Laptop 13 / 13 Pro / 16.** Modular, repairable, Linux a first-class target (Ubuntu and Fedora guides, in-house Linux engineers, upstreamed fixes). The 13 Pro (April 2026) offers an Ubuntu pre-built. AMD Ryzen AI 300-series boards had early WiFi (MediaTek MT7925) and suspend issues on kernels before ~6.15; resolved. Excellent keyboard and touchpad. Fedora, Ubuntu and NixOS (`nixos-hardware` modules) are the well-trodden paths; Bluefin and Bazzite publish Framework-specific images. The best "buy for Linux" option for most people.
- **System76** (Lemur Pro, Darter, Pangolin, Oryx, Adder, Serval). Pop!_OS or Ubuntu pre-installed; open-source coreboot firmware on many models; NVIDIA options with hybrid graphics that actually work. US-centric; build quality fine, not premium.
- **Tuxedo Computers** (Germany; Pulse, InfinityBook, Aura, Stellaris). Tuxedo OS (Ubuntu + Plasma) pre-installed; their control-centre software and kernel modules are packaged for other distros. Good European option. Tuxedo cancelled its Snapdragon X Elite laptop in late 2025 because Linux support wasn't viable — an honest signal.
- **Slimbook** (Spain), **Star Labs** (UK), **Laptop with Linux** (Netherlands), **Juno**, **Malibal** — smaller vendors, mostly Clevo/Tongfang chassis with Linux pre-installed. Fine.
- **Lenovo ThinkPad** — many models are Ubuntu- and Fedora-certified and some ship with them (T14, T14s, X1 Carbon, P-series, X13). Lenovo's Linux firmware support via LVFS is the best of the big OEMs. ThinkPads remain the default "Linux laptop," and the **used-ThinkPad market (T480, T14 Gen 1–3, X1 Carbon Gen 7–10) is the best budget route for students.** Caveat: the Snapdragon X ThinkPads (T14s Gen 6 Snapdragon) are a different story — §10.5.
- **Dell XPS 13/14/16 Developer Edition and Precision mobile workstations** — Ubuntu-certified; some ship with Ubuntu (Project Sputnik, since 2012). Good LVFS support. XPS models with the Intel IPU6 webcam (2022–2024) needed extra work until kernel 6.10+.
- **HP** — the Dev One (2022, Pop!_OS) was discontinued; some EliteBook/ZBook models are Ubuntu-certified. Less consistent than Lenovo/Dell.

**Tier 2 — not sold with Linux, well supported**

Most Intel/AMD business laptops (ThinkBook/Yoga, Latitude, EliteBook, ASUS ExpertBook/Zenbook, Acer Swift), gaming laptops with AMD GPUs, and older Intel MacBooks (2013–2019 — Broadcom WiFi firmware needed; T2 models via the `t2linux` project). Check the exact model on the ArchWiki (per-laptop pages), Ubuntu's certification database, and linux-hardware.org before buying.

**Tier 3 — proceed with caution**

- **Anything with an NVIDIA GPU** — works, see §10.3.
- **Ultra-thin consumer laptops with unusual components** — Surface devices (`linux-surface` project makes them work, but it's a project), some Huawei/Honor, Samsung Galaxy Books (speakers often need quirks).
- **Brand-new hardware (< 3 months)** — the kernel may not have drivers yet; you'll want a rolling or six-month distro and patience.
- **Snapdragon X** — §10.5. **Apple Silicon** — §10.4.

## 10.3 GPUs: the decisive component

| Vendor | Driver | In-tree | Wayland | Gaming | Compute | Verdict |
|---|---|---|---|---|---|---|
| **AMD** (RDNA 2/3/4; Ryzen APUs) | `amdgpu` + Mesa RADV/RadeonSI | **yes** | flawless | excellent (Valve-funded RADV) | ROCm — Ubuntu 26.04 packages it natively; AMD repos elsewhere; improving but behind CUDA's ecosystem | **Best choice for Linux.** Nothing to install, nothing breaks. |
| **Intel** (Arc, Xe, Iris/UHD) | `i915`/`xe` + Mesa ANV/Iris | **yes** | flawless | good | oneAPI/OpenVINO — niche | **Excellent.** Zero effort. |
| **NVIDIA** Turing+ (RTX 20/30/40/50, GTX 16) | `nvidia-open` kernel modules (default since 560) + proprietary userland | **no** (out-of-tree; in-tree `nova` emerging, not daily-ready) | good since 555–590 (explicit sync, VRR) | very good | **CUDA — the reason to own one** | Works well *if* delivered as pre-built modules; the main source of Linux update pain otherwise. |
| **NVIDIA** Pascal and older (GTX 10xx/9xx) | legacy `580xx` branch (security fixes only since 590 dropped them, Dec 2025) or Nouveau (slow) | no | acceptable | poor on Nouveau | old CUDA only | **Time to upgrade.** New kernels will eventually outrun the legacy branch. |

**On NVIDIA, in detail.** Ten years ago NVIDIA on Linux meant tearing, no Wayland, black screens after kernel updates. In 2026 it's *fine* for most users: open kernel modules are default and NVIDIA participates upstream; Wayland works on GNOME, KDE, Hyprland, Sway; VRR and HDR work; explicit sync fixed the flicker; 590/6xx are stable. What remains:

1. **Out-of-tree delivery.** Every kernel update needs a matching module. Pre-building distros (Ubuntu, Arch `nvidia-open`, Universal Blue images, openSUSE's NVIDIA repo) make this invisible; DKMS/akmods distros (Fedora, Debian, Arch with custom kernels) make you wait minutes and occasionally break for days after a major kernel bump.
2. **Secure Boot** needs the module signed — automated on Ubuntu, one-time setup on Fedora/openSUSE/Universal Blue, manual on Arch, or turn it off.
3. **Hybrid graphics** (iGPU + NVIDIA dGPU). PRIME render offload works everywhere (`prime-run`, DE's "launch with dedicated GPU"). Switching the whole session for external displays wired to the dGPU is where Pop!_OS's `system76-power`, `envycontrol`, and `supergfxctl` earn their keep. Ensure runtime power management works or battery life suffers.
4. **Suspend/resume** needs `nvidia-suspend`/`nvidia-resume` services and `NVreg_PreserveVideoMemoryAllocations=1`; most distros do this now; first thing to check if resume is black.
5. **CUDA pinning.** PyTorch/TensorFlow wheels bundle their own CUDA runtime and need only a new-enough *driver*; the *system* toolkit matters only if you compile CUDA code. Manage the ML stack with `uv`/conda, not the distro's `cuda` package.

**Recommendation matrix for NVIDIA owners:**

| You want | Pick |
|---|---|
| Least friction | Ubuntu 26.04 LTS (installer's third-party driver checkbox), or Pop!_OS NVIDIA ISO |
| Least friction and zero maintenance | Bluefin/Aurora/Bazzite `-nvidia` / `-nvidia-open` image |
| Fedora | RPM Fusion `akmod-nvidia`; enrol the signing key; wait 2–3 days after each new kernel major |
| Arch | `nvidia-open` + `linux-lts` + `nvidia-lts-open` fallback; read the news; or let CachyOS's installer do it |
| openSUSE | Tumbleweed + NVIDIA's openSUSE repo; MOK auto-generated |
| Debian | `nvidia-driver` from `non-free` (DKMS); newer GPUs may need backports |
| NixOS | `hardware.nvidia` module; rebuilds with the kernel; pin if a build fails |

**If you're buying and don't need CUDA: buy AMD.** The difference in Linux experience is larger than any distro-to-distro difference in this guide.

## 10.4 Apple Silicon

**Asahi Linux** reverse-engineered Apple's M-series hardware from 2021 and upstreamed most of the result. **Fedora Asahi Remix** is the flagship distro (the Asahi team's own; platform packages fully in upstream Fedora as of 44). NixOS (`nixos-apple-silicon`), Arch (`asahi-alarm`, less maintained) and community Ubuntu ports exist.

**Status by chip (September 2026):**

| Chip | Status |
|---|---|
| **M1 / M1 Pro / Max / Ultra, M2 / M2 Pro / Max / Ultra** | **Daily-driver ready.** GPU (OpenGL 4.6 and Vulkan 1.4 conformant via Honeykrisp — a remarkable feat), WiFi, Bluetooth, audio with DSP speaker protection, keyboard/trackpad, 120 Hz ProMotion, USB-C DisplayPort alt mode (since Feb 2026), Thunderbolt partial, camera, microphone, s2idle sleep. **Not working:** Touch ID for auth, some Thunderbolt features. x86 games run via FEX + muvm — surprisingly well. |
| **M3 series** | **Early alpha** — bring-up in early 2026; "roughly the level of the first M1 alpha" as of April 2026. Boots, displays, basic peripherals; GPU and many drivers in progress. Not for daily use. |
| **M4 series** | Feature-tracking page exists; earlier than M3. Not usable. |
| **M5** | Nothing. |

**Practicalities.** Install via a `curl | sh` from macOS that repartitions and installs alongside macOS (dual-boot is the design; macOS must stay for firmware updates). The M1/M2 experience is excellent — a MacBook Air M1 with Fedora Asahi Remix + KDE is one of the best Linux laptops available: silent, fast, 12+ hour battery, gorgeous screen. Costs: higher sleep drain than macOS, no Touch ID login, and arm64-only software (open source is fine; proprietary Linux software is often x86-only — Steam via FEX, while Zoom/Slack/VS Code/JetBrains have arm64 builds).

**Recommendation.** Own an M1/M2: Fedora Asahi Remix is a genuinely great Linux machine. Own an M3/M4: run macOS with Linux in a VM (UTM, Parallels; OrbStack for containers) or remotely; check Asahi in 2027. Buying a Mac *for* Linux: a used M1/M2, not a new M4.

## 10.5 Snapdragon X (ARM Windows laptops)

Snapdragon X Elite/Plus laptops (Surface Laptop 7, ThinkPad T14s Gen 6 Snapdragon, XPS 13 9345, HP OmniBook X, ASUS Vivobook S15, Yoga Slim 7x) were pitched as Windows-on-ARM's MacBook moment. Qualcomm promised Linux support; Linaro did upstream work. Reality in 2026:

- Most models boot Linux (Ubuntu concept images, Fedora with custom device trees) using **firmware blobs extracted from the Windows partition** — Qualcomm/OEMs don't redistribute them.
- GPU acceleration works on some (Freedreno); audio hit-and-miss; webcams mostly don't; battery far below Windows; suspend flaky; **each model needs its own device tree** — no ACPI-style plug-and-play.
- Tuxedo cancelled its Snapdragon Linux laptop (Nov 2025) citing exactly this. Community sentiment shifted to "Apple Silicon is better supported than Snapdragon, which is embarrassing for Qualcomm." The X2 Elite generation restarts the cycle.

**Do not buy a Snapdragon X laptop to run Linux in 2026.** If you have one, keep Windows and use WSL2, which is genuinely good.

## 10.6 The usual suspects, component by component

**WiFi and Bluetooth**

| Vendor | Status |
|---|---|
| **Intel** (AX200/210/211, BE200/201) | Excellent, in-tree, firmware in `linux-firmware`. The gold standard. WiFi 7 (BE200) fine since 6.7. |
| **Qualcomm Atheros** (QCA6174, QCNFA765, WCN6855/7850) | Good to excellent in-tree (`ath11k`/`ath12k`); WCN7850 fine since ~6.8. Bluetooth sometimes needs newer firmware. |
| **MediaTek** (MT7921/7922/7925) | Common in AMD laptops (Framework AMD, Lenovo, ASUS). In-tree; 2024–2025 stability regressions (disconnects, slow speeds, suspend) mostly fixed by 6.15+. Fine on a 2026 kernel; on Debian 13's 6.12, use the backports kernel. |
| **Realtek** (RTL8852BE/CE, RTL8822, USB dongles) | In-tree `rtw88`/`rtw89` for most PCIe; variable performance; some USB dongles need out-of-tree DKMS drivers (avoid). |
| **Broadcom** (BCM43xx — older Macs, Dells, HPs) | The historical villain: `broadcom-wl` (proprietary DKMS, breaks on new kernels) or `b43` with extracted firmware. Replace with an Intel AX210 (M.2, ~$20) if the slot allows. |

**Webcams.** UVC USB cameras (99% of laptops) work everywhere. **Intel IPU6 MIPI cameras** (XPS 13 Plus/9315, some X1 Carbon Gen 10–12, some 2022–2024 designs) needed out-of-tree drivers; upstream support landed in 6.10+ and PipeWire/libcamera integration matured through 2025 — on a 2026 kernel with `libcamera` and the PipeWire camera portal they work in Firefox/Chrome/Zoom. Many 2025+ laptops moved back to UVC.

**Fingerprint readers.** `fprintd` + `libfprint`: most Synaptics and Validity readers, some Goodix and Elan. Check libfprint's supported-devices list for your USB ID. Framework's works; most ThinkPads work; many consumer laptops don't. Ubuntu 26.04 improved enrolment UX. Windows Hello IR cameras: `howdy`.

**Touchpads.** Near-universally fine (libinput); Mac-quality gestures on GNOME. Occasional I2C quirks on brand-new laptops, fixed within a release or two.

**Displays.** HiDPI: GNOME 50 and Plasma 6 handle 2× and fractional scaling well on Wayland; Xwayland apps (some Electron/Java) can be blurry at fractional scales until you set per-app flags (`--ozone-platform=wayland` for Electron). Mixed-DPI multi-monitor works. **HDR:** Plasma 6 mature; GNOME 50 has compositor support with apps arriving; content sources limited (mpv, games via gamescope; no HDR in browsers/streaming). **VRR:** both stable. OLED: fine.

**Sleep and battery.** Linux battery life trails Windows by 10–25% on the same laptop, more on Intel than AMD lately. Tools: `power-profiles-daemon` (default; adequate), **TLP** (more aggressive; conflicts with PPD — choose one), `powertop` for diagnosis. **Suspend:** s2idle (Modern Standby) is the norm; on well-supported laptops ~1%/hr drain; on bad firmware 5–10%/hr or failure to wake. S3 is often disabled in new firmware. **Hibernate** needs swap ≥ RAM and often a kernel parameter; works on most, fails on some, never default. AMD Ryzen laptops from 2023+ have the best x86 Linux sleep/battery; Apple M1/M2 under Asahi beat them on battery but drain more in sleep.

**Audio.** PipeWire + `sof-firmware` handles modern Intel/AMD audio. Laptop-specific speaker quirks (some Dell/HP/Samsung/Huawei) usually land upstream within a release. Bluetooth codecs: LDAC, AAC, aptX (`libfreeaptx`), SBC-XQ; mSBC for headset mic; LE Audio arriving.

**Thunderbolt/USB4 docks.** Work well on Intel and AMD; `bolt` handles authorisation. NVIDIA dGPU + dock display output may need the whole session on the dGPU.

**Printers/scanners.** Driverless IPP Everywhere for anything post-2015. HP: `hplip`. Brother: their `.deb`/`.rpm`. Canon: variable. Scanners via SANE; `sane-airscan` for network scanners.

**Storage.** NVMe fine. Some laptops ship with Intel VMD/RST RAID mode — switch to AHCI in firmware or the installer won't see the disk (Windows needs a registry tweak to boot afterwards; the ArchWiki explains).

**TPM and firmware.** TPM 2.0 is universal: Ubuntu's TPM FDE, `systemd-cryptenroll`, Secure Boot measurements. Firmware updates via **LVFS/fwupd** — Lenovo, Dell, HP, Framework, System76, Star Labs and many peripheral makers publish there; ASUS, Acer, MSI mostly don't (update firmware from Windows before installing Linux).

## 10.7 Desktops

Simpler. Any modern motherboard works; Ethernet (Intel or Realtek) is fine; check on-board WiFi isn't an oddball. GPU advice as above. Secure Boot + NVIDIA + MOK is the only common wrinkle. Dual-boot Windows on a *separate drive* rather than a partition — it sidesteps Windows overwriting the ESP and BitLocker complaints. RGB: **OpenRGB**. Fans: `lm_sensors`, `CoolerControl`. Ryzen tuning: `ryzen_smu`/`ryzenadj`.

## 10.8 Buying checklist (2026)

1. **GPU:** AMD or Intel unless you need CUDA. If NVIDIA, Turing (RTX 20xx / GTX 16xx) or newer.
2. **WiFi:** Intel ideally; Qualcomm or MediaTek acceptable; not Broadcom; check it's replaceable.
3. **Vendor:** Framework, System76, Tuxedo, Slimbook, or a Linux-certified ThinkPad/Dell/HP. Or a used ThinkPad T/X1 (2019+).
4. **Webcam:** UVC, or a supported IPU6 model.
5. **Fingerprint:** libfprint's list, if you care.
6. **RAM:** 16 GB minimum for a developer; 32 GB for VMs, containers, local ML. Soldered RAM is common — buy enough up front.
7. **Storage:** 512 GB minimum if dual-booting; 1 TB comfortable.
8. **LVFS:** search fwupd.org for the model.
9. **Check the ArchWiki page and linux-hardware.org for the exact model.**
10. **Not Snapdragon X. Not an M3/M4 Mac for Linux (yet).**

---

### Key takeaways

- **GPU is the decisive component.** AMD and Intel are in-tree and effortless; NVIDIA works well in 2026 but is out-of-tree and the main source of update pain — choose distros that pre-build its modules (Ubuntu, Pop!_OS, Universal Blue `-nvidia`, Arch `nvidia-open`). Pascal and older are on a legacy branch; upgrade.
- **Buy for Linux** if you can: Framework, System76, Tuxedo, Slimbook, or a Linux-certified ThinkPad/Dell. Used ThinkPads are the student's best budget route.
- **Apple M1/M2** under Fedora Asahi Remix is an excellent Linux laptop; **M3** is early alpha; **M4** unusable. **Snapdragon X** is not viable for Linux in 2026.
- **Intel WiFi** is the gold standard; MediaTek is fine on 2026 kernels; Broadcom should be replaced. IPU6 webcams work on current kernels; fingerprint readers depend on libfprint's list.
- Linux battery life trails Windows by 10–25%; AMD laptops and Apple M-series do best; sleep quality depends on firmware.
- New hardware (< 6 months) wants a current kernel — Fedora, Arch-family, Tumbleweed, Universal Blue, or Ubuntu LTS with HWE; not Debian stable or Mint between point releases.


---

# Chapter 11 — Developer Workflow on Linux

This chapter is about *doing the work* once the distro is installed. Much of it is distro-agnostic by design — that's the point of Chapter 4's argument that the toolchain layer has decoupled from the base system. Where the distro matters, I say so.

## 11.1 The mental model: three layers

Think of your development machine as three layers, each with its own update cadence and its own tooling:

1. **The base system** — kernel, drivers, desktop, system libraries, terminal, shell, `git`, `ssh`, container runtime. Managed by the distro's package manager (or the image, on atomic distros). Changes rarely; when it does, it's the distro's job to keep it coherent.
2. **Your toolchains** — compilers, runtimes, SDKs, language servers, CLI utilities. Managed by *version managers* and *Homebrew*, or by Nix, or inside Distrobox/devcontainers. Changes per project. Should never be the distro's job.
3. **Your projects** — with their own declared dependencies (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, `flake.nix`, `devcontainer.json`). Managed by the project's own tooling.

The most common source of developer misery on Linux is collapsing layers 1 and 2 — `sudo apt install python3-pip` then `sudo pip install` into the system Python, or `sudo npm install -g`, or building a project against the distro's `libssl` and then wondering why it breaks after an upgrade. Keep the layers separate and the distro becomes almost irrelevant to your work.

## 11.2 Toolchains, language by language

The pattern for every language: **install the version manager once (from its upstream), let it manage every version, never use the distro's package for the language itself except as a bootstrap.** Distro packages of `python3`, `nodejs`, `go`, `rustc` exist to build the distro's own software; treat them as read-only.

| Language | Recommended manager (2026) | Notes |
|---|---|---|
| **Python** | **`uv`** (Astral) | Replaces `pip`, `venv`, `pyenv`, `pipx`, `poetry`, `pip-tools` in one fast Rust binary. `uv python install 3.12 3.14`, `uv venv`, `uv run`, `uv tool install ruff`. The 2024–2026 consensus; nothing else is close. Never `pip install` into system Python (PEP 668 will stop you on modern distros anyway). |
| **Node.js** | **`fnm`** or **`volta`** (or `mise`) | Both fast, respect `.nvmrc`/`package.json#engines`. `nvm` works but is slow (shell-function based). Corepack for `pnpm`/`yarn`. |
| **Rust** | **`rustup`** | The only way. `rustup toolchain install stable nightly`, per-project `rust-toolchain.toml`. Distro `rustc` is for building distro packages. |
| **Go** | Official tarball to `/usr/local/go` or `~/go`, **`mise`**, or the distro package | Go's toolchain is self-contained and versioned per-module (`go.mod` `toolchain` directive downloads what's needed). Distro packages are usually fine here. |
| **JVM (Java/Kotlin/Scala)** | **SDKMAN!** or **`mise`** | Multiple JDK vendors (Temurin, GraalVM, Zulu, Corretto) and versions side by side. `jenv` also fine. |
| **.NET** | Microsoft's `dotnet-install.sh` or distro package (`dotnet-sdk-9.0` etc. — Microsoft ships repos for Ubuntu/Debian/Fedora/RHEL) | Ubuntu/Fedora package it natively; fine either way. |
| **Ruby** | **`mise`**, `rbenv` + `ruby-build`, or `chruby` | `rvm` is legacy. |
| **PHP** | distro package for CLI + Docker for apps; `phpenv`/`mise` for multi-version | |
| **Haskell** | **`ghcup`** | Manages GHC, cabal, stack, HLS. |
| **OCaml** | **`opam`** | Switches per project. |
| **Elixir/Erlang** | **`mise`** (via asdf plugins) or `kerl`/`kiex` | |
| **C/C++** | distro `gcc`/`clang` + **CMake** + **Ninja**; `conan`/`vcpkg` for libraries; multiple compiler versions via distro (`gcc-14`, `clang-18`) or Distrobox | The one place the distro's compiler *is* your toolchain by default. On an LTS, newer compilers come via `apt install gcc-15` (Ubuntu toolchain PPA), `dnf install gcc-toolset`, or a container. |
| **Zig** | `zigup`, `mise`, or the tarball | |
| **Polyglot** | **`mise`** (successor to `asdf`, Rust, fast, reads `.tool-versions` and `.mise.toml`, also manages env vars and tasks) | If you juggle many languages, `mise` alone can replace most of the above. |

**Homebrew on Linux** deserves separate mention. Installed to `/home/linuxbrew/.linuxbrew`, it provides thousands of current CLI tools — `ripgrep`, `fd`, `bat`, `eza`, `fzf`, `zoxide`, `lazygit`, `gh`, `jq`, `yq`, `k9s`, `helm`, `terraform`, `neovim` — independent of the distro and identical to macOS. It's the answer to "my LTS has a two-year-old `neovim`." Bluefin ships it by default; anyone can install it. Downsides: it duplicates libraries the distro already has (disk), and a few formulae assume macOS quirks. Distro packages are still preferable for anything that integrates with the system (shells, terminals, `git`, `ssh`).

## 11.3 Containers

**Docker vs. Podman.** Both run OCI containers; both use the same images and the same `Dockerfile`s; both support Compose (`docker compose` / `podman compose` or `podman-compose`). Differences that matter:

- **Docker** — the daemon model (`dockerd` as root; users in the `docker` group have effective root), the reference implementation everyone's docs assume, Docker Desktop *not needed on Linux* (the engine is native and faster than on macOS/Windows). Rootless Docker exists and works. Install from **Docker's own repo**, not the distro's (Ubuntu's `docker.io` package lags and Fedora's `moby-engine` is fine but behind). Debian/Ubuntu/Arch users usually pick Docker.
- **Podman** — daemonless, rootless by default (each container runs as your user via user namespaces), Docker-CLI-compatible (`alias docker=podman` works for 95% of cases), generates systemd units (Quadlet) for services, and is the default on Fedora/RHEL and the atomic distros. Some tools that talk to the Docker socket (Testcontainers, some IDE integrations, some CI runners) need `podman system service` and `DOCKER_HOST` set, or the `podman-docker` compatibility package. Fedora users usually pick Podman.

Either is fine. If your team uses Docker, use Docker. If you're on Fedora/atomic, Podman is smoother. Bluefin DX ships both.

**Local Kubernetes.** `kind` (Kubernetes in Docker/Podman — fastest, most common), `minikube` (VM- or container-based, more features), `k3s`/`k3d` (lightweight real distribution), or Podman's `kube play` for single-manifest testing. All distro-agnostic.

**Distrobox** (and Fedora's **Toolbox**) — covered in Chapter 4. For developers it's the tool that makes the distro choice nearly irrelevant: `distrobox create -i ubuntu:24.04 -n dept` gives you the department's exact Ubuntu with your `$HOME` mounted; `distrobox create -i archlinux -n arch` gives you the AUR on Fedora; `distrobox-export --app code` puts a container's app in your host menu. On atomic distros it's the *primary* way to install CLI tools. Chapter 12 shows the student use case.

**Devcontainers.** A `.devcontainer/devcontainer.json` in the repo declares the image, features (Node, Python, Docker-in-Docker…), extensions and post-create commands. VS Code (Dev Containers extension), JetBrains (Gateway/native), the `devcontainer` CLI, and DevPod all build and attach to it. Onboarding becomes `git clone` + "Reopen in Container." The laptop's distro is irrelevant to the project's build. Strongly recommended for any team project.

## 11.4 Virtual machines

You'll want a VM for: OS-course kernels (QEMU, see Chapter 12), testing installers and other distros, Windows for the occasional tool, and isolating dodgy software.

- **KVM/QEMU + libvirt** — the native Linux hypervisor, in the kernel, fastest, most capable. Front-ends: **virt-manager** (full-featured, slightly dated UI), **GNOME Boxes** (simple, good for "just give me a Windows/Ubuntu VM"), **Cockpit Machines** (web UI), `quickemu` (scripted downloads of Windows/macOS/many Linux ISOs — genuinely convenient). Windows 11 guests work well with virtio drivers and a TPM emulator (`swtpm`). GPU passthrough (VFIO) for gaming VMs is a hobby unto itself. **This is what you should use.**
- **VirtualBox** — familiar from Windows/macOS, works on Linux, but needs out-of-tree kernel modules (DKMS — breaks on new kernels), is slower than KVM, and is essentially impossible on atomic distros. Use only if a course mandates `.ova` appliances (you can convert them: `qemu-img convert`).
- **VMware Workstation** — free for personal use since 2024, out-of-tree modules, similar caveats.
- **Vagrant** — works with libvirt via `vagrant-libvirt`; the VirtualBox provider is the default in many tutorials, so expect to add `--provider=libvirt`.

Enable nested virtualization if you'll run VMs inside VMs (Android emulator inside a VM, etc.). Add yourself to the `libvirt` and `kvm` groups.

## 11.5 Editors and IDEs

All the major editors are first-class on Linux. Installation channel matters more than distro:

| Editor | Best install channel | Notes |
|---|---|---|
| **VS Code** | Microsoft's `.deb`/`.rpm` repo (adds itself on first install), or AUR `visual-studio-code-bin` | Flatpak and Snap versions work but sandbox the integrated terminal and hide host toolchains/Docker socket — avoid unless on an atomic distro (where Bluefin DX puts it in the image instead). **VSCodium** if you want it without telemetry (loses the marketplace by default; Open VSX instead). |
| **Cursor / Windsurf / other VS Code forks** | AppImage or `.deb` from the vendor | Same sandbox caveats if you find a Flatpak. |
| **JetBrains** (IntelliJ, PyCharm, CLion, GoLand, Rider, RustRover…) | **JetBrains Toolbox** app (manages installs/updates in `~/.local/share/JetBrains/Toolbox`) | Distro-agnostic, per-user, no root. Flatpaks exist with the usual sandbox caveats. Increase `fs.inotify.max_user_watches` (the Toolbox prompts you). |
| **Neovim** | distro package if ≥ 0.10, else Homebrew/AppImage/`bob` | Distro versions on LTS lag; Arch/Fedora/Homebrew are current. LazyVim, AstroNvim, NvChad, kickstart.nvim for configs. |
| **Emacs** | distro package (29/30 fine everywhere) | Doom Emacs, Spacemacs. `emacs-pgtk` for native Wayland. |
| **Helix** | distro package or Homebrew | Modal, batteries-included, Rust. |
| **Zed** | official Linux build (`curl | sh` installer) or Flatpak or AUR | Native Linux since 2024, Wayland-native, fast; collaboration features. |
| **Android Studio** | Google's tarball, Flatpak, AUR, or JetBrains Toolbox | Needs `/dev/kvm` access for the emulator (`kvm` group). |
| **Eclipse** | Eclipse Installer or Flatpak | Some university courses still mandate it; works. |
| **Vim/nano** | there already | |

**Wayland note for Electron apps** (VS Code, Cursor, Slack, Discord, Obsidian…): they run under Xwayland by default and can look blurry at fractional scaling. Add `--ozone-platform-hint=auto` (or `--enable-features=UseOzonePlatform --ozone-platform=wayland`) to the `.desktop` file or `~/.config/code-flags.conf` (Arch's package reads this) to run natively. Most distros' packages have started doing this by default in 2025–2026.

## 11.6 Terminal, shell, and multiplexer

**Terminal emulators.** All GPU-accelerated, all Wayland-native, all fine — pick on taste:

- **Ptyxis** — GNOME's new default (Fedora, Ubuntu 26.04); GTK4, tabs, container-aware (remembers which Distrobox/Toolbox you were in). The sensible default on GNOME.
- **Konsole** — KDE's; feature-rich, split panes, profiles. The sensible default on Plasma.
- **Ghostty** — Mitchell Hashimoto's (2024); native GTK4/libadwaita on Linux, fast, zero-config good defaults, Kitty graphics protocol. The 2025–2026 enthusiast favourite.
- **Kitty** — fast, scriptable, its own graphics/keyboard protocols, tabs and layouts built in.
- **Alacritty** — minimal, fast, no tabs (use tmux/zellij).
- **WezTerm** — Lua-configured, cross-platform, multiplexer built in.
- **foot** — tiny, Wayland-only, the Sway/niri crowd's pick.
- **COSMIC Terminal** — Pop!_OS's; fine.

**Shells.** `bash` is the default and what scripts assume. **`zsh`** with a framework (Oh My Zsh is heavy; `zinit`/`antidote` + a few plugins is lighter) or **`fish`** (autosuggestions and syntax highlighting out of the box, saner scripting, not POSIX — which almost never matters interactively). **Starship** for a fast cross-shell prompt. **`zoxide`** (smarter `cd`), **`fzf`** (fuzzy everything), **`atuin`** (synced, searchable shell history) are the three add-ons that most change daily life. Set your login shell with `chsh` — or better, keep `bash` as login shell and have your terminal launch `fish`/`zsh`, so scripts and `ssh` sessions stay predictable.

**Multiplexers.** **tmux** (universal, on every server you'll ever SSH into — learn it regardless), **zellij** (modern, discoverable keybindings, floating panes, Rust). One or the other; not needed if your terminal has good splits and you don't detach sessions.

## 11.7 Dotfiles

Your shell config, editor config, `git` config, terminal config, and the hundred small files in `~/.config` are your *actual* development environment. Put them in git on day one. Tools, in rough order of ceremony:

- **A bare git repo in `$HOME`** (`git init --bare ~/.dotfiles`, alias `config='git --git-dir=$HOME/.dotfiles --work-tree=$HOME'`) — zero dependencies, widely documented, works everywhere.
- **GNU Stow** — symlink farm from `~/dotfiles/<package>/` into `$HOME`. Simple, transparent.
- **chezmoi** — templating (per-machine differences), secrets integration (1Password, Bitwarden, age), scripts, one-command bootstrap on a new machine (`chezmoi init --apply github.com/you/dotfiles`). The best general-purpose choice in 2026.
- **yadm** — bare-repo approach plus templates and encryption.
- **Home Manager** (Nix) — declarative user environment including the *packages* your dotfiles need. The most powerful; requires Nix; works on any distro and macOS.

Whatever you pick, add a `bootstrap.sh` (or `chezmoi` run-once scripts) that installs your version managers, Homebrew, and Flatpaks. A new machine should be yours in thirty minutes.

## 11.8 Git, SSH, GPG, and hardware keys

- **Git**: install from the distro (current everywhere). Use `git config --global init.defaultBranch main`, `pull.rebase true`, `rerere.enabled true`, `commit.gpgsign` if you sign. **`gh`** (GitHub CLI) or **`glab`**. **`lazygit`** or **`gitui`** for a TUI. **`delta`** or **`difftastic`** for diffs.
- **SSH**: generate an ed25519 key (`ssh-keygen -t ed25519`). The desktop's keyring (GNOME Keyring / KDE Wallet) acts as an SSH agent and unlocks your key at login; or use `ssh-agent` via systemd user service; or 1Password/Bitwarden's SSH agent. Put per-host config in `~/.ssh/config`. **Sign commits with SSH keys** (`gpg.format ssh`) — simpler than GPG and supported by GitHub/GitLab since 2022–2023.
- **GPG**: only if you need it (some projects require GPG-signed commits; `pass` password store; encrypting files). `gpg-agent` with `pinentry-gnome3`/`pinentry-qt`.
- **Hardware keys** (YubiKey, Nitrokey, SoloKey): FIDO2 for web logins works in Firefox/Chromium out of the box; `ssh-keygen -t ed25519-sk` for FIDO-backed SSH keys (resident on the key — genuinely excellent for portable identity); GPG on the key via `ykman`/`gpg --card-edit`; PAM U2F for sudo/login. Install `libfido2`, `yubikey-manager`, `pam-u2f`; udev rules come with them on every distro.

## 11.9 Distro command cheat-sheet

When a tutorial says `sudo apt install foo` and you're not on Debian/Ubuntu:

| Debian/Ubuntu | Fedora | Arch | openSUSE | NixOS (imperative / declarative) |
|---|---|---|---|---|
| `sudo apt update && sudo apt upgrade` | `sudo dnf upgrade` | `sudo pacman -Syu` | `sudo zypper dup` | `sudo nixos-rebuild switch --upgrade` |
| `sudo apt install foo` | `sudo dnf install foo` | `sudo pacman -S foo` | `sudo zypper in foo` | `nix profile install nixpkgs#foo` / add to config |
| `sudo apt remove --purge foo` | `sudo dnf remove foo` | `sudo pacman -Rns foo` | `sudo zypper rm -u foo` | `nix profile remove foo` / remove from config |
| `apt search foo` | `dnf search foo` | `pacman -Ss foo` (AUR: `paru -Ss`) | `zypper se foo` | `nix search nixpkgs foo` |
| `apt show foo` | `dnf info foo` | `pacman -Si foo` | `zypper if foo` | `nix eval nixpkgs#foo.meta` |
| `dpkg -S /path/file` | `dnf provides /path/file` | `pacman -Qo /path/file` | `zypper se --provides /path/file` | `nix-locate` (nix-index) |
| `dpkg -L foo` | `dnf repoquery -l foo` | `pacman -Ql foo` | `rpm -ql foo` | `ls $(nix build --print-out-paths nixpkgs#foo)` |
| `sudo apt autoremove` | `sudo dnf autoremove` | `sudo pacman -Rns $(pacman -Qdtq)` | `sudo zypper rm -u` (on removal) | `nix-collect-garbage -d` |
| `build-essential` | `@development-tools` / `gcc gcc-c++ make` | `base-devel` | `-t pattern devel_basis` | `nix develop` / `mkShell` |
| `foo-dev` (headers) | `foo-devel` | (included in `foo`) | `foo-devel` | `foo.dev` output |
| `add-apt-repository ppa:x/y` | `dnf copr enable x/y` | (AUR) | `zypper ar <obs-url>` | overlay / flake input |

Package names differ (`libssl-dev` → `openssl-devel` → `openssl`); `pkgs.org` and Repology map them across distros.

## 11.10 The honest comparison: Linux vs. WSL2 vs. macOS for development

Since many readers are choosing *whether* to run Linux, not just which one:

| | Native Linux | Windows + WSL2 | macOS |
|---|---|---|---|
| **Containers** | native, fastest, no VM | Docker Desktop or Podman inside a lightweight VM; good, some file-I/O overhead across the Windows/Linux boundary; keep repos inside the WSL filesystem | Docker Desktop / OrbStack / Podman in a VM; noticeably slower file I/O; arm64 images vs. x86 emulation issues |
| **Toolchain parity with servers/CI** | identical | identical inside WSL (it's real Ubuntu/Fedora) | close but different (BSD userland, `brew` vs `apt`, arm64, case-insensitive FS by default) |
| **GUI apps / desktop polish** | good to excellent (Chapter 5); some proprietary apps missing (Adobe, MS Office desktop) | Windows' — everything runs; WSLg runs Linux GUI apps acceptably | excellent; everything commercial runs |
| **Hardware / battery / sleep** | good on supported hardware; 10–25% worse battery than Windows | Windows' — best battery on x86 laptops | best in class |
| **Gaming** | 4–5% of Steam, most titles via Proton, anti-cheat exceptions | everything | poor |
| **Proctoring / corporate agents** | mostly unsupported | supported | supported |
| **Understanding the system** | full | Linux inside, Windows outside; two systems to know | Unix-ish, but opaque below the surface |
| **Cost** | free; runs on anything | Windows licence (usually bundled) | Apple hardware only |
| **Package management** | excellent | Linux side excellent; Windows side `winget`/`scoop`, okay | Homebrew, good |
| **Kernel/driver/systems work** | native | limited (custom WSL kernels possible; no real hardware access) | Darwin — irrelevant to Linux targets |

The honest take: **WSL2 is good enough that "I need Linux for development" is no longer a sufficient reason to install Linux on a Windows laptop.** The reasons that remain are: you want the *whole* machine to be Linux (desktop, workflow, ownership), you do systems/kernel/driver/embedded work, you want native container performance, you object to Windows itself, you're on hardware Windows serves poorly, or you simply prefer it. Those are all fine reasons — but be clear which one is yours, because "Linux is required for coding" isn't true in 2026 and will disappoint you if it's your only motivation.

macOS remains the default for iOS development and a very good general developer machine; its costs are the hardware lock-in, arm64/x86 container friction, and a desktop you can't reshape. Many developers run macOS for the laptop and Linux for everything the code actually runs on, and that's a coherent choice too.

---

### Key takeaways

- Keep three layers separate: **base system** (distro-managed), **toolchains** (version managers / Homebrew / Nix / Distrobox), **projects** (their own manifests). Never install language packages into the system interpreter.
- Per language: `uv` (Python), `fnm`/`volta` (Node), `rustup`, SDKMAN/`mise` (JVM), `ghcup`, `opam`, and **`mise`** as the polyglot manager. Homebrew on Linux for fresh CLI tools on any distro.
- Docker (from Docker's repo) or Podman (Fedora/atomic default) — both fine; Distrobox and devcontainers make the host distro nearly irrelevant to your projects.
- Use **KVM/QEMU** (virt-manager, GNOME Boxes, quickemu) for VMs; avoid VirtualBox unless a course forces `.ova` files.
- Install VS Code from Microsoft's repo, JetBrains via Toolbox; avoid Flatpak IDEs on mutable distros. Run Electron apps natively on Wayland.
- Put dotfiles in git on day one (chezmoi recommended); use ed25519 SSH keys with SSH commit signing; consider a FIDO2 hardware key.
- **WSL2 is good enough that "I need Linux to code" isn't a reason on its own.** Choose Linux because you want the whole machine to be Linux, do low-level work, want native containers, or prefer it — all legitimate.


---

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


---

# Chapter 13 — Daily-Driver Realities

The non-programming half of your life on the machine. This chapter is a status report on each area as of 2026, with the distro-relevant bits flagged. The short version: **almost everything works, a few things need a one-time fix, and a small list of things don't work and won't.**

## 13.1 Browsers, DRM, and video

**Firefox and Chromium/Chrome** are first-class. Brave, Vivaldi, Edge, Opera, Zen, LibreWolf all ship Linux builds. Distro packaging: Ubuntu ships Firefox as a snap (fine in 2026; the `.deb` is available from Mozilla's own apt repo if you object); Fedora/Arch/openSUSE/Debian ship native packages; Flathub has all of them.

**DRM (Widevine)** for Netflix, Disney+, Prime, Spotify, etc. ships in Firefox and Chrome on x86-64 and is enabled on first use. Quality caps at **1080p** on most services — Linux browsers only get Widevine L3 (software), and services gate 4K/HDR behind L1 or platform-specific DRM. This is a *service* decision, not a Linux limitation, and no distro changes it. On **arm64** (Asahi, Raspberry Pi) Widevine is officially unavailable; the Asahi project ships a workaround using ChromeOS's arm64 Widevine that works for most services.

**Hardware video decode** (VA-API) saves battery and CPU on YouTube/Twitch. Works in Firefox and Chromium on **AMD and Intel** out of the box on most distros — Fedora and openSUSE need the RPM Fusion/Packman `mesa-va-drivers-freeworld` swap for H.264/H.265 (the one real "codec" step). **NVIDIA** needs `libva-nvidia-driver` (nvidia-vaapi-driver) and a Firefox flag; Chromium's NVIDIA VA-API support is unreliable. AV1 decode is universal on 2022+ hardware and needs nothing extra.

**Extensions, password managers, sync:** identical to other platforms. 1Password, Bitwarden, Proton Pass, KeePassXC (native and excellent) all have Linux desktop apps and browser integration.

## 13.2 Media and codecs

Playback of H.264/H.265/AAC/MP3/etc.:

| Distro family | Status |
|---|---|
| Ubuntu, Mint, Pop!_OS, Zorin | "Install third-party software" checkbox at install, or `ubuntu-restricted-extras` — done |
| Debian | `libavcodec-extra` — done (Debian has no patent qualms) |
| Arch family, Void, Gentoo, NixOS | included; nothing to do |
| **Fedora** | enable RPM Fusion, `dnf swap ffmpeg-free ffmpeg --allowerasing`, `dnf install mesa-va-drivers-freeworld` (AMD) — two minutes, well documented, the number-one newcomer trap |
| **openSUSE** | `opi codecs` (adds Packman and swaps the packages) — one command |
| Universal Blue (Bluefin/Aurora/Bazzite) | included |
| Fedora Atomic (stock) | Flatpak apps bring their own codecs via the Freedesktop runtime's `ffmpeg-full` extension; the host needs layering |

Flatpak apps (VLC, Celluloid, Showtime) get codecs through the runtime regardless of distro, which is one reason Flatpak is so useful on Fedora.

**Music/video apps:** Spotify (Flatpak/snap/AUR — official Linux client, maintained), Apple Music (web), YouTube Music (web/PWA), Tidal (web or `tidal-hifi`), Plex/Jellyfin (native), VLC, mpv, Celluloid, Haruna, Amberol, Rhythmbox, Elisa, Strawberry. Kodi. OBS Studio (Flatpak, excellent on Wayland via PipeWire). DaVinci Resolve (official Linux build, needs NVIDIA or a recent AMD with ROCm, free version lacks H.264 import — a known annoyance). Kdenlive, Shotcut (good). Audacity/Tenacity, Ardour, Reaper (native), Bitwig (native). Audio production is genuinely good on Linux with PipeWire's pro-audio profile.

**Photos:** darktable, RawTherapee, digiKam, Shotwell, GIMP 3, Krita. Lightroom/Photoshop: no (web Photopea, or Wine for very old versions). Google Photos/iCloud Photos: web.

## 13.3 Gaming

**The state of play (2026).** Steam's Linux share hovers at 4–5% (5.3% record in March 2026, ~4% mid-year), roughly double macOS. Nearly all of that is Proton — Valve's Wine-based compatibility layer that runs Windows games, often at native performance, sometimes better. ProtonDB rates the catalogue: the large majority of single-player titles are Gold/Platinum; the failures are concentrated in **kernel-level anti-cheat multiplayer games whose publishers have chosen not to enable Linux** (a shrinking but stubborn list — some large battle-royale and competitive shooters). Check ProtonDB and areweanticheatyet.com for your specific games before assuming.

**What you need:**
- **Steam** — Flatpak (fine; slightly more permission fiddling for external drives), native package (Fedora third-party repo, Arch `multilib`, Ubuntu `.deb` from Valve or the snap, openSUSE), or preinstalled (Bazzite, CachyOS gaming meta, Nobara, Pop!_OS).
- **Proton** — automatic via Steam. **Proton-GE** (community build with extra fixes/codecs) via `protonup-qt`/`protonplus`. **CachyOS ships its own Proton build.**
- **Non-Steam launchers:** **Heroic** (Epic, GOG, Amazon), **Lutris** (everything, including Battle.net, EA, Ubisoft), **Bottles** (Wine prefixes with a nice UI). All Flatpak.
- **GPU drivers:** AMD/Intel — Mesa, already there, and *newer Mesa = better gaming*, which favours Fedora/Arch/Tumbleweed/UBlue over Debian/Mint. NVIDIA — the proprietary/open driver as per Chapter 10.
- **32-bit libraries** — Steam needs them; Arch requires enabling `[multilib]`; Ubuntu/Fedora/openSUSE have them available by default.
- **Controllers:** Xbox (wired: kernel; wireless dongle: `xone`/`xpadneo` DKMS), PlayStation (kernel), Switch Pro (kernel), Steam Controller/Deck (Steam). Bazzite preloads all the DKMS ones.
- **gamescope** — Valve's micro-compositor for HDR, upscaling, frame limiting; **MangoHud** for overlays; **GameMode** for CPU governor switching. Bazzite/CachyOS/Nobara preconfigure these.
- **HDR** — works in Plasma 6 via gamescope; GNOME 50 partial.

**Distro impact.** Any distro games well after setup. The tuned ones — **Bazzite** (the closest thing to SteamOS for a PC; also a great handheld/HTPC OS), **CachyOS** (Arch + tuned kernel + its Proton), **Nobara** (Fedora + gaming patches, by the GloriousEggroll of Proton-GE fame; small team), **Garuda** — remove the setup and add a few percent. A "normal" Fedora/Ubuntu/Arch with Steam installed is within a few percent of them. Kernel schedulers (BORE, `sched-ext`/`scx_lavd`) and `ntsync` (in-kernel since 6.14) give measurable frame-time consistency gains that CachyOS and Bazzite enable by default.

**VR:** SteamVR on Linux works with Valve Index and some others; Meta Quest via ALVR/WiVRn; it's a hobby, not a polished experience. **Emulation:** excellent (RetroArch, Dolphin, PCSX2, RPCS3, Ryujinx forks, Duckstation — all native). **Minecraft:** native (Prism Launcher). **Roblox:** via Sober (Flatpak). **Game streaming:** Moonlight/Sunshine, Steam Link, GeForce Now (browser), Xbox Cloud (browser).

## 13.4 Video calls and chat

| App | How | Wayland screen-share |
|---|---|---|
| **Zoom** | native `.deb`/`.rpm`/Flatpak/snap | works via PipeWire portal (window and screen); occasional regressions in Zoom updates, usually fixed within a release |
| **Microsoft Teams** | **PWA** (install teams.microsoft.com from Chromium/Edge/Firefox) or community **Teams for Linux** Electron client | works (Chromium-based, PipeWire); the PWA is the officially supported path since Microsoft retired the native client in 2022 |
| **Google Meet** | browser | works in Firefox/Chromium |
| **Slack** | native `.deb`/`.rpm`/snap/Flatpak | works since 2023 (Electron with PipeWire); huddle screen-share fine |
| **Discord** | native `.deb`/Flatpak/AUR, or **Vesktop** (community client with better Wayland/screen-share-with-audio) | works; audio in screen-share needs Vesktop or the newer official builds |
| **Webex** | native (older), or browser | okay |
| **Signal / Telegram / WhatsApp** | native / native / web or unofficial wrappers | n/a |
| **FaceTime / iMessage** | no (FaceTime links work in browser for receiving) | — |

**Webcams and mics:** UVC cameras universal; IPU6 as per Chapter 10; **background blur/effects** are done in-app (Zoom, Meet, Teams PWA all do it) or via **OBS Virtual Camera** / `webcamoid`. **Echo cancellation** is via PipeWire's `echo-cancel` module (some distros enable it; `easyeffects` adds a full processing chain including noise suppression — the closest thing to NVIDIA Broadcast/Krisp). **Bluetooth headset mic** quality is poor on every OS (HFP codec); mSBC helps; a wired or USB mic is better for calls.

## 13.5 Office and documents

- **LibreOffice** — installed by default nearly everywhere; handles 95% of `.docx/.xlsx/.pptx`; complex layouts, tracked changes, macros and fonts can drift. Good for your own documents; risky for round-tripping a professor's or employer's template.
- **OnlyOffice** — renders MS Office formats more faithfully (it's built around OOXML), familiar ribbon UI, weaker on ODF. Flatpak/`.deb`/`.rpm`/AUR. Better choice for round-tripping.
- **Microsoft 365 web** — full Word/Excel/PowerPoint in the browser; the safest option for anything graded or shared. Install as PWAs. Requires a subscription or school account (most universities provide one).
- **Google Docs/Sheets/Slides** — web; fine.
- **WPS Office** — closest visual clone of MS Office; Chinese company; telemetry concerns; works.
- **Fonts:** metric-compatible replacements for Arial/Times/Courier (Liberation) and Calibri/Cambria (Carlito/Caladea) are installed by default on most distros, so documents don't reflow. For pixel-perfect: `ttf-mscorefonts-installer` (Ubuntu), or copy the fonts from a Windows install/Office 365 to `~/.local/share/fonts` (licence-grey, universally done).
- **PDF:** Papers/Evince (GNOME), Okular (KDE — annotations, forms, signing), Firefox's viewer, Xournal++ for handwriting/annotation, `qpdf`/`pdftk`/`ocrmypdf` for CLI work, LibreOffice Draw for editing. Adobe Acrobat: no; most needs are covered.
- **Notes:** Obsidian (native), Logseq, Joplin, Notion (web), Apple Notes (no), OneNote (web only, no native).
- **Email:** Thunderbird, Evolution (best Exchange/Office 365 support via EWS), Geary, Betterbird, Mailspring; Outlook web as a PWA. Exchange calendars in GNOME Calendar/KOrganizer via Evolution-EWS.

## 13.6 Peripherals and integration

**Printing/scanning:** covered in Chapter 10 — driverless for anything modern; `hplip` for HP; vendor packages for Brother/Canon; SANE + `simple-scan`/`skanpage`/`sane-airscan`.

**Bluetooth:** BlueZ + PipeWire. Pairing via the DE's settings. Audio codecs as per Chapter 10. Multipoint headphones work. AirPods pair and work (AAC; no spatial audio/auto-switch). Xbox/PS controllers pair. Bluetooth keyboards/mice fine. LE Audio arriving in 2026 kernels/PipeWire.

**Phone integration:**
- **Android:** **KDE Connect** (KDE; also on GNOME via the **GSConnect** extension, and standalone on any DE) — notifications, SMS, clipboard, file transfer, remote input, media control, find my phone. Genuinely excellent. **scrcpy** for screen mirroring/control over USB or WiFi. **LocalSend** / **Warpinator** for file transfer. Android file access via MTP (works) or **ADB**.
- **iPhone:** limited on any non-Apple platform. Photos/files via `libimobiledevice` (`ifuse`) — works for camera roll. iMessage/FaceTime/AirDrop: no. KDE Connect has a limited iOS client (file transfer, clipboard). If you're deep in Apple's ecosystem, this is a real friction point Linux can't fix.

**Cloud storage:**
- **Nextcloud** — first-class desktop client; the "own your cloud" option.
- **Dropbox** — official client works (ext4 required for the sync folder unless you use the Flatpak or `rclone`).
- **Google Drive** — GNOME Online Accounts mounts it in Files (slow, on-demand); `rclone mount`/`bisync` for real sync; KDE's KIO GDrive.
- **OneDrive** — `onedriver` (FUSE, on-demand, good), `rclone`, or the abraunegg `onedrive` client (full sync, CLI); web.
- **iCloud Drive** — web only.
- **Proton Drive** — Linux client arrived in 2025.
- **Syncthing** — peer-to-peer, no cloud, superb for syncing between your own devices.

**Smart home / misc:** Home Assistant (web), Philips Hue (web/apps), Sonos (web/`noson`), Tailscale (native, excellent), Steam Link, Chromecast casting from Chromium (works) and via `mkchromecast`/`catt`.

## 13.7 Display, scaling, and multi-monitor

- **Fractional scaling** — stable in GNOME 50 and Plasma 6 on Wayland; Xwayland apps (some Electron, Java, older games) may be blurry until told to use Wayland natively. GNOME's Xwayland scaling is bilinear-blurry; Plasma lets you choose sharp-but-small or blurry-but-right-size for legacy apps.
- **Mixed-DPI multi-monitor** — works on both (a 4K 27" at 150% next to a 1080p at 100%). This was a Wayland selling point and it delivers.
- **VRR / adaptive sync** — stable in both; per-monitor toggle.
- **HDR** — Plasma 6: works for games (gamescope), mpv, and the desktop with tone-mapping; GNOME 50: compositor support landed, app support arriving; browsers and streaming services: no HDR on Linux.
- **High refresh** — fine. **Ultrawide** — fine. **Docking/undocking** — hot-plug works; monitor arrangement is remembered per-configuration.
- **Night light / colour management** — both DEs; GNOME 50 improved colour management; Plasma has ICC profile support and a calibration flow.
- **Screen tearing** — gone with Wayland.

## 13.8 Power, sleep, and battery

Covered in Chapter 10 §10.6; the daily-driver summary: expect 10–25% less battery than Windows on the same laptop (less on AMD), use `power-profiles-daemon` (default) or TLP (not both), enable **hibernate** only if you need it and are willing to set it up, and treat "wakes up warm with a dead battery" as a firmware/kernel-version issue worth a search for your model. Suspend-then-hibernate (`systemd`'s `suspend-then-hibernate` with a timer) is the best of both worlds when it works.

## 13.9 Accessibility

GNOME leads: Orca screen reader (overhauled in GNOME 50), magnifier, high-contrast, large text, visual alerts, sticky/slow/bounce keys, on-screen keyboard, mouse keys, dwell click. Plasma has equivalents (Orca works there too), somewhat less integrated. Wayland accessibility (the `a11y` protocol work) matured through 2025. Speech-to-text: Whisper-based local tools (`nerd-dictation`, Speech Note); Windows/mac have better commercial options. Screen readers on Linux are usable but behind macOS VoiceOver and Windows NVDA/JAWS in polish — if you depend on one, evaluate carefully before switching.

## 13.10 What doesn't work (and won't soon)

Be honest with yourself about these before switching:

- **Adobe Creative Cloud** (Photoshop, Illustrator, Premiere, Lightroom, InDesign). No. Alternatives are good (GIMP 3, Krita, Inkscape, Kdenlive/Resolve, darktable, Scribus) but they are *different tools*, and if your work or degree requires Adobe files round-tripping with Adobe users, Linux is the wrong primary OS.
- **Microsoft Office desktop apps.** Web versions work fully; desktop apps do not (Wine + Office 2016 is a hobby). Fine for 90% of people; not fine if you live in Excel macros or complex PowerPoint.
- **iOS development / Xcode.** No.
- **Proctoring and some anti-cheat.** Covered.
- **4K/HDR streaming in browsers.** 1080p cap.
- **Some enterprise VPN/compliance agents.** Check with IT.
- **iMessage/FaceTime/AirDrop/Apple ecosystem lock-in.** No.
- **Autodesk (AutoCAD, Fusion 360, Maya — Maya has a Linux build, the rest don't), SolidWorks, most commercial CAD.** FreeCAD, Onshape (web), Blender exist. Engineering students: this is the reason your department runs Windows.
- **Some games** with kernel anti-cheat. Check the list.
- **Bluetooth headset mic quality.** Same as every OS; not Linux-specific.

Everything else on a normal person's list — browsing, video, music, calls, documents, photos, printing, phones, cloud, most games — works, and works well.

---

### Key takeaways

- Browsers, DRM (1080p cap — a service decision), and hardware video decode all work; Fedora/openSUSE need the two-minute codec step, Ubuntu/Mint a checkbox, everyone else nothing.
- Gaming via Steam/Proton covers most of the catalogue; kernel anti-cheat holdouts are the exception. Any distro games well; Bazzite/CachyOS/Nobara pre-tune. Newer Mesa (Fedora/Arch/Tumbleweed/UBlue) beats older (Debian/Mint) for AMD/Intel gaming.
- Zoom, Teams (PWA), Meet, Slack, Discord all work with Wayland screen-sharing via PipeWire portals.
- Use MS 365 web or OnlyOffice for documents that must round-trip with Office users; LibreOffice for your own.
- KDE Connect/GSConnect make Android integration excellent; iPhone integration is poor on any non-Apple OS.
- Fractional scaling, mixed-DPI, VRR and (on Plasma) HDR are solved on Wayland.
- **Won't work:** Adobe, MS Office desktop, Xcode, proctoring, some anti-cheat, 4K browser streaming, Apple ecosystem features, most commercial CAD. Decide if any of those is a dealbreaker *before* switching.


---

# Chapter 14 — Security, Privacy, and Long-Term Maintenance

A Linux desktop is not automatically secure, and it is not automatically maintained. It is *more securable* than the alternatives, with less effort, and it respects your privacy by default. This chapter covers what to turn on, what to leave alone, and how to keep the machine healthy for years.

## 14.1 Threat model for a laptop

Be concrete about what you're defending against, in rough order of likelihood for a student or engineer:

1. **Loss or theft of the device.** Someone has your laptop and wants your data (or just the hardware). → **Full-disk encryption** is the entire answer. Nothing else matters if this isn't done.
2. **Malicious or compromised software you installed.** A poisoned `npm` package, a malicious AUR PKGBUILD, a fake "Zoom installer," a browser extension gone bad. → Sandboxing (Flatpak), reading what you install, not running `curl | sudo sh` from random sites, keeping secrets out of reach of arbitrary processes.
3. **Network attacks on public WiFi.** → Firewall on, no listening services, VPN if you're paranoid, HTTPS everywhere (already default).
4. **Phishing and account compromise.** → Password manager, hardware keys/passkeys, not the OS's job.
5. **Evil-maid / physical tampering.** Someone modifies your bootloader while you're away. → Secure Boot + TPM-measured boot. Relevant to very few students; relevant to some engineers.
6. **Targeted remote exploitation.** Zero-days against your browser or kernel. → Update promptly; use a browser with sandboxing (both do); Flatpak browsers add a layer. If you're a real target, you need more than this chapter.

Everything below maps to one of these.

## 14.2 Full-disk encryption

**Do it at install time.** Every mainstream installer offers LUKS encryption; retrofitting it later is possible but painful.

- **Passphrase at boot** — the default. Choose a long passphrase (a sentence). You'll type it once per boot. Works everywhere.
- **TPM-backed auto-unlock** — the disk key is sealed to the TPM 2.0 chip and released only if the measured boot chain (firmware, bootloader, kernel) matches. You boot straight to the login screen; a thief who pulls the drive gets ciphertext; a thief who boots your laptop hits the login screen and (with a good password and no exploitable bugs) gets nothing. **Ubuntu 26.04 offers this in the installer.** On Fedora/Arch/openSUSE/Universal Blue you set it up after install with `systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=0+7 /dev/nvme0n1p3` (PCR selection is a trade-off between security and "a firmware update locked me out"); Universal Blue has a `ujust` recipe; openSUSE Aeon does it by default. **Keep the passphrase as a fallback slot and write down a recovery key.** A firmware update, a bootloader change, or toggling Secure Boot can change the measurements and require the fallback. This is normal, not a bug.
- **Encrypted `/home` only** (eCryptfs, fscrypt) is an older approach; full-disk is simpler and stronger.
- **Btrfs/ext4 on LUKS** is the standard layout. Encrypting swap matters too (installers handle it; zram swap is in RAM and needs nothing).
- **Performance cost:** negligible on any CPU with AES-NI (all of them since ~2010).

If you do nothing else in this chapter, do this.

## 14.3 Secure Boot

What it does: prevents unsigned bootloaders and kernels from running, closing off a class of persistent bootkits. What it doesn't do: protect against anything once the OS is running.

- **Ubuntu, Fedora, openSUSE, Debian, Mint, Universal Blue, Zorin**: work with Secure Boot on, out of the box, via the Microsoft-signed `shim`.
- **Third-party modules** (NVIDIA, VirtualBox, some VPNs) need signing: Ubuntu prompts you to set a MOK password during driver install and enrol at next boot; Fedora's akmods can auto-sign with a one-time `kmodgenca` + `mokutil --import`; openSUSE generates a MOK automatically; Universal Blue provides `ujust enroll-secure-boot-key`.
- **Arch, EndeavourOS, Pop!_OS, Void, Gentoo**: no signed shim; either disable Secure Boot or use `sbctl` to create and enrol your own keys and sign your kernel/bootloader (~20 minutes, well documented; CachyOS's installer can do it).
- **NixOS**: Lanzaboote (community; works; manual).

**Should you keep it on?** If your distro supports it, yes — it's free protection and required for Windows 11 dual-boot, TPM-backed encryption, and some corporate/anti-cheat contexts. If you're on Arch and don't want to set up `sbctl`, turning it off is a reasonable trade for a personal machine; know that you've done it.

## 14.4 Mandatory access control: SELinux and AppArmor

- **SELinux** (Fedora, RHEL, openSUSE Leap 16/Tumbleweed): enforcing by default with the targeted policy. Confines system daemons; mostly invisible to desktop users. When something's denied: `sudo ausearch -m avc -ts recent` or the `sealert` GUI explains it and suggests a fix (`setsebool`, `restorecon`, or a local policy module). Don't set it to permissive as a "fix" — find the actual denial. Worth learning if you'll administer RHEL.
- **AppArmor** (Ubuntu, Debian, Mint, Pop!_OS): path-based profiles for specific programs; confines snaps and some services. Ubuntu 24.04+ also restricts unprivileged user namespaces via AppArmor, which sometimes breaks Chromium-based Electron apps, some dev tools, or `bwrap`-based sandboxes — the fix is an AppArmor profile for the binary (or, less ideally, `sysctl kernel.apparmor_restrict_unprivileged_userns=0`).
- **Neither** (Arch, Void, Gentoo default, NixOS default): installable; most desktop users don't.

Neither should drive your distro choice. Both are fine. Leave whichever you have enabled.

## 14.5 Firewall

A laptop that connects to café and campus WiFi should have a firewall dropping unsolicited inbound connections. Linux distros disagree about defaults:

- **Fedora, openSUSE, EndeavourOS, CachyOS, Universal Blue**: `firewalld` on, with the "public" zone blocking inbound except SSH (Fedora) or nothing. Good.
- **Ubuntu, Mint, Pop!_OS, Debian**: `ufw` installed but **off** (Mint's firewall GUI makes enabling it obvious). Rationale: no services listen by default. Enable it anyway: `sudo ufw enable`. It takes two seconds.
- **Arch**: nothing. Install `ufw` or `firewalld` and enable it.
- **NixOS**: `networking.firewall.enable = true;` is the default.

Then don't punch holes you don't need. If you run a local dev server, bind it to `localhost`, not `0.0.0.0`, unless you're deliberately testing from your phone. KDE Connect needs ports 1714–1764 (its installer adds a `firewalld` service; on `ufw` add the range manually).

## 14.6 Application sandboxing and permissions

- **Flatpak** apps run in a bubblewrap sandbox with declared permissions (filesystem paths, network, devices, D-Bus). Review and adjust with **Flatseal** or the built-in permission UI in GNOME Settings / KDE System Settings. Many apps ask for broad filesystem access they don't need (`filesystem=home`); tightening it is a real security gain. Portals (file chooser, screenshot, screen share) let sandboxed apps do things without broad grants.
- **Snaps** are confined by AppArmor; permissions ("interfaces") via `snap connections` or the Software app.
- **AppImages** and **vendor `.deb`/`.rpm`s** run unconfined, as your user, with access to everything your user has — including `~/.ssh`, browser sessions, and your password manager's local vault if it's unlocked. This is the normal Linux state and it's why "don't run random binaries" is the key habit.
- **Browser sandboxing** is built into Firefox and Chromium and works on every distro. Firefox-as-Flatpak adds an outer layer with a slight cost to hardware acceleration and extension native-messaging setup.
- **Containers are not a security boundary** for untrusted code by default (rootful Docker especially). Rootless Podman is meaningfully better. For genuinely untrusted software, use a VM.

## 14.7 Supply chain: what you're trusting

- **Official repositories** of every mainstream distro: signed, reviewed, built on distro infrastructure. Trust these most.
- **Flathub**: apps reviewed on submission, built on Flathub's infrastructure from declared sources (or, for proprietary apps, repackaged vendor binaries — marked as such), sandboxed. Good.
- **AUR**: user-submitted build scripts, *not* reviewed, built on your machine. Read the PKGBUILD (your helper shows the diff). Prefer packages with many votes and an active maintainer. It has been abused a handful of times (2018, 2025 — malware in orphaned or newly-uploaded packages, caught within days). Treat it like `npm`: mostly fine, occasionally not.
- **PPAs / COPR / OBS**: binaries from individuals. Same trust calculus as the AUR, with less transparency (you don't see the build). Prefer well-known maintainers.
- **`curl | sh` installers** (rustup, uv, Homebrew, mise, nvm…): you're trusting the vendor's domain and TLS. The mainstream ones are fine; read the script for anything less known.
- **Docker Hub / GHCR images**: trust the publisher; prefer official/verified images; pin digests in production.
- **Universal Blue / other community image builders**: you're trusting their GitHub org and CI pipeline. Transparent (public builds, signed images via cosign) and well-run so far; a different surface than a distro foundation.
- **Reproducible builds**: Debian (95%+), Arch (progressing, Valve-funded), NixOS (high) can prove binaries match sources. A genuine supply-chain advantage that most users never think about.

## 14.8 Privacy and telemetry

Linux distros are, by default, dramatically more private than Windows or macOS. Specifics:

- **Ubuntu**: an optional, opt-in-at-install "Help improve Ubuntu" hardware/usage report; the Ubuntu Pro advertisement in `apt` output (disable with `pro config set apt_news=false`); snap store telemetry (minimal); Canonical's 2012 Amazon search lens is long gone. Firefox snap phones home to Mozilla like any Firefox.
- **Fedora**: proposed opt-in telemetry in 2023 was heavily debated and shipped as opt-in only (Fedora 40+ asks once, default off). Countme (a privacy-preserving mirror-hit counter) is on.
- **Everyone else**: essentially nothing. Debian's `popularity-contest` is opt-in. Arch counts nothing. NixOS nothing.
- **Applications** are another matter: VS Code, JetBrains, Chrome, Discord, Spotify, Steam collect what they collect on any OS. VSCodium, Firefox with tweaks, and Flatpak permissions can limit some of it.
- **DNS**: use DNS-over-TLS/HTTPS via `systemd-resolved` (`DNSOverTLS=yes`) or the browser's built-in DoH.
- **MAC randomisation** for WiFi: NetworkManager supports per-network random MACs (`wifi.cloned-mac-address=random`/`stable`); GNOME/KDE expose it in the connection editor.
- **Location services**: GNOME uses Mozilla Location Service's successor (BeaconDB); off by default on most distros.

## 14.9 Update discipline

The single biggest determinant of security *and* stability over time is how you update. By release model:

**Point release (Ubuntu, Mint, Debian, Fedora):**
- Enable automatic security updates: Ubuntu/Debian `unattended-upgrades` (Ubuntu enables it by default for security), Fedora `dnf-automatic` (or GNOME Software's auto-updates), Mint's Update Manager auto-update option.
- Apply everything else weekly. Reboot when the kernel updates (Ubuntu Pro's Livepatch defers this).
- Do the major upgrade within a few months of release (Fedora) or within a year (Ubuntu LTS→LTS), during a break, after a backup.

**Rolling (Arch, Tumbleweed, EndeavourOS, CachyOS):**
- Update **at least weekly**; daily is fine. Long gaps (months) cause keyring and partial-upgrade problems.
- **Read the news** (Arch: `informant` package; openSUSE: the factory mailing list is optional — openQA does the worrying).
- **Never partial-upgrade** on Arch (`pacman -Sy foo` without `-u` is the classic footgun; always `-Syu`).
- **Handle `.pacnew`/`.rpmnew` files** (`pacdiff`, `rpmconf`).
- Keep an **LTS kernel installed** as a fallback (`linux-lts` on Arch).
- Have **snapshots** (Snapper/Timeshift) taken before each update — CachyOS/openSUSE do this automatically; on Arch, `snap-pac` hooks it into pacman.
- **Don't update in the 48 hours before a deadline or demo.** This rule alone eliminates most rolling-release horror stories.

**Atomic (Universal Blue, Silverblue, Aeon):**
- Updates are automatic and staged; you reboot when convenient. There is nothing to do. If an update misbehaves, boot the previous deployment (`rpm-ostree rollback` / `bootc rollback` to make it stick).

**Declarative (NixOS):**
- `nixos-rebuild switch --upgrade` when you like. Roll back by booting a previous generation. Run `nix-collect-garbage --delete-older-than 30d` periodically or the store grows unboundedly.

**Everything:**
- **Flatpaks**: `flatpak update` weekly or let GNOME Software/Discover do it automatically.
- **Firmware**: `fwupdmgr refresh && fwupdmgr update` monthly, or via GNOME Software/Discover.
- **Language toolchains and Homebrew**: on your own schedule; these don't affect system stability.

## 14.10 Backups

Everyone agrees backups matter; almost nobody does them until after the first loss. A Linux laptop makes it easy.

**Three kinds of "backup," all needed:**

1. **System snapshots** (undo a bad update in 30 seconds): **Btrfs + Snapper** (openSUSE default; CachyOS default; Fedora with `snapper` + `btrfs-assistant`; Arch with `snap-pac` + `grub-btrfs`) or **Timeshift** (Mint default; works on ext4 via rsync or Btrfs). Atomic distros have this built in. **Not a backup** — same disk, same failure domain — but the most-used safety net.
2. **Data backups** (your files survive the disk dying or the laptop being stolen): **Pika Backup** or **Déjà Dup** (GNOME; Borg/Duplicity underneath; point at an external drive or cloud), **Kup** (KDE), or the CLI kings **`restic`** and **`borg`** (deduplicated, encrypted, incremental, to any destination — external disk, NAS, S3/B2/any cloud via `rclone`). Schedule with a systemd timer. `restic` + Backblaze B2 costs a few dollars a month for a typical home directory. **Vorta** is a GUI for Borg.
3. **Configuration in git** (rebuild the machine from scratch in an hour): dotfiles via chezmoi/stow (Chapter 11); a list of installed packages (`pacman -Qqe > pkglist.txt`, `dnf repoquery --userinstalled`, `apt-mark showmanual`, `flatpak list --app --columns=application`) committed alongside; on NixOS, the config *is* this.

**Test a restore** once. A backup you've never restored from is a hope, not a backup.

**Don't back up:** `~/.cache`, `node_modules`, `.venv`, build directories, browser caches, Steam libraries (re-downloadable). Every backup tool has an exclude list; use it.

**Sync ≠ backup.** Dropbox/OneDrive/Nextcloud/Syncthing propagate deletions and ransomware. They're convenient and worth having; they don't replace versioned backups (though some offer file version history).

## 14.11 Long-term health: the yearly checklist

Once a year — during a semester break or a quiet week — spend an hour:

- [ ] **Firmware**: `fwupdmgr update`; check the vendor site if not on LVFS.
- [ ] **Major upgrade** if on a point release and one is due (Fedora N→N+1, Ubuntu LTS if new LTS is out and .1 has shipped).
- [ ] **Orphaned packages**: `pacman -Qdt`, `dnf autoremove`, `apt autoremove`, `flatpak uninstall --unused`, `nix-collect-garbage -d`.
- [ ] **Disk hygiene**: `journalctl --vacuum-time=4weeks`; check `~/.cache` size; `docker system prune`; old kernels (Ubuntu/Fedora keep 2–3 automatically).
- [ ] **Snapshot pruning**: verify Snapper/Timeshift retention isn't filling the disk.
- [ ] **Backup restore test**: pull one file back from `restic`/Borg.
- [ ] **Secrets rotation**: SSH keys if old; password manager audit; revoke tokens you don't use.
- [ ] **Extensions/plugins audit**: remove GNOME/KDE extensions, browser extensions, editor plugins you don't use.
- [ ] **Review Flatpak permissions** in Flatseal.
- [ ] **Battery health**: `upower -i /org/freedesktop/UPower/devices/battery_BAT0` — check capacity; set charge thresholds if the laptop supports them (ThinkPads, Framework, ASUS via `tlp`/`power-profiles-daemon`/sysfs).
- [ ] **Read your distro's release notes** for the past year — there's usually one thing you didn't know had changed.

Do this and a Linux install lasts the life of the hardware. Machines running the same Arch install for a decade, or Ubuntu upgraded LTS-to-LTS since 2012, are common and unremarkable.

## 14.12 When things break: a triage order

1. **Can you boot?** If not: previous kernel from the boot menu → snapshot/previous deployment from the boot menu → live USB, mount, `chroot`, fix (ArchWiki "General troubleshooting" applies to every distro).
2. **Boots but no graphics?** Almost always a GPU driver vs. kernel mismatch (NVIDIA) — boot the LTS/previous kernel, or `Ctrl+Alt+F3` to a TTY and rebuild/reinstall the driver.
3. **Boots, graphics, but the desktop is wrong?** Check `journalctl -b -p err`; a GNOME extension or Plasma widget is the usual suspect (disable them; `dconf reset -f /org/gnome/shell/` in extremis).
4. **A specific app is wrong?** Run it from a terminal and read the output; check Flatpak permissions; search the exact error with your distro's name.
5. **Something's slow or hot?** `btop`/`htop`, `powertop`, `journalctl` for a stuck service, `systemd-analyze blame` for boot.
6. **Still stuck?** Your distro's forum/Discourse/Matrix with: distro+version, DE, GPU, the exact command, the exact error, what you tried. The ArchWiki and Ask Fedora answer most things regardless of your distro.

---

### Key takeaways

- **Full-disk encryption at install time is non-negotiable for a laptop.** TPM auto-unlock (Ubuntu 26.04 installer; `systemd-cryptenroll` elsewhere) is convenient — keep a recovery key.
- Keep **Secure Boot** on where the distro supports it (all mainstream except Arch-family/Pop!_OS, which need `sbctl` or disabling); sign third-party modules via MOK.
- SELinux vs AppArmor doesn't matter; leave whichever you have on. **Enable the firewall** — Ubuntu/Mint/Debian/Arch ship it off.
- **Flatpak sandboxing + Flatseal** is your app-level defence; vendor binaries and AppImages run unconfined. Trust official repos > Flathub > AUR/PPA/COPR > random `curl | sh`.
- Linux is private by default; Ubuntu and Fedora's telemetry is opt-in or trivially disabled.
- **Update discipline by model:** auto-security + weekly on point releases; weekly + read-the-news + snapshots + no-updates-before-deadlines on rolling; nothing on atomic; `nixos-rebuild` + garbage-collect on NixOS.
- **Three backup layers:** snapshots (Snapper/Timeshift/atomic) for undo; `restic`/Borg/Pika to an external or cloud target for data; dotfiles + package list in git for rebuild. Test a restore.
- A yearly hour of maintenance keeps an install healthy for the life of the hardware.


---

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


---

# Chapter 16 — Post-Install Playbook

You've chosen. Here's how to go from a fresh install to a machine you trust, in roughly an hour, for each of the top picks. Commands are current as of September 2026; if one fails, the distro's own post-install docs will have the updated form.

## 16.1 Before you install (all distros)

1. **Back up** anything on the target disk. Obviously. Especially if dual-booting.
2. **Update the firmware** from the existing OS (Windows vendor tool, or LVFS from a Linux live USB) — BIOS/UEFI, SSD firmware, Thunderbolt.
3. **Firmware settings:** Secure Boot on (unless Arch-family/Pop!_OS and you don't want to enrol keys); SATA/NVMe mode = AHCI (not RAID/VMD/RST); TPM enabled; Fast Boot off (it can skip USB device init); if dual-booting, **disable Windows Fast Startup** and, if BitLocker is on, **suspend or decrypt it and save the recovery key** before touching partitions.
4. **Write the ISO** with **Ventoy** (drop multiple ISOs on one USB, pick at boot — ideal for trying GNOME and KDE), **Fedora Media Writer**, **balenaEtcher**, or `dd`. Rufus works from Windows (use DD mode for Fedora/Arch ISOs).
5. **Boot the live environment and test:** WiFi, display (correct resolution), touchpad, sound, webcam, Bluetooth, sleep/wake (close the lid). Fifteen minutes here beats discovering a dead WiFi card after wiping the disk.
6. **Decide partitioning:** Linux-only → let the installer use the whole disk with LUKS. Dual-boot → shrink Windows from *within Windows* (Disk Management), leave the space unallocated, let the installer use it. Separate `/home` partition is optional (Btrfs subvolumes make it moot; it eases reinstalls on ext4).
7. **Have your passwords ready:** disk passphrase (long), user password, WiFi.

## 16.2 Universal first-hour checklist

Regardless of distro, in this order:

- [ ] **Connect to WiFi and update everything** (the ISO is weeks old). Reboot if the kernel changed.
- [ ] **Confirm encryption** is active: `lsblk` shows a `crypt` device; or `sudo cryptsetup status <name>`.
- [ ] **Enable the firewall** if it's off.
- [ ] **Firmware updates:** `fwupdmgr refresh && fwupdmgr update` (or via GNOME Software/Discover).
- [ ] **Codecs** (Fedora/openSUSE only — see per-distro).
- [ ] **Flathub** if not preconfigured: `flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo`.
- [ ] **Snapshots:** Snapper/Timeshift if not preconfigured (per-distro).
- [ ] **GPU driver** (NVIDIA only — per-distro).
- [ ] **Browser** — the default is fine; add your password manager extension.
- [ ] **Terminal + shell + dotfiles:** clone your dotfiles (`chezmoi init --apply <repo>`), or start one.
- [ ] **Developer basics:** `git`, build tools, `docker`/`podman`, `distrobox`, your language managers (`uv`, `mise`, `rustup`…), your editor.
- [ ] **Backups:** install `restic`/Pika/Déjà Dup, point it at an external disk or cloud, run the first backup, schedule it.
- [ ] **Power:** confirm `power-profiles-daemon` (or TLP, not both); check sleep works and battery drain overnight is acceptable.
- [ ] **Fonts** (if rendering looks thin): `noto-fonts`, `noto-fonts-cjk`, `noto-fonts-emoji`, Liberation, a Nerd Font for the terminal (JetBrainsMono Nerd Font is the popular one).
- [ ] **Bluetooth**: pair your devices; confirm codec (`pactl list sinks | grep -i codec`).
- [ ] **Printer**: add via Settings; confirm a test page.
- [ ] **Write down**: LUKS recovery key, MOK password (if any), and where your backups live.

## 16.3 Fedora Workstation / Fedora KDE Plasma Desktop

```bash
# 1. Update
sudo dnf upgrade --refresh -y && systemctl reboot

# 2. RPM Fusion (free + nonfree) — enables codecs, NVIDIA, Steam, etc.
sudo dnf install -y \
  https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
  https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1   # dnf5 syntax

# 3. Codecs: full ffmpeg + hardware decode
sudo dnf swap -y ffmpeg-free ffmpeg --allowerasing
sudo dnf update -y @multimedia --setopt="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
# AMD:   sudo dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld && sudo dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld
# Intel: sudo dnf install -y intel-media-driver     (Broadwell+; libva-intel-driver for older)
# NVIDIA (below) provides its own VA-API via libva-nvidia-driver

# 4. NVIDIA (Turing+; skip if AMD/Intel)
sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda libva-nvidia-driver
# Wait ~5 min for the akmod to build: watch with `sudo akmods --force && modinfo -F version nvidia`
# Secure Boot: one-time key enrolment before reboot:
sudo dnf install -y kmodtool akmods mokutil openssl && sudo kmodgenca -a && sudo mokutil --import /etc/pki/akmods/certs/public_key.der
# (set a password; on reboot choose "Enroll MOK" in the blue screen)

# 5. Flathub is preconfigured since F38; verify:
flatpak remotes    # should show flathub. If only "fedora": flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# 6. Snapshots (Btrfs is default; Snapper is not)
sudo dnf install -y snapper btrfs-assistant python3-dnf-plugin-snapper
sudo snapper -c root create-config /
sudo snapper -c home create-config /home
# btrfs-assistant GUI to set retention; dnf snapper plugin snapshots before/after each transaction

# 7. Dev basics
sudo dnf install -y git gcc gcc-c++ make cmake clang podman podman-compose distrobox toolbox
sudo dnf group install -y development-tools
# Docker instead of / alongside Podman: follow docs.docker.com/engine/install/fedora
# VS Code: import Microsoft's key + repo per code.visualstudio.com/docs/setup/linux, then dnf install code

# 8. Nice-to-haves
sudo dnf install -y gnome-tweaks   # GNOME; or on KDE nothing needed
# Firmware
fwupdmgr refresh && fwupdmgr update
```

**Fedora-specific notes.** Twice-yearly upgrade: `sudo dnf system-upgrade download --releasever=45 && sudo dnf system-upgrade reboot` (or GNOME Software/Discover's prompt). Hostname: `hostnamectl set-hostname mybox`. `firewalld` is on; `firewall-config` is the GUI. SELinux denials: `sudo dnf install setroubleshoot` for desktop alerts. Fedora's own Flatpak remote can shadow Flathub for some apps — prefer Flathub in GNOME Software's source dropdown, or `flatpak remote-modify --disable fedora` if it annoys you.

## 16.4 Ubuntu 26.04 LTS / Kubuntu 26.04 LTS

```bash
# 1. Update
sudo apt update && sudo apt full-upgrade -y && systemctl reboot

# 2. Codecs (if you didn't tick "Install third-party software")
sudo apt install -y ubuntu-restricted-extras   # accepts the MS fonts EULA
# Kubuntu: kubuntu-restricted-extras

# 3. NVIDIA (skip if AMD/Intel)
sudo ubuntu-drivers install            # picks the recommended pre-built, signed driver
# or: sudo ubuntu-drivers list ; sudo apt install nvidia-driver-590-open (or current)
# Secure Boot: you'll be asked to set a MOK password; on reboot choose "Enroll MOK"
# CUDA users: PyTorch via uv with a cuXXX wheel index — no system toolkit needed unless compiling CUDA C++

# 4. Firewall
sudo ufw enable

# 5. Flatpak + Flathub (Ubuntu ships snap only)
sudo apt install -y flatpak gnome-software-plugin-flatpak    # or plasma-discover-backend-flatpak on Kubuntu
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# 5b. OPTIONAL: remove snaps entirely (only if you've decided you want to)
#   snap list ; sudo snap remove --purge <each>, firefox/thunderbird/snap-store/gtk-common-themes/gnome-*/bare/core*/snapd
#   sudo apt purge -y snapd && sudo apt-mark hold snapd
#   Firefox from Mozilla's apt repo: see support.mozilla.org "Install Firefox on Linux" (adds packages.mozilla.org)
#   Pin apt to prefer the deb over the snap transitional package.

# 6. Snapshots (ext4 default → Timeshift rsync; or choose Btrfs at install → Timeshift btrfs mode)
sudo apt install -y timeshift
# Launch Timeshift, pick RSYNC (ext4) or BTRFS, schedule daily + on-boot; exclude /home if you back it up separately

# 7. Dev basics
sudo apt install -y git build-essential cmake clang curl wget gnupg ca-certificates \
  podman podman-compose distrobox
# Docker: follow docs.docker.com/engine/install/ubuntu (adds Docker's apt repo), then sudo usermod -aG docker $USER
# VS Code: Microsoft's apt repo per code.visualstudio.com/docs/setup/linux ; sudo apt install code

# 8. Quality of life
pro config set apt_news=false          # silence the Ubuntu Pro advert in apt output
sudo apt install -y gnome-shell-extension-manager   # GNOME: manage extensions
fwupdmgr refresh && fwupdmgr update
```

**Ubuntu-specific notes.** TPM-backed FDE was an installer option; if you chose passphrase and want TPM later, Ubuntu's docs cover `snap install --classic` of the FDE tooling — or use `systemd-cryptenroll` manually. Ubuntu Pro (free for 5 personal machines): `sudo pro attach <token>` for 10-year `universe` security coverage and Livepatch. Unattended security upgrades are on by default. HWE kernels arrive automatically for the Desktop image (`linux-generic-hwe-26.04`). LTS→LTS upgrade in 2028: `do-release-upgrade` after 28.04.1 ships. AppArmor userns restriction breaking an app: `sudo aa-status`, and either a profile in `/etc/apparmor.d/` or `sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0` (less secure).

## 16.5 Arch Linux / EndeavourOS / CachyOS

EndeavourOS and CachyOS installers do most of this; the notes tell you what to verify.

```bash
# 0. (Vanilla Arch) Install with archinstall or the wiki. Choose: Btrfs, LUKS, systemd-boot or GRUB,
#    a desktop profile, NetworkManager, pipewire. Add `linux-lts` as a second kernel.

# 1. Update, then mirrors
sudo pacman -Syu
sudo pacman -S reflector && sudo reflector --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
# (EndeavourOS: eos-rankmirrors / Welcome app; CachyOS: cachyos-rate-mirrors)

# 2. AUR helper (EndeavourOS ships yay; CachyOS ships paru)
sudo pacman -S --needed base-devel git && git clone https://aur.archlinux.org/paru.git && cd paru && makepkg -si && cd ..

# 3. Read-the-news enforcement
paru -S informant        # blocks pacman -Syu until you've read unread Arch news

# 4. Essentials often missing on vanilla Arch
sudo pacman -S --needed noto-fonts noto-fonts-cjk noto-fonts-emoji ttf-liberation ttf-jetbrains-mono-nerd \
  cups cups-pdf system-config-printer bluez bluez-utils \
  power-profiles-daemon firewalld flatpak xdg-desktop-portal-gtk \
  pacman-contrib pkgfile fwupd
sudo systemctl enable --now cups bluetooth power-profiles-daemon firewalld fwupd-refresh.timer
# GNOME: xdg-desktop-portal-gnome ; KDE: xdg-desktop-portal-kde (usually pulled in by the DE group)

# 5. Snapshots (Btrfs assumed)
sudo pacman -S snapper snap-pac grub-btrfs btrfs-assistant inotify-tools   # grub-btrfs only if using GRUB
sudo snapper -c root create-config /
sudo systemctl enable --now snapper-timeline.timer snapper-cleanup.timer grub-btrfsd
# CachyOS: already configured; verify with `snapper list`

# 6. NVIDIA (Turing+)
sudo pacman -S nvidia-open nvidia-utils lib32-nvidia-utils nvidia-settings libva-nvidia-driver
sudo pacman -S linux-lts nvidia-lts-open      # fallback kernel + matching driver
# Pascal/older: paru -S nvidia-580xx-dkms nvidia-580xx-utils
sudo systemctl enable nvidia-suspend nvidia-hibernate nvidia-resume
# Secure Boot (optional): sudo pacman -S sbctl ; sbctl create-keys ; sbctl enroll-keys -m ; sbctl sign -s <efi files> ; see wiki

# 7. Gaming (optional): enable [multilib] in /etc/pacman.conf, then
sudo pacman -Syu steam gamemode mangohud lib32-mesa   # lib32-nvidia-utils if NVIDIA

# 8. Dev basics
sudo pacman -S --needed git base-devel cmake clang docker docker-compose distrobox podman
sudo systemctl enable --now docker && sudo usermod -aG docker $USER
paru -S visual-studio-code-bin        # or `code` (OSS build) from extra

# 9. Flathub
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# 10. Maintenance hooks
paru -S pacman-cleanup-hook            # or manual: paccache -rk2 weekly
# Check .pacnew after updates: sudo pacdiff  (set DIFFPROG=meld or vimdiff)
```

**Arch-family notes.** `paru -Syu` weekly minimum. Before big updates check archlinux.org/news (informant enforces it). If boot fails after an update: choose the LTS kernel or a Snapper snapshot from the boot menu. CachyOS-specific: `cachyos-hello` for one-click tasks; `linux-cachyos` is default with `linux-cachyos-lts` as fallback; `chwd` handles GPU drivers. EndeavourOS-specific: the Welcome app's "After Install" tab covers mirrors, drivers and package cleanup; `eos-update` wraps `yay -Syu` with keyring refresh.

## 16.6 Bluefin / Aurora / Bazzite (Universal Blue)

There's almost nothing to do; that's the point.

```bash
# 1. Let it update (it already started in the background). Reboot once.
ujust update             # force image + Flatpak + Homebrew update if impatient

# 2. Codecs, NVIDIA, Flathub, firewall, fwupd, Homebrew: already done by the image.
#    Wrong variant (want NVIDIA or DX)? Rebase — one command, one reboot:
sudo bootc switch ghcr.io/ublue-os/bluefin-dx-nvidia:stable      # or aurora-dx, bazzite-nvidia, etc.
# (or: ujust rebase-helper — interactive)

# 3. Secure Boot key (if you see a MOK prompt or the NVIDIA module won't load)
ujust enroll-secure-boot-key      # password is "universalblue"

# 4. Developer mode (non-DX → DX)
ujust devmode                     # or rebase to the -dx image

# 5. Distroboxes for host-style package management
ujust distrobox                   # interactive: Ubuntu / Arch / Fedora / Alpine boxes
distrobox enter ubuntu            # then apt install whatever; distrobox-export --app <name> adds it to the host menu

# 6. CLI tools via Homebrew (preinstalled)
brew install ripgrep fd bat eza zoxide fzf lazygit gh mise uv

# 7. Layering (last resort; slows updates): rpm-ostree install <pkg> → reboot
#    Prefer: Flatpak (GUI), brew (CLI), Distrobox (everything else)

# 8. Browse recipes:
ujust --choose                    # Steam, Tailscale, virtualization, fingerprint, CLI box, auto-update toggles…

# 9. Snapshots / rollback: built in
rpm-ostree status                 # deployments; the previous one is bootable from the boot menu
sudo bootc rollback               # make the previous deployment default
```

**UBlue notes.** Automatic updates run daily; you boot into them at next restart. Recipes live in `/usr/share/ublue-os/just/`. GNOME extensions come preconfigured on Bluefin. VS Code (DX) is in the image with Dev Containers; open a repo with `.devcontainer/` and it builds in Podman. Bazzite: `ujust` recipes for Decky, EmuDeck, Sunshine, handheld tweaks; "Bazzite Portal" runs at first boot.

## 16.7 openSUSE Tumbleweed

```bash
# 1. Update (dup, not up, on Tumbleweed)
sudo zypper ref && sudo zypper dup -y && systemctl reboot

# 2. Codecs via Packman — one command
sudo zypper in opi && opi codecs

# 3. NVIDIA — official repo, pre-built kmp
sudo zypper addrepo --refresh https://download.nvidia.com/opensuse/tumbleweed NVIDIA
sudo zypper in-pattern nvidia-open-driver-G06-kmp   # Turing+
# Secure Boot: the installer creates a MOK; enrol on first reboot if prompted

# 4. Flathub
sudo zypper in flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# 5. Snapshots: Snapper preconfigured with pre/post zypper snapshots + GRUB boot entries. Verify:
sudo snapper list
# Rollback from a booted snapshot: sudo snapper rollback && reboot

# 6. Dev basics
sudo zypper in -t pattern devel_basis devel_C_C++
sudo zypper in git cmake clang podman distrobox docker docker-compose
sudo systemctl enable --now docker && sudo usermod -aG docker $USER
# VS Code: Microsoft's rpm repo (same key as Fedora); zypper in code

# 7. opi for anything else (OBS search + install, popular proprietary apps)
opi vscode ; opi chrome ; opi steam ; opi msfonts
```

**Tumbleweed notes.** `zypper dup` weekly. If the NVIDIA kmp lags a kernel bump, `dup` shows a conflict — wait a day or two rather than forcing. `firewalld` is on. SELinux is default since 2025. YaST is present but deprecated; Myrlyn is the package GUI, Cockpit for admin. Slowroll: identical steps with Slowroll repos.

## 16.8 NixOS 26.05

The playbook is a configuration file. A minimal, opinionated starting point after the graphical installer generates `/etc/nixos/configuration.nix`:

```nix
{ config, pkgs, ... }:
{
  imports = [ ./hardware-configuration.nix ];

  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;
  boot.kernelPackages = pkgs.linuxPackages_latest;   # or leave the default LTS

  networking.hostName = "laptop";
  networking.networkmanager.enable = true;
  networking.firewall.enable = true;
  time.timeZone = "Europe/Berlin";

  # Desktop: pick one
  services.xserver.enable = true;
  services.displayManager.gdm.enable = true;
  services.desktopManager.gnome.enable = true;
  # services.displayManager.sddm = { enable = true; wayland.enable = true; };
  # services.desktopManager.plasma6.enable = true;

  services.pipewire = { enable = true; alsa.enable = true; pulse.enable = true; };
  hardware.bluetooth.enable = true;
  services.printing.enable = true;
  services.fwupd.enable = true;
  services.flatpak.enable = true;
  hardware.enableRedistributableFirmware = true;

  # NVIDIA (Turing+):
  # services.xserver.videoDrivers = [ "nvidia" ];
  # hardware.nvidia = { open = true; modesetting.enable = true; powerManagement.enable = true; };

  nix.settings.experimental-features = [ "nix-command" "flakes" ];
  nix.gc = { automatic = true; dates = "weekly"; options = "--delete-older-than 30d"; };

  programs.nix-ld.enable = true;   # run non-Nix binaries (VS Code server, downloaded tools)
  virtualisation.podman = { enable = true; dockerCompat = true; };

  users.users.me = {
    isNormalUser = true;
    extraGroups = [ "wheel" "networkmanager" "video" "kvm" "libvirtd" ];
    shell = pkgs.fish;
  };
  programs.fish.enable = true;

  environment.systemPackages = with pkgs; [
    git vim wget curl ripgrep fd bat eza fzf zoxide
    gcc gnumake cmake clang distrobox vscode firefox
  ];
  fonts.packages = with pkgs; [ noto-fonts noto-fonts-cjk-sans noto-fonts-color-emoji liberation_ttf nerd-fonts.jetbrains-mono ];

  system.stateVersion = "26.05";
}
```

Then `sudo nixos-rebuild switch`. Next: move to a **flake**, add **Home Manager** for dotfiles and user packages, pull in **nixos-hardware** for your laptop model, keep it all in git. Use `nix develop`/`direnv` for per-project toolchains rather than global packages. Undo: `nixos-rebuild switch --rollback` or the boot menu.

## 16.9 Linux Mint

```bash
# 1. Welcome screen → First Steps: Timeshift (RSYNC on ext4; daily + boot), Driver Manager (NVIDIA/Broadcom),
#    Update Manager (refresh, install all; optional auto-updates), Firewall (enable).
sudo apt update && sudo apt full-upgrade -y

# 2. Codecs (if not chosen at install)
sudo apt install -y mint-meta-codecs

# 3. Flathub is preconfigured; Software Manager shows Flatpaks alongside debs.

# 4. Dev basics
sudo apt install -y git build-essential cmake clang curl podman distrobox
# Docker / VS Code: vendor repos, as for Ubuntu. Prefer Microsoft's .deb over the Flatpak.

# 5. Cinnamon Wayland session (22.3+/23): choose at the login screen to try it.
```

**Mint notes.** Snaps are blocked via `/etc/apt/preferences.d/nosnap.pref` — delete it if you want them. Update Manager → View → Linux Kernels for HWE kernels. `mintupgrade` for 22→23 in 2027.

## 16.10 Dual-boot with Windows: the short version

1. **In Windows:** disable Fast Startup (Power Options → "Choose what the power buttons do"); if BitLocker is on, save the recovery key and suspend it; shrink `C:` in Disk Management to free ≥ 100 GB.
2. **Firmware:** Secure Boot can stay on for Ubuntu/Fedora/Mint/openSUSE/UBlue; AHCI mode.
3. **Install Linux** into the free space; the installer detects Windows and adds a boot entry (GRUB), or you use the firmware boot menu (systemd-boot detects Windows on the same ESP; Pop!_OS/Arch may need `os-prober` or a manual entry).
4. **Post-install:** set Linux first in the firmware boot order (Windows updates sometimes reset it — `efibootmgr -o` fixes it from Linux). Fix the clock disagreement: `timedatectl set-local-rtc 1` on Linux.
5. **Shared data:** a separate NTFS/exFAT partition, or read-write access to the Windows partition from Linux (safe *only* with Fast Startup off and Windows fully shut down). Don't write to Linux partitions from Windows.
6. Windows may re-arm BitLocker or reset boot order after major updates; keep the recovery key handy.

Separate physical disks for each OS sidestep most of this.

---

### Key takeaways

- **Before install:** firmware update, AHCI mode, Fast Startup off, BitLocker suspended, live-USB hardware test.
- **First hour, every distro:** update, verify encryption, firewall, fwupd, codecs (Fedora/openSUSE), Flathub, snapshots, GPU driver, dotfiles, dev basics, **first backup**.
- **Fedora:** RPM Fusion → `ffmpeg` swap → `akmod-nvidia` if needed → Snapper. **Ubuntu:** `ubuntu-drivers`, `ufw enable`, Flatpak, Timeshift; snaps removable in ten minutes. **Arch-family:** `informant`, fonts/CUPS/portal essentials, Snapper + `snap-pac`, `nvidia-open` + LTS fallback. **Universal Blue:** nothing — `ujust` for extras, `bootc switch` to change variant. **Tumbleweed:** `opi codecs`, NVIDIA repo, Snapper already done. **NixOS:** a 60-line `configuration.nix` gets you a full desktop; add flakes + Home Manager next. **Mint:** the Welcome screen does it.
- **Dual boot:** Fast Startup off, BitLocker key saved, shrink from Windows, `set-local-rtc 1`, watch boot order after Windows updates.


---

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


---

# Chapter 18 — Conclusion

Sixty thousand words ago I promised not to declare a single winner, and I've kept that promise — but not because there's no answer. There is one; it just has a shape rather than a name.

## What the evidence says

**The distribution matters less than you were told, and differently.** For the *work* — compilers, containers, editors, languages — it barely matters at all. Version managers, Homebrew, Distrobox, devcontainers and Flatpak have made every mainstream distro an equally good host for your toolchain. Anyone who tells you that you need distro X "for programming" is describing 2014.

Where the distribution *does* matter is in four places: **whether your hardware works** (kernel currency, and whether NVIDIA's module is pre-built or left to you); **what happens when an update goes wrong** (nothing, a 30-second rollback, or an afternoon); **how much of the world assumes you're running it** (vendor packages, tutorials, university labs, employer IT); and **how the desktop feels for eight hours a day** — which is really a question about GNOME vs. KDE, not about the distro at all.

**The mainstream choices have converged.** Under any reasonable weighting of the criteria that matter to a software engineer, a CS student, or a person who wants one machine for everything, the top handful — Fedora, Ubuntu LTS, Universal Blue's Bluefin/Aurora/Bazzite, openSUSE Tumbleweed — land within a few tenths of a point of each other. They are *all excellent*. The internet's endless arguments about them are arguments about weights, not about quality.

**Your situation moves the ranking more than distro quality does.** An NVIDIA GPU, a CUDA requirement, a heavy semester, an OS course, a university mandate, an Apple Silicon Mac, a proctoring requirement — each of these reorders the top of the list more than any distro's engineering does. Which is why the decision tree in Chapter 15 asks about *you* first and distros last.

**Two things constrain students more than any distro choice**, and neither is Linux's fault: proctoring software that only runs on Windows and macOS, and the need to match a department's Ubuntu toolchain. Plan for the first with a dual-boot or a second device; solve the second with a Distrobox or by simply running Ubuntu.

**The atomic desktops are the most important new development in years.** Universal Blue's images deliver what the Linux desktop has promised for decades — a system that updates itself and never breaks — with Fedora's currency underneath and the proprietary bits already baked in. Their one real cost is friction for host-level hacking. For the large majority of developers whose work lives in containers, that cost is zero.

**NixOS is the other frontier**, for a different temperament: total reproducibility at the price of a language and a non-standard filesystem. It rewards the people who make it through the curve more than any other distro rewards anyone; it punishes the people who don't more than any other distro punishes anyone. Try Nix first.

**Arch remains what it has always been:** the best Linux for people who enjoy administering a Linux, and a mistake for people who don't. EndeavourOS and CachyOS have made it far more approachable without changing that fundamental fact.

## The shape of the answer

If you've read the whole guide and want it in one paragraph:

> Run **Fedora** (Workstation or KDE — try both live) on a modern AMD or Intel machine. Run **Ubuntu 26.04 LTS** if you have NVIDIA, need CUDA, have a mandate, or want five years of quiet. Run **Bluefin DX or Aurora DX** if you never want to maintain anything and your work lives in containers — or **Bazzite** if you also game. Run **CachyOS or EndeavourOS** if you want the newest everything and enjoy the work. Run **Linux Mint** if you're installing for a newcomer or want a computer that feels like it did in 2015, in the best way. Run **Fedora Asahi Remix** on an M1/M2 Mac. Whatever you pick: encrypt the disk, turn on the firewall, set up snapshots, put your dotfiles in git, take a backup, and then **stop thinking about the distro and go build things.**

## A last word on the argument itself

The Linux community's fondness for distro debate is a sign of health — it means people care, and it means there are real choices, which no other desktop platform offers. But it has a cost: it convinces newcomers that the choice is high-stakes and permanent, when it is neither. Switching costs an afternoon. Every one of the top options will serve you for years. The only genuinely bad outcome is the one where a newcomer picks something ill-suited, has a miserable first month, and concludes that Linux itself is the problem.

So: use the framework, pick something from the top of the table that matches your hardware and temperament, commit to it for a semester, fix things in place when they break, and revisit the question only when your *situation* changes. The distro is the floor you stand on. Build on it.

---

*This guide is dated September 2026. Kernel versions, driver states, and "what's broken this month" will drift; the reasoning is built to outlast them. If you find an error or a change worth recording, open an issue or a pull request — the source is a set of Markdown files in a git repository, which is, after all, the point.*


---

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


---

# Appendix B — Sources and Further Reading

Facts in this guide were checked against the sources below during September 2026. Where a claim is a judgement rather than a fact, it's marked as such in the text. Raw research notes with dates are in `research/` in this repository.

## Primary sources consulted for 2026 facts

**Kernel**
- kernel.org release table (7.2.3 stable, 6.18 LTS, 2026-09-02).
- Phoronix, "Linux 7.1 Released" (June 2026); LWN stable-kernel announcements.
- LWN, "Bcachefs removed from the mainline kernel" (September 2025).

**Ubuntu**
- Ubuntu 26.04 LTS release notes — documentation.ubuntu.com/release-notes/26.04/
- Canonical blog, "Canonical releases Ubuntu 26.04 LTS Resolute Raccoon" (April 2026).
- It's FOSS, "Ubuntu 26.04 LTS Releases Today: Check New Features" (April 2026) — TPM FDE, sudo-rs, uutils, APT 3.2, Ptyxis, amd64v3, ROCm, flavour LTS status.
- Ubuntu Discourse, "Ubuntu 26.04 LTS — The Roadmap"; "Introducing architecture variants: amd64v3".
- OMG! Ubuntu, "Two Ubuntu Flavours Won't Be LTS Releases Next Year" (December 2025).

**Fedora**
- Fedora Project Wiki, Releases/44/ChangeSet; Fedora Magazine release announcements and "What's New in Fedora Workstation 44" (April 2026).
- Fedora Discussion, "Fedora 44 release date" (slips to 2026-04-28).
- Fedora Docs, "Framework" hardware page.

**Debian**
- Debian 13 "Trixie" release notes — debian.org/releases/trixie/ (August 2025).
- 9to5Linux, "Debian 13 Trixie Is Now Available for Download".

**Linux Mint**
- Linux Mint monthly news (June/July 2026) via It's FOSS "Linux Mint Now Considers Wayland Stable" and OMG! Ubuntu "Linux Mint 23 to offer full Wayland support"; Phoronix "Linux Mint 23 Making Progress On Ubuntu 26.04 Base" (Christmas 2026 target).

**Pop!_OS / COSMIC**
- System76 blog, "The Latest Updates to COSMIC Epoch 1" (Epoch 1 released 2025-12-11); COSMIC 1.7.0 (August 2026) per Wikipedia's COSMIC article; System76 blog COSMIC 1.0.8 (February 2026).

**KDE**
- KDE announcements: Plasma 6.6 (2026-02-17), 6.7 (2026-07-14); KDE blog "Going all-in on a Wayland future" (X11 session removal in 6.8, November 2025); "Bullet-proof KDE" Plasma 6.6 LTS until 2029 (August 2026).

**GNOME**
- GNOME 50 release notes (March 2026) — X11 session removal, VRR/fractional scaling stable, Orca overhaul.

**NixOS**
- nixos.org blog, "NixOS 26.05 released" (2026-05-30; support to 2026-12-31); NixOS Discourse release retrospective.

**openSUSE**
- openSUSE forums and LWN "The last of YaST?" (May 2025); computingforgeeks "What's New in openSUSE Leap 16" (SLE 16 rebase, YaST retirement, SELinux default); openSUSE Reddit/forum threads on Tumbleweed YaST deprecation (2026).

**Arch**
- Arch Linux news: "NVIDIA 590 driver drops Pascal and lower support / switch to -open" (December 2025); Phoronix "Arch Linux's Main NVIDIA Driver Packages Now Using The Open Kernel Modules"; 9to5Linux "Archinstall 4.0 … 4.1 removed NVIDIA proprietary option" (March 2026); ArchWiki NVIDIA page.

**CachyOS**
- DistroWatch CachyOS page and ratings; Linuxiac "CachyOS Topped DistroWatch's Rankings" (August 2025); The Register (August 2025); How-To Geek "I tested the top 5 Linux distros on DistroWatch" (July 2026).

**NVIDIA**
- NVIDIA Developer Forums, 590 release feedback threads; 9to5Linux "NVIDIA 590 Linux Graphics Driver Released with More Wayland Improvements" (December 2025); NVIDIA driver installation guide (open kernel modules default since 560).

**Apple Silicon**
- asahilinux.org progress reports: Linux 6.19 (February 2026 — USB-C DP, M3 strategy), Linux 7.0 (April 2026 — M3 at first-M1-alpha level); Fedora Asahi Remix page (packages upstream in Fedora 44); M4 feature-support page.

**Snapdragon X**
- Phoronix "Snapdragon X Elite Laptop Performance On Linux Ends 2025"; TechPowerUp "Tuxedo Gives Up on Snapdragon X Elite-Powered Linux Laptop" (November 2025); Linaro blog (July 2025); Ubuntu Discourse "Ubuntu on ARM: summer '26 update".

**Universal Blue**
- universal-blue.org; Bluefin docs "Bluefin Spring 2026: Fedora 44" (May 2026); Universal Blue Discourse; Hacker News "Bluefin LTS Is Released" (September 2025); XDA "Universal Blue wants to redefine the entire Linux ecosystem" (February 2026).

**Gaming / Steam**
- Steam Hardware & Software Survey, March–August 2026 (Linux 5.33% record in March; 4.01% July; ~3.6–3.9% August) via GamingOnLinux and Phoronix.

**Proctoring**
- Respondus support, "What are the computer requirements for installations of Respondus LockDown Browser" (July 2026); Wharton/UBC/Ontario Tech student guides ("Linux … not supported"); Proctorio system requirements page.

**Framework**
- 9to5Linux "Framework Announces Framework Laptop 13 Pro" (April 2026); Phoronix "Benchmarking Six Linux Distributions On The Framework Laptop 13 Pro" (August 2026); Framework community WiFi PSA (2025).

## Standing references worth bookmarking

- **ArchWiki** — wiki.archlinux.org. The best Linux documentation in existence; applicable to every distro. Per-laptop pages under "Laptop/<vendor>".
- **Fedora Docs** and **Ask Fedora** — docs.fedoraproject.org, discussion.fedoraproject.org.
- **Ubuntu documentation** — documentation.ubuntu.com; **Ask Ubuntu**.
- **Debian Administrator's Handbook** — debian-handbook.info (free).
- **Gentoo Wiki** — wiki.gentoo.org (excellent even for non-Gentoo users).
- **NixOS manual, wiki.nixos.org, nix.dev, Zero to Nix**.
- **openSUSE Wiki** — en.opensuse.org.
- **Universal Blue docs** — docs.projectbluefin.io, docs.getaurora.dev, docs.bazzite.gg.
- **ProtonDB** — protondb.com; **Are We Anti-Cheat Yet?** — areweanticheatyet.com.
- **linux-hardware.org** — hardware probe database.
- **LVFS** — fwupd.org (which vendors publish firmware).
- **libfprint supported devices** — fprint.freedesktop.org/supported-devices.html.
- **Repology** — repology.org (package versions across distros).
- **pkgs.org** — package name lookup across distros.
- **DistroWatch** — distrowatch.com (for release tracking, not for popularity).
- **Phoronix** — phoronix.com (kernel, driver, and benchmark news).
- **LWN** — lwn.net (the kernel and Linux community's paper of record).
- **It's FOSS**, **OMG! Ubuntu**, **9to5Linux**, **GamingOnLinux** — release and news coverage.
- **Asahi Linux** — asahilinux.org (Apple Silicon status).
- **Flathub** — flathub.org; **Flatseal** for permissions.

## On the scoring model

The weighted scores in Chapter 9 are produced by `build/score.py` in this repository. Criterion scores are the author's judgement informed by the reviews in Chapters 6–8; persona weights derive from Chapter 3's ranked criteria. Both are meant to be edited. Run `python3 build/score.py` to regenerate.

## Licence

The text of this guide is released under **CC BY-SA 4.0**. Distro names and logos belong to their respective projects. No affiliate links; no sponsorship.

