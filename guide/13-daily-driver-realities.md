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
