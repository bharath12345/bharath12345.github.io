PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

help:
	@echo 'Makefile for Pelican site'
	@echo ''
	@echo 'Usage:'
	@echo '   make html                        (re)generate the web site'
	@echo '   make clean                       remove the generated files'
	@echo '   make regenerate                  regenerate files upon modification'
	@echo '   make publish                     generate using production settings'
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   serve and regenerate together'
	@echo '   make github                      upload the web site via gh-pages'
	@echo ''

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

github: publish
	ghp-import -m "Generate Pelican site" -b master $(OUTPUTDIR)
	git push origin master

.PHONY: html help clean regenerate serve devserver publish github
