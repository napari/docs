.PHONY: docs clean

clean:
	echo clean
	rm -rf docs/_build/
	rm -rf docs/api/napari*.rst
	rm -rf docs/gallery/*
	rm -rf docs/_tags

docs-install:
	python -m pip install -qr requirements.txt

docs-build:
	python docs/_scripts/prep_docs.py
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 sphinx-build -b html docs/ docs/_build

docs: clean docs-install docs-build

html: clean docs-build

html-noplot: clean
	python -qr docs/_scripts/prep_docs.py
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 sphinx-build -D plot_gallery=0 -b html docs/ docs/_build

linkcheck-files:
	NAPARI_APPLICATION_IPY_INTERACTIVE=0 sphinx-build -b linkcheck -D plot_gallery=0 --color docs/ docs/_build