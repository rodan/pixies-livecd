# livecd-stage1 example specfile
# used to build a livecd-stage1

# The subarch can be any of the supported catalyst subarches (like athlon-xp).
# Refer to "man catalyst" or <http://www.gentoo.org/proj/en/releng/catalyst/>
# for supported subarches
# example:
# subarch: athlon-xp
subarch: amd64

# The version stamp is an identifier for the build.  It can be anything you wish# it to be, but it is usually a date.
# example:
# version_stamp: 2006.1
version_stamp: hardened-2015.02

# The target specifies what target we want catalyst to do.  For building a CD,
# we start with livecd-stage1 as our target.
# example:
# target: livecd-stage1
target: livecd-stage1

# The rel_type defines what kind of build we are doing.  This is merely another
# identifier, but it useful for allowing multiple concurrent builds.  Usually,
# default will suffice.
# example:
# rel_type: default
rel_type: default

# This is the system profile to be used by catalyst to build this target.  It is# specified as a relative path from /usr/portage/profiles.
# example:
# profile: default-linux/x86/2006.1
profile: hardened/linux/amd64/no-multilib

# This specifies which snapshot to use for building this target.
# example:
# snapshot: 2006.1
snapshot: 20150204

# This specifies where the seed stage comes from for this target,  The path is
# relative to $clst_sharedir/builds.  The rel_type is also used as a path prefix# for the seed.
# example:
# default/stage3-x86-2006.1
source_subpath: stage3-amd64-hardened+nomultilib-20150108

# These are the hosts used as distcc slaves when distcc is enabled in your
# catalyst.conf.  It follows the same syntax as distcc-config --set-hosts and
# is entirely optional.
# example:
# distcc_hosts: 127.0.0.1 192.168.0.1
distcc_hosts:

# This is an optional directory containing portage configuration files.  It
# follows the same syntax as /etc/portage and should be consistent across all
# targets to minimize problems.
# example:
# portage_confdir: /etc/portage
portage_confdir: /local/catalyst/build/portage

# This option specifies the location to a portage overlay that you would like to
# have used when building this target.
# example:
# portage_overlay: /usr/local/portage
portage_overlay: /local/portage/overlay

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
pkgcache_path: /local/catalyst/packages/hardened-2015.02

# The livecd-stage1 target is where you will build packages for your CD.  These
# packages can be built with customized USE settings.  The settings here are
# additive to the default USE configured by the profile.  For building release
# media, the first thing we do is disable all default USE flags with -* and then
# begin to set our own.
# example:
# livecd/use: -* ipv6 socks5 livecd fbcon ncurses readline ssl
livecd/use: -* hardened pic unicode threads nptl mmx sse sse2 crypt ssl caps ipv6 zlib bzip2 cxx acl pcre readline ncurses udev xattr

#-* livecd hardened pic utf8 unicode readline sse sse2 crypt ssl zlib bzip2 ipv6 nptl caps

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
livecd/packages: 
	app-admin/paxtest
	app-admin/pwgen
	app-arch/bzip2
	app-arch/cpio
	app-arch/gzip
	app-arch/rar
	app-arch/tar
	app-arch/unrar
	app-arch/unzip
	app-arch/zip
	app-editors/vim
	app-misc/beep
	app-misc/pax-utils
	app-misc/screen
	app-shells/bash
	net-analyzer/arpwatch
	net-analyzer/fping
	net-analyzer/macchanger
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/rp-pppoe
	net-dialup/minicom
	net-dns/bind-tools
	net-firewall/iptables
	net-fs/nfs-utils
	net-fs/samba
	net-ftp/lftp
	net-irc/irssi
	net-misc/connect
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/knock
	net-misc/nemesis
	net-misc/openssh
	net-misc/pump
	net-misc/rsync
	net-misc/telnet-bsd
	net-misc/wget
	net-misc/whois
	sys-apps/acl
	sys-apps/attr
	sys-apps/baselayout
	sys-apps/busybox
	sys-apps/paxctl
	sys-apps/coreutils
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/dmapi
	sys-apps/ethtool
	sys-apps/file
	sys-apps/findutils
	sys-apps/gawk
	sys-apps/grep
	sys-apps/hdparm
	sys-apps/hwdata-gentoo
	sys-apps/hwsetup
	sys-apps/iproute2
	sys-apps/kbd
	sys-apps/less
	sys-apps/lshw
	sys-apps/net-tools
	sys-block/parted
	sys-apps/paxctl
	sys-apps/pciutils
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/sg3_utils
	sys-apps/smartmontools
	sys-apps/usbutils
	sys-apps/util-linux
	sys-apps/which
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/jfsutils
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/squashfs-tools
	sys-fs/sysfsutils
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-libs/glibc
	sys-libs/pwdb
	sys-process/htop
	sys-process/lsof
	sys-process/procps
	sys-process/psmisc
	www-client/lynx
	sys-apps/ipmitool
	sys-apps/dmidecode
	app-misc/mc
	net-misc/dhcp
	net-ftp/tftp-hpa
	www-servers/nginx
	sys-process/daemontools-scripts
	sys-process/daemontools
	net-misc/ntp
	sys-apps/hwids
	sys-devel/bc


