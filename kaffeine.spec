%define prever pre3

Name:          kaffeine
Version:       1.0
Release:       %mkrel -c %prever 1
Summary:       Media Player for KDE4
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kaffeine.kde.org/
Source:        http://sourceforge.net/projects/kaffeine/files/kaffeine/%{name}-%{version}-%{prever}/%{name}-%{version}-%{prever}.tar.gz
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel
BuildRequires: libxine-devel
BuildRequires: libdvb-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: kaffeine4 = %version
Obsoletes: kaffeine4 < 1.0
Obsoletes: kaffeine-engine-xine
Obsoletes: kaffeine-engine-gstreamer
Obsoletes: %{_lib}kaffeine0

%description
Kaffeine is a KDE4 Multi Engine Media Player.

%files 
%defattr(-,root,root)
%_kde_bindir/kaffeine
%_kde_bindir/kaffeine-xbu
%_kde_libdir/kde4/kaffeinedvb.so
%_kde_appsdir/kaffeine
%_kde_appsdir/solid/actions/*
%_kde_datadir/locale/*
%_kde_iconsdir/*/*/*/*
%_kde_datadir/applications/kde4/kaffeine.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%{prever}

%build
%cmake_kde4
%make 

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}
