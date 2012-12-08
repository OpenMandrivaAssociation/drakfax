%define version 0.17.3
%define name drakfax

Summary:	Fax configuration tool
Name:		%{name}
Version:	%{version}
Release:	%mkrel 7
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
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install 

#install lang
%{find_lang} drakfax

#install menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-drakfax.desktop << EOF
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
rm -rf $RPM_BUILD_ROOT

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




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.17.3-5mdv2011.0
+ Revision: 663851
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17.3-4mdv2011.0
+ Revision: 604816
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17.3-3mdv2010.1
+ Revision: 522485
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.17.3-2mdv2010.0
+ Revision: 413379
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.17.3-1mdv2009.1
+ Revision: 367438
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.17.2-1mdv2009.1
+ Revision: 362301
- translation updates

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.17.1-2mdv2009.1
+ Revision: 350836
- rebuild

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.17.1-1mdv2009.0
+ Revision: 286971
- renamed Uzbek translations to follow the libc standard (#35090)
- translation updates

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.17-5mdv2009.0
+ Revision: 218424
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.17-5mdv2008.1
+ Revision: 192099
- renamed Uzbek translations to follow the libc standard (#35090)
- translation updates

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.15-5mdv2008.1
+ Revision: 190091
- fix group
- better group
- fix no-buildroot-tag

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.15-3mdv2008.1
+ Revision: 149223
- rebuild
- kill re-definition of %%buildroot on Pixel's request

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 0.15-2mdv2008.0
+ Revision: 94265
- updated translation

* Wed Sep 19 2007 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2008.0
+ Revision: 90960
- hide menu entry by default
- fix short title (#33764)

* Sat Sep 15 2007 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2008.0
+ Revision: 86823
- translation snapshot

* Sat Sep 15 2007 Adam Williamson <awilliamson@mandriva.org> 0.12-2mdv2008.0
+ Revision: 85816
- rebuild for 2008
- drop old menu and X-Mandriva menu category
- Fedora license policy


* Tue Mar 13 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.12-1mdv2007.1
+ Revision: 142427
- add XDG menu entry
- Import drakfax

* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.12-1mdv2007.1
- translation snapshot

* Fri Apr 14 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.11-1mdk
- do not add extra stacked quotes in drakfax config file (#21947)
- fix empty subdialogs (#21946)
- sanitize GUI:
  o make some buttons aligned
  o remove from toolbar icons that are already availlable from the
    menu bar and make what's left of toolbar be actually what it is,
    that is the very tabs of the notebook

* Tue Sep 20 2005 Daouda LO <daouda@mandriva.com> 0.10-7mdk
- remove warnings 
- po updates

* Sun May 08 2005 Daouda LO <daouda@mandriva.com> 0.10-6mdk
- switch to Mandriva

* Fri Jan 21 2005 Daouda LO <daouda@mandrakesoft.com> 0.10-5mdk
- fix main loop

* Wed Oct 06 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.10-4mdk
- Rebuild

* Tue Oct 05 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.10-3mdk
- updated po files

* Wed Sep 15 2004 Daouda LO <daouda@mandrakesoft.com> 0.10-2mdk
- po updates
- bump release to 2mdk

* Sat May 22 2004 Daouda LO <daouda@mandrakesoft.com> 0.10-0.6mdk
- Buildrequires (per Oyvind)

* Thu Mar 25 2004 Daouda LO <daouda@mandrakesoft.com> 0.10-0.5mdk
- launch drakfax_server from mcc
- remove banner when embedded

