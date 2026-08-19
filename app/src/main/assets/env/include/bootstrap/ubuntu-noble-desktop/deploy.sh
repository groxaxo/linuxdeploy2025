#!/bin/sh
# Custom Ubuntu deployment script for Linux Deploy
# Supports noble (24.04 LTS) and jammy (22.04 LTS)
# Accepts SUITE and UBUNTU_FLAVOR variables
# Default values are substituted in deploy.conf directories
# Determine default suite and flavor from directory name if not set
BASENAME=$(basename "$(dirname "$0")")
# BASENAME format: ubuntu-<suite>-<flavor>
if [ -z "$SUITE" ]; then SUITE=$(echo "$BASENAME" | cut -d'-' -f2); fi
if [ -z "$UBUNTU_FLAVOR" ]; then UBUNTU_FLAVOR=$(echo "$BASENAME" | cut -d'-' -f3); fi

# Determine architecture
if [ -z "$ARCH" ]; then
  case "$(get_platform)" in
    x86) ARCH="i386";;
    x86_64) ARCH="amd64";;
    arm) ARCH="armhf";;
    arm_64) ARCH="arm64";;
  esac
fi

# Determine source mirror
if [ -z "$SOURCE_PATH" ]; then
  case "$(get_platform $ARCH)" in
    x86*) SOURCE_PATH="http://archive.ubuntu.com/ubuntu/";;
    arm*) SOURCE_PATH="http://ports.ubuntu.com/";;
  esac
fi

# Configure APT repositories inside chroot
apt_repository() {
  # Backup existing sources list
  if [ -e "${CHROOT_DIR}/etc/apt/sources.list" ]; then
    cp "${CHROOT_DIR}/etc/apt/sources.list" "${CHROOT_DIR}/etc/apt/sources.list.bak"
  fi
  # Disable drop privileges for resolv.conf handling
  echo 'Debug::NoDropPrivs "true";' > "${CHROOT_DIR}/etc/apt/apt.conf.d/00no-drop-privs"
  # Disable seccomp sandbox (required for modern Ubuntu)
  echo 'APT::Sandbox::Seccomp "false";' > "${CHROOT_DIR}/etc/apt/apt.conf.d/999seccomp-off"
  # Create sources.list for main, universe and multiverse
  echo "deb ${SOURCE_PATH} ${SUITE} main universe multiverse" > "${CHROOT_DIR}/etc/apt/sources.list"
  echo "deb-src ${SOURCE_PATH} ${SUITE} main universe multiverse" >> "${CHROOT_DIR}/etc/apt/sources.list"
  # Add security and updates repositories
  echo "deb ${SOURCE_PATH} ${SUITE}-security main universe multiverse" >> "${CHROOT_DIR}/etc/apt/sources.list"
  echo "deb ${SOURCE_PATH} ${SUITE}-updates main universe multiverse" >> "${CHROOT_DIR}/etc/apt/sources.list"
}

# Post-installation: install server or desktop meta-package
post_install() {
  case "$UBUNTU_FLAVOR" in
    desktop) FLAVOR_PKG="ubuntu-desktop";;
    server|*) FLAVOR_PKG="ubuntu-server";;
  esac
  chroot_exec -u root apt-get update
  # Install meta-package without recommends to keep size manageable
  chroot_exec -u root apt-get install -y --no-install-recommends "$FLAVOR_PKG"
}

# Help message displayed by Linux Deploy UI
# Provide information about supported suites and flavors

do_help() {
  cat <<EOF
Usage: ubuntu deploy script
Optional parameters passed via environment variables:
  SUITE           Ubuntu release name (noble or jammy)
  UBUNTU_FLAVOR   Installation flavor: server (default) or desktop
This script configures APT sources for the selected release and installs
either the ubuntu-server or ubuntu-desktop meta-package inside the chroot.
EOF
}
