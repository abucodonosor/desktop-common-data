%define name mandrake_desk
%define version 8.0
%define release 6mdk

Summary:	The Desktop configuration files for Linux Mandrake
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		System/Configuration/Other
Icon:		mandrake-small.xpm
Packager:	David BAUDENS <baudens@mandrakesoft.com>

# get the source from our cvs repository (see	
# http://www.linuxmandrake.com/en/cvs.php3)
Source:		mandrake_desk.tar.bz2
Source1:	eazel-engine-0.3.tar.bz2
Source2:	gtkrc
#Patch:          mandrake_desk-8.0-zip_mount_typo.patch.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
This package contains useful icons, backgrounds and others goodies for the
Mandrake desktop.

%prep

%setup -q -n %name
#%patch -p1
%build
find . -type 'd' -name 'CVS'|xargs rm -rf

# Dadou - 8.0-4mdk - Very very Quick and very very very dirty hack to make FredL happy.
#                    It will be done nicely later
(
cd $RPM_BUILD_DIR/mandrake_desk
tar yxf %SOURCE1
cd eazel-engine-0.3/
%configure
#perl -pi -e "s|imgdir =.*|imgdir = %_datadir/pixmaps/mdk/|" Makefile
#perl -pi -e "s|imgdir =.*|imgdir = %_datadir/pixmaps/mdk/|" data/Makefile
%make
make install DESTDIR=%buildroot
rm -fr %buildroot/%_datadir/control-center/
mkdir -p %buildroot/etc/gtk
install -m644 %SOURCE2 %buildroot/etc/gtk
rm -fr %buildroot/%_datadir/themes
)

%install
make install RPM_BUILD_ROOT=$RPM_BUILD_ROOT mandir=%{_mandir}

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmsession.d/

rm -f special/mandrake-small.xpm

cd $RPM_BUILD_ROOT%_datadir/faces
cp user-hat-mdk.png root.png
cp root.png root
cp user-default-mdk.png default.png

cd $RPM_BUILD_ROOT%_datadir/pixmaps/backgrounds/linux-mandrake
ln -s ICE-640.png PP5-640.png
ln -s ICE-800.png PP5-800.png
ln -s ICE-1024.png PP5-1024.png
ln -s ICE-1280.png PP5-1280.png
ln -s ICE-1600.png PP5-1600.png
ln -s nature-640.png PP6-640.png
ln -s nature-800.png PP6-800.png
ln -s nature-1024.png PP6-1024.png
ln -s nature-1280.png PP6-1280.png
ln -s nature-1600.png PP6-1600.png
ln -s logoMDK1-640.png PP7-640.png
ln -s logoMDK1-800.png PP7-800.png
ln -s logoMDK1-1024.png PP7-1024.png
ln -s logoMDK1-1280.png PP7-1280.png
ln -s logoMDK1-1600.png PP7-1600.png

ln -s ICE-640.png DKP5-640.png
ln -s ICE-800.png DKP5-800.png
ln -s ICE-1024.png DKP5-1024.png
ln -s ICE-1280.png DKP5-1280.png
ln -s ICE-1600.png DKP5-1600.png
ln -s nature-640.png DKP6-640.png
ln -s nature-800.png DKP6-800.png
ln -s nature-1024.png DKP6-1024.png
ln -s nature-1280.png DKP6-1280.png
ln -s nature-1600.png DKP6-1600.png
ln -s logoMDK1-640.png DKP7-640.png
ln -s logoMDK1-800.png DKP7-800.png
ln -s logoMDK1-1024.png DKP7-1024.png
ln -s logoMDK1-1280.png DKP7-1280.png
ln -s logoMDK1-1600.png DKP7-1600.png

%post
if [ -f /etc/X11/window-managers.rpmsave ];then
	/usr/sbin/convertsession -f /etc/X11/window-managers.rpmsave || exit 0
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%config /etc/skel/Desktop/
%config /etc/skel/.kde
%config /etc/gtk/gtkrc
%doc TRANSLATORS special/*
%dir /etc/X11/wmsession.d/
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/faces
%{_iconsdir}/*.xpm
%{_miconsdir}/*
%{_liconsdir}/*
%{_datadir}/pixmaps/backgrounds/linux-mandrake
%{_datadir}/pixmaps/mdk
%_datadir/eazel-engine
%{_libdir}/mc/desktop-scripts/mandrake.links.sh
%{_libdir}/gtk/themes/engines/*
%{_mandir}/*/*
%{_datadir}/lmdk/

%changelog
* Thu Apr 12 2001 Daouda LO <daouda@mandrakesoft.com> 8.0-6mdk
- remove kde dir and kdelnks 
- cvs resync 

* Wed Apr 4 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-5mdk
- fix zip mount point typo

* Thu Mar 29 2001 David BAUDENS <baudens@mandrakesoft.com> - 8.0-4mdk
- Add new GTK theme

* Tue Mar 20 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-3mdk
- remove Drakconf workaround patch

* Tue Mar 20 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-2mdk
- better workaround for DrakConf, waiting for Holy Traktopel to show me the way to fix. 

* Wed Mar 14 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-1mdk
- workaround to DrakConf crash (ugly) 
- update version number to 8.0 

* Mon Oct 09 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-18mdk
- Fix bugs 750, 732, 625, 623

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-17mdk
- Fix META_CLASS detection
- Redraw some icons (for FPons)

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-16mdk
- Fix faces for userdrake

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-15mdk
- Fix a typo

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-14mdk
- Fix icon for DrakConf

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-12mdk
- Fix bug # 639

* Thu Oct 05 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-11mdk
- Add icons for Pixel

* Wed Oct 04 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-10mdk
- Really create destdir when not present

* Wed Oct 04 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-9mdk
- More background & create destdir when not present (createbackground.sh)

* Tue Oct 02 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-8mdk
- Change default background names in createbackground.sh

* Mon Oct 02 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-7mdk
- Add createbackground.sh from Frederic CROZAT
- Remove old default background

* Fri Sep 22 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-6mdk
- New PATH for Linux-Mandrake backgrounds
- Put/remove backgrounds

* Wed Sep 20 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-5mdk
- Add new image for XFdrake
- Remove Templates and Autostart from /etc/skel/Desktop

* Tue Sep 05 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-4mdk
- Add KDM pixmap

* Fri Sep 01 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-3mdk
- Add some icons in faces (aka make Pixel happy)

* Fri Sep 01 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-2mdk
- Fix CD-ROM & Co links (KDE)

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-1mdk
- KDE 2 compliant

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 7.1-1mdk
- Add new Chmouel chksession
- Update description

* Thu Aug 24 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-9mdk
- Add a link "root" to make GDM happy
- Remove old links

* Wed Aug 23 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-8mdk
- Add links default.png and root.png to make KDM happy

* Wed Aug 23 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-7mdk
- Convert /usr/share/faces/*.xpm to /usr/share/faces/*.png to make KDM happy

* Tue Aug 22 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-6mdk
- Move user icons in /usr/share/faces

* Sat Jul 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-5mdk
- Oups forgot the BM.

* Tue Jul 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-4mdk
- sbin/chksession: Set support for KDE2 by default when generating
  session.

* Tue Jul 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-3mdk
- Remove /etc/X11/window-managers
- bin/DrakWM: 
  	* Add -i options to launch with xinit.
	* Add -a option to provide alias for bash.
 
* Mon Jul 17 2000 dam's <damien@mandrakesoft.com> 1.0.4-2mdk
- replaced sawmill by sawfish

* Tue Jul 11 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-1mdk
- Add convertsession
- Make window-managers file dynamic and set them in /etc/X11/wmsession.d/.

* Mon May 29 2000 dam's <damien@mandrakesoft.com> 1.0.3-22mdk
- corrected doc url on gnome-desktop

* Fri May 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.3-21mdk
- corrected chksession for gnome.

* Fri May 12 2000 dam's <damien@mandrakesoft.com> 1.0.3-20mdk
- added gnome desktop entries.

* Wed May 10 2000 dam's <damien@mandrakesoft.com> 1.0.3-19mdk
- corrected buggy script. 

* Tue May  9 2000 dam's <damien@mandrakesoft.com> 1.0.3-18mdk
- added Netscape on desktop.

* Tue May  9 2000 dam's <damien@mandrakesoft.com> 1.0.3-17mdk
- corrected Netscape and rpmdrake gnome icons

* Tue May  9 2000 dam's <damien@mandrakesoft.com> 1.0.3-16mdk
- removed Netscape and rpmdrake gnome icons

* Sat May  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.3-15mdk
- sbin/chksession: if icewm is not here by default launch twm.

* Fri May  5 2000 Pixel <pixel@mandrakesoft.com> 1.0.3-14mdk
- fix for kdeDesktopCleanup

* Thu May 04 2000 dam's <damien@mandrakesoft.com> 1.0.3-13mdk
- cleaned gnome desktop.

* Sun Apr 30 2000 dam's <damien@mandrakesoft.com> 1.0.3-12mdk
- re-added XKill in kdelnk. 

* Fri Apr 28 2000 dam's <damien@mandrakesoft.com> 1.0.3-11mdk
- corrected xfce entry in windowmanagers.

* Thu Apr 27 2000 dam's <damien@mandrakesoft.com> 1.0.3-10mdk
- Corrected wmaker path.
- Added Update.kdelnk.

* Fri Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.3-9mdk
- Adjust wmaker path
- Maker rpmlint happy

* Thu Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.3-8mdk
- Update doc icons

* Thu Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.3-7mdk
- Update doc icons

* Thu Apr 20 2000 Fran�ois Pons <fpons@mandrakesoft.com> 1.0.3-6mdk
- updated WindowMaker priority again.

* Thu Apr 20 2000 Fran�ois Pons <fpons@mandrakesoft.com> 1.0.3-5mdk
- moved WindowMaker to a lower priority.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.0.3-4mdk
- removed some kdelnk for desktop cleaning.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.0.3-3mdk
- removed kdelnk/KAppfinder.kdelnk

* Sun Apr 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.3-2mdk
- DrakWM: a new greatest hit.

* Tue Apr 11 2000 dam's <damien@mandrakesoft.com> 1.0.3-1mdk
- new icons, new place for default background.

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.2-1mdk
- mandrake_desk.spec: adjust groups.
- Makefile: correct dis and rpm target.
- window-managers: fix blakbox with last blackbox package.
- Makefile: don't need to bzip (spec-helper do this job).

* Wed Feb  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-19mdk
- window-managers: Add a sawmill entry (V.Danen).

* Thu Jan 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-18mdk
- backgrounds/mandrake_background_*: add background from helene.
- mandrake_desk.spec: Remove the mandrake_background.xpm

* Mon Jan 10 2000 Pixel <pixel@mandrakesoft.com>
- icons/mini/hd_umount.xpm: renamed in hd_unmount.xpm (for coherence)

* Fri Jan  7 2000 Pixel <pixel@mandrakesoft.com>
- window-managers (NAME): KDE => kde.
- sbin/chksession: look at /etc/sysconfig/desktop to sort

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- icons/*: convert back and from .gif for kfm compliance :-/

* Wed Jan  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-13mdk
- Fix gnome links.

* Tue Jan  4 2000 Pixel <pixel@mandrakesoft.com>
- sbin/kdeDesktopCleanup: perl's glob in not " " compliant :(

* Tue Jan 04 2000 David BAUDENS <baudens@mandrakesoft.com>
- Use BBDrake & WMDrake for BlackBox & Window Maker

* Fri Dec 31 1999 Pixel <pixel@mandrakesoft.com>
- Makefile (dis): added a missing \
- kdelnk: Name field changes (dadou)

* Tue Dec 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add a manpages for chksession from camille.
- sbin/chksession: no errror when no Session is present.

* Mon Dec 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Various fix and changes (icons & links).
- bin/chkSession check if we are root.

* Fri Dec 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- window-managers: various change from (jerome).
- kdelnk/Kppp.kdlnk: (new).
- icons/user-*: added user icons for kdm (pixel).
- gnome/*: sync with kde desktop. (pablo).

* Tue Dec 23 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included the mandrake.links* files formerly in gmc package

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- sbin/fndSession: new script with the new chksession.
- sbin/chksession: a new greatest hit.
- window-managers: list of current window manager.

* Mon Dec 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Another icons change.

* Mon Dec 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add new icons large and mini.

* Mon Dec 20 1999 Pixel <pixel@mandrakesoft.com>
- added icons/mini and icons/large

* Sun Dec 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add fndSession.
- Use mktemp instead of $$ for fndSession.
- Add a real Makefile and clean-up the .spec.

* Fri Dec 17 1999 Pixel <pixel@mandrakesoft.com>
- add perl script to remove icons pointing to binaries not present

* Thu Dec 16 1999 Pixel <pixel@mandrakesoft.com>
- new icons

* Thu Dec 16 1999 Fran�ois PONS <fpons@mandrakesoft.com>
- removed Cd-Rom.kdelnk and floppy.kdelnk, since handled by DrakX.

* Mon Dec 13 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- reordered the mess with the *.kdelnk translations
- put old files in a old/ directory (the translations inside them
  can be handy if a similar icon is needed in the future)

* Fri Dec 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove my CVS DIR :\.

* Fri Dec 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove Hwiz.kdelnk
- Add/Remove icons.
- A lots of new icons (hel�ne).
- Add the doc.

* Mon Dec 06 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added ca, cs, gl language

* Mon Nov 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add Hwiz.kdelnk to Autostart kde.

* Thu Nov 04 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- changed the type of icons for CD and floppy

* Mon Oct 25 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added da, br, sk, uk translations

* Mon Oct 04 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added lt, ru translations
- added kdelnk/Dos_C.kdelnk icon (will be used as a pattern 
  by initscripts' kdeicons when creating icons for the FAT partitions)
- the horribly big *.xpm backgrounds are now created at %install time
  with 'convert'; that way we avoid the bzip2 taking forever each time
  a new version is done. 

* Fri Sep 28 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added de, is, it, ro translations

* Tue Sep 14 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Gaeilge (irish gaelic) translations

* Thu Sep 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included translations in several languages (et,hr,hu,id,nl,no)
  Currently covered are: es,et,fr,hr,hu,id,nl,no,wa you are welcome
  to add descriptions for the missing languages, get in touch with me.

* Wed Aug 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Launch kpackage with kdesu.
- Add script to launch this fu***ng linuxconf as kdesu (i love to do awfull
  thing :-(( ).

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix another typo :-((.

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Move floppy.kdelnk to FLOPPY.kdelnk for backward compatibilities.

* Fri Aug 20 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included norwegian nad indonesian texts for icons

* Wed Aug 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rebuild with defattr(root,root). (Thanks to Michael Irving <laric@laric.com>)

* Wed Aug 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Reinsert {FLOPPY,CDROM} and remove from kdesupport.

* Tue Aug 03 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove {FLOPPY,CDROM} (already in kdesupport).

* Mon Aug 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- desktop-links/* for gmc are installed through gmc package
- put an icon for the rpm

* Wed Jul 21 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added some stuff for Gnome

* Wed Jul 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Relifting of kde link.
- Add link for gnome.

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add new icons.

* Mon Jul 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add mandrake backgrounds xpm.

* Mon Jul 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix background to backgrounds.
- Add mandrake background images.

* Sat May 22 1999 Ga�l Duval <gael@linux-mandrake.com>
- fixed bad owner/group files
- added PRINTER.kdelnk

* Wed May 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix url of kde links.

* Sat May 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add new icons.
