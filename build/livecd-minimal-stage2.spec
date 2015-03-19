# livecd-stage2 example specfile
# used to build a livecd-stage2 iso image

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
# we continue with livecd-stage2 as the target.
# example:
# target: livecd-stage2
target: livecd-stage2

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
# default/livecd-stage1-x86-2006.1
source_subpath: default/livecd-stage1-amd64-hardened-2015.02

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

# This allows the optional directory containing the output packages for kernel
# builds.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# kerncache_path: /tmp/kernel
#kerncache_path:

# The fstype is used to determine what sort of CD we should build.  This is
# used to set the type of loopback filesystem that we will use on our CD.
# Possible options are as follows:
# squashfs - This gives the best compression, but requires a kernel patch.
# zisofs - This uses in-kernel compression and is supported on all platforms.
# normal - This creates a loop without compression.
# noloop - This copies the files to the CD directly, without using a loopback.
# example:
# livecd/fstype: squashfs
livecd/fstype: squashfs

# The fsops are a list of optional parameters that can be passed to the tool
# which will create the filesystem specified in livecd/fstype.  It is valid for
# the following fstypes: squashfs, jffs, jffs2, cramfs
# example:
# livecd/fsops: -root-owned
livecd/fsops:

# The cdtar is essentially the bootloader for the CD.  It also holds the main
# configuration for the bootloader.  On x86/amd64, it also can include a small
# memory testing application, called memtest86+.
# example:
# livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-2.13-memtest86+-cdtar.tar.bz2
livecd/cdtar:

# This is the full path and filename to the ISO image that the livecd-stage2
# target will create.
# example:
# livecd/iso: /tmp/installcd-x86-minimal.iso
livecd/iso: /local/livecd/livecd-minimal-2015.02-amd64.iso

# A fsscript is simply a shell script that is copied into the chroot of the CD
# after the kernel(s) and any external modules have been compiled and is
# executed within the chroot.  It can contain any commands that are available
# via the packages installed by our stages or by the packages installed during
# the livecd-stage1 build.  We do not use one for the official release media, so
# there will not be one listed below.  The syntax is simply the full path and
# filename to the shell script that you wish to execute.  The script is copied
# into the chroot by catalyst automatically.
# example:
# livecd/fsscript:
livecd/fsscript: /local/catalyst/build/fsscript.sh

livecd/integritycheck: /local/catalyst/build/integritycheck.sh

# This is where you set the splash theme.  This theme must be present in
# /etc/splash, before the kernel has completed building.
# example:
# livecd/splash_theme: livecd-2006.1
livecd/splash_theme:

# This is a set of arguments that get passed to the bootloader for your CD.  It
# is used on the x86/amd64 release media to enable keymap selection.
# example:
# livecd/bootargs: dokeymap
livecd/bootargs:

# This is a set of arguments that will be passed to genkernel for all kernels
# defined in this target.  It is useful for passing arguments to genkernel that
# are not otherwise available via the livecd-stage2 spec file.
# example:
# livecd/gk_mainargs: --lvm --dmraid
livecd/gk_mainargs:

# This option allows you to specify your own linuxrc script for genkernel to use
# when building your CD.  This is not checked for functionality, so it is up to
# you to debug your own script.  We do not use one for the official release
# media, so there will not be one listed below.
# example:
# livecd/linuxrc:
livecd/linuxrc:

# This option controls quite a bit of catalyst internals and sets up several
# defaults.  Each type behaves slightly differently and is explained below.
# gentoo-release-minimal - This creates an official minimal InstallCD.
# gentoo-release-universal - This creates an official universal InstallCD.
# gentoo-release-livecd - This creates an official LiveCD environment.
# gentoo-gamecd - This creates an official Gentoo GameCD.
# generic-livecd - This should be used for all non-official media.
# example:
# livecd/type: gentoo-release-minimal
livecd/type: generic-livecd

# This is for the README.txt on the root of the CD.  For Gentoo releases, we
# use a default README.txt, and this will be used on your CD if you do not
# provide one yourself.  Since we do not use this for the official releases, it
# is left blank below.
# example:
# livecd/readme:
livecd/readme:

# This is for the CD's message of the day.  It is not required for official
# release media, as catalyst builds a default motd when the livecd/type is set
# to one of the gentoo-* options.  This setting overrides the default motd even
# on official media.  Since we do not use this for the official releases, it is
# left blank below.
# example:
# livecd/motd:
livecd/motd:

# This is for blacklisting modules from being hotplugged that are known to cause
# problems.  Putting a module name here will keep it from being auto-loaded,
# even if ti is detected by hotplug.
# example:
# livecd/modblacklist: 8139cp
livecd/modblacklist:

# This is for adding init scripts to runlevels.  The syntax for the init script
# is the script name, followed by a pipe, followed by the runlevel in which you
# want the script to run.  It looks like spind|default and is space delimited.
# We do not use this on the official media, as catalyst sets up the runlevels
# correctly for us.  Since we do not use this, it is left blank below.
# This option will automatically create missing runlevels
# example:
# livecd/rcadd:
livecd/rcadd:

# This is for removing init script from runlevels.  It is executed after the
# defaults shipped with catalyst, so it is possible to remove the defaults using
# this option.  It can follow the same syntax as livcd/rcadd, or you can leave
# the runlevel off to remove the script from any runlevels detected.  We do not
# use this on the official media, so it is left blank.
# example:
# livecd/rcdel:
livecd/rcdel:

# This overlay is dropped onto the CD filesystem and is outside any loop which
# has been configured.  This is typically used for adding the documentation,
# distfiles, snapshots, and stages to the official media.  These files will not
# be available if docache is enabled, as they are outside the loop.
# example:
# livecd/overlay: /tmp/overlay-minimal
livecd/overlay: cd_overlay

# This overlay is dropped onto the filesystem within the loop.  This can be used
# for such things as updating configuration files or adding anything else you
# would want within your CD filesystem.  Files added here are available when
# docache is used.  We do not use this on the official media, so we will leave
# it blank below.
# example:
# livecd/root_overlay:
livecd/root_overlay: root_overlay_minimal

# This is used by catalyst to copy the specified file to /etc/X11/xinit/xinitrc
# and is used by the livecd/type gentoo-gamecd and generic-livecd.  While the
# file will still be copied for any livecd/type, catalyst will only create the
# necessary /etc/startx for those types, so X will not be automatically started.
# This is useful also for setting up X on a CD where you do not wish X to start
# automatically.  We do not use this on the release media, so it is left blank.
# example:
# livecd/xinitrc:
livecd/xinitrc:

# This is used by catalyst to determine which display manager you wish to
# become the default.  This is used on the official Gentoo LiveCD and is valid
# for any livecd/type.
# example:
# livecd/xdm: gdm
livecd/xdm:

# This is used by catalyst to determine which X session should be started by
# default by the display manager.  This is used on the official Gentoo LiveCD
# and is valid for any livecd/type.
# example:
# livecd/xsession: gnome
livecd/xsession:

# This option is used to create non-root users on your CD.  It takes a space
# separated list of user names.  These users will be added to the following
# groups: users,wheel,audio,games,cdrom,usb
# If this is specified in your spec file, then the first user is also the user
# used to start X. Since this is not used on the release media, it is blank.
# example:
# livecd/users:
livecd/users:

# This option sets the volume ID of the CD created.
# example:
# livecd/volid: Gentoo Linux 2006.1 X86
livecd/volid: Peter's LiveCD 2015.02 amd64

# This option is only used when creating a GameCD.  This specifies the file that
# contains the definitions for GAME_NAME and GAME_EXECUTABLE, which are used by
# the GameCD scripts to set some specific options for the game.  This is not
# used on the release media, and is therefore blank.
# example:
# gamecd/conf:
gamecd/conf:

# This option is used to specify the number of kernels to build and also the
# labels that will be used by the CD bootloader to refer to each kernel image.
# example:
# boot/kernel: gentoo
boot/kernel: gentoo

# This option tells catalyst which kernel sources to merge for this kernel
# label.  This can use normal portage atoms to specify a specific version.
# example:
# boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/sources: grsec-sources

# This option is the full path and filename to a kernel .config file that is
# used by genkernel to compile the kernel this label applies to.
# example:
# boot/kernel/gentoo/config: /tmp/2.6.11-smp.config
boot/kernel/gentoo/config: 3.14.27-s003.config

# This option sets genkernel parameters on a per-kernel basis and applies only
# to this kernel label.  This can be used for building options into only a
# single kernel, where compatibility may be an issue.  Since we do not use this
# on the official release media, it is left blank, but it follows the same
# syntax as livecd/gk_mainargs.
# example:
# boot/kernel/gentoo/gk_kernargs:
boot/kernel/gentoo/gk_kernargs: --makeopts=-j2

# This option sets the USE flags used to build the kernel and also any packages
# which are defined under this kernel label.  These USE flags are additive from
# the default USE for the specified profile.
# example:
# boot/kernel/gentoo/use: pcmcia usb -X
boot/kernel/gentoo/use:

# This option appends an extension to the name of your kernel, as viewed by a
# uname -r/  This also affects any modules built under this kernel label.  This
# is useful for having two kernels using the same sources to keep the modules
# from overwriting each other.  We do not use this on the official media, so it
# is left blank.
# example:
# boot/kernel/gentoo/extraversion:
boot/kernel/gentoo/extraversion:

# This option is for merging kernel-dependent packages and external modules that
# are configured against this kernel label.
# example:
# boot/kernel/gentoo/packages: pcmcia-cs speedtouch slmodem globespan-adsl hostap-driver hostap-utils ipw2100 ipw2200 fritzcapi fcdsl cryptsetup
boot/kernel/gentoo/packages:
	cryptsetup

# This option is only for ppc64 machines.  If used it will create the /etc/yaboot.conf
# entry used for booting a ibm powerpc machine.
# example:
# boot/kernel/gentoo/machine_type: ibm
boot/kernel/gentoo/machine_type:

# This is only supported on ppc64 currently.  This entry sets up the console=
# boot parameters required for sending the output to the appropriate console.
# example:
# boot/kernel/gentoo/console: hvsi0
# boot/kernel/gentoo/console: hvc0
# boot/kernel/gentoo/console: tty0 ttyS0
boot/kernel/gentoo/console:

# This is a list of packages that will be unmerged after all the kernels have
# been built.  There are no checks on these packages, so be careful what you
# add here.  They can potentially break your CD.
# example:
# livecd/unmerge: acl attr autoconf automake bin86 binutils libtool m4 bison ld.so make perl patch linux-headers man-pages sash bison flex gettext texinfo ccache distcc man groff lib-compat miscfiles rsync sysklogd bc lcms libmng genkernel diffutils libperl gnuconfig gcc-config gcc bin86 cpio cronbase ed expat grub lilo help2man libtool gentoo-sources
livecd/unmerge:
	app-admin/eselect
	app-admin/eselect-python
	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-editors/nano
	app-portage/portage-utils
	app-text/build-docbook-catalog
	app-text/docbook-xml-dtd
	app-text/docbook-xsl-stylesheets
	app-text/openjade
	app-text/opensp
	app-text/po4a
	app-text/sgml-common
	app-vim/gentoo-syntax
	dev-lang/perl
	dev-lang/python
	dev-lang/python-exec
	dev-perl/Locale-gettext
	dev-perl/SGMLSpm
	dev-perl/TermReadKey
	dev-perl/Text-CharWidth
	dev-perl/Text-WrapI18N
	dev-perl/XML-Parser
	perl-core/File-Temp
	dev-python/pypax
	dev-python/pyxattr
	dev-python/setuptools
	sys-apps/texinfo
	sys-apps/openrc
	sys-apps/tcp-wrappers
	sys-boot/grub
	sys-devel/autoconf
	sys-devel/autoconf-wrapper
	sys-devel/automake
	sys-devel/automake-wrapper
	sys-devel/binutils
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/libtool
	sys-devel/m4
	sys-devel/make
	sys-kernel/linux-headers
	sys-fs/udev
    genkernel
    help2man
    sandbox
	net-analyzer/arpwatch
	net-fs/nfs-utils
	net-fs/samba
	net-ftp/tftp-hpa
	net-misc/dhcp
	net-misc/knock
	net-misc/nemesis
	net-nds/rpcbind
	sys-apps/kbd
	sys-apps/man-pages-posix
	sys-process/daemontools
	sys-process/daemontools-scripts
	www-servers/nginx
	sys-apps/sg3_utils
	sys-apps/hwsetup
	sys-apps/hwdata-gentoo
	sys-apps/lshw
	#sys-apps/man-db
	#sys-apps/man-pages
	#sys-apps/groff

# This option is used to empty the directories listed.  It is useful for getting
# rid of files that don't belong to a particular package, or removing files from
# a package that you wish to keep, but won't need the full functionality.
# example:
# livecd/empty: /var/tmp /var/cache /var/db /var/empty /var/lock /var/log /var/run /var/spool /var/state /tmp /usr/portage /usr/share/man /usr/share/info /usr/share/unimaps /usr/include /usr/share/zoneinfo /usr/share/dict /usr/share/doc /usr/share/ss /usr/share/state /usr/share/texinfo /usr/lib/python2.2 /usr/lib/portage /usr/share/gettext /usr/share/i18n /usr/share/rfc /usr/lib/X11/config /usr/lib/X11/etc /usr/lib/X11/doc /usr/src /usr/share/doc /usr/share/man /root/.ccache /etc/cron.daily /etc/cron.hourly /etc/cron.monthly /etc/cron.weekly /etc/logrotate.d /etc/rsync /usr/lib/awk /usr/lib/ccache /usr/lib/gcc-config /usr/lib/nfs /usr/local /usr/diet/include /usr/diet/man /usr/share/consolefonts/partialfonts /usr/share/consoletrans /usr/share/emacs /usr/share/gcc-data /usr/share/genkernel /etc/bootsplash/gentoo /etc/bootsplash/gentoo-highquality /etc/splash/gentoo /etc/splash/emergence /usr/share/gnuconfig /usr/share/lcms /usr/share/locale /etc/skel
livecd/empty:
    /var/tmp
    /var/cache
    /var/empty
    /var/cache
    /var/lock
    /tmp
    /usr/portage
    /usr/share/unimaps
    /usr/include
    /usr/share/zoneinfo
    /usr/share/dict
    /usr/share/doc
    /usr/share/ss
    /usr/lib/python2.4
    /usr/share/i18n
    /usr/src
    /usr/share/doc
    /root/.ccache
    /var/db
	/usr/share/man/??
	/usr/share/man/??\.*
	/usr/share/man/??_*
	#/usr/share/man

# This option tells catalyst to clean specific files from the filesystem and is
# very usefu in cleaning up stray files in /etc left over after livecd/unmerge.
# example:
# livecd/rm: /lib/*.a /usr/lib/*.a /usr/lib/gcc-lib/*/*/libgcj* /etc/dispatch-conf.conf /etc/etc-update.conf /etc/*- /etc/issue* /etc/portage/make.conf /etc/man.conf /etc/*.old /root/.viminfo /usr/sbin/bootsplash* /usr/sbin/fb* /usr/sbin/fsck.cramfs /usr/sbin/fsck.minix /usr/sbin/mkfs.minix /usr/sbin/mkfs.bfs /usr/sbin/mkfs.cramfs /lib/security/pam_access.so /lib/security/pam_chroot.so /lib/security/pam_debug.so /lib/security/pam_ftp.so /lib/security/pam_issue.so /lib/security/pam_mail.so /lib/security/pam_motd.so /lib/security/pam_mkhomedir.so /lib/security/pam_postgresok.so /lib/security/pam_rhosts_auth.so /lib/security/pam_userdb.so /usr/share/consolefonts/1* /usr/share/consolefonts/7* /usr/share/consolefonts/8* /usr/share/consolefonts/9* /usr/share/consolefonts/A* /usr/share/consolefonts/C* /usr/share/consolefonts/E* /usr/share/consolefonts/G* /usr/share/consolefonts/L* /usr/share/consolefonts/M* /usr/share/consolefonts/R* /usr/share/consolefonts/a* /usr/share/consolefonts/c* /usr/share/consolefonts/dr* /usr/share/consolefonts/g* /usr/share/consolefonts/i* /usr/share/consolefonts/k* /usr/share/consolefonts/l* /usr/share/consolefonts/r* /usr/share/consolefonts/s* /usr/share/consolefonts/t* /usr/share/consolefonts/v* /etc/splash/livecd-2006.1/16* /etc/splash/livecd-2006.1/12* /etc/splash/livecd-2006.1/6* /etc/splash/livecd-2006.1/8* /etc/splash/livecd-2006.1/images/silent-16* /etc/splash/livecd-2006.1/images/silent-12* /etc/splash/livecd-2006.1/images/silent-6* /etc/splash/livecd-2006.1/images/silent-8* /etc/splash/livecd-2006.1/images/verbose-16* /etc/splash/livecd-2006.1/images/verbose-12* /etc/splash/livecd-2006.1/images/verbose-6* /etc/splash/livecd-2006.1/images/verbose-8* /etc/portage/make.conf.example /etc/make.globals /etc/resolv.conf
livecd/rm:
	/boot
	/etc/cron*
	/etc/eselect
	/lib/*.a
	/lib/modules
	/lib/udev
	/usr/bin/i386-pc*
	/usr/bin/yacc
	/sbin/rescan-scsi-bus
	/usr/*-pc-linux-gnu
	/usr/include
	/usr/portage
	/usr/bin/c++*
	/usr/share/aclocal
	/usr/share/applications
	/usr/share/bash-completion
	/usr/share/gdb
	/usr/share/gtk-doc
	/usr/share/locale
	/usr/share/pixmaps
	/usr/share/pkgconfig
	/usr/share/portage
	/usr/share/sgml
	/usr/share/info
	/usr/share/build*
	/usr/share/misc/pci.ids
	/usr/share/misc/usb.ids
	/local
	/usr/local
	/usr/lib/gconv
	/usr/lib/portage
	/usr/lib/systemd
	/usr/lib64/python*
	/usr/lib64/libpython*
	/usr/lib64/perl5
	/usr/lib64/pkgconfig
	/usr/bin/idle*
	/usr/bin/pydoc*
	/usr/bin/2to3*
	/usr/bin/python*
	/usr/bin/x86_64*
	/etc/conf.d
	/etc/init.d
	/etc/env.d
	/etc/runlevels
	/etc/sgml
	/etc/systemd
	/etc/udev
	/etc/xinetd.d
	/media
	/var/lib/gentoo/news
	/var/lock
	/run/openrc
	/usr/sbin/ntpd
	/usr/bin/calc_tickadj
	/usr/bin/ntp-keygen
	/usr/bin/ntp-wait
	/usr/bin/ntpdc
	/usr/bin/ntpq
	/usr/bin/ntptime
	/usr/bin/ntptrace
	/usr/bin/sntp
	/usr/bin/tickadj
	/var/log/*
