Summary:	CD Drive plugin for the Xfce panel
Name:		xfce4-cddrive-plugin
Version:	0.0.1
Release:	%mkrel 9
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cddrive-plugin
Source0:	http://goodies.xfce.org/_media/projects/panel-plugins/%{name}-%{version}.tar.bz2
Patch0:		xfce4-cddrive-plugin-libtool-fixes.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	exo-devel
BuildRequires:	intltool
BuildRequires:	dbus-glib-devel
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-cddrive-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A CD Drive control panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%define Werror_cflags %nil
./autogen.sh

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} 

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
