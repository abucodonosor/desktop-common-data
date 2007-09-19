PACKAGE = desktop-common-data
NAME = desktop-common-data
TAG := $(shell echo "V$(VERSION)_$(RELEASE)" | tr -- '-.' '__')
mandir=/usr/share/man
SVNROOT = svn+ssh://svn.mandriva.com/svn/soft/$(PACKAGE)

menus: applications.menu kde-applications.menu

menu/validated-menu: menu/applications.menu.in
	xmllint --noout --dtdvalid menu/menu.dtd $?

applications.menu: menu/validated-menu
	@echo -n "generating $@ "
	@sed -e 's,@MAIN_DESKTOP@,GNOME,g' -e 's,@MAIN_TOOLKIT@,GTK,g' < menu/applications.menu.in > $@
	@xmllint --noout --dtdvalid menu/menu.dtd $@
	@echo " OK"

kde-applications.menu: menu/validated-menu
	@echo -n "generating $@ "
	@sed -e 's,@MAIN_DESKTOP@,KDE,g' -e 's,@MAIN_TOOLKIT@,Qt,g' < menu/applications.menu.in > $@
	@xmllint --noout --dtdvalid menu/menu.dtd $@
	@echo " OK"

checktag:
	@if [ "x$(VERSION)" == "x" -o "x$(RELEASE)" = "x" ]; then \
 	  echo usage is "make VERSION=version_number RELEASE=release_number dist" ; \
	  exit 1 ; \
	fi

clean:
	find . -type d -name '.xvpics' -o -name '*~' |xargs rm -rf
	rm -f applications.menu kde-applications.menu

# rules to build a test rpm

localdist: menus cleandist dir localcopy tar

cleandist: checktag
	rm -rf $(PACKAGE)-$(VERSION) $(PACKAGE)-$(VERSION).tar.bz2
	rm -f applications.menu kde-applications.menu

dir: checktag
	mkdir $(PACKAGE)-$(VERSION)

localcopy: checktag
	find . -not -name "$(PACKAGE)-$(VERSION)"|cpio -pd $(PACKAGE)-$(VERSION)/
	find $(PACKAGE)-$(VERSION) -type d -name CVS -o -type d -name '.svn' -o -name .cvsignore -o -name '*~' |xargs rm -rf

tar: checktag
	tar cvf $(PACKAGE)-$(VERSION).tar $(PACKAGE)-$(VERSION)
	bzip2 -9vf $(PACKAGE)-$(VERSION).tar
	rm -rf $(PACKAGE)-$(VERSION)

# rules to build a distributable rpm

dist: menus checktag cleandist changelog svntag export tar


export: checktag
	svn export $(SVNROOT)/tags/$(TAG) $(PACKAGE)-$(VERSION)

svntag: checktag 
	svn copy $(SVNROOT)/trunk $(SVNROOT)/tags/$(TAG) -m "$(TAG)"

changelog: ../common/username
#svn2cl is available in our contrib.
	svn2cl --authors ../common/username.xml --accum
	rm -f ChangeLog.bak
	svn commit -m "Generated by svn2cl the `date '+%c'`" ChangeLog
