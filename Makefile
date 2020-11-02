init:
	rm -r docs/index.html || true
	(cd planet && pelican --debug -s pelicanconf.py)
