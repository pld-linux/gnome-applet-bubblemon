Summary:	Bubbling Load Monitoring Applet for the GNOME Panel
Name:		bubblemon
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.student.nada.kth.se/~d92-jwa/code/bubblemon/%{name}-%{version}.tar.gz
URL:		http://www.nada.kth.se/~d92-jwa/code/
Requires:	gnome-libs >= 1.2
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a panel applet that displays the CPU and memory load as a
bubbling liquid. The latest version is available off
http://www.nada.kth.se/~d92-jwa/code. Choose Add
Applet->Monitors->Bubbling Load Monitor in your GNOME Panel.

%prep
%setup -q -n bubblemon-%{version}

%build
%configure \
	--with-all-linguas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnulocaledir=/tmp/bubblemon-1.2.0%{_datadir}/locale

gzip -9nf AUTHORS FAQ README FAQ PROFILING TRANSLATIONS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/bubblemon-gnome1
%{_sysconfdir}/CORBA/servers/bubblemon-gnome1.gnorba
%{_datadir}/applets/Monitors/bubblemon-gnome1.desktop
%{_datadir}/locale/*/LC_MESSAGES/bubblemon.mo
%{_mandir}/man1/bubblemon-gnome1.1*
%lang(hu) %{_mandir}/hu/man1/bubblemon-gnome1.1*
%lang(sv) %{_mandir}/sv/man1/bubblemon-gnome1.1*
