# Choosing a Linux Distribution for Software Engineering, CS Study, and Daily Life

**The definitive, opinionated, long-form guide — 2026 edition.**

> Status: **complete first edition** (September 2026) — 19 chapters + 2 appendices, ~62,000 words.
> Read it chapter by chapter below, or as one file: [`guide/FULL_GUIDE.md`](guide/FULL_GUIDE.md).
> Working notes: [`PROGRESS.md`](PROGRESS.md) · outline: [`PLAN.md`](PLAN.md) · research notes: [`research/`](research/) · scoring model: [`build/score.py`](build/score.py).

## What this is

A very long, very thorough essay/review/guide answering one question honestly:

> *"I'm a software engineer and/or a computer science student, and I want one Linux machine that I can also live on every day. Which distribution should I pick?"*

It covers the fundamentals you need to reason about the choice yourself, deep reviews of every distribution that matters, hardware realities, developer workflow, the awkward specifics of being a student (proctoring software, eduroam, coursework toolchains), daily-driver concerns (gaming, video calls, printing), security and maintenance, and finally a concrete decision framework and post-install playbooks.

## The sixty-second answer

| Situation | Pick |
|---|---|
| Modern AMD/Intel machine, want current + stable | **Fedora Workstation** or **Fedora KDE** |
| NVIDIA / CUDA / employer or university mandate / 5+ years support | **Ubuntu 26.04 LTS** (or Kubuntu) |
| Newcomer, want it to feel like Windows | **Linux Mint** |
| Newest everything, enjoy administering | **Arch** via **CachyOS** or **EndeavourOS** |
| Never want to maintain anything; work lives in containers | **Bluefin DX** / **Aurora DX** (or **Bazzite** for gaming) |
| Whole machine defined in a text file | **NixOS** |
| Apple Silicon M1/M2 | **Fedora Asahi Remix** |
| Must run proctoring software | any of the above **plus a Windows fallback** |

Full reasoning in Chapter 0 and the decision tree in Chapter 15.

## Table of contents

| # | Chapter |
|---|---|
| 00 | [Preface & the 60-second answer](guide/00-preface.md) |
| 01 | [How to think about the choice](guide/01-how-to-think-about-the-choice.md) |
| 02 | [Foundations: what a distribution is made of](guide/02-foundations.md) |
| 03 | [Requirements: SWE, CS student, daily driver](guide/03-requirements.md) |
| 04 | [Release models & package management](guide/04-release-models-and-package-management.md) |
| 05 | [Desktop environments & window managers](guide/05-desktop-environments.md) |
| 06 | [Distro reviews: mainstream](guide/06-distro-reviews-mainstream.md) |
| 07 | [Distro reviews: enthusiast & rolling](guide/07-distro-reviews-enthusiast.md) |
| 08 | [Distro reviews: atomic & declarative](guide/08-distro-reviews-atomic-and-declarative.md) |
| 09 | [Comparison matrices](guide/09-comparison-matrices.md) |
| 10 | [Hardware considerations](guide/10-hardware.md) |
| 11 | [Developer workflow on Linux](guide/11-developer-workflow.md) |
| 12 | [CS student specifics](guide/12-cs-student-specifics.md) |
| 13 | [Daily-driver realities](guide/13-daily-driver-realities.md) |
| 14 | [Security, privacy & long-term maintenance](guide/14-security-privacy-maintenance.md) |
| 15 | [The decision framework](guide/15-decision-framework.md) |
| 16 | [Post-install playbook](guide/16-post-install-playbook.md) |
| 17 | [Myths, FAQ & migration](guide/17-myths-faq-migration.md) |
| 18 | [Conclusion](guide/18-conclusion.md) |
| A | [Glossary](guide/A-glossary.md) |
| B | [Sources & further reading](guide/B-sources.md) |

A single concatenated version is generated at [`guide/FULL_GUIDE.md`](guide/FULL_GUIDE.md) by `build/build.sh`.

## License

Text: CC BY-SA 4.0.
