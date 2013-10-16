Summary:	Fax configuration tool
Name:		drakfax
Version:	0.17.3
Release:	11
License:	GPLv2+
Group:		System/Configuration/Networking
Url:		https://qa.mandriva.com
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch

Buildrequires:	perl-MDK-Common-devel
Requires:	drakxtools
Requires:	hylafax-client
Requires:	perl-Gtk2

%description
drakfax is a tool to setup a fax (modem fax), to send and receive 
facsimiles.
drakfax also provides a client to send facsimile locally or via 
a hylafax server.

%prep
%setup -q

%build

%install
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

%files -f drakfax.lang
%doc FEATURES
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/drakfax
%{_datadir}/applications/mandriva-*.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png

