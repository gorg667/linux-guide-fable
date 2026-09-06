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

*(Continued: Tumbleweed, NixOS, Mint, dual-boot, takeaways.)*
