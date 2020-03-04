STATES=ak al ar az ca co ct dc de fl ga hi ia id il in ks ky la ma md me mi mn mo ms mt nc nd ne nh nj nm nv ny oh ok or pa pr ri sc sd tn tx ut va vt wa wi wv wy
LIMIT=100
GEODIR=/mnt/data/2010_sf1/geo

all:
	@echo Please read the Makefile.
	@exit 1

test:
	py.test cb_spec_decoder_test.py

tags:
	etags *.py */*py

clean:
	find . -name '*~' -print -exec rm -f {} \;

clean_data:
	@echo To erase all of the data that have been downloaded, type:
	@echo /bin/rm -rf data

download_pl94:
	python download_all.py pl94

load_pl94:
	python dbload_pl94.py --wipe data/2010_pl94/dist/*.zip
	rm -f pl94_ro.sqlite3
	cp -c pl94.sqlite3 pl94_ro.sqlite3
	chmod 444 pl94_ro.sqlite3

load_pl94ak:
	python dbload_pl94.py --wipe data/2010_pl94/dist/ak2010.pl.zip

load_pl94_just_geo: dbload_pl94.py
	python dbload_pl94.py data/??geo2010.pl

download_ak:
	@echo Downloading all of the data associated with AK.
	python download_all.py --state ak pl94 sf1 sf2

make_crosswalks:
	bash make_all_crosswalks

