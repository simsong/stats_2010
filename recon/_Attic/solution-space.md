Here's the pared back, stable version of compute_radii.py, the primary script in the solution variability code:

https://github.ti.census.gov/CB-DAS/reid-reconhdf/blob/master/solution_variability/compute_radii.py

It also expects that helper.py ( https://github.ti.census.gov/CB-DAS/reid-reconhdf/blob/master/solution_variability/helper.py ) will be present in the same directory.

compute_radii.py has invocation signature like:

python compute_radii.py input_file output_file

The file loving_texas_example.lp  ( https://github.ti.census.gov/CB-DAS/reid-reconhdf/blob/master/solution_variability/loving_texas_example.lp ) is included in the solution_variability/ subfolder for use getting used to compute_radii's output. It can be called like:

python compute_radii.py loving_texas_example.lp loving.out

I've removed (commented out or trapped in an if False:) all functionality except the basic solution variability estimate for now, so it only computes the distance between the initial and furthest histograms. it writes this value to stdout with the line

 
    for key in radii.keys():
        print(key, " = ", radii[key])
 

where key = "radius", so this can easily be altered to instead return the radius to another script instead've just printing it to stdout. In the Loving example, the calculated radius is 68.

One notable comment: right now, solution variability re-computes Tammy's solution by re-optimizing over the input .lp file to get its starting pointing, because that was slightly easier than writing a new method to read her csv or sol files. Eventually this should be changed to directly reading her .csv/.sol files, though, as gurobi can display some mildly nondeterministic behavior if e.g. we switch machines when solving.
