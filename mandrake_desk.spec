Summary:	The Desktop configuration files for Mandrake Linux
Name:		mandrake_desk
Version:	9.0
Release:	5mdk
License:	GPL
URL:		http://www.mandrakelinux.com/
Group:		System/Configuration/Other

# get the source from our cvs repository (see
# http://www.linuxmandrake.com/en/cvs.php3)
# no extra source or patch are allowed here.
Source:		mandrake_desk-%{version}.tar.bz2

BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:	menu



%description
This package contains useful icons, backgrounds and others goodies for the
Mandrake desktop.



%prep



%setup -q
find . -type 'd' -name 'CVS' | xargs rm -fr



%install
rm -rf %buildroot


## Install backgrounds
# User & root's backgrounds
install -d -m 0755 %buildroot/%_datadir/mdk/backgrounds/root/
install -m 0644 backgrounds/default.png %buildroot/%_datadir/mdk/backgrounds/default.png
install -m 0644 backgrounds/default-root.png %buildroot/%_datadir/mdk/backgrounds/root/default.png

# XFdrake test card
install -d -m 0755 %buildroot/%_datadir/mdk/xfdrake/
install -m 0644 backgrounds/xfdrake-test-card.jpg %buildroot/%_datadir/mdk/xfdrake/xfdrake-test-card.jpg



## Install scripts
install -d -m 0755 %buildroot/%_bindir/
for i in bin/*.sh ; do install -m 0755 $i %buildroot/_bindir/ ; done



## Install faces
install -d -m 0755 %buildroot/%_datadir/mdk/faces/
install -d -m 0755 %buildroot/%_datadir/faces/
for i in faces/*.png ; do install -m 0644 $i %buildroot/%_datadir/faces/
		
# David - 9.0-5mdk - For KDE
install -m 0644 faces/default.png %buildroot/%_datadir/faces/default.png

# David - 9.0-5mdk - For GDM
install -m 0644 faces/default.png %buildroot/%_datadir/mdk/faces/user-default-mdk.png




%post
if [ -f %_sysconfdir/X11/window-managers.rpmsave ];then
	%_prefix/sbin/convertsession -f %_sysconfdir/X11/window-managers.rpmsave || :
fi
%update_menus

%postun
%clean_menus



%clean
rm -fr %buildroot



%files
%defattr(-,root,root,-)



%changelog
* Wed Jul 31 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-5mdk
- Remove eazel-mdk-engine, krozat, krootwarnig (moved in their own modules/packages)
- Add new icons
- Rewrite spec

* Wed Jul 31 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 9.0-4mdk
- Fix GNOME entry for Crux theme applet
- Fix menu entries for simplified menu

* Tue Jul 30 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-3mdk
- New default user image

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-2mdk
- Fix Requires
- Add Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> changes :
	- As usual, search for qt/kde libraries in the right directories

* Thu Jul 18 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-1mdk
- Remove old users images. Add new images. Feedback welcome using cooker@linux-mandrake.com.

* Fri Mar 15 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-13mdk
- Fix text color in progress bar in Mandrake GTK theme 

* Thu Mar  7 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-12mdk
- No longer create icon for root
- Modify Mandrake GTK theme - Frederic Crozat
- Change name of Mandrake Control Center to Control Center in GNOME desktop
 (Thanks to Mattias Dahlberg) - Frederic Crozat

* Tue Feb 26 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-11mdk
- Add/remove some icons
- Don't allow spec to skip a build or install step without stop
- Remove DrakWM

* Mon Feb 25 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-10mdk
- Fix mdk-eazel-engine text color (Thanks to Brice Figureau)
- Update po files

* Wed Feb 20 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-9mdk
- Oops, fix location of capplet for mdk-eazel-engine

* Wed Feb 20 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-8mdk
- Fix building of package
- Fix english title for "What to do?" menu (Thanks to Till and Phil Lavigna)

* Mon Feb 18 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-7mdk
- Various fixes for simplified menu

* Tue Feb 12 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-6mdk
- Clean simplified menu

* Tue Jan 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-5mdk
- Add link to Crux configuration applet
- Fix menu entries for simplified menu

* Mon Jan 28 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-4mdk
- New icons for GNOME desktop

* Sun Jan 27 2002 Stefan van der Eijk <stefan@eijk.nu> 8.2-3mdk
- BuildRequires

* Thu Jan 24 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-2mdk
- Fix path used for images in krozat

* Fri Jan 11 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-1mdk
- Move screensaver images to mandrake_desk package
- Configure default desktop for nautilus

* Mon Dec 24 2001 Stefan van der Eijk <stefan@eijk.nu> 8.1-22mdk
- BuildRequires

* Thu Oct 18 2001 Stefan van der Eijk <stefan@eijk.nu> 8.1-21mdk
- BuildRequires: arts

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-20mdk
- Fix GMC URL (Frederic Crozat)

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-19mdk
- Fix GMC script

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-18mdk
- Fix my mistake with default user icon for GDM

* Wed Sep 19 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-17mdk
- Add simplified menu file
- Gnome: don't put special icons on root desktop
- Gnome: fix Internet icon
- Gnome: fix URL (Fred CROZAT)
- mv man.png aman.png
- Remove some obsolete faces (LN)
- put mdk-eazel-engine capplet to separate package

* Sat Sep 16 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-16mdk
- Update gnome desktop

* Fri Sep 14 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-15mdk
- Update ga translations

* Tue Sep 13 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-14mdk
- Re-add mandrakeexpert and mandrakecampus icons

* Tue Sep 04 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-13mdk
- Remove old icons and nearly all old images
- Move eazel-engine-capplet in mdk-eazel-engine
- Use man.png as default image for users

* Tue Sep 04 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-12mdk
- Make Monseigneur Pascal Rigaux, Prince de DrakX, Marquis de Pixel, happy (aka,
  move eazel-engine in a separate package)

* Mon Sep 03 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 8.1-11mdk
- An other fix for krootwarning

* Sat Sep 01 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 8.1-10mdk
- Autostart krootwarning

* Thu Aug 30 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-9mdk
- Bazoocate /etc/gtkrc to the moon request

* Mon Aug 27 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-8mdk
- Build without rpath

* Mon Aug 27 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-7mdk
- Add menu entry for krozat

* Mon Aug 27 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-6mdk
- Fix %%defattr

* Sat Aug 25 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-5mdk
- Split package

* Fri Aug 24 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-4mdk
- Add krozat (our Chef ;)

* Tue Aug 08 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-3mdk
- Add krootwarning

* Tue Aug 07 2001 Vincent Saugey <vince@mandrakesoft.com> 8.1-2mdk
- Move faces png to /usr/share/mdk/faces

* Tue Jul 31 2001 Frederic Lepied <flepied@mandrakesoft.com> 8.1-1mdk
- reworked Makefile and spec
- resync with cvs
- generate the kdm sessions with the right path to Xsession.

* Tue Jun 12 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 8.0-12mdk
- Fix patch0 with authors comments

* Mon Jun 11 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-11mdk
- Add control-center-devel, db1-devel, gdk-pixbuf-devel and libglade-devel to
  BuildRequires (thanks to Stefan van der Eijk)

* Fri Jun  8 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 8.0-10mdk
- Patch0: fix eazel engine for gfloppy and xcdroast

* Fri Jun  8 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 8.0-9mdk
- Update eazel-engine to latest CVS snapshot (correct bug in Gimp)

* Wed Apr 18 2001 David BAUDENS <baudens@mandrakesot.com> 8.0-8mdk
- Fix some bugs in theme
- Update gnome-desktop

* Sat Apr 15 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-7mdk
- chksession: fix Window Managers list for GDM
- Update gnome-desktop

* Thu Apr 12 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-6mdk
- Remove KDE stuff
- Remove patch #1
- Add icons for Mandrake Campus and Mandrake Expert
- Add print-cups.sh script - Frederic CROZAT

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
