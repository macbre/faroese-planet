init:
	rm -r docs/index.html || true
	(cd planet && pelican -s pelicanconf.py)
