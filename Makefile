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

STATES=ak al ar az ca co ct dc de fl ga hi ia id il in ks ky la ma md me mi mn mo ms mt nc nd ne nh nj nm nv ny oh ok or pa pr ri sc sd tn tx ut va vt wa wi wv wy
LIMIT=100
GEODIR=/mnt/data/2010_sf1/geo
make_crosswalks:
	bash make_all_crosswalks

upload:
	(cd crosswalks;for i in *.csv ; do aws s3 cp $$i $$DAS_S3ROOT/2010/geounit_crosswalks/vars-`date -I`/$$i ; done)
