import os

arrays_xml_content = """<resources>

    <string-array name="language_values" translatable="false">
        <item>de</item>
        <item>en</item>
        <item>es</item>
        <item>fr</item>
        <item>in</item>
        <item>it</item>
        <item>ko</item>
        <item>pl</item>
        <item>pt</item>
        <item>ru</item>
        <item>sk</item>
        <item>vi</item>
        <item>zh</item>
    </string-array>
    <string-array name="language_entries" translatable="false">
        <item>Deutsch</item>
        <item>English</item>
        <item>Español</item>
        <item>Français</item>
        <item>Bahasa Indonesia</item>
        <item>Italiano</item>
        <item>한국어</item>
        <item>Polish</item>
        <item>Português</item>
        <item>Русский</item>
        <item>Slovenský</item>
        <item>Tiếng Việt</item>
        <item>简体中文</item>
    </string-array>
    <string-array name="theme_values" translatable="false">
        <item>dark</item>
        <item>light</item>
    </string-array>
    <string-array name="theme_entries">
        <item>Dark</item>
        <item>Light</item>
    </string-array>
    <string-array name="target_type_values" translatable="false">
        <item>file</item>
        <item>directory</item>
        <item>partition</item>
        <item>ram</item>
        <item>custom</item>
    </string-array>
    <string-array name="target_type_entries">
        <item>File</item>
        <item>Directory</item>
        <item>Partition</item>
        <item>RAM</item>
        <item>Custom</item>
    </string-array>
    <string-array name="fs_type_values" translatable="false">
        <item>ext2</item>
        <item>ext3</item>
        <item>ext4</item>
    </string-array>
    <string-array name="locale_values" translatable="false">
        <item>C</item>
        <item>aa_DJ.UTF-8</item>
        <item>af_ZA.UTF-8</item>
        <item>an_ES.UTF-8</item>
        <item>ar_AE.UTF-8</item>
        <item>ar_BH.UTF-8</item>
        <item>ar_DZ.UTF-8</item>
        <item>ar_EG.UTF-8</item>
        <item>ar_IQ.UTF-8</item>
        <item>ar_JO.UTF-8</item>
        <item>ar_KW.UTF-8</item>
        <item>ar_LB.UTF-8</item>
        <item>ar_LY.UTF-8</item>
        <item>ar_MA.UTF-8</item>
        <item>ar_OM.UTF-8</item>
        <item>ar_QA.UTF-8</item>
        <item>ar_SA.UTF-8</item>
        <item>ar_SD.UTF-8</item>
        <item>ar_SY.UTF-8</item>
        <item>ar_TN.UTF-8</item>
        <item>ar_YE.UTF-8</item>
        <item>ast_ES.UTF-8</item>
        <item>be_BY.UTF-8</item>
        <item>bg_BG.UTF-8</item>
        <item>br_FR.UTF-8</item>
        <item>bs_BA.UTF-8</item>
        <item>ca_AD.UTF-8</item>
        <item>ca_ES.UTF-8</item>
        <item>ca_FR.UTF-8</item>
        <item>ca_IT.UTF-8</item>
        <item>cs_CZ.UTF-8</item>
        <item>cy_GB.UTF-8</item>
        <item>da_DK.UTF-8</item>
        <item>de_AT.UTF-8</item>
        <item>de_BE.UTF-8</item>
        <item>de_CH.UTF-8</item>
        <item>de_DE.UTF-8</item>
        <item>de_LI.UTF-8</item>
        <item>de_LU.UTF-8</item>
        <item>el_CY.UTF-8</item>
        <item>el_GR.UTF-8</item>
        <item>en_AU.UTF-8</item>
        <item>en_BW.UTF-8</item>
        <item>en_CA.UTF-8</item>
        <item>en_DK.UTF-8</item>
        <item>en_GB.UTF-8</item>
        <item>en_HK.UTF-8</item>
        <item>en_IE.UTF-8</item>
        <item>en_NZ.UTF-8</item>
        <item>en_PH.UTF-8</item>
        <item>en_SG.UTF-8</item>
        <item>en_US.UTF-8</item>
        <item>en_ZA.UTF-8</item>
        <item>en_ZW.UTF-8</item>
        <item>eo.UTF-8</item>
        <item>es_AR.UTF-8</item>
        <item>es_BO.UTF-8</item>
        <item>es_CL.UTF-8</item>
        <item>es_CO.UTF-8</item>
        <item>es_CR.UTF-8</item>
        <item>es_DO.UTF-8</item>
        <item>es_EC.UTF-8</item>
        <item>es_ES.UTF-8</item>
        <item>es_GT.UTF-8</item>
        <item>es_HN.UTF-8</item>
        <item>es_MX.UTF-8</item>
        <item>es_NI.UTF-8</item>
        <item>es_PA.UTF-8</item>
        <item>es_PE.UTF-8</item>
        <item>es_PR.UTF-8</item>
        <item>es_PY.UTF-8</item>
        <item>es_SV.UTF-8</item>
        <item>es_US.UTF-8</item>
        <item>es_UY.UTF-8</item>
        <item>es_VE.UTF-8</item>
        <item>et_EE.UTF-8</item>
        <item>eu_ES.UTF-8</item>
        <item>eu_FR.UTF-8</item>
        <item>fi_FI.UTF-8</item>
        <item>fo_FO.UTF-8</item>
        <item>fr_BE.UTF-8</item>
        <item>fr_CA.UTF-8</item>
        <item>fr_CH.UTF-8</item>
        <item>fr_FR.UTF-8</item>
        <item>fr_LU.UTF-8</item>
        <item>ga_IE.UTF-8</item>
        <item>gd_GB.UTF-8</item>
        <item>gl_ES.UTF-8</item>
        <item>gv_GB.UTF-8</item>
        <item>he_IL.UTF-8</item>
        <item>hr_HR.UTF-8</item>
        <item>hsb_DE.UTF-8</item>
        <item>hu_HU.UTF-8</item>
        <item>id_ID.UTF-8</item>
        <item>is_IS.UTF-8</item>
        <item>it_CH.UTF-8</item>
        <item>it_IT.UTF-8</item>
        <item>iw_IL.UTF-8</item>
        <item>ja_JP.UTF-8</item>
        <item>ka_GE.UTF-8</item>
        <item>kk_KZ.UTF-8</item>
        <item>kl_GL.UTF-8</item>
        <item>ko_KR.UTF-8</item>
        <item>ku_TR.UTF-8</item>
        <item>kw_GB.UTF-8</item>
        <item>lg_UG.UTF-8</item>
        <item>lt_LT.UTF-8</item>
        <item>lv_LV.UTF-8</item>
        <item>mg_MG.UTF-8</item>
        <item>mi_NZ.UTF-8</item>
        <item>mk_MK.UTF-8</item>
        <item>ms_MY.UTF-8</item>
        <item>mt_MT.UTF-8</item>
        <item>nb_NO.UTF-8</item>
        <item>nl_BE.UTF-8</item>
        <item>nl_NL.UTF-8</item>
        <item>nn_NO.UTF-8</item>
        <item>oc_FR.UTF-8</item>
        <item>om_KE.UTF-8</item>
        <item>pl_PL.UTF-8</item>
        <item>pt_BR.UTF-8</item>
        <item>pt_PT.UTF-8</item>
        <item>ro_RO.UTF-8</item>
        <item>ru_RU.UTF-8</item>
        <item>ru_UA.UTF-8</item>
        <item>sk_SK.UTF-8</item>
        <item>sl_SI.UTF-8</item>
        <item>so_DJ.UTF-8</item>
        <item>so_KE.UTF-8</item>
        <item>so_SO.UTF-8</item>
        <item>sq_AL.UTF-8</item>
        <item>st_ZA.UTF-8</item>
        <item>sv_FI.UTF-8</item>
        <item>sv_SE.UTF-8</item>
        <item>tg_TJ.UTF-8</item>
        <item>th_TH.UTF-8</item>
        <item>tl_PH.UTF-8</item>
        <item>tr_CY.UTF-8</item>
        <item>tr_TR.UTF-8</item>
        <item>uk_UA.UTF-8</item>
        <item>uz_UZ.UTF-8</item>
        <item>wa_BE.UTF-8</item>
        <item>xh_ZA.UTF-8</item>
        <item>yi_US.UTF-8</item>
        <item>zh_CN.UTF-8</item>
        <item>zh_HK.UTF-8</item>
        <item>zh_SG.UTF-8</item>
        <item>zh_TW.UTF-8</item>
        <item>zu_ZA.UTF-8</item>
    </string-array>
    <string-array name="vnc_depth_values" translatable="false">
        <item>8</item>
        <item>15</item>
        <item>16</item>
        <item>24</item>
    </string-array>
    <string-array name="desktop_values" translatable="false">
        <item>xterm</item>
        <item>lxde</item>
        <item>xfce</item>
        <item>mate</item>
        <item>other</item>
    </string-array>
    <string-array name="desktop_entries">
        <item>XTerm</item>
        <item>LXDE</item>
        <item>Xfce</item>
        <item>MATE</item>
        <item>Other</item>
    </string-array>
    <string-array name="distrib_values" translatable="false">
        <item>alpine</item>
        <item>archlinux</item>
        <item>debian</item>
        <item>fedora</item>
        <item>kali</item>
        <item>slackware</item>
        <item>ubuntu</item>
        <item>docker</item>
        <item>rootfs</item>
    </string-array>
    <string-array name="distrib_entries" translatable="false">
        <item>Alpine</item>
        <item>Arch</item>
        <item>Debian</item>
        <item>Fedora</item>
        <item>Kali</item>
        <item>Slackware</item>
        <item>Ubuntu</item>
        <item>Docker</item>
        <item>rootfs.tar</item>
    </string-array>
    <string-array name="init_values" translatable="false">
        <item>run-parts</item>
        <item>sysv</item>
    </string-array>
    <string-array name="graphics_values" translatable="false">
        <item>vnc</item>
        <item>x11</item>
        <item>fb</item>
    </string-array>
    <string-array name="graphics_entries" translatable="false">
        <item>VNC</item>
        <item>X11</item>
        <item>Framebuffer</item>
    </string-array>
    <string-array name="fb_freeze_values" translatable="false">
        <item>none</item>
        <item>pause</item>
        <item>stop</item>
    </string-array>
    <string-array name="fb_freeze_entries">
        <item>Don\\'t freeze</item>
        <item>Pause</item>
        <item>Stop</item>
    </string-array>


    <!-- Debian -->

    <string-array name="debian_suite_values" translatable="false">
        <item>oldstable</item>
        <item>stable</item>
        <item>testing</item>
        <item>unstable</item>
        <item>jessie</item>
        <item>stretch</item>
        <item>buster</item>
    </string-array>
    <string-array name="debian_arch_values" translatable="false">
        <item>armel</item>
        <item>armhf</item>
        <item>arm64</item> <!-- jessie and later -->
        <item>i386</item>
        <item>amd64</item>
    </string-array>

    <!-- Ubuntu -->

    <string-array name="ubuntu_suite_values" translatable="false">
        <item>precise</item>
        <item>trusty</item>
        <item>xenial</item>
        <item>bionic</item>
    </string-array>
    <string-array name="ubuntu_arch_values" translatable="false">
        <item>armel</item> <!-- precise only -->
        <item>armhf</item>
        <item>arm64</item> <!-- trusty and later -->
        <item>i386</item>
        <item>amd64</item>
    </string-array>

    <!-- Kali Linux -->

    <string-array name="kali_suite_values" translatable="false">
        <item>kali-rolling</item>
    </string-array>
    <string-array name="kali_arch_values" translatable="false">
        <item>armel</item>
        <item>armhf</item>
        <item>arm64</item>
        <item>i386</item>
        <item>amd64</item>
    </string-array>

    <!-- Fedora -->

    <string-array name="fedora_suite_values" translatable="false">
        <item>30</item>
    </string-array>
    <string-array name="fedora_arch_values" translatable="false">
        <item>armhfp</item> <!-- f19 and later -->
        <item>aarch64</item> <!-- f21 and later -->
        <item>i386</item>
        <item>x86_64</item>
    </string-array>

    <!-- Arch Linux -->

    <string-array name="archlinux_suite_values" translatable="false">
        <item>latest</item>
    </string-array>
    <string-array name="archlinux_arch_values" translatable="false">
        <item>arm</item>
        <item>armv6h</item>
        <item>armv7h</item>
        <item>aarch64</item>
        <item>i686</item>
        <item>x86_64</item>
    </string-array>

    <!-- Slackware -->

    <string-array name="slackware_suite_values" translatable="false">
        <item>14.2</item>
    </string-array>
    <string-array name="slackware_arch_values" translatable="false">
        <item>arm</item>
        <item>x86</item>
        <item>x86_64</item>
    </string-array>

    <!-- Alpine Linux -->

    <string-array name="alpine_suite_values" translatable="false">
        <item>latest-stable</item>
        <item>edge</item>
    </string-array>
    <string-array name="alpine_arch_values" translatable="false">
        <item>armv7</item>
        <item>armhf</item>
        <item>aarch64</item>
        <item>x86</item>
        <item>x86_64</item>
    </string-array>

    <!-- Docker -->

    <string-array name="docker_suite_values" translatable="false">
        <item>linux</item>
    </string-array>
    <string-array name="docker_arch_values" translatable="false">
        <item>arm</item>
        <item>arm64</item>
        <item>386</item>
        <item>amd64</item>
    </string-array>

    <!-- RootFS -->

    <string-array name="rootfs_suite_values" translatable="false" />
    <string-array name="rootfs_arch_values" translatable="false" />

</resources>
"""

preferences_xml_content = """<resources>

    <string name="screenlock" translatable="false">true</string>
    <string name="wifilock" translatable="false">false</string>
    <string name="wakelock" translatable="false">false</string>
    <string name="fontsize" translatable="false">10</string>
    <string name="maxlines" translatable="false">100</string>
    <string name="language" translatable="false"></string>
    <string name="theme" translatable="false">dark</string>
    <string name="timestamp" translatable="false">true</string>
    <string name="appicon" translatable="false">true</string>
    <string name="stealth" translatable="false">false</string>
    <string name="autostart" translatable="false">false</string>
    <string name="autostart_delay" translatable="false">30</string>
    <string name="nettrack" translatable="false">false</string>
    <string name="powertrack" translatable="false">false</string>
    <string name="env_dir" translatable="false"></string>
    <string name="repository_url" translatable="false">http://hub.meefik.ru</string>
    <string name="path" translatable="false"></string>
    <string name="is_telnet" translatable="false">false</string>
    <string name="telnet_port" translatable="false">5023</string>
    <string name="telnet_localhost" translatable="false">true</string>
    <string name="is_http" translatable="false">false</string>
    <string name="http_port" translatable="false">5080</string>
    <!-- https://wiki.openwrt.org/doc/howto/http.httpd -->
    <string name="http_conf" translatable="false">A:127.0.0.1 D:*</string>
    <string name="profile" translatable="false">linux</string>
    <string name="debug_mode" translatable="false">false</string>
    <string name="trace_mode" translatable="false">false</string>
    <string name="logger" translatable="false">false</string>
    <string name="logfile" translatable="false">output.log</string>
    <string name="chroot_dir" translatable="false">/data/local/mnt</string>
    <string name="distrib" translatable="false">debian</string>
    <string name="suite" translatable="false">@string/debian_suite</string>
    <string name="arch" translatable="false">@string/arm_debian_arch</string>
    <string name="source_path" translatable="false">@string/arm_debian_source_path</string>
    <string name="target_type" translatable="false">file</string>
    <string name="target_path" translatable="false">@string/target_path_file</string>
    <string name="target_path_file" translatable="false">${EXTERNAL_STORAGE}/linux.img</string>
    <string name="target_path_directory" translatable="false">${EXTERNAL_STORAGE}/linux</string>
    <string name="target_path_partition" translatable="false">/dev/block/mmcblkXpY</string>
    <string name="target_path_ram" translatable="false">/data/local/ram</string>
    <string name="target_path_custom" translatable="false"></string>
    <string name="rootfs_archive" translatable="false">${EXTERNAL_STORAGE}/linux-rootfs.tar.gz</string>
    <string name="disk_size" translatable="false">0</string>
    <string name="fs_type" translatable="false">ext4</string>
    <string name="user_name" translatable="false">android</string>
    <string name="user_password" translatable="false"></string>
    <string name="privileged_users" translatable="false">android:aid_inet android:aid_sdcard_rw android:aid_graphics</string>
    <string name="locale" translatable="false">C</string>
    <string name="dns" translatable="false"></string>
    <string name="net_trigger" translatable="false"></string>
    <string name="power_trigger" translatable="false"></string>
    <string name="is_init" translatable="false">false</string>
    <string name="init" translatable="false">run-parts</string>
    <string name="init_path" translatable="false">/etc/rc.local</string>
    <string name="init_level" translatable="false">3</string>
    <string name="init_user" translatable="false">root</string>
    <string name="init_async" translatable="false">false</string>
    <string name="is_mounts" translatable="false">false</string>
    <string name="mounts" translatable="false">/system /sdcard:/mnt/sdcard</string>
    <string name="is_ssh" translatable="false">false</string>
    <string name="ssh_port" translatable="false">22</string>
    <string name="ssh_options" translatable="false"></string>
    <string name="is_pulse" translatable="false">false</string>
    <string name="pulse_host" translatable="false">127.0.0.1</string>
    <string name="pulse_port" translatable="false">4712</string>
    <string name="is_gui" translatable="false">false</string>
    <string name="graphics" translatable="false">vnc</string>
    <string name="desktop" translatable="false">lxde</string>
    <string name="vnc_display" translatable="false">0</string>
    <string name="vnc_depth" translatable="false">16</string>
    <string name="vnc_dpi" translatable="false">75</string>
    <string name="vnc_width" translatable="false"></string>
    <string name="vnc_height" translatable="false"></string>
    <string name="vnc_args" translatable="false"></string>
    <string name="x11_display" translatable="false">0</string>
    <string name="x11_host" translatable="false">127.0.0.1</string>
    <string name="x11_sdl" translatable="false">false</string>
    <string name="x11_sdl_delay" translatable="false">15</string>
    <string name="fb_display" translatable="false">0</string>
    <string name="fb_dev" translatable="false">/dev/graphics/fb0</string>
    <string name="fb_input" translatable="false">/dev/input/event0</string>
    <string name="fb_args" translatable="false">-dpi 100 -sharevts vt0</string>
    <string name="fb_refresh" translatable="false">true</string>
    <string name="fb_freeze" translatable="false">none</string>

    <!-- Debian -->
    <string name="debian_suite" translatable="false">buster</string>
    <!-- arm -->
    <string name="arm_debian_source_path" translatable="false">http://ftp.debian.org/debian/</string>
    <string name="arm_debian_arch" translatable="false">armhf</string>
    <!-- arm_64 -->
    <string name="arm_64_debian_source_path" translatable="false">http://ftp.debian.org/debian/</string>
    <string name="arm_64_debian_arch" translatable="false">arm64</string>
    <!-- x86 -->
    <string name="x86_debian_source_path" translatable="false">http://ftp.debian.org/debian/</string>
    <string name="x86_debian_arch" translatable="false">i386</string>
    <!-- x86_64 -->
    <string name="x86_64_debian_source_path" translatable="false">http://ftp.debian.org/debian/</string>
    <string name="x86_64_debian_arch" translatable="false">amd64</string>

    <!-- Ubuntu -->
    <string name="ubuntu_suite" translatable="false">bionic</string>
    <!-- arm -->
    <string name="arm_ubuntu_source_path" translatable="false">http://ports.ubuntu.com/</string>
    <string name="arm_ubuntu_arch" translatable="false">armhf</string>
    <!-- arm_64 -->
    <string name="arm_64_ubuntu_source_path" translatable="false">http://ports.ubuntu.com/</string>
    <string name="arm_64_ubuntu_arch" translatable="false">arm64</string>
    <!-- x86 -->
    <string name="x86_ubuntu_source_path" translatable="false">http://archive.ubuntu.com/ubuntu/</string>
    <string name="x86_ubuntu_arch" translatable="false">i386</string>
    <!-- x86_64 -->
    <string name="x86_64_ubuntu_source_path" translatable="false">http://archive.ubuntu.com/ubuntu/</string>
    <string name="x86_64_ubuntu_arch" translatable="false">amd64</string>

    <!-- Kali Linux -->
    <string name="kali_suite" translatable="false">kali-rolling</string>
    <!-- arm -->
    <string name="arm_kali_source_path" translatable="false">http://http.kali.org/kali/</string>
    <string name="arm_kali_arch" translatable="false">armhf</string>
    <!-- arm_64 -->
    <string name="arm_64_kali_source_path" translatable="false">http://http.kali.org/kali/</string>
    <string name="arm_64_kali_arch" translatable="false">arm64</string>
    <!-- x86 -->
    <string name="x86_kali_source_path" translatable="false">http://http.kali.org/kali/</string>
    <string name="x86_kali_arch" translatable="false">i386</string>
    <!-- x86_64 -->
    <string name="x86_64_kali_source_path" translatable="false">http://http.kali.org/kali/</string>
    <string name="x86_64_kali_arch" translatable="false">amd64</string>

    <!-- Fedora -->
    <string name="fedora_suite" translatable="false">30</string>
    <!-- arm -->
    <string name="arm_fedora_source_path" translatable="false">http://dl.fedoraproject.org/pub/</string>
    <string name="arm_fedora_arch" translatable="false">armhfp</string>
    <!-- arm_64 -->
    <string name="arm_64_fedora_source_path" translatable="false">http://dl.fedoraproject.org/pub/</string>
    <string name="arm_64_fedora_arch" translatable="false">aarch64</string>
    <!-- x86 -->
    <string name="x86_fedora_source_path" translatable="false">http://dl.fedoraproject.org/pub/</string>
    <string name="x86_fedora_arch" translatable="false">i386</string>
    <!-- x86_64 -->
    <string name="x86_64_fedora_source_path" translatable="false">http://dl.fedoraproject.org/pub/</string>
    <string name="x86_64_fedora_arch" translatable="false">x86_64</string>

    <!-- Arch Linux -->
    <string name="archlinux_suite" translatable="false">latest</string>
    <!-- arm -->
    <string name="arm_archlinux_source_path" translatable="false">http://mirror.archlinuxarm.org/</string>
    <string name="arm_archlinux_arch" translatable="false">armv7h</string>
    <!-- arm_64 -->
    <string name="arm_64_archlinux_source_path" translatable="false">http://mirror.archlinuxarm.org/</string>
    <string name="arm_64_archlinux_arch" translatable="false">aarch64</string>
    <!-- x86 -->
    <string name="x86_archlinux_source_path" translatable="false">http://mirror.archlinux32.org/</string>
    <string name="x86_archlinux_arch" translatable="false">i686</string>
    <!-- x86_64 -->
    <string name="x86_64_archlinux_source_path" translatable="false">http://mirrors.kernel.org/archlinux/</string>
    <string name="x86_64_archlinux_arch" translatable="false">x86_64</string>

    <!-- Slackware -->
    <string name="slackware_suite" translatable="false">14.2</string>
    <!-- arm -->
    <string name="arm_slackware_source_path" translatable="false">http://ftp.arm.slackware.com/slackwarearm/</string>
    <string name="arm_slackware_arch" translatable="false">arm</string>
    <!-- arm_64 -->
    <string name="arm_64_slackware_source_path" translatable="false">http://ftp.arm.slackware.com/slackwarearm/</string>
    <string name="arm_64_slackware_arch" translatable="false">arm</string>
    <!-- x86 -->
    <string name="x86_slackware_source_path" translatable="false">http://mirrors.slackware.com/slackware/</string>
    <string name="x86_slackware_arch" translatable="false">x86</string>
    <!-- x86_64 -->
    <string name="x86_64_slackware_source_path" translatable="false">http://mirrors.slackware.com/slackware/</string>
    <string name="x86_64_slackware_arch" translatable="false">x86_64</string>

    <!-- Alpine Linux -->
    <string name="alpine_suite" translatable="false">latest-stable</string>
    <!-- arm -->
    <string name="arm_alpine_source_path" translatable="false">http://dl-cdn.alpinelinux.org/alpine/</string>
    <string name="arm_alpine_arch" translatable="false">armhf</string>
    <!-- arm_64 -->
    <string name="arm_64_alpine_source_path" translatable="false">http://dl-cdn.alpinelinux.org/alpine/</string>
    <string name="arm_64_alpine_arch" translatable="false">aarch64</string>
    <!-- x86 -->
    <string name="x86_alpine_source_path" translatable="false">http://dl-cdn.alpinelinux.org/alpine/</string>
    <string name="x86_alpine_arch" translatable="false">x86</string>
    <!-- x86_64 -->
    <string name="x86_64_alpine_source_path" translatable="false">http://dl-cdn.alpinelinux.org/alpine/</string>
    <string name="x86_64_alpine_arch" translatable="false">x86_64</string>

    <!-- Docker -->
    <string name="docker_suite" translatable="false">linux</string>
    <!-- arm -->
    <string name="arm_docker_source_path" translatable="false">library/ubuntu:18.04</string>
    <string name="arm_docker_arch" translatable="false">arm</string>
    <!-- arm_64 -->
    <string name="arm_64_docker_source_path" translatable="false">library/ubuntu:18.04</string>
    <string name="arm_64_docker_arch" translatable="false">arm64</string>
    <!-- x86 -->
    <string name="x86_docker_source_path" translatable="false">library/ubuntu:18.04</string>
    <string name="x86_docker_arch" translatable="false">386</string>
    <!-- x86_64 -->
    <string name="x86_64_docker_source_path" translatable="false">library/ubuntu:18.04</string>
    <string name="x86_64_docker_arch" translatable="false">amd64</string>

    <!-- RootFS -->
    <string name="rootfs_suite" translatable="false" />
    <!-- arm -->
    <string name="arm_rootfs_source_path" translatable="false" />
    <string name="arm_rootfs_arch" translatable="false" />
    <!-- arm_64 -->
    <string name="arm_64_rootfs_source_path" translatable="false" />
    <string name="arm_64_rootfs_arch" translatable="false" />
    <!-- x86 -->
    <string name="x86_rootfs_source_path" translatable="false" />
    <string name="x86_rootfs_arch" translatable="false" />
    <!-- x86_64 -->
    <string name="x86_64_rootfs_source_path" translatable="false" />
    <string name="x86_64_rootfs_arch" translatable="false" />

</resources>
"""

adapter_java_content = """package ru.meefik.linuxdeploy.adapter;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

import ru.meefik.linuxdeploy.R;
import ru.meefik.linuxdeploy.model.RepositoryProfile;

public class RepositoryProfileAdapter extends RecyclerView.Adapter<RepositoryProfileAdapter.ViewHolder> {

    private List<RepositoryProfile> repositoryProfiles;
    private OnItemClickListener listener;

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.repository_row, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.setRepository(repositoryProfiles.get(position));
    }

    @Override
    public int getItemCount() {
        return repositoryProfiles != null ? repositoryProfiles.size() : 0;
    }

    public void setRepositoryProfiles(List<RepositoryProfile> repositoryProfiles) {
        this.repositoryProfiles = repositoryProfiles;
        notifyDataSetChanged();
    }

    public void setOnItemClickListener(OnItemClickListener listener) {
        this.listener = listener;
    }

    class ViewHolder extends RecyclerView.ViewHolder {

        private View view;
        private TextView title;
        private TextView subTitle;
        private ImageView icon;

        ViewHolder(@NonNull View itemView) {
            super(itemView);

            view = itemView;
            title = itemView.findViewById(R.id.repo_entry_title);
            subTitle = itemView.findViewById(R.id.repo_entry_subtitle);
            icon = itemView.findViewById(R.id.repo_entry_icon);
        }

        public void setRepository(RepositoryProfile repositoryProfile) {
            int iconRes = R.raw.linux;
            if (repositoryProfile.getType() != null) {
                switch (repositoryProfile.getType()) {
                    case "alpine":
                        iconRes = R.raw.alpine;
                        break;
                    case "archlinux":
                        iconRes = R.raw.archlinux;
                        break;
                    case "debian":
                        iconRes = R.raw.debian;
                        break;
                    case "fedora":
                        iconRes = R.raw.fedora;
                        break;
                    case "kali":
                        iconRes = R.raw.kali;
                        break;
                    case "slackware":
                        iconRes = R.raw.slackware;
                        break;
                    case "ubuntu":
                        iconRes = R.raw.ubuntu;
                        break;
                }
            }

            icon.setImageResource(iconRes);
            title.setText(repositoryProfile.getProfile());
            if (repositoryProfile.getDescription() != null && !repositoryProfile.getDescription().isEmpty())
                subTitle.setText(repositoryProfile.getDescription());
            else
                subTitle.setText(view.getContext().getString(R.string.repository_default_description));

            view.setOnClickListener(v -> {
                if (listener != null)
                    listener.onClick(repositoryProfile);
            });
        }
    }

    public interface OnItemClickListener {
        void onClick(RepositoryProfile repositoryProfile);
    }
}
"""

def pack_files():
    print("--- Start of file: app/src/main/res/values/arrays.xml ---")
    print(arrays_xml_content)
    print("--- End of file: app/src/main/res/values/arrays.xml ---")
    print("\\n" * 3)
    print("--- Start of file: app/src/main/res/values/preferences.xml ---")
    print(preferences_xml_content)
    print("--- End of file: app/src/main/res/values/preferences.xml ---")
    print("\\n" * 3)
    print("--- Start of file: app/src/main/java/ru/meefik/linuxdeploy/adapter/RepositoryProfileAdapter.java ---")
    print(adapter_java_content)
    print("--- End of file: app/src/main/java/ru/meefik/linuxdeploy/adapter/RepositoryProfileAdapter.java ---")

if __name__ == "__main__":
    pack_files()
