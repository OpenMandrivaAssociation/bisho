Name: bisho
Summary: MeeGo's web services settings
Group: System/Configuration/Other
Version: 0.27.2
Release: %mkrel 3
License: LGPL 2.1
URL: https://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
BuildRequires: libsocialweb-devel
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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MeeGo's web services settings

%package devel
Summary: Bisho development libraries and files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Bisho development libraries and files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/*.desktop
%find_lang bisho

rm %{buildroot}%{_libdir}/bisho/*la
rm %{buildroot}%{_libdir}/control-center-1/extensions/*la
rm %{buildroot}%{_libdir}/*la


%clean
rm -rf %{buildroot}

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/bisho.schemas \
    > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
    %{_sysconfdir}/gconf/schemas/bisho.schemas \
    > /dev/null || :
fi

%post
/sbin/ldconfig
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/bisho.schemas  > /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%postun
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| :

%files -f bisho.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/bisho.png
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bisho/*.so
%{_libdir}/control-center-1/extensions/*.so
%{_libdir}/libbisho-common.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libbisho-common.so
%{_includedir}/bisho/*
