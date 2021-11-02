#!/usr/bin/env python3

import sys
import json
from datetime import *
import requests

URL=" http://20.185.44.219:5000/"

Lat=float(sys.argv[1].strip())
Lng=float(sys.argv[2].strip())
D = float(sys.argv[3].strip())

for line in sys.stdin:
    json.loads(line)
    data=json.loads(line)
    a=((data['Start_Lat']!='NaN')&(data['Start_Lng']!='NaN')&(Lat!='NaN')&(Lng!='NaN'))
    if(a):
        distance=((data['Start_Lat']-Lat)**2+(data['Start_Lng']-Lng)**2)**(0.5)
        if(distance<=D):
            parameters={"latitude": data["Start_Lat"],
                        "longitude": data["Start_Lng"]}
            r = requests.post(" http://20.185.44.219:5000/",json=parameters)
            '''y=json.loads(r.text)
            city=y["city"]
            state=y["state"]'''
            #print(state,"\t",city,"\t",1)
            print("%s ~ %s ~ " % (r.json()['state'],r.json()['city']),1)
