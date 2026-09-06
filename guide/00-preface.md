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
