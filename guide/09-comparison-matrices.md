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
