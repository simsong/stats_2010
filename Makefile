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
## Load data into databases. Data must be downloaded first with
## 'make pl94_download'

pl94_load: pl94.sqlite3 

pl94.sqlite3: pl94_dbload.py
	python3 pl94_dbload.py --wipe data/2010_pl94/dist/*.zip
	rm -f pl94_ro.sqlite3
	cp -c pl94.sqlite3 pl94_ro.sqlite3
	chmod 444 pl94_ro.sqlite3

# Create the geographies. These can't be parallelized because v3 depends on v2

v1_geo: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v1

v2_geo: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v2

v21_geo: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v2.1

v3_geo: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v3

v4_geo: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v4

v5_geo: pl94_geofile.py
	python3 geotree.py --drop --create --scheme v5


################################################################
##
# Create the reports
# These can be made at the same time
v123: v1 v2 v3 
VARGS=--db pl94.sqlite3 --report --xpr --xempty

v1_report: geotree.py
	python geotree.py $(VARGS) --scheme v1 

v2_report: geotree.py
	python geotree.py $(VARGS)  --scheme v2

v3_report: geotree.py
	python geotree.py $(VARGS) --scheme v3

v4_report: geotree.py
	python geotree.py $(VARGS)  --scheme v4

v4_report_ak: geotree.py
	@echo a quick report of the v4 geography for just AK
	python geotree.py $(VARGS)  --scheme v4 --report_stusab ak

v5_report: geotree.py
	python geotree.py $(VARGS)  --scheme v5 

################################################################
##
## Combined

v4:
	make v4_geo
	make v4_report

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

################################################################
## Checking out inside ITE
checkout_ite:
	@echo run after git clone git@github.ti.census.gov:CB-DAS/stats_2010.git
	@echo edit .gitmodules and change all of the URL bases to be https://github.ti.census.gov/CB-DAS
	@echo git submodule init
	@echo git submodule update



################################################################
## Targets for downloading data

pl94_download:
	@echo Downloading pl94 from the public internet
	python3 download_all.py pl94


download_ak:
	@echo Downloading all of the data associated with AK.
	python3 download_all.py --state ak pl94 sf1 sf2

download_s3:
	@echo Copying data from AWS bucket
	mkdir -p data/2010_pl94/dist
	aws s3 cp --recursive $(DAS_S3ROOT)/2010/pl94/zips/ data/2010_pl94/dist

