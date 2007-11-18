Summary:	CD Drive plugin for the Xfce panel
Name:		xfce4-cddrive-plugin
Version:	0.0.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cddrive-plugin
Source0:	http://goodies.xfce.org/_media/projects/panel-plugins/%{name}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4.1
BuildRequires:	xfce-panel-devel >= 4.4.1
BuildRequires:	perl(XML::Parser)
BuildRequires:	exo-devel
BuildRequires:	intltool
BuildRequires:	dbus-glib-devel
Obsoletes:	xfce-cddrive-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A CD Drive control panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

sh autogen.sh
 
%build
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
%doc README ChangeLog COPYING AUTHORS INSTALL
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*