Name:          kaffeine
Version:       2.0.3
Release:       1
Summary:       Media Player for KDE4
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kaffeine.kde.org/
Source0:       http://downloads.sourceforge.net/kaffeine/kaffeine-%{version}.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libdvb)
Obsoletes: kaffeine4 < 2.0.3
Obsoletes: kaffeine-engine-xine
Obsoletes: kaffeine-engine-gstreamer
Obsoletes: %{_lib}kaffeine0

%description
Kaffeine is a Multi Engine Media Player.

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
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja

%install
%ninja_install -C build

%find_lang %{name}
