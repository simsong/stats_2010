DB=sf1.sqlite3
DBDIR=../data/2010_sf1

TODO: Options to print the blocks in the tract; options to restrict model to specific blocks (and no tract-level.)

check: $(DB)
	python smt_solve.py --db $(DB) --segments 8 --onlytables P12F,P12G,P12H
	time z3 parallel.enable=true solve_AK105000200.smt

$(DB): ../dbload.py
	/bin/rm -f sf1.sqlite3
	python ../dbload.py --db $(DB) $(DBDIR)/akgeo2010.sf1 $(DBDIR)/ak000012010.sf1
