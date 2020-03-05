#!/usr/bin/env python3
"""
get_map: Given a state and a county, gets the map

"""

import os
import sys

import sqlite3
import pl94_dbload
import statistics
import numpy as np

from geocode_stats import GeocodeStats
import constants


if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Gets the County Map',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--db", help="Specify database location", default=pl94_dbload.DBFILE)
    parser.add_argument("stusab")
    parser.add_argument("county",type=int)
    args = parser.parse_args()
    gs = GeocodeStats(args.db)

    stusab = args.stusab.upper()
    county = args.county
    county_name = gs.county_name(stusab,county).lower().replace(" county","")
    state = constants.stusab_to_state(stusab)
    url = f"www2.census.gov/geo/maps/dc10map/tract/st{state}_{stusab.lower()}/c{state}{county:03}_{county_name}"
    print(url)
