Name:          kaffeine
Version:       1.3.1
Release:       1
Summary:       Media Player for KDE4
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kaffeine.kde.org/
Source0:       http://downloads.sourceforge.net/kaffeine/kaffeine-%{version}.tar.gz
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libvlc)
Requires:      qt4-database-plugin-sqlite
Requires:      kdebase4-runtime
Provides: kaffeine4 = %version
Obsoletes: kaffeine4 < 1.0
Obsoletes: kaffeine-engine-xine
Obsoletes: kaffeine-engine-gstreamer
Obsoletes: %{_lib}kaffeine0

%description
Kaffeine is a KDE4 Multi Engine Media Player.

%files -f %name.lang
%_kde_bindir/dtvdaemon
%_kde_bindir/kaffeine
%_kde_appsdir/kaffeine
%_kde_appsdir/profiles/kaffeine.profile.xml
%_kde_appsdir/solid/actions/*
%_kde_iconsdir/*/*/*/*
%_kde_datadir/applications/kde4/kaffeine.desktop
%_kde_datadir/appdata/kaffeine.appdata.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%apply_patches

%build
%cmake_kde4
%make 

%install
%makeinstall_std -C build

%find_lang %name

