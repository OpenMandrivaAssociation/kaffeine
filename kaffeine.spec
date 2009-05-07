Name:          kaffeine
Version:       1.0
Release:       %mkrel 0.1
Summary:       Media Player for KDE4
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kaffeine.kde.org/
Source:        %{name}-%{version}-pre1.tar.gz
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel
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
%_kde_appsdir/kaffeine
%_kde_appsdir/solid/actions/*
%_kde_datadir/locale/*
%_kde_iconsdir/*/*/*/*
%_kde_datadir/applications/kde4/kaffeine.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}-pre1

%build
%cmake_kde4

%make 

%install
cd build
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}
