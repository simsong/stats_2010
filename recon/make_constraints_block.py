
import csv, time, itertools, sys, os, json
from math import floor
import pandas as pd


####Get input parameters



def make_constraints_block(f,n_con,summary_nums,geo_id, state_code, county_code, state_abbr, level):
    print_num=0
    print_list = []

    print('hi')


    tuple_list=[]
    constraint_list=[]

    for s in summary_nums:
        info = summary_nums[s]
        tuple_list.extend(info['tuple_list'])
        constraint_list.extend(info['constraints'])

    summary_nums={}

    tuple_frame=pd.DataFrame(tuple_list, columns=['TID','sex','age','white','black', 'aian','asian','nh','sor','hisp','print_val', 'geoid'])

    tuple_list=[]



    #constraint_out = csv.writer(open('./{state_abbr}/{state_code}{county_code}/synth_out/const_{geoid}.csv'.format(state_abbr=state_abbr,state_code=state_code, county_code=county_code,geoid=s), 'w'))

    con_frame_list=[]
    for c in constraint_list:
        c2=list(itertools.product(*c[1:10]))
        for c3 in c2:
            #value, table number, geoid
            x=[c[0]]
            x.extend(c3)
            x.append(c[10])
            x.append(c[11])
            x.append(c[12])
            con_frame_list.append(x)

    constraint_list=[]


    con_frame=pd.DataFrame(con_frame_list, columns=['value','sex','age','white','black', 'aian','asian','nh','sor','hisp','table_num','geoid','cell_number'])

    con_frame['geo_table'] = con_frame['cell_number'] + '_' + con_frame['geoid']

    if level=='block':
        merge_list=['geoid','sex','age','white','black', 'aian','asian','nh','sor','hisp']
    else:
        merge_list=['sex','age','white','black', 'aian','asian','nh','sor','hisp']

    lp=pd.merge(tuple_frame, con_frame, how='inner', on=merge_list)

    lp_short=lp[['geo_table', 'value','print_val']]

    lp_df=lp_short.groupby(['geo_table', 'value']).agg(lambda x: ' + '.join(x))


    for index, row in lp_df.iterrows():
        print_list.append("_C_{geo_table}_{n_con}: {group} = {n} \n".format(geo_table=index[0],
                                                                               n_con=n_con, group=row['print_val'], n=index[1]))
        n_con += 1
        print_num += 1

    #
    # f.write(''.join(print_list))
    #
    # print_list=[]
    # f.close()
    # f=open('./{state_abbr}/{state_code}{county_code}/lp/model_parms_small_{geo_id}_{n_con}.lp'
    #        .format(state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id, n_con=n_con), 'w')
    #print n_con, print_num
    #print 'writing now ' + str((millis() - start_time) / 1000 / 60)
    print_num = 0


    f.write(''.join(print_list))

    return n_con
