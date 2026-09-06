# PROGRESS.md — Working Log & Resume Instructions

> **If you are a fresh instance of the AI reading this after a context compaction or account switch: READ THIS FILE FIRST, then `PLAN.md`, then skim the latest chapter files in `guide/`. Do not redo finished work. Continue from the "NEXT ACTION" section at the bottom.**

## The Task (verbatim intent from user)

Create the best possible, most detailed, comprehensive, in-depth essay/review/guide on
**which Linux distribution to choose for a software engineer / CS student / daily-driver user**.

Constraints from the user:
- Workflow may be interrupted at any time (credits). **Push to GitHub constantly.**
- Context will be compacted periodically. **Document reasoning here so a fresh instance can continue.**
- Work is incremental; every chapter is its own file so partial progress is always useful.

## Repository layout

```
/home/user/webapp
├── README.md            — public-facing entry point, TOC linking to chapters
├── PROGRESS.md          — THIS FILE. Status log + resume instructions
├── PLAN.md              — full outline of the guide (chapter-by-chapter, with bullets of what to cover)
├── research/            — raw research notes gathered from the web (dated, sourced)
├── guide/               — the actual guide, one Markdown file per chapter (00-, 01-, ...)
├── build/               — scripts to concatenate chapters into one file (guide/FULL_GUIDE.md) and optional HTML
└── .github/             — (none needed)
```

## Working conventions

- **Branch**: work directly on `main` and push after every meaningful edit (user explicitly wants
  constant pushes; PR overhead is counterproductive here for a solo docs repo). Commit messages:
  `docs(chNN): ...`, `research: ...`, `chore: ...`.
- **Chapter files** live in `guide/NN-slug.md`. Each starts with a `# Title` H1 and ends with a
  short "Key takeaways" block. Keep chapters self-contained.
- **Tone**: opinionated but fair, technical, honest about trade-offs, no marketing fluff.
  Write for a smart reader who may be new to Linux but not new to computers.
- **Date context**: current date is **2026-09-06**. Use research/ notes for version numbers. When
  unsure about a very recent fact, say so rather than inventing a version number.
- **Length target**: very long. Aim for ~40–60k words total across chapters. Depth > breadth,
  but breadth must also be complete.
- After finishing each chapter: update status table below, `git add -A && git commit && git push`.

## Status

| # | Chapter file | Status | Notes |
|---|---|---|---|
| 00 | guide/00-preface.md | DONE | how to read, who this is for, TL;DR |
| 01 | guide/01-how-to-think-about-the-choice.md | DONE | framing, why the question is mis-posed, what actually matters |
| 02 | guide/02-foundations.md | DONE | distro anatomy: kernel, init, packaging, release models, DE, Wayland, FS |
| 03 | guide/03-requirements.md | DONE | needs of SWE / CS student / daily driver; the union & conflicts |
| 04 | guide/04-release-models-and-package-management.md | DONE | point vs rolling vs atomic; apt/dnf/pacman/zypper/nix; flatpak/snap/appimage; distrobox, toolbox, devcontainers |
| 05 | guide/05-desktop-environments.md | DONE | GNOME, KDE, Cosmic, Xfce, Cinnamon, tiling WMs (Hyprland, Sway, i3, niri) |
| 06 | guide/06-distro-reviews-mainstream.md | DONE | Ubuntu (+flavours), Fedora Workstation/KDE, Linux Mint, Pop!_OS, Debian, Zorin, elementary |
| 07 | guide/07-distro-reviews-enthusiast.md | DONE | Arch, EndeavourOS, CachyOS, Manjaro, openSUSE TW/Leap/Slowroll, Gentoo, Void, Alpine |
| 08 | guide/08-distro-reviews-atomic-and-declarative.md | DONE | Fedora Silverblue/Kinoite/Atomic, Universal Blue (Bluefin/Aurora/Bazzite), NixOS, openSUSE Aeon/Kalpa, Vanilla OS, GNOME OS |
| 09 | guide/09-comparison-matrices.md | DONE | big tables: packaging, release, DE, hw, security, corporate backing, community, docs |
| 10 | guide/10-hardware.md | DONE |
| 11 | guide/11-developer-workflow.md | DONE |
| 12 | guide/12-cs-student-specifics.md | DONE | coursework realities: C/asm/OS courses, ML/CUDA, Java/Eclipse, Office/LaTeX, exam software, proctoring, Windows dual-boot |
| 13 | guide/13-daily-driver-realities.md | DONE | browsers, media, gaming (Proton), office, Zoom/Teams, printing, Bluetooth, phones (KDE Connect), fonts, HDR |
| 14 | guide/14-security-privacy-maintenance.md | DONE | updates, SELinux/AppArmor, secure boot, FDE (LUKS), backups (btrfs snapshots, Timeshift), long-term maintenance |
| 15 | guide/15-decision-framework.md | TODO | decision trees, persona recommendations, "if X then Y" |
| 16 | guide/16-post-install-playbook.md | TODO | concrete step-by-step for top 3 picks |
| 17 | guide/17-myths-faq-migration.md | TODO | myths, FAQ, migrating from Windows/macOS, dual boot, when to switch |
| 18 | guide/18-conclusion.md | TODO | final verdict |
| A | guide/A-glossary.md | TODO | glossary |
| B | guide/B-sources.md | TODO | sources & further reading |

## Log (append-only, newest at bottom)

- 2026-09-06 04:15 — Repo was empty (only .git with origin https://github.com/gorg667/linux-guide-fable.git). Created scaffold: README.md, PROGRESS.md, PLAN.md. Decided on chapter-per-file structure to make progress resumable.

## NEXT ACTION

1. Finish scaffold push (README, PLAN).
2. Do web research into `research/` (distro versions as of Sep 2026, notable changes: Ubuntu 26.04 LTS, Fedora 44/45, Debian 13 Trixie, COSMIC status, Wayland-only moves, NVIDIA driver status, Asahi status, etc.).
3. Start writing chapters in order 00 → 18. Push after each.
- 2026-09-06 04:19 — ch00 written (~1500 words). Research complete enough; writing chapters sequentially.
- 2026-09-06 04:21 — ch01 written (~2100 words).
- 2026-09-06 04:24 — ch02 written (~4300 words). bcachefs fact verified and corrected (removed in 6.18, Sep 2025).
- 2026-09-06 04:26 — ch03 written (~3400 words). Total so far ~11k words.
- 2026-09-06 04:30 — ch04 written (~5100 words). Total ~16k.
- 2026-09-06 04:37 — Account switch occurred; ch05 was lost mid-write and rewritten (~2600 words). Total ~19k. LESSON: keep chapters ≤ ~3500 words per Write call, or split into two files/appends, so a lost turn costs less.
- 2026-09-06 04:38 — ch06 part 1 (Ubuntu 8.5, Fedora 9) pushed.
- 2026-09-06 04:40 — ch06 complete (~5800 words). Scores: Fedora 9, Ubuntu 8.5, Mint 8, Pop 7.5, Debian 7, Zorin 7, elementary 6.
- 2026-09-06 04:42 — ch07 part 1 pushed (Arch 7.5/9, EOS 8, CachyOS 8, Manjaro 6, Garuda 6.5, Artix 6, Omarchy 7.5).
- 2026-09-06 04:44 — ch07 complete (~5000 words). TW 8.5, Slowroll 8, Leap 7, Gentoo 5, Void 6.5, Alpine 4, Solus 5.5, Slack 3, MX 6.
- 2026-09-06 04:46 — ch08 written (~4000 words). Bluefin/Aurora 8.5, DX 9, Bazzite 8.5, Aeon 7.5, NixOS 7/9.5, Silverblue 7, Kalpa 6.5, Vanilla 6, Guix 5. Total ~32k.
- 2026-09-06 04:49 — ch09 written (~2800 words) with build/score.py weighted model. Total ~35k. Next: ch10 hardware.
- 2026-09-06 04:56 — 2nd account switch; ch10 lost and being rewritten in halves. Part 1 pushed.
- 2026-09-06 04:56 — ch10 complete (~3300 words). Total ~39k. Next: ch11 developer workflow.
- 2026-09-06 04:58 — ch11 part 1 pushed.
- 2026-09-06 04:59 — ch11 complete (~3900 words). Total ~42k. Next: ch12 CS student specifics.
- 2026-09-06 05:01 — ch12 written (~3200 words). Total ~45k. Next: ch13 daily driver.
- 2026-09-06 05:03 — ch13 written (~3100 words). Total ~47k. Next: ch14 security/maintenance.
- 2026-09-06 05:05 — ch14 written (~3300 words). Total ~50k. Next: ch15 decision framework (the key chapter).
