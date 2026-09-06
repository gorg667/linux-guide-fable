# Research notes: state of the Linux desktop as of 2026-09-06

Sourced from web searches on 2026-09-06. Use these facts in chapters; cite "as of September 2026".

## Kernel
- kernel.org (2026-09-02): mainline 7.3-rc1; stable 7.2.3 (7.2 released 2026-08-16); 7.1.13 EOL; longterm 6.18.49 (6.18 is the current LTS); older LTS 6.12, 6.6, 6.1, 5.15, 5.10 still alive.
- Linux 7.0 was the version that shipped in Ubuntu 26.04 LTS; 7.1 released 2026-06-14 (new NTFS driver, Intel FRED).
- Rust support in kernel "officially stable" as of 7.0 per press coverage.

## Ubuntu
- **Ubuntu 26.04 LTS "Resolute Raccoon"** released 2026-04-23. Kernel 7.0, GNOME 50, Wayland-only (GDM X11 removed in GNOME 50).
- TPM-backed full-disk encryption now a stable first-class installer option (needs Secure Boot + TPM 2.0).
- sudo → sudo-rs by default; GNU coreutils → uutils rust-coreutils by default (originals still in repos as `sudo-ws` and `coreutils`).
- APT 3.2: `apt history-list`, `apt history-undo`, `apt history-rollback`, `apt why`, `apt why-not`.
- Default terminal is Ptyxis (GTK4, container-aware; was already in 25.10). Default video player Showtime; system monitor Resources.
- Software & Updates GUI removed from default install (too dangerous); Ubuntu Pro settings moved to Security Center.
- App Center now lists/uninstalls debs alongside snaps.
- amd64v3 (x86-64-v3) architecture variants for all packages (opt-in).
- Native ROCm packages (`apt install rocm`) via Canonical+AMD partnership; CUDA "native support" claimed in Canonical blog.
- Improved NVIDIA on Wayland; GNOME triple buffering; fingerprint reader improvements.
- Min requirements: 2 GHz dual-core, 6 GB RAM, 25 GB disk.
- Flavours: Xubuntu, Lubuntu, Ubuntu Budgie, Ubuntu Cinnamon, Ubuntu Studio, Edubuntu, Ubuntu Kylin, Kubuntu are LTS. **Ubuntu MATE and Ubuntu Unity skipped LTS status** (contributor shortage).
- linux-lowlatency package retired → `lowlatency-kernel` boot tweak.
- Post-quantum crypto work mentioned.

## Fedora
- **Fedora 44** released 2026-04-28 (slipped from Apr 14 → Apr 21 → Apr 28). GNOME 50. Fedora KDE Plasma Desktop is an edition (since F42).
- Fedora 45 expected ~Oct/Nov 2026 (usual cadence). Don't claim specifics.
- Asahi platform packages are now fully in upstream Fedora and "fully supported in Fedora Linux 44".
- GNOME Papers stuck at 49 in F44 (minor).

## Debian
- **Debian 13 "Trixie"** released 2025-08-09. APT 3.0, official riscv64, arm64 ROP/COP hardening, HTTP boot, systemd soft-reboot, wcurl, HTTP/3 curl. Kernel 6.12 LTS, GNOME 48, KDE Plasma 6.3.
- Debian 14 "Forky" is testing. Trixie point releases ongoing.

## Pop!_OS / COSMIC
- **COSMIC Epoch 1 released 2025-12-11** with **Pop!_OS 24.04 LTS**. Point releases: 1.0.8 (Feb 2026) ... **COSMIC 1.7.0 released 2026-08-26** (Wikipedia).
- "Pop!_OS 26" discussed as upcoming on reddit — base on Ubuntu 26.04 presumably; not confirmed released as of Sep 2026. Say "Pop!_OS 24.04 LTS is current; a 26.04-based release is in the works."

## Linux Mint
- Mint 22.x series (Ubuntu 24.04 base) current; 22.3 was released ~Dec 2025/Jan 2026.
- **Linux Mint 23** (Ubuntu 26.04 base) targeted for **Christmas/December 2026**. Cinnamon 6.7/7.0 with **Wayland no longer experimental**; both X11 and Wayland sessions fully supported. New installer with Secure Boot + LVM/LUKS.
- LMDE 7 (Debian 13 base) exists.

## KDE
- Plasma 6.6 released 2026-02-17 (virtual desktops on primary screen only, optional new login manager, auto brightness). Plasma 6.7 released 2026-07-14. "Bullet-proof KDE": Plasma 6.6 to be supported as an LTS until 2029 (KDE + Techpaladin + Kubuntu Focus), announced Aug 2026.

## NixOS
- **NixOS 26.05 "Yarara"** released 2026-05-30; supported until 2026-12-31. Linux 6.18 LTS, GNOME 50. Next: 26.11.

## openSUSE
- **Leap 16.0** released (2025-10) — based on SLE 16 / "SUSE Linux Framework One" codebase, **YaST retired**, replaced by Agama (installer), Cockpit (system mgmt), Myrlyn (package GUI). SELinux default on Leap 16. Tumbleweed still ships YaST but deprecated.
- Tumbleweed rolling; Slowroll continues as a monthly-ish snapshot of TW.
- Aeon (GNOME immutable) and Kalpa (KDE immutable) exist.

## NVIDIA
- Driver 590 series (Dec 2025) **dropped Pascal (GTX 10xx) and older** → legacy 580xx branch for those. Arch replaced `nvidia` with `nvidia-open` as default for Turing+.
- 595 series discussed; a 610.x driver referenced building on kernel 7.1.4 (Arch BBS) — so current mainline branch is ~610 as of Aug/Sep 2026. Be vague: "the 590/6xx series".
- Open kernel modules default since 560 for Turing and newer.
- Wayland on NVIDIA is now broadly fine (explicit sync landed 2024; 590 improved).

## Apple Silicon (Asahi)
- Fedora Asahi Remix 44 is the flagship. M1/M2 well supported. **M3 bring-up working** (Jan–Apr 2026: "roughly the level of the first M1 alpha"). M4 early/feature-support page exists; not daily-driver ready. USB-C DisplayPort working (Feb 2026), 120 Hz display.

## Universal Blue
- Bluefin/Aurora Spring 2026 update rebased on Fedora 44 (May 2026). Bluefin LTS (CentOS Stream based) released Sept 2025. Bazzite uses bootc updates. All use bootc now.

## GNOME
- GNOME 50 (March 2026): X11 session removed from GDM; VRR & fractional scaling stable; Digital Wellbeing/parental controls; GTK4 native SVG.
- GNOME 51 expected Sept 2026 (likely ~Sept 17). Don't cite specifics.
