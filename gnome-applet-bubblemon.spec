Summary: Bubbling Load Monitoring Applet for the GNOME Panel
Name: bubblemon
Version: 1.2.0
Release: 1
Source: bubblemon-1.2.0.tar.gz
Buildroot: /tmp/bubblemon-1.2.0
Packager: Johan Walles (d92-jwa@nada.kth.se)
URL: http://www.nada.kth.se/~d92-jwa/code/
Copyright: GPL
Group: User Interface/GNOME Applets
Requires: gnome-libs >= 1.2

%description
This is a panel applet that displays the CPU and memory
load as a bubbling liquid.  The latest version is available
off http://www.nada.kth.se/~d92-jwa/code.  Choose
Add Applet->Monitors->Bubbling Load Monitor in your GNOME Panel.

%changelog

%prep

%setup

./configure --with-all-linguas --prefix=/usr

%build

make

%install

# The following line is a workaround for a problem with gettext.
make install-strip DESTDIR=/tmp/bubblemon-1.2.0 gnulocaledir=/tmp/bubblemon-1.2.0/usr/share/locale

# The following line is what *should* be used if the gettext
# Makefile.in would be working like the Makefile.ins generated by
# automake.  The problem has already been reported to the Debian bug
# tracking system under numbers #38414, #41823 and #52571.  Actually,
# those bugs have now been fixed, but since the above syntax still
# works I'll just leave it alone.

#DESTDIR=/tmp/bubblemon-1.2.0 make -e install-strip

%clean

make clean

%files 

/usr/bin/bubblemon-gnome1
/etc/CORBA/servers/bubblemon-gnome1.gnorba
/usr/share/applets/Monitors/bubblemon-gnome1.desktop
/usr/share/locale/*/LC_MESSAGES/bubblemon.mo

%doc AUTHORS COPYING FAQ README FAQ PROFILING TRANSLATIONS TODO

/usr/man/man1/bubblemon-gnome1.1*
/usr/man/sv/man1/bubblemon-gnome1.1*
/usr/man/hu/man1/bubblemon-gnome1.1*
