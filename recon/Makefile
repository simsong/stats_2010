mem03-all:
	echo python 02_build_state_stats.py --mem de 
	python 02_build_state_stats.py --mem --stdout ca
	python 02_build_state_stats.py --mem --stdout tx
 


mem02-dc:
	python 02_build_state_stats.py --mem dc

mem02-ak:
	python 02_build_state_stats.py --mem ak 

mem03:
	python 03_synth_lp_files.py --mem ak 013 000100

mem03-medium:
	python 03_synth_lp_files.py --mem de 001 040100 

clean:
	/bin/rm -f *.log *.dfxml

setuptest:
	mkdir -p /data/sf1/recon_test/al
	cp /data/sf1/recon/al/*.csv /data/sf1/recon_test/al/

tags:
	etags *.py ../ctools/*.py

schema.sql:
	mysqldump -h$(MYSQL_HOST) -p$(MYSQL_PASSWORD) -u$(MYSQL_USER) -d $(MYSQL_DATABASE) > schema.sql

backup.sql.gz:
	mysqldump -h$(MYSQL_HOST) -p$(MYSQL_PASSWORD) -u$(MYSQL_USER) $(MYSQL_DATABASE) | gzip > backup.sql.gz

backups:
	/bin/mv -f schema.sql schema.bak
	/bin/mv -f backup.sql.gz backup.sql.gz.bak
	make schema.sql
	make backup.sql.gz

