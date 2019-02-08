Name:          kaffeine
Version:       2.0.16
Release:       1
Summary:       Media Player for Plasma 5
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kaffeine.kde.org/
#Source0:       https://github.com/KDE/kaffeine/archive/v%{version}-.tar.gz
Source0:       http://download.kde.org/stable/kaffeine/%{name}-%{version}-2.tar.xz
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libdvbv5)
BuildRequires: pkgconfig(xscrnsaver)
Obsoletes: kaffeine4 < 2.0.3
Obsoletes: kaffeine-engine-xine
Obsoletes: kaffeine-engine-gstreamer
Obsoletes: %{_lib}kaffeine0

%description
Kaffeine is a Multi Engine Media Player.

%files -f %name.lang
%{_kde5_bindir}/kaffeine
%{_kde5_datadir}/%{name}/
%{_kde5_datadir}/profiles/%{name}.profile.xml
%{_kde5_datadir}/solid/actions/*.desktop
%{_kde5_iconsdir}/*/*/*/*
%{_kde5_applicationsdir}/org.kde.%{name}.desktop
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-2
%apply_patches

#export CC=gcc
#export CXX=g++
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html --with-man
