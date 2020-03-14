STATES=ak al ar az ca co ct dc de fl ga hi ia id il in ks ky la ma md me mi mn mo ms mt nc nd ne nh nj nm nv ny oh ok or pa pr ri sc sd tn tx ut va vt wa wi wv wy
LIMIT=100
GEODIR=/mnt/data/2010_sf1/geo

all:
	@echo Please read the Makefile.
	@exit 1

which:
	printenv
	which python3

test:
	py.test cb_spec_decoder_test.py

tags:
	etags *.py */*py

clean:
	find . -name '*~' -print -exec rm -f {} \;

clean_data:
	@echo To erase all of the data that have been downloaded, type:
	@echo /bin/rm -rf data

pl94_download:
	python3 download_all.py pl94

pl94_load:
	python3 pl94_dbload.py --wipe data/2010_pl94/dist/*.zip
	rm -f pl94_ro.sqlite3
	cp -c pl94.sqlite3 pl94_ro.sqlite3
	chmod 444 pl94_ro.sqlite3

r3:
	python3 geocode_stats.py --db pl94.sqlite3 --geocode3 --geocode_report \
	        --prefixset "3:6,3:11,11:20,20:22,22:26" --loglevel INFO

s3:
	python3 geocode_stats.py --db pl94.sqlite3 --geocode3 --geolevel_report \
                --prefixset "nation:state/aianh:0:3,state:county:3:6,state/aianh:place:3:11,place:tract:11:20,tract:blkgrp:20:22,blkgrp:block:22:26"\
	        --loglevel INFO  --open

ak_r3:
	python3 geocode_stats.py --db ak.sqlite3   --geocode3 --geocode_report --prefixset "3:3,6:5,11:5,16:1,17:4" --loglevel INFO --details

ak_s3:
	python3 geocode_stats.py --db ak.sqlite3   --geocode3 --geolevel_report --prefixset "nation:state/aianh:0:3,state/aianh:place:3:8,place:tract:8:20,tract:blkgrp:20:22,blkgrp:block:22:26" --loglevel INFO  --open

dc_r3:
	python3 geocode_stats.py --db dc.sqlite3 --geocode3 --geocode_report --prefixset "3:3,6:5,11:5,16:1,17:5"

ak_load:
	@echo Just loading ak in ak.sqlite3
	python3 pl94_dbload.py --db ak.sqlite3 --wipe data/2010_pl94/dist/ak2010.pl.zip

az_load:
	@echo Just loading ak in az.sqlite3
	python3 pl94_dbload.py --db az.sqlite3 --wipe data/2010_pl94/dist/az2010.pl.zip

pr_load:
	@echo Just loading ak in pr.sqlite3
	python3 pl94_dbload.py --db pr.sqlite3 --wipe data/2010_pl94/dist/pr2010.pl.zip --debuglogrecno=11735

pl94_load_geo: pl94_dbload.py
	python3 pl94_dbload.py data/??geo2010.pl

download_ak:
	@echo Downloading all of the data associated with AK.
	python3 download_all.py --state ak pl94 sf1 sf2

make_crosswalks:
	bash crosswalk_generator_all


