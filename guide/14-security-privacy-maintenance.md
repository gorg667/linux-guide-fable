# Chapter 14 — Security, Privacy, and Long-Term Maintenance

A Linux desktop is not automatically secure, and it is not automatically maintained. It is *more securable* than the alternatives, with less effort, and it respects your privacy by default. This chapter covers what to turn on, what to leave alone, and how to keep the machine healthy for years.

## 14.1 Threat model for a laptop

Be concrete about what you're defending against, in rough order of likelihood for a student or engineer:

1. **Loss or theft of the device.** Someone has your laptop and wants your data (or just the hardware). → **Full-disk encryption** is the entire answer. Nothing else matters if this isn't done.
2. **Malicious or compromised software you installed.** A poisoned `npm` package, a malicious AUR PKGBUILD, a fake "Zoom installer," a browser extension gone bad. → Sandboxing (Flatpak), reading what you install, not running `curl | sudo sh` from random sites, keeping secrets out of reach of arbitrary processes.
3. **Network attacks on public WiFi.** → Firewall on, no listening services, VPN if you're paranoid, HTTPS everywhere (already default).
4. **Phishing and account compromise.** → Password manager, hardware keys/passkeys, not the OS's job.
5. **Evil-maid / physical tampering.** Someone modifies your bootloader while you're away. → Secure Boot + TPM-measured boot. Relevant to very few students; relevant to some engineers.
6. **Targeted remote exploitation.** Zero-days against your browser or kernel. → Update promptly; use a browser with sandboxing (both do); Flatpak browsers add a layer. If you're a real target, you need more than this chapter.

Everything below maps to one of these.

## 14.2 Full-disk encryption

**Do it at install time.** Every mainstream installer offers LUKS encryption; retrofitting it later is possible but painful.

- **Passphrase at boot** — the default. Choose a long passphrase (a sentence). You'll type it once per boot. Works everywhere.
- **TPM-backed auto-unlock** — the disk key is sealed to the TPM 2.0 chip and released only if the measured boot chain (firmware, bootloader, kernel) matches. You boot straight to the login screen; a thief who pulls the drive gets ciphertext; a thief who boots your laptop hits the login screen and (with a good password and no exploitable bugs) gets nothing. **Ubuntu 26.04 offers this in the installer.** On Fedora/Arch/openSUSE/Universal Blue you set it up after install with `systemd-cryptenroll --tpm2-device=auto --tpm2-pcrs=0+7 /dev/nvme0n1p3` (PCR selection is a trade-off between security and "a firmware update locked me out"); Universal Blue has a `ujust` recipe; openSUSE Aeon does it by default. **Keep the passphrase as a fallback slot and write down a recovery key.** A firmware update, a bootloader change, or toggling Secure Boot can change the measurements and require the fallback. This is normal, not a bug.
- **Encrypted `/home` only** (eCryptfs, fscrypt) is an older approach; full-disk is simpler and stronger.
- **Btrfs/ext4 on LUKS** is the standard layout. Encrypting swap matters too (installers handle it; zram swap is in RAM and needs nothing).
- **Performance cost:** negligible on any CPU with AES-NI (all of them since ~2010).

If you do nothing else in this chapter, do this.

## 14.3 Secure Boot

What it does: prevents unsigned bootloaders and kernels from running, closing off a class of persistent bootkits. What it doesn't do: protect against anything once the OS is running.

- **Ubuntu, Fedora, openSUSE, Debian, Mint, Universal Blue, Zorin**: work with Secure Boot on, out of the box, via the Microsoft-signed `shim`.
- **Third-party modules** (NVIDIA, VirtualBox, some VPNs) need signing: Ubuntu prompts you to set a MOK password during driver install and enrol at next boot; Fedora's akmods can auto-sign with a one-time `kmodgenca` + `mokutil --import`; openSUSE generates a MOK automatically; Universal Blue provides `ujust enroll-secure-boot-key`.
- **Arch, EndeavourOS, Pop!_OS, Void, Gentoo**: no signed shim; either disable Secure Boot or use `sbctl` to create and enrol your own keys and sign your kernel/bootloader (~20 minutes, well documented; CachyOS's installer can do it).
- **NixOS**: Lanzaboote (community; works; manual).

**Should you keep it on?** If your distro supports it, yes — it's free protection and required for Windows 11 dual-boot, TPM-backed encryption, and some corporate/anti-cheat contexts. If you're on Arch and don't want to set up `sbctl`, turning it off is a reasonable trade for a personal machine; know that you've done it.

## 14.4 Mandatory access control: SELinux and AppArmor

- **SELinux** (Fedora, RHEL, openSUSE Leap 16/Tumbleweed): enforcing by default with the targeted policy. Confines system daemons; mostly invisible to desktop users. When something's denied: `sudo ausearch -m avc -ts recent` or the `sealert` GUI explains it and suggests a fix (`setsebool`, `restorecon`, or a local policy module). Don't set it to permissive as a "fix" — find the actual denial. Worth learning if you'll administer RHEL.
- **AppArmor** (Ubuntu, Debian, Mint, Pop!_OS): path-based profiles for specific programs; confines snaps and some services. Ubuntu 24.04+ also restricts unprivileged user namespaces via AppArmor, which sometimes breaks Chromium-based Electron apps, some dev tools, or `bwrap`-based sandboxes — the fix is an AppArmor profile for the binary (or, less ideally, `sysctl kernel.apparmor_restrict_unprivileged_userns=0`).
- **Neither** (Arch, Void, Gentoo default, NixOS default): installable; most desktop users don't.

Neither should drive your distro choice. Both are fine. Leave whichever you have enabled.

## 14.5 Firewall

A laptop that connects to café and campus WiFi should have a firewall dropping unsolicited inbound connections. Linux distros disagree about defaults:

- **Fedora, openSUSE, EndeavourOS, CachyOS, Universal Blue**: `firewalld` on, with the "public" zone blocking inbound except SSH (Fedora) or nothing. Good.
- **Ubuntu, Mint, Pop!_OS, Debian**: `ufw` installed but **off** (Mint's firewall GUI makes enabling it obvious). Rationale: no services listen by default. Enable it anyway: `sudo ufw enable`. It takes two seconds.
- **Arch**: nothing. Install `ufw` or `firewalld` and enable it.
- **NixOS**: `networking.firewall.enable = true;` is the default.

Then don't punch holes you don't need. If you run a local dev server, bind it to `localhost`, not `0.0.0.0`, unless you're deliberately testing from your phone. KDE Connect needs ports 1714–1764 (its installer adds a `firewalld` service; on `ufw` add the range manually).

## 14.6 Application sandboxing and permissions

- **Flatpak** apps run in a bubblewrap sandbox with declared permissions (filesystem paths, network, devices, D-Bus). Review and adjust with **Flatseal** or the built-in permission UI in GNOME Settings / KDE System Settings. Many apps ask for broad filesystem access they don't need (`filesystem=home`); tightening it is a real security gain. Portals (file chooser, screenshot, screen share) let sandboxed apps do things without broad grants.
- **Snaps** are confined by AppArmor; permissions ("interfaces") via `snap connections` or the Software app.
- **AppImages** and **vendor `.deb`/`.rpm`s** run unconfined, as your user, with access to everything your user has — including `~/.ssh`, browser sessions, and your password manager's local vault if it's unlocked. This is the normal Linux state and it's why "don't run random binaries" is the key habit.
- **Browser sandboxing** is built into Firefox and Chromium and works on every distro. Firefox-as-Flatpak adds an outer layer with a slight cost to hardware acceleration and extension native-messaging setup.
- **Containers are not a security boundary** for untrusted code by default (rootful Docker especially). Rootless Podman is meaningfully better. For genuinely untrusted software, use a VM.

## 14.7 Supply chain: what you're trusting

- **Official repositories** of every mainstream distro: signed, reviewed, built on distro infrastructure. Trust these most.
- **Flathub**: apps reviewed on submission, built on Flathub's infrastructure from declared sources (or, for proprietary apps, repackaged vendor binaries — marked as such), sandboxed. Good.
- **AUR**: user-submitted build scripts, *not* reviewed, built on your machine. Read the PKGBUILD (your helper shows the diff). Prefer packages with many votes and an active maintainer. It has been abused a handful of times (2018, 2025 — malware in orphaned or newly-uploaded packages, caught within days). Treat it like `npm`: mostly fine, occasionally not.
- **PPAs / COPR / OBS**: binaries from individuals. Same trust calculus as the AUR, with less transparency (you don't see the build). Prefer well-known maintainers.
- **`curl | sh` installers** (rustup, uv, Homebrew, mise, nvm…): you're trusting the vendor's domain and TLS. The mainstream ones are fine; read the script for anything less known.
- **Docker Hub / GHCR images**: trust the publisher; prefer official/verified images; pin digests in production.
- **Universal Blue / other community image builders**: you're trusting their GitHub org and CI pipeline. Transparent (public builds, signed images via cosign) and well-run so far; a different surface than a distro foundation.
- **Reproducible builds**: Debian (95%+), Arch (progressing, Valve-funded), NixOS (high) can prove binaries match sources. A genuine supply-chain advantage that most users never think about.

## 14.8 Privacy and telemetry

Linux distros are, by default, dramatically more private than Windows or macOS. Specifics:

- **Ubuntu**: an optional, opt-in-at-install "Help improve Ubuntu" hardware/usage report; the Ubuntu Pro advertisement in `apt` output (disable with `pro config set apt_news=false`); snap store telemetry (minimal); Canonical's 2012 Amazon search lens is long gone. Firefox snap phones home to Mozilla like any Firefox.
- **Fedora**: proposed opt-in telemetry in 2023 was heavily debated and shipped as opt-in only (Fedora 40+ asks once, default off). Countme (a privacy-preserving mirror-hit counter) is on.
- **Everyone else**: essentially nothing. Debian's `popularity-contest` is opt-in. Arch counts nothing. NixOS nothing.
- **Applications** are another matter: VS Code, JetBrains, Chrome, Discord, Spotify, Steam collect what they collect on any OS. VSCodium, Firefox with tweaks, and Flatpak permissions can limit some of it.
- **DNS**: use DNS-over-TLS/HTTPS via `systemd-resolved` (`DNSOverTLS=yes`) or the browser's built-in DoH.
- **MAC randomisation** for WiFi: NetworkManager supports per-network random MACs (`wifi.cloned-mac-address=random`/`stable`); GNOME/KDE expose it in the connection editor.
- **Location services**: GNOME uses Mozilla Location Service's successor (BeaconDB); off by default on most distros.

## 14.9 Update discipline

The single biggest determinant of security *and* stability over time is how you update. By release model:

**Point release (Ubuntu, Mint, Debian, Fedora):**
- Enable automatic security updates: Ubuntu/Debian `unattended-upgrades` (Ubuntu enables it by default for security), Fedora `dnf-automatic` (or GNOME Software's auto-updates), Mint's Update Manager auto-update option.
- Apply everything else weekly. Reboot when the kernel updates (Ubuntu Pro's Livepatch defers this).
- Do the major upgrade within a few months of release (Fedora) or within a year (Ubuntu LTS→LTS), during a break, after a backup.

**Rolling (Arch, Tumbleweed, EndeavourOS, CachyOS):**
- Update **at least weekly**; daily is fine. Long gaps (months) cause keyring and partial-upgrade problems.
- **Read the news** (Arch: `informant` package; openSUSE: the factory mailing list is optional — openQA does the worrying).
- **Never partial-upgrade** on Arch (`pacman -Sy foo` without `-u` is the classic footgun; always `-Syu`).
- **Handle `.pacnew`/`.rpmnew` files** (`pacdiff`, `rpmconf`).
- Keep an **LTS kernel installed** as a fallback (`linux-lts` on Arch).
- Have **snapshots** (Snapper/Timeshift) taken before each update — CachyOS/openSUSE do this automatically; on Arch, `snap-pac` hooks it into pacman.
- **Don't update in the 48 hours before a deadline or demo.** This rule alone eliminates most rolling-release horror stories.

**Atomic (Universal Blue, Silverblue, Aeon):**
- Updates are automatic and staged; you reboot when convenient. There is nothing to do. If an update misbehaves, boot the previous deployment (`rpm-ostree rollback` / `bootc rollback` to make it stick).

**Declarative (NixOS):**
- `nixos-rebuild switch --upgrade` when you like. Roll back by booting a previous generation. Run `nix-collect-garbage --delete-older-than 30d` periodically or the store grows unboundedly.

**Everything:**
- **Flatpaks**: `flatpak update` weekly or let GNOME Software/Discover do it automatically.
- **Firmware**: `fwupdmgr refresh && fwupdmgr update` monthly, or via GNOME Software/Discover.
- **Language toolchains and Homebrew**: on your own schedule; these don't affect system stability.

## 14.10 Backups

Everyone agrees backups matter; almost nobody does them until after the first loss. A Linux laptop makes it easy.

**Three kinds of "backup," all needed:**

1. **System snapshots** (undo a bad update in 30 seconds): **Btrfs + Snapper** (openSUSE default; CachyOS default; Fedora with `snapper` + `btrfs-assistant`; Arch with `snap-pac` + `grub-btrfs`) or **Timeshift** (Mint default; works on ext4 via rsync or Btrfs). Atomic distros have this built in. **Not a backup** — same disk, same failure domain — but the most-used safety net.
2. **Data backups** (your files survive the disk dying or the laptop being stolen): **Pika Backup** or **Déjà Dup** (GNOME; Borg/Duplicity underneath; point at an external drive or cloud), **Kup** (KDE), or the CLI kings **`restic`** and **`borg`** (deduplicated, encrypted, incremental, to any destination — external disk, NAS, S3/B2/any cloud via `rclone`). Schedule with a systemd timer. `restic` + Backblaze B2 costs a few dollars a month for a typical home directory. **Vorta** is a GUI for Borg.
3. **Configuration in git** (rebuild the machine from scratch in an hour): dotfiles via chezmoi/stow (Chapter 11); a list of installed packages (`pacman -Qqe > pkglist.txt`, `dnf repoquery --userinstalled`, `apt-mark showmanual`, `flatpak list --app --columns=application`) committed alongside; on NixOS, the config *is* this.

**Test a restore** once. A backup you've never restored from is a hope, not a backup.

**Don't back up:** `~/.cache`, `node_modules`, `.venv`, build directories, browser caches, Steam libraries (re-downloadable). Every backup tool has an exclude list; use it.

**Sync ≠ backup.** Dropbox/OneDrive/Nextcloud/Syncthing propagate deletions and ransomware. They're convenient and worth having; they don't replace versioned backups (though some offer file version history).

## 14.11 Long-term health: the yearly checklist

Once a year — during a semester break or a quiet week — spend an hour:

- [ ] **Firmware**: `fwupdmgr update`; check the vendor site if not on LVFS.
- [ ] **Major upgrade** if on a point release and one is due (Fedora N→N+1, Ubuntu LTS if new LTS is out and .1 has shipped).
- [ ] **Orphaned packages**: `pacman -Qdt`, `dnf autoremove`, `apt autoremove`, `flatpak uninstall --unused`, `nix-collect-garbage -d`.
- [ ] **Disk hygiene**: `journalctl --vacuum-time=4weeks`; check `~/.cache` size; `docker system prune`; old kernels (Ubuntu/Fedora keep 2–3 automatically).
- [ ] **Snapshot pruning**: verify Snapper/Timeshift retention isn't filling the disk.
- [ ] **Backup restore test**: pull one file back from `restic`/Borg.
- [ ] **Secrets rotation**: SSH keys if old; password manager audit; revoke tokens you don't use.
- [ ] **Extensions/plugins audit**: remove GNOME/KDE extensions, browser extensions, editor plugins you don't use.
- [ ] **Review Flatpak permissions** in Flatseal.
- [ ] **Battery health**: `upower -i /org/freedesktop/UPower/devices/battery_BAT0` — check capacity; set charge thresholds if the laptop supports them (ThinkPads, Framework, ASUS via `tlp`/`power-profiles-daemon`/sysfs).
- [ ] **Read your distro's release notes** for the past year — there's usually one thing you didn't know had changed.

Do this and a Linux install lasts the life of the hardware. Machines running the same Arch install for a decade, or Ubuntu upgraded LTS-to-LTS since 2012, are common and unremarkable.

## 14.12 When things break: a triage order

1. **Can you boot?** If not: previous kernel from the boot menu → snapshot/previous deployment from the boot menu → live USB, mount, `chroot`, fix (ArchWiki "General troubleshooting" applies to every distro).
2. **Boots but no graphics?** Almost always a GPU driver vs. kernel mismatch (NVIDIA) — boot the LTS/previous kernel, or `Ctrl+Alt+F3` to a TTY and rebuild/reinstall the driver.
3. **Boots, graphics, but the desktop is wrong?** Check `journalctl -b -p err`; a GNOME extension or Plasma widget is the usual suspect (disable them; `dconf reset -f /org/gnome/shell/` in extremis).
4. **A specific app is wrong?** Run it from a terminal and read the output; check Flatpak permissions; search the exact error with your distro's name.
5. **Something's slow or hot?** `btop`/`htop`, `powertop`, `journalctl` for a stuck service, `systemd-analyze blame` for boot.
6. **Still stuck?** Your distro's forum/Discourse/Matrix with: distro+version, DE, GPU, the exact command, the exact error, what you tried. The ArchWiki and Ask Fedora answer most things regardless of your distro.

---

### Key takeaways

- **Full-disk encryption at install time is non-negotiable for a laptop.** TPM auto-unlock (Ubuntu 26.04 installer; `systemd-cryptenroll` elsewhere) is convenient — keep a recovery key.
- Keep **Secure Boot** on where the distro supports it (all mainstream except Arch-family/Pop!_OS, which need `sbctl` or disabling); sign third-party modules via MOK.
- SELinux vs AppArmor doesn't matter; leave whichever you have on. **Enable the firewall** — Ubuntu/Mint/Debian/Arch ship it off.
- **Flatpak sandboxing + Flatseal** is your app-level defence; vendor binaries and AppImages run unconfined. Trust official repos > Flathub > AUR/PPA/COPR > random `curl | sh`.
- Linux is private by default; Ubuntu and Fedora's telemetry is opt-in or trivially disabled.
- **Update discipline by model:** auto-security + weekly on point releases; weekly + read-the-news + snapshots + no-updates-before-deadlines on rolling; nothing on atomic; `nixos-rebuild` + garbage-collect on NixOS.
- **Three backup layers:** snapshots (Snapper/Timeshift/atomic) for undo; `restic`/Borg/Pika to an external or cloud target for data; dotfiles + package list in git for rebuild. Test a restore.
- A yearly hour of maintenance keeps an install healthy for the life of the hardware.
