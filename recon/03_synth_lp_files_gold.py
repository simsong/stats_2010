from multiprocessing import Pool
import csv, time, itertools, sys, os, json
from math import floor
import pandas as pd

CONDA_PATH = '/apps/Anaconda/bin/'

####Get input parameters

state_code=sys.argv[1]
county_code=sys.argv[2]
state_abbr=sys.argv[3]
zipped=sys.argv[4]

##function for timing later
def millis():
    return int(round(time.time() * 1000))

#####Function to get p01_counts list for an entity (block or tract)
def get_p01(p01_counts, data_dict, level):
    for s in data_dict:
        if level=='block': q1=data_dict[s]
        elif level=='tract': q1=data_dict
        #q1 = data_dict[s]
        for q in q1:
            if q['table_number'] == 'P1': p01_counts[q['geoid']] = q['value']
    return p01_counts


####Function to get the summary dict to create constraints
def get_constraint_summary(summary_nums, data_dict, level, master_tuple_list):

        ###Loops through the data to create the constraints and the value that it should be output to.
        # for example, if it is female, hispanic, age 10-14, then it will create a list for each of the
        # sex/race/age combos to be used later.
        # I don't have medians in here.  working on it...they are weird because of the fractional
        # medians provided in the sf files
        # creates a block level dictionary with the associated constraints
        # Also creates a list of table P12 (sex*age for a block) to be used to instantiate people

    ###Initial values of sex and race and origin

    Sex = ["male", "female"]
    white =['Y','N']
    black =['Y','N']
    indian =['Y','N']
    asian =['Y','N']
    hawaiian =['Y','N']
    sor=['Y','N']
    hispanic=['Y','N']



    for s in data_dict:
        #print("in get constraint summary, working on s = ")
        #print(s)

        if s['geoid'] not in summary_nums: summary_nums[s['geoid']] = {'n_people': '0', 'constraints': [],
                                                                       'tuple_list': []}
        if s['table_number'] == 'P1':
            summary_nums[s['geoid']]['n_people'] = s['value']
        # else:
        constraint_value = s['value']

        ###Initialize all constraint values to the default values
        S = Sex
        A = [x for x in range(0, 111)]
        Wh = white
        Bl = black
        AIAN = indian
        Asian = asian
        NH = hawaiian
        SOR = sor
        Hisp = hispanic

        ###use race and origin binaries and the two or more races

        if s['white'] != 'missing':
            Wh = [s['white']]
        if s['black'] != 'missing':
            Bl = [s['black']]
        if s['aian'] != 'missing':
            AIAN = [s['aian']]
        if s['asian'] != 'missing':
            Asian = [s['asian']]
        if s['nhopi'] != 'missing':
            NH  = [s['nhopi']]
        if s['sor'] != 'missing':
            SOR = [s['sor']]
        if s['hispanic'] != 'missing':
            if s['hispanic']=='hispanic':
                Hisp=['Y']
            else: Hisp = [s['hispanic']]




        if s['sex'] != 'missing':
            if s['sex'] == 'both': S = Sex
            if s['sex'] == 'male': S = ['male']
            if s['sex'] == 'female': S = ['female']
        if s['start_age'] != 'missing':
            A = [x for x in range(int(s['start_age']), int(s['end_age']) + 1)]
        if s['median_age'] != 'missing':
            if s['start_age'] == 'missing':
                ##constrain to age
                A = [x for x in range(int(0), int(floor(constraint_value)) + 1)]
                constraint_value = floor(p01_counts[s['geoid']] / 2)
            if s['start_age'] != 'missing':
                ##constrain to age
                A = [x for x in range(int(s['start_age']), int(floor(constraint_value)) + 1)]
                constraint_value = floor(p01_counts[s['geoid']] / 2)


        if s['two']!='two':
            constraint = [constraint_value, S, A, Wh, Bl, AIAN, Asian, NH, SOR, Hisp, s['table_number'], s['geoid'], s['cell_number']]
            summary_nums[s['geoid']]['constraints'].append(constraint)


            if s['table_number'] == 'P12' and not (s['start_age'] == 0 and s['end_age'] == 110) and constraint_value > 0:
                s_tuple_list = []
                # format of tuple=(p,s,a,wh,bl,aian,nh,sor,hisp) where the person number is s_a_number
                ###Note -- the person number is made against table P12, which is sex by age.  It ensures that there
                ###are fewer records to enter the optimization to speed it up.




                s_tuple_list = [['{}_{}_{}_{}'.format(s['geoid'], s['sex'], s['start_age'], p), s['sex'], age, wh, bl, AI,
                                 As, nh, so, hisp]
                                for p in range(0, int(s['value']))
                                for wh in Wh
                                for bl in Bl
                                for AI in AIAN
                                for As in Asian
                                for nh in NH
                                for so in SOR
                                for hisp in Hisp
                                for age in [x for x in range(int(s['start_age']), int(s['end_age']) + 1)]]
                if level=='block':
                    for i in s_tuple_list:
                        join_it = 'C_'+'_'.join(map(str, i))
                        i.append(join_it)
                        i.append(s['geoid'])
                        #print("appending i to sum nums geoid tuplist. i =")
                        #print(i)
                        summary_nums[s['geoid']]['tuple_list'].append(i)
                        master_tuple_list.append(i)

    return summary_nums, master_tuple_list


def make_lp(list, rhv, n_con, table_num, geoid):
    clist = []
    clist = ' + '.join(list)
    f.write("_C_{table_num}_{geoid}_{n_con}: {clist} = {n} \n".format(table_num=table_num, geoid=geoid, n_con=n_con, clist=clist, n=rhv))
    n_con += 1
    return n_con

print("STARTNIG")

###Has the variables and the collapsing values we want (e.g, to collapse race, etc)
sf1_vars=pd.read_csv('sf1_vars_race_binaries.csv', quoting=2)
sf1_vars_block=sf1_vars[(sf1_vars['level']=='block')]
sf1_vars_tract=sf1_vars[(sf1_vars['level']=='tract')]


####The actual data -- reformatted sf1.

sf1_block_data=csv.DictReader(open('./{state_abbr}/{state_code}{county_code}/sf1_block_{state_code2}{county_code2}.csv'
                                   .format(state_abbr=state_abbr,state_code=state_code, county_code=county_code, state_code2=state_code, county_code2=county_code),'r'))
sf1_tract_data=csv.DictReader(open('./{state_abbr}/{state_code}{county_code}/sf1_tract_{state_code2}{county_code2}.csv'
                                   .format(state_abbr=state_abbr,state_code=state_code, county_code=county_code, state_code2=state_code, county_code2=county_code),'r'))

start_time=millis()

print("GOT ACTUAL DATA")

###make key value pairs so i can summarize the data
sf1_block_list=[]
for s in sf1_block_data:
    temp_list=[]
    if s['STATE'][:1].isdigit() and int(s['P0010001'])>0:
        geo_id=str(s['STATE'])+str(s['COUNTY']).zfill(3)+str(s['TRACT']).zfill(6)+str(s['BLOCK'])
        print(("getting actual data for ", geo_id))
        for k,v in list(s.items()):
            if k[:1]=='P' and geo_id[:1]!='S' and v.strip()!='': sf1_block_list.append([geo_id,k,float(v)])

sf_block=pd.DataFrame.from_records(sf1_block_list, columns=['geoid','tablevar','value'])

print("MERGING SOME SMORES STUFF")
####merge data with var definitions
sf_block_all=pd.merge(sf_block, sf1_vars_block, how='inner', left_on=['tablevar'], right_on=['cell_number'])

sf_block_all['value'].fillna(0)

#print sf_block_all.head()

####make sf_block_dict have a tract key to loop through by tract.

print("DUMPING TO DICT")
dump=sf_block_all.to_dict(orient='records')

sf1_block_dict={}
for d in dump:
    tract=d['geoid'][5:-4]
    block=d['geoid'][11:]
    print(("dump is doin tract block ", tract, " : ", block))
    if tract not in sf1_block_dict: sf1_block_dict[tract]={}
    if block not in sf1_block_dict[tract]: sf1_block_dict[tract][block]=[]
    sf1_block_dict[tract][block].append(d)

#####Get tract data ready

###make key value pairs so i can summarize the data

print("GET TRACT DATA RDY")
sf1_tract_list=[]
for s in sf1_tract_data:
    temp_list=[]
    if s['STATE'][:1].isdigit() and int(s['P0010001'])>0:
        geo_id=str(s['STATE'])+str(s['COUNTY']).zfill(3)+str(s['TRACT']).zfill(6)
        print(("getting tract fata rdy for ", geo_id))
        for k,v in list(s.items()):
            if k[:3]=='PCT' and geo_id[:1]!='S':
                sf1_tract_list.append([geo_id,k,float(v)])

sf_tract=pd.DataFrame.from_records(sf1_tract_list, columns=['geoid','tablevar','value'])

####merge data with var definitions
sf_tract_all=pd.merge(sf_tract, sf1_vars_tract, how='inner', left_on=['tablevar'], right_on=['cell_number'])

#print sf_tract.head()
#print sf1_vars_tract.head()

sf_tract_all['value'].fillna(0)

dump=sf_tract_all.to_dict(orient='records')

sf1_tract_dict={}
for d in dump:
    tract=d['geoid'][5:]
    print(("dumpin dumpin dumpin tract geoid ", tract))
    if tract not in sf1_tract_dict: sf1_tract_dict[tract]=[]
    sf1_tract_dict[tract].append(d)

print("BOUT TO CREATE SOME CONSTRAINTS IN A DICT")
### Create constraints in a dictionary

#print 'done with file read' + str((millis() - start_time) / 1000 / 60)

missing_tracts = open("../geo_tracking/missing_tracts",'r').readlines()
missing_tracts = [m.strip() for m in missing_tracts]

done_tracts = open("../geo_tracking/done_tracts",'r').readlines()
done_tracts = [m.strip() for m in done_tracts]

#for index, t1 in enumerate(sf1_tract_dict):
def build_next_tract_lp(t1):
    print(("MAKING CONSTRAINTS FOR TRACT? t1 = ", t1))#, " # ", index, " of ", len(sf1_tract_dict))

    full_geoid = str(state_code) + str(county_code) + str(t1)

    #### alter these if states to control which tracts ot process
    #if full_geoid in missing_tracts and full_geoid not in done_tracts:
    #if full_geoid not in done_tracts:
    if 1:
        #print(full_geoid, " is missing & not done, processing")
        #print(full_geoid, " is not done, processing")
        try:

            tract=t1
            n_inst = 1
            n_con=1
            geo_id=sf1_tract_dict[tract][0]['geoid']

            print("tammy code thinks geo_id is ", geo_id)


            #initialize the constraint file


            if not os.path.exists(
                    './{state_abbr}/{state_code}{county_code}/lp'.format(state_abbr=state_abbr, state_code=state_code,
                                                                                county_code=county_code)):
                os.makedirs(
                    './{state_abbr}/{state_code}{county_code}/lp'.format(state_abbr=state_abbr, state_code=state_code,
                                                                                county_code=county_code))


            f = open('./{state_abbr}/{state_code}{county_code}/lp/model_parms_small_{geo_id}_0.lp'
                     .format(state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id), 'w')
            ###Write initial stuff

            f.write("\* DB Recon *\ \n")
            f.write("Minimize \n")
            f.write("Arbitrary_Objective_Function: __dummy \n")
            f.write("Subject To \n")

            f.close()

            master_tuple_list=[]



            ############block constraint building

            # loop through blocks to get block constraints and the master tuple list
            summary_nums = {}
            p01_counts = {}

            p01_counts=get_p01(p01_counts, sf1_block_dict[tract], 'block')

            #print "start constraint summary" + str((millis() - start_time) / 1000 / 60)
            ####Create the constraints from the block dict
            for s1 in sf1_block_dict[tract]:
                s2=sf1_block_dict[tract][s1]
                #print("s2 is: ")
                #print(s2)
                summary_nums, master_tuple_list=get_constraint_summary(summary_nums, s2, 'block',
                                                                   master_tuple_list)

            #print "end constraint summary" + str((millis() - start_time) / 1000 / 60)
            ###Loop through the constraints to write to file

            ###make file to hold n_con

            sum_nums_file="./{state_abbr}/{state_code}{county_code}/sum_nums_{geo_id}.json"\
                .format(state_abbr=state_abbr, state_code=state_code, county_code=county_code,
                    geo_id=geo_id)


            with open(sum_nums_file, 'w') as a:
                json.dump(summary_nums, a)

            #summary_nums, n_con=make_constraints_block(summary_nums, n_con, 'block')
            print("starting os sys block")
            os.system(CONDA_PATH+"python make_constraints_block.py {geo_id} {state_code} {county_code} {state_abbr} {level} > ./synth/python_out.txt"
                      .format(summary_nums=sum_nums_file, geo_id=geo_id, state_code=state_code, county_code=county_code,
                              state_abbr=state_abbr, level='block'))
            print(("done with block constraint print in " + str((millis() - start_time) / 1000 / 60)))

            #########Tract constraint building

            # loop through blocks to get block constraints and the master tuple list
            summary_nums = {}
            p01_counts = {}

            p01_counts = get_p01(p01_counts, sf1_tract_dict[t1], 'tract')

            summary_nums, master_tuple_list = get_constraint_summary(summary_nums, sf1_tract_dict[tract], 'tract',
                                                                     master_tuple_list)
            for i in master_tuple_list: ###for tracts, need to add the master_tuple_list just once
                    summary_nums[geo_id]['tuple_list'].append(i)




            with open(sum_nums_file, 'w') as a:
                json.dump(summary_nums, a)

            ###Loop through the constraints to write to file
            #summary_nums, n_con = make_constraints(summary_nums, n_con, 'tract')
            print("starting os sys tract")
            os.system(CONDA_PATH+"python make_constraints_block.py {geo_id} {state_code} {county_code} {state_abbr} {level} > ./synth/python_out.txt"
                      .format(summary_nums=sum_nums_file, geo_id=geo_id, state_code=state_code, county_code=county_code,
                              state_abbr=state_abbr, level='tract'))
            print(("done with tract constraint print in " + str((millis() - start_time) / 1000 / 60)))

            f = open('./{state_abbr}/{state_code}{county_code}/lp/model_parms_small_{geo_id}_end.lp'
                     .format(state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id, n_con=n_con+1), 'w')

            f.write("Bounds\n  __dummy = 0 \n Binaries \n")
            f.write('\n'.join([t[10] for t in master_tuple_list]) + '\n End')

            #f.write("End")
            f.close()

            # print "find ./{state_abbr}/{state_code}{county_code}/lp -type f -name 'model_parms_small_{geo_id}_*.lp' -print0 | sort -z | xargs -0 cat -- > ./{state_abbr2}/{state_code2}{county_code2}/lp/model_parms_{geo_id2}.lp".format(
            #     state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id,
            #     state_abbr2=state_abbr, state_code2=state_code, county_code2=county_code, geo_id2=geo_id
            # )
            #
            # os.system("find ./{state_abbr}/{state_code}{county_code}/lp -type f -name 'model_parms_small_{geo_id}_*.lp' -print0 | sort -z | xargs -0 cat -- > ./{state_abbr2}/{state_code2}{county_code2}/lp/model_parms_{geo_id2}.lp".format(
            #     state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id,
            #     state_abbr2=state_abbr, state_code2=state_code, county_code2=county_code, geo_id2=geo_id
            # ))

            #print 'model_parms_small_{}_end.lp'.format(geo_id)

            lp_list=['model_parms_small_{}_0.lp'.format(geo_id), 'model_parms_small_{}_block.lp'.format(geo_id),
                                  'model_parms_small_{}_tract.lp'.format(geo_id), 'model_parms_small_{}_end.lp'.format(geo_id)]
            #print lp_list

            lp_dir='./{state_abbr2}/{state_code2}{county_code2}/lp/'.format(state_abbr2=state_abbr, state_code2=state_code, county_code2=county_code, geo_id2=geo_id)
            file_list=[lp_dir+i for i in lp_list]
            file_string=' '.join(file_list)

            os.system("cat {file_string} > ./{state_abbr2}/{state_code2}{county_code2}/lp/model_parms_{geo_id2}.lp".format(
                file_string=file_string,
                state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id,
                state_abbr2=state_abbr, state_code2=state_code, county_code2=county_code, geo_id2=geo_id))
            
            os.system("echo rm {file_string}".format(file_string=file_string))

            print("uploading partial results to s3")
            os.system("echo aws s3 cp ./{state_abbr2}/{state_code2}{county_code2}/lp/model_parms_{geo_id2}.lp s3://uscb-decennial-ite-das/title13_reid_cleanup/{state_abbr2}/{state_code2}{county_code2}/lp/model_parms_{geo_id2}.lp".format(
                file_string=file_string,
                state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id,
                state_abbr2=state_abbr, state_code2=state_code, county_code2=county_code, geo_id2=geo_id))

            os.system("echo " + str(full_geoid) + " | cat >> ../geo_tracking/done_tracts") 

            if zipped=='Y':
                os.system("gzip -f ./{state_abbr2}/{state_code2}{county_code2}/lp/model_parms_{geo_id2}.lp".format(
                state_abbr=state_abbr, state_code=state_code, county_code=county_code, geo_id=geo_id,
                state_abbr2=state_abbr, state_code2=state_code, county_code2=county_code, geo_id2=geo_id))
        except Exception as e:
            print(t1)
            print((e.message))
            os.system("echo " + str(full_geoid) + " | cat >> error_tracts")
            with open('./{state_abbr}_error_file.txt'.format(state_abbr=state_abbr),'a') as e_file:
                e_file.write(geo_id)
                e_file.write('\n')
    else:
        #print(full_geoid, " is not missing or is done, not processing")
        print(full_geoid, " is done, not processing")

p = Pool(3)
p.map(build_next_tract_lp, sf1_tract_dict)
