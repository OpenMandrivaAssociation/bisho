Name: bisho
Summary: Moblin's web services settings
Group: System/Configuration/Other
Version: 0.12
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: bisho-0.12-format.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: mojito-devel
BuildRequires: libgtk+2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libsoup-2.4-devel
BuildRequires: librest-devel
BuildRequires: unique-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gettext

%description
Moblin's web services settings

%prep
%setup -q 
%patch0 -p1
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
