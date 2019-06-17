#!/usr/bin/python3
# -*- mode: python -*-

import cgi
import os
import sys
import socket
import json
import cgi

import ctools.dbfile as dbfile
import ctools.env as env

DEFAULT_SECONDS=60

# https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
import decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def getstats():
    form = cgi.FieldStorage()
    try:
        seconds = int(form.getfirst("seconds",DEFAULT_SECONDS))
    except ValueError:
        seconds = int(DEFAULT_SECONDS)


    vars_file = os.path.join( env.get_home(), 'dbreader.bash' ) 
    db_vars = env.get_vars( vars_file )
    auth = dbfile.DBMySQLAuth(host=db_vars['MYSQL_HOST'],
                              database=db_vars['MYSQL_DATABASE'],
                              user=db_vars['MYSQL_USER'],
                              password=db_vars['MYSQL_PASSWORD'])

    stats = {}                            
    query = 'select unix_timestamp(A.t),A.host,B.min1 from (select max(t) t,host from sysload  group by host) A left join sysload B on A.t=B.t and A.host=B.host'
    rows = dbfile.DBMySQL.csfr(auth,query)
    stats['sysload'] = [{'time_t':row[0],
                         'host':row[1],
                         'min1':row[2]
                         } for row in rows]


    print("content-type: text/json\n")
    # cls = DecimalEncoder to interpret decimal points
    print(json.dumps(stats, cls=DecimalEncoder))

if __name__=="__main__":
    getstats()
