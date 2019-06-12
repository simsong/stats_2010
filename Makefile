test:
	py.test cb_spec_decoder_test.py

load_geo: dbload.py
	/bin/rm -f data.sqlite3
	python dbload.py data/??geo2010.pl

load_blocks:
	python dbload.py data/??0000[12]2010.pl

clean:
	/bin/rm -f *~

clean_data:
	/bin/rm -rf pl94 sf1 sf2

download_ak:
	python download_all.py --state ak pl94 sf1 sf2

tags:
	etags *.py */*py
