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

*(§10.4–10.8 continue below.)*
