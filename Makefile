PACKAGE = mandrake_desk
VERSION:=$(shell grep 'Version:' $(PACKAGE).spec| cut -f 2)
RELEASE:=$(shell grep 'Release:' $(PACKAGE).spec| cut -f 2)
TAG := $(shell echo "V$(VERSION)_$(RELEASE)" | tr -- '-.' '__')
mandir=/usr/share/man

all:
	@echo "Run make install"

clean:
	find . -type d -name '.xvpics'|xargs rm -rf

install:
	mkdir -p $(RPM_BUILD_ROOT)/usr/{s,}bin
	mkdir -p $(RPM_BUILD_ROOT)/$(mandir)/man8/
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/{faces,icons,icons/large,icons/mini,pixmaps/backgrounds/linux-mandrake}
	mkdir -p $(RPM_BUILD_ROOT)/etc/X11/
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk
	mkdir -p $(RPM_BUILD_ROOT)/etc/skel/Desktop
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/desktop-links
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/gnome/apps/Internet
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/gnome/apps/System
	install -m644 man/*8 $(RPM_BUILD_ROOT)/$(mandir)/man8/
	install -m755 sbin/* $(RPM_BUILD_ROOT)/usr/sbin/
	install -m755 bin/* $(RPM_BUILD_ROOT)/usr/bin/
	install -m644 icons/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/
	install -m644 icons/*.png $(RPM_BUILD_ROOT)/usr/share/icons/
	install -m644 icons/mini/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/mini
	install -m644 icons/large/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/large
	install -m644 backgrounds/* \
	$(RPM_BUILD_ROOT)/usr/share/pixmaps/backgrounds/linux-mandrake/

	install -m644 icons/mandrake*.xpm $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk/

	install -m644 faces/* $(RPM_BUILD_ROOT)/usr/share/faces

	install -m644 login/loging100.png $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk

	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts
	cp gnome/mandrake.links.sh $(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts/mandrake.links.sh
	chmod 0755 $(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts/mandrake.links.sh

# rules to build a test rpm

localrpm: localdist buildrpm

localdist: cleandist dir localcopy tar

cleandist:
	rm -rf $(PACKAGE)-$(VERSION) $(PACKAGE)-$(VERSION).tar.bz2

dir:
	mkdir $(PACKAGE)-$(VERSION)

localcopy:
	find . | grep -v -- "$(PACKAGE)-$(VERSION)\|\.bz2\|CVS\|~" |cpio -pd $(PACKAGE)-$(VERSION)/

tar:
	tar cvf $(PACKAGE)-$(VERSION).tar $(PACKAGE)-$(VERSION)
	bzip2 -9vf $(PACKAGE)-$(VERSION).tar
	rm -rf $(PACKAGE)-$(VERSION)

buildrpm:
	rpm -ta $(PACKAGE)-$(VERSION).tar.bz2

# rules to build a distributable rpm

rpm: changelog cvstag dist buildrpm

dist: cleandist dir export tar

export:
	cvs export -d $(PACKAGE)-$(VERSION) -r $(TAG) $(PACKAGE)
	cd $(PACKAGE)-$(VERSION); autoconf

cvstag:
	cvs commit
	cvs tag $(CVSTAGOPT) $(TAG)

changelog: ../common/username
	cvs2cl -U ../common/username -I ChangeLog 
	rm -f ChangeLog.bak
	cvs commit -m "Generated by cvs2cl the `date '+%d_%b'`" ChangeLog
