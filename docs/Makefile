# Minimal makefile for Sphinx documentation
#

#The supported flags are 'members', 'undoc-members', 'private-members', 'special-members', 'inherited-members' and 'show-inheritance'.
#export SPHINX_APIDOC_OPTIONS=members,undoc-members,show-inheritance
export SPHINX_APIDOC_OPTIONS=members,no-undoc-members,show-inheritance

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = PyCollect
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


buildapi:
	sphinx-apidoc -fMeET -o source/_modules ../pycollect
	cp ../notebooks/research.ipynb source/content
	rm -r source/content/research_files
	jupyter nbconvert --to rst source/content/research.ipynb
	#jupyter nbconvert --to markdown source/content/research.ipynb --output ../../README.md
	rm source/content/research.ipynb

