%define version 0.17.3
%define name drakfax

Summary:	Fax configuration tool
Name:		%{name}
Version:	%{version}
Release:	%mkrel 5
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+
URL:		https://qa.mandriva.com
Group:		System/Configuration/Networking
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	drakxtools >= 10-0.9mdk, perl-Gtk2 >= 1.023-2mdk, hylafax-client >= 4.1.8-2mdk
Buildrequires:	perl-MDK-Common-devel
BuildArch:	noarch

%description
drakfax is a tool to setup a fax (modem fax), to send and receive 
facsimiles.
drakfax also provides a client to send facsimile locally or via 
a hylafax server.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot} install 

#install lang
%{find_lang} drakfax

#install menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-drakfax.desktop << EOF
[Desktop Entry]
Name=Fax configuration
Comment=A client and server fax configuration tool
Exec=%{_bindir}/%{name}
Icon=%{name}
Type=Application
Categories=GTK;Settings;
NoDisplay=true
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f drakfax.lang
%defattr(-,root,root)
%doc FEATURES
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/drakfax
%{_datadir}/applications/mandriva-*.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png


