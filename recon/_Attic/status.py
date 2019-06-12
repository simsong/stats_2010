#!/usr/bin/env python3
"""
Report the status of the reconstruction.
"""

import dbrecon


STATE_ABBRS = dbrecon.all_state_abbrs()

################################################################
## Restrict report range
##

def states():
    return [args.state] if args.state else STATE_ABBRS

def which_states():
    return args.state if args.state else 'all states'

def counties_in_state(state):
    return [args.county] if args.county else dbrecon.counties_for_state(state_abbr)



################################################################



def check_phase0(state_abbr):
    sf1_dist_dir = dbrecon.dpath_expand("$SF1_DIST")
    sf1_zipfilename  = dbrecon.dpath_expand("$SF1_DIST/{state_abbr}2010.sf1.zip").format(state_abbr=state_abbr)
    return dbrecon.dpath_exists(sf1_zipfilename)

def check_phase1(state_abbr):
    state_code = dbrecon.state_fips(state_abbr)
    state_county_list_filename=(f'$ROOT/{state_abbr}/state_county_list_{state_code}.csv'
                                .format(state_abbr=state_abbr,state_code=state_code))
    return dbrecon.dpath_exists(state_county_list_filename)

def check_phase2(state_abbr):
    done_filename    = f"$ROOT/{state_abbr}/completed_{state_abbr}_02"
    return dbrecon.dpath_exists(done_filename)

def state_county_has_csv_file(state_abbr,county):
    state_code = dbrecon.state_fips(state_abbr)
    try:
        csv_block_filename = (f"$ROOT/{state_abbr}/{state_code}{county}/sf1_block_{state_code}{county}.csv"
                              .format(state_abbr=state_abbr,state_code=state_code,county=county))
        return dbrecon.dpath_exists(csv_block_filename)
    except FileNotFoundError:
        return False

def check_phase2b(state_abbr):
    return all([state_county_has_csv_file(state_abbr,county) for county in counties_in_state(state_abbr)])


def report_phase(name,func):
    state_status = [(state_abbr,func(state_abbr)) for state_abbr in states()]
    if all([st[1] for st in state_status]):
        print("{}: complete for {}".format(name,which_states()))
    else:
        print("{}: complete for: {}".format(name, " ".join([st[0] for st in state_status if st[1]])))
        print("{}: waiting  for: {}".format(name, " ".join([st[0] for st in state_status if not st[1]])))

if __name__=="__main__":
    config = dbrecon.get_config()
    from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
    parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                             description="Data Migration Tool" )
    dbrecon.argparse_add_logging(parser)
    parser.add_argument("--state", help="Just give the status on this state")
    parser.add_argument("--county", help="Just give the status on this county")
    parser.add_argument("--config", help="config file")
    args = parser.parse_args()

    report_phase("Phase 0: Downloading", check_phase0)
    report_phase("Phase 1: County lists made", check_phase1)
    report_phase("Phase 2: Finished per-county state SF1 extractions", check_phase2)
    report_phase("Phase 2: Complete per-county CSV files", check_phase2b)

    for state_abbr in states():
        counties = counties_in_state(state_abbr)
        counties_with_csv_files = [county for county in counties_in_state(state_abbr) if state_county_has_csv_file(state_abbr,county)]
        if len(counties)!=len(counties_with_csv_files):
            print(f"{state_abbr} counties: {len(counties)}  with CSV files: {len(counties_with_csv_files)}")

    print()
    print("Examining LP files...")
    state_has_some_tracts = set()
    state_county_nolpfiles = {}
    for state_abbr in states():
        print(f"Examining LP files for {state_abbr}")
        for county in counties_in_state(state_abbr):
            nolpfiles = []
            tracts      = dbrecon.tracts_for_state_county(state_abbr=state_abbr,county=county)
            if tracts:
                tracts_with_lp_files = dbrecon.tracts_with_files(state_abbr,county,'lp')
                for tract in tracts:
                    if tract in tracts_with_lp_files:
                        state_has_some_tracts.add(state_abbr)
                    else:
                        nolpfiles.append(tract)
            else:
                nolpfiles = ['all']
            state_county_nolpfiles[(state_abbr,county)] = nolpfiles
        print(f"{state_abbr} complete counties: ",end='')
        completed_counties = []
        for county in counties_in_state(state_abbr):
            if not state_county_nolpfiles[(state_abbr,county)]:
                completed_counties.append(county)
        print(f" ({len(completed_counties)}/{len(counties_in_state(state_abbr))}) {' '.join(completed_counties)}")

    for state_abbr in states():
        if state_abbr not in state_has_some_tracts:
            print(f"{state_abbr}: no LP files for any tract in the state")
            continue
        for county in counties_in_state(state_abbr):
            tracts  = dbrecon.tracts_for_state_county(state_abbr=state_abbr,county=county)
            without = state_county_nolpfiles[(state_abbr,county)]
            if without:
                print(f"{state_abbr} {county} LP files missing for {len(without)}/{len(tracts)} tracts: ",end='')
                print(" ".join(without[0:3]),end='')
                if len(without)>3:
                    print("...",end='')
                print()
        print("\n")

