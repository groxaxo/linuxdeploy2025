# Linux Deploy
Copyright (C) 2012-2019  Anton Skshidlevsky, [GPLv3](https://github.com/meefik/linuxdeploy/blob/master/LICENSE)
This application is open source software for quick and easy installation of the operating system (OS) GNU/Linux on your Android device.
The application creates a disk image or a directory on a flash card or uses a partition or RAM, mounts it and installs an OS distribution. Applications of the new system are run in a chroot environment and working together with the Android platform. All changes made on the device are reversible, i.e. the application and components can be removed completely. Installation of a distribution is done by downloading files from official mirrors online over the internet. The application can run better with superuser rights (root).
The program supports multi language interface. You can manage the process of installing the OS, and after installation, you can start and stop services of the new system (there is support for running your scripts) through the UI. The installation process is reported as text in the main application window. During the installation, the program will adjust the environment, which includes the base system, SSH server, VNC server and desktop environment. The program interface can also manage SSH and VNC settings.
## Ubuntu Support (2025 Update)

This fork adds support for modern Ubuntu LTS releases:

- ✅ **Ubuntu 24.04 LTS (Noble Numbat)** - Supported until 2029
- ✅ **Ubuntu 22.04 LTS (Jammy Jellyfish)** - Supported until 2027
- ✅ **Ubuntu 20.04 LTS (Focal Fossa)** - Supported until 2025

You can now install current Ubuntu versions with the latest security patches, modern packages, and better ARM64 optimization. Simply select Ubuntu from the distribution list and choose your preferred version.

Donations:

- E-Money: <https://meefik.github.io/donate>
- Google Play: <https://play.google.com/store/apps/details?id=ru.meefik.donate>
