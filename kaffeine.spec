Name:          kaffeine
Version:       1.2.2
Release:       %mkrel 2
Summary:       Media Player for KDE4
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kaffeine.kde.org/
Source:        http://downloads.sourceforge.net/kaffeine/kaffeine-%{version}.tar.gz
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel
BuildRequires: libxine-devel
Requires:      xine-plugins
Requires:      qt4-database-plugin-sqlite
Requires:      kdebase4-runtime
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: kaffeine4 = %version
Obsoletes: kaffeine4 < 1.0
Obsoletes: kaffeine-engine-xine
Obsoletes: kaffeine-engine-gstreamer
Obsoletes: %{_lib}kaffeine0

%description
Kaffeine is a KDE4 Multi Engine Media Player.

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/kaffeine
%_kde_bindir/kaffeine-xbu
%_kde_appsdir/kaffeine
%_kde_appsdir/profiles/kaffeine.profile.xml
%_kde_appsdir/solid/actions/*
%_kde_iconsdir/*/*/*/*
%_kde_datadir/applications/kde4/kaffeine.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make 

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %{buildroot}
