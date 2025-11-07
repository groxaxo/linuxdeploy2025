# Linux Deploy
Copyright (C) 2012-2019  Anton Skshidlevsky, [GPLv3](https://github.com/meefik/linuxdeploy/blob/master/LICENSE)
This application is open source software for quick and easy installation of the operating system (OS) GNU/Linux on your Android device.
The application creates a disk image or a directory on a flash card or uses a partition or RAM, mounts it and installs an OS distribution. Applications of the new system are run in a chroot environment and working together with the Android platform. All changes made on the device are reversible, i.e. the application and components can be removed completely. Installation of a distribution is done by downloading files from official mirrors online over the internet. The application can run better with superuser rights (root).
The program supports multi language interface. You can manage the process of installing the OS, and after installation, you can start and stop services of the new system (there is support for running your scripts) through the UI. The installation process is reported as text in the main application window. During the installation, the program will adjust the environment, which includes the base system, SSH server, VNC server and desktop environment. The program interface can also manage SSH and VNC settings.
## Ubuntu Support (2025 Update)

This fork adds support for modern Ubuntu LTS releases with improved deployment logic:

### Supported Versions

- ✅ **Ubuntu 24.04 LTS (Noble Numbat)** - Supported until 2029
  - ARM64 and AMD64 architectures only (i386 not supported)
  - Latest features and packages
  
- ✅ **Ubuntu 22.04 LTS (Jammy Jellyfish)** - Supported until 2027
  - **Default version** - Recommended for new installations
  - Full architecture support: armhf, arm64, i386, amd64
  - Excellent stability and security updates
  
- ✅ **Ubuntu 20.04 LTS (Focal Fossa)** - Supported until 2025
  - Full architecture support: armhf, arm64, i386, amd64
  - Stable and well-tested

### Legacy Versions (Limited Support)

- ⚠️ **Ubuntu 18.04 LTS (Bionic Beaver)** - EOL April 2023 (ESM available)
- ⚠️ **Ubuntu 16.04 LTS (Xenial Xerus)** - EOL April 2021 (ESM available)
- ⚠️ **Ubuntu 14.04 LTS (Trusty Tahr)** - EOL April 2019
- ⚠️ **Ubuntu 12.04 LTS (Precise Pangolin)** - EOL April 2017 (armel support)

### Features

- **Automatic security updates** - Security and update repositories are automatically configured
- **Modern package support** - Access to the latest software packages
- **ARM64 optimization** - Better performance on modern ARM devices
- **Improved compatibility** - Enhanced apt configuration for Android chroot environments
- **Easy installation** - Simply select Ubuntu from the distribution list and choose your preferred version

### Architecture Compatibility

| Ubuntu Version | armhf | arm64 | i386 | amd64 | armel |
|---------------|-------|-------|------|-------|-------|
| Noble (24.04) | ✅    | ✅    | ❌   | ✅    | ❌    |
| Jammy (22.04) | ✅    | ✅    | ✅   | ✅    | ❌    |
| Focal (20.04) | ✅    | ✅    | ✅   | ✅    | ❌    |
| Bionic (18.04)| ✅    | ✅    | ✅   | ✅    | ❌    |
| Xenial (16.04)| ✅    | ✅    | ✅   | ✅    | ❌    |
| Trusty (14.04)| ✅    | ✅    | ✅   | ✅    | ❌    |
| Precise (12.04)| ✅   | ❌    | ✅   | ✅    | ✅    |

**Note:** Ubuntu 24.04 (Noble) and later versions do not support i386 architecture.

Donations:

- E-Money: <https://meefik.github.io/donate>
- Google Play: <https://play.google.com/store/apps/details?id=ru.meefik.donate>
