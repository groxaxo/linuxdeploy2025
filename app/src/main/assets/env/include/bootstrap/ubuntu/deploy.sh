#!/bin/sh
# Linux Deploy Component
# (c) Anton Skshidlevsky <meefik@gmail.com>, GPLv3

[ -n "${SUITE}" ] || SUITE="jammy"

if [ -z "${ARCH}" ]
then
    case "$(get_platform)" in
    x86) ARCH="i386" ;;
    x86_64) ARCH="amd64" ;;
    arm) ARCH="armhf" ;;
    arm_64) ARCH="arm64" ;;
    esac
fi

if [ -z "${SOURCE_PATH}" ]
then
    case "$(get_platform ${ARCH})" in
    x86*) SOURCE_PATH="http://archive.ubuntu.com/ubuntu/" ;;
    arm*) SOURCE_PATH="http://ports.ubuntu.com/" ;;
    esac
fi

apt_repository()
{
    # Backup sources.list
    if [ -e "${CHROOT_DIR}/etc/apt/sources.list" ]; then
        cp "${CHROOT_DIR}/etc/apt/sources.list" "${CHROOT_DIR}/etc/apt/sources.list.bak"
    fi
    # Fix for resolv problem (required for older versions like xenial)
    echo 'Debug::NoDropPrivs "true";' > "${CHROOT_DIR}/etc/apt/apt.conf.d/00no-drop-privs"
    # Fix for seccomp policy (required for modern versions)
    echo 'APT::Sandbox::Seccomp "false";' > "${CHROOT_DIR}/etc/apt/apt.conf.d/999seccomp-off"
    # Update sources.list
    echo "deb ${SOURCE_PATH} ${SUITE} main universe multiverse" > "${CHROOT_DIR}/etc/apt/sources.list"
    echo "deb-src ${SOURCE_PATH} ${SUITE} main universe multiverse" >> "${CHROOT_DIR}/etc/apt/sources.list"
    # Add security updates repository
    case "${SUITE}" in
        noble|jammy|focal|bionic|xenial|trusty)
            echo "deb ${SOURCE_PATH} ${SUITE}-security main universe multiverse" >> "${CHROOT_DIR}/etc/apt/sources.list"
            echo "deb ${SOURCE_PATH} ${SUITE}-updates main universe multiverse" >> "${CHROOT_DIR}/etc/apt/sources.list"
            ;;
        # Note: precise (12.04) is excluded as it's EOL and no longer receives security updates
    esac
    # Fix for upstart (only needed for older versions)
    if [ -e "${CHROOT_DIR}/sbin/initctl" ]; then
        chroot_exec -u root dpkg-divert --local --rename --add /sbin/initctl
        ln -s /bin/true "${CHROOT_DIR}/sbin/initctl"
    fi
}

do_help()
{
cat <<EOF
   --arch="${ARCH}"
     Architecture of Linux distribution, supported "armel", "armhf", "arm64", "i386" and "amd64".
     Note: i386 is not supported in Ubuntu 24.04 (noble) and later versions.
     Note: armel is only supported in Ubuntu 12.04 (precise).

   --suite="${SUITE}"
     Version of Linux distribution, supported versions:
     - "noble" (24.04 LTS) - Supported until 2029
     - "jammy" (22.04 LTS) - Supported until 2027
     - "focal" (20.04 LTS) - Supported until 2025
     - "bionic" (18.04 LTS) - EOL April 2023 (ESM available)
     - "xenial" (16.04 LTS) - EOL April 2021 (ESM available)
     - "trusty" (14.04 LTS) - EOL April 2019
     - "precise" (12.04 LTS) - EOL April 2017

   --source-path="${SOURCE_PATH}"
     Installation source, can specify address of the repository or path to the rootfs archive.

   --extra-packages="${EXTRA_PACKAGES}"
     List of optional installation packages, separated by spaces.

EOF
}
