# Changed by Makefile of cvs.
# DON'T MODIFY THIS FILE OUT OF CVS!

%define version 0.12
%define name drakfax

Summary:	Fax configuration tool
Name:		%{name}
Version:	%{version}
Release:    %mkrel 1
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
URL:		https://qa.mandriva.com
Group:		System/Configuration/Other
Requires:	drakxtools >= 10-0.9mdk, perl-Gtk2 >= 1.023-2mdk, hylafax-client >= 4.1.8-2mdk
Buildrequires: perl-MDK-Common-devel
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
drakfax is a tool to setup a fax (modem fax), to send and receive 
facsimiles.
drakfax also provides a client to send facsimile locally or via 
a hylafax server.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install 

#install lang
%{find_lang} drakfax

#install menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}):\ 
needs="x11" \
icon="drakfax.png" \
section="Office/Communications/Fax" \
title="DrakFax" \
longtitle="A client and server fax configuration tool" \
command="/usr/bin/drakfax" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-drakfax.desktop << EOF
[Desktop Entry]
Name=A client and server fax configuration tool
Comment=A client and server fax configuration tool
Exec=/usr/bin/drakfax
Icon=/usr/share/icons/drakfax.png
Type=Application
Categories=GTK;X-MandrivaLinux-System-Configuration;Settings;
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files -f drakfax.lang
%defattr(-,root,root)
%doc COPYING FEATURES
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/drakfax
%{_datadir}/applications/mandriva-*.desktop
%{_menudir}/%{name}
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png


