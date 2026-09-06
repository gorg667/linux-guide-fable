---
title: Home
hide:
  - navigation
---

# Choosing a Linux Distribution

**for software engineering, CS study, and daily life — the definitive, opinionated guide. 2026 edition.**

A very long, very thorough answer to one question:

> *"I'm a software engineer and/or a computer science student, and I want one Linux machine that I can also live on every day. Which distribution should I pick?"*

Nineteen chapters and two appendices, ~62,000 words. Read it front to back, jump straight to the [decision framework](15-decision-framework.md), or take the sixty-second answer below.

<div class="grid cards" markdown>

-   :material-timer-sand:{ .lg .middle } **60 seconds**

    ---

    The short table below, then stop.

-   :material-clock-fast:{ .lg .middle } **15 minutes**

    ---

    [Preface](00-preface.md) → [How to think about it](01-how-to-think-about-the-choice.md) → [Decision framework](15-decision-framework.md)

-   :material-school:{ .lg .middle } **I'm a student**

    ---

    [CS student specifics](12-cs-student-specifics.md) — proctoring, matching the grader, course by course.

-   :material-laptop:{ .lg .middle } **Buying a laptop**

    ---

    [Hardware](10-hardware.md) — GPUs, Apple Silicon, Snapdragon, WiFi, the buying checklist.

-   :material-table-large:{ .lg .middle } **Compare everything**

    ---

    [Comparison matrices](09-comparison-matrices.md) — master fact table and a weighted scoring model you can re-weight.

-   :material-wrench:{ .lg .middle } **Already chose**

    ---

    [Post-install playbook](16-post-install-playbook.md) — first-hour checklists for seven distros.

</div>

## The sixty-second answer

| Your situation | Pick | Why, in one line |
|---|---|---|
| Modern AMD/Intel machine; want current *and* stable | **Fedora Workstation** or **Fedora KDE** | Six-month cadence, current kernel, upstream-first, polished after a two-minute codec step. |
| NVIDIA / CUDA / employer or university mandate / 5+ years of support | **Ubuntu 26.04 LTS** (or **Kubuntu**) | Pre-built signed drivers, TPM disk encryption, the ecosystem everyone assumes. |
| Newcomer; want it to feel like Windows | **Linux Mint** | Best defaults in Linux; Ubuntu base without snaps; Timeshift built in. |
| Newest everything; you enjoy administering | **Arch** via **CachyOS** or **EndeavourOS** | The AUR, the ArchWiki, tuned kernels; attention is the price. |
| Never want to maintain anything; work lives in containers | **Bluefin DX** / **Aurora DX** (or **Bazzite** for gaming) | Fedora Atomic image with everything baked in, automatic updates, guaranteed rollback. |
| Whole machine defined in a text file | **NixOS** | Reproducible everything; steep curve; try Nix on another distro first. |
| Apple Silicon M1/M2 | **Fedora Asahi Remix** | The only serious option; M3 alpha, M4 not yet. |
| Must run proctoring software (LockDown Browser, Proctorio…) | any of the above **plus a Windows fallback** | Nothing runs them on Linux. Plan the dual-boot now. |

## The decision tree

```mermaid
--8<-- "assets/decision-tree.mmd"
```

Full walkthrough with twelve personas in [Chapter 15](15-decision-framework.md).

## What you'll learn

- Why the distro matters *less* than you think for development (containers, version managers and Flatpak flattened the differences) and *more* than you think for hardware and desktop polish.
- The real trade-off under every distro argument — **freshness vs. stability vs. maintenance**, pick two.
- What rolling, LTS, atomic and declarative actually mean on a Tuesday afternoon.
- Why GNOME vs. KDE is a bigger decision than Fedora vs. Ubuntu.
- How NVIDIA, Secure Boot and proctoring software constrain you more than any philosophy does.
- How to set up whatever you pick so it stays reliable for years.

---

*Dated September 2026. Source on [GitHub](https://github.com/gorg667/linux-guide-fable) — corrections welcome. Text licensed CC BY-SA 4.0.*
