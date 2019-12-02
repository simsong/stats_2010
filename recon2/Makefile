DB=sf1.sqlite3
DBDIR=../data/2010_sf1

# Note --state=AK --county=105 --tract=200 --maxsegments=30 took 1695 seconds, never went multi-threaded, and got unsat
#      --state=AK --county=105 --tract=200 --maxsegments=48 produced "unknown" without combined_solver.solver2_unknown=2; took YY seconds otherwise
check: $(DB)
	python smt_solve.py --db $(DB) --maxsegments=10
	time z3 parallel.enable=true combined_solver.solver2_unknown=2 solve_AK105000200.smt

regress: $(DB)
	python smt_solve.py --db $(DB) --onlyblock=1005 --outfile=AK105000200-1004.smt
	time z3 parallel.enable=true combined_solver.solver2_unknown=2 AK105000200-1004.smt

quick: $(DB)
	python smt_solve.py --db $(DB) --maxsegments=4
	time z3 parallel.enable=true combined_solver.solver2_unknown=2 solve_AK105000200.smt | sort > solve_AK105000200.sol
	diff solve_AK105000200.sol solve_AK105000200.sol.dist

$(DB): ../dbload.py
	/bin/rm -f sf1.sqlite3
	python ../dbload.py --db $(DB) $(DBDIR)/akgeo2010.sf1 $(DBDIR)/ak000012010.sf1
