Summary:	Bubbling Load Monitoring Applet for the GNOME Panel
Summary(pl.UTF-8):	Aplet z bulgoczącym monitorem obciążenia dla panelu GNOME
Name:		gnome-applet-bubblemon
Version:	1.2.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.student.nada.kth.se/~d92-jwa/code/bubblemon/bubblemon-%{version}.tar.gz
# Source0-md5:	f4888d1144ed0328895f1d17a5252d90
URL:		http://www.nada.kth.se/~d92-jwa/code/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-core-devel
BuildRequires:	libgtop-devel
Obsoletes:	bubblemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
This is a panel applet that displays the CPU and memory load as a
bubbling liquid. The latest version is available off
http://www.nada.kth.se/~d92-jwa/code/. Choose Add
Applet->Monitors->Bubbling Load Monitor in your GNOME Panel.

%description -l pl.UTF-8
To jest aplet panelu GNOME wyświetlający obciążenie procesora i
pamięci jako bulgoczącą ciecz. Dodać aplet do panelu można poprzez
Add Applet->Monitors->Bubbling Load Monitor w paneli GNOME.

%prep
%setup -q -n bubblemon-%{version}

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--with-all-linguas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang bubblemon

%clean
rm -rf $RPM_BUILD_ROOT

%files -f bubblemon.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ README PROFILING TRANSLATIONS TODO
%attr(755,root,root) %{_bindir}/bubblemon-gnome1
%{_sysconfdir}/CORBA/servers/bubblemon-gnome1.gnorba
%{_mandir}/man1/bubblemon-gnome1.1*
%lang(hu) %{_mandir}/hu/man1/bubblemon-gnome1.1*
%lang(sv) %{_mandir}/sv/man1/bubblemon-gnome1.1*
%{_datadir}/applets/Monitors/bubblemon-gnome1.desktop
%{_pixmapsdir}/*
