%define version 0.16
%define rel 1
%define snapshot git20091027
%define release %mkrel 0.%{snapshot}.%{rel}

%define sversion %{version}%{snapshot}

Name: bisho
Summary: Moblin's web services settings
Group: System/Configuration/Other
Version: %{version}
License: LGPL 2.1
URL: http://www.moblin.org
Release: %{release}
Source0: %{name}-%{sversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: mojito-devel
BuildRequires: libgtk+2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libsoup-2.4-devel
BuildRequires: librest-devel
BuildRequires: unique-devel
BuildRequires: nbtk-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gettext

%description
Moblin's web services settings

%prep
%setup -q -n %{name}-%{sversion} 
perl -pi -e 's,&& ./configure.*,,' ./autogen.sh

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/bisho.png
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/locale/*
