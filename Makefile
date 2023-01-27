.PHONY: docs clean

# Gallery path must be given relative to the docs/ folder

ifeq ($(GALLERY_PATH),)
GALLERY_PATH := ../../napari/examples
endif

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(dir $(mkfile_path))
docs_dir := $(current_dir)docs

clean:
	echo clean
	echo $(current_dir)
	rm -rf $(docs_dir)/_build/
	rm -rf $(docs_dir)/api/napari*.rst
	rm -rf $(docs_dir)/gallery/*
	rm -rf $(docs_dir)/_tags

docs-install:
	python -m pip install -qr $(current_dir)requirements.txt

docs-build:
	python $(docs_dir)/_scripts/prep_docs.py
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 sphinx-build -b html docs/ docs/_build -D sphinx_gallery_conf.examples_dirs=$(GALLERY_PATH)

docs-xvfb:
	python $(docs_dir)/_scripts/prep_docs.py
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 xvfb-run --auto-servernum sphinx-build -b html docs/ docs/_build -D sphinx_gallery_conf.examples_dirs=$(GALLERY_PATH)

docs: clean docs-install docs-build

html: clean docs-build

html-noplot: clean
	python -qr $(docs_dir)/_scripts/prep_docs.py
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 sphinx-build -D plot_gallery=0 -b html docs/ docs/_build -D sphinx_gallery_conf.examples_dirs=$(GALLERY_PATH)

linkcheck-files:
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 sphinx-build -b linkcheck -D plot_gallery=0 --color docs/ docs/_build -D sphinx_gallery_conf.examples_dirs=$(GALLERY_PATH)
