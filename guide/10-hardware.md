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
