STATES=ak al ar az ca co ct dc de fl ga hi ia id il in ks ky la ma md me mi mn mo ms mt nc nd ne nh nj nm nv ny oh ok or pa pr ri sc sd tn tx ut va vt wa wi wv wy
LIMIT=100
GEODIR=/mnt/data/2010_sf1/geo

help:
	@echo Please read the Makefile.
	@exit 1

all: cb_spec_decoder.py pl94_geofile.py pl94.sqlite3 
	make -j1 v1_geo_create v2_geo_create v21_geo_create v3_geo_create 

### Cleaning targets ##

clean:
	/bin/rm pl94.sqlite3
	find . -name '*~' -print -exec rm -f {} \;

clean_data:
	@echo To erase all of the data that have been downloaded, type:
	@echo /bin/rm -rf data

################################################################
## Load data into databases

pl94_load: pl94.sqlite3 

pl94.sqlite3: pl94_dbload.py
	python3 pl94_dbload.py --wipe data/2010_pl94/dist/*.zip
	rm -f pl94_ro.sqlite3
	cp -c pl94.sqlite3 pl94_ro.sqlite3
	chmod 444 pl94_ro.sqlite3

# Create the geographies. These can't be parallelized because v3 depends on v2

v1_geo_create: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v1

v2_geo_create: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v2

v21_geo_create: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v2.1

v3_geo_create: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v3

v31_geo_create: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v3.1


################################################################
##
# Create the reports
# These can be made at the same time
v123: v1 v2 v3 
VARGS=--db pl94.sqlite3 --report --xpr

v1_report: geotree.py
	@echo a quick report of the v1 geography down to the states
	python geotree.py $(VARGS) --scheme v1 

v2_report: geotree.py
	@echo a quick report of the v2 geography down to the states
	python geotree.py $(VARGS)  --scheme v2

v21_report: geotree.py
	@echo a quick report of the v2 geography down to the states
	python geotree.py $(VARGS)  --scheme v2.1

v3_report: geotree.py
	@echo a quick report of the v2 geography down to the states
	python geotree.py $(VARGS) --scheme v3

v31_report: geotree.py
	@echo a quick report of the v2 geography down to the states
	python geotree.py $(VARGS)  --scheme v3.1


################################################################
##
## generate the automatically generated files

pl94_geofile.py: cb_spec_decoder.py
	python cb_spec_decoder.py --geoclassdump  pl94_geofile.py

pl94_geofile.sql: cb_spec_decoder.py
	python cb_spec_decoder.py --geosqldump  pl94_geofile.sql

geotree.py: pl94_geofile.py
pl94_dbload.py: pl94_geofile.py

################
test:
	py.test cb_spec_decoder_test.py

tags:
	etags *.py */*py

pl94_download:
	python3 download_all.py pl94


ak_s3:
	python3 geocode_stats.py --db ak.sqlite3   --geocode3 --geolevel_report --prefixset "nation:state/aianh:0:3,state/aianh:place:3:8,place:tract:8:20,tract:blkgrp:20:22,blkgrp:block:22:26" --loglevel INFO  --open

dc_r3:
	python3 geocode_stats.py --db dc.sqlite3 --geocode3 --geocode_report --prefixset "3:3,6:5,11:5,16:1,17:5"

################
##
## Work with subsets

ak_load:
	@echo Just loading ak in ak.sqlite3
	python3 pl94_dbload.py --db ak.sqlite3 --wipe data/2010_pl94/dist/ak2010.pl.zip


ak_r3:
	python3 geocode_stats.py --db ak.sqlite3   --geocode3 --geocode_report --prefixset "3:3,6:5,11:5,16:1,17:4" --loglevel INFO --details

################

az_load:
	@echo Just loading ak in az.sqlite3
	python3 pl94_dbload.py --db az.sqlite3 --wipe data/2010_pl94/dist/az2010.pl.zip

pr_load:
	@echo Just loading ak in pr.sqlite3
	python3 pl94_dbload.py --db pr.sqlite3 --wipe data/2010_pl94/dist/pr2010.pl.zip --debuglogrecno=11735

download_ak:
	@echo Downloading all of the data associated with AK.
	python3 download_all.py --state ak pl94 sf1 sf2

