#!/usr/bin/env python3

import sys
import json
from datetime import *

for line in sys.stdin:
    json.loads(line)
    data=json.loads(line)
    x=data['Weather_Condition']
    #print(data["Start_Time"])

    a = (data['Description']!="NaN")
    i = "lane blocked" in  data['Description'].lower()
    b = "shoulder blocked" in  data['Description'].lower()
    c = "overturned vehicle" in  data['Description'].lower()
    d=(data['Severity']!="NaN") & (data['Severity']>=2)
    e=( data['Sunrise_Sunset']!="NaN") & ("Night"== data['Sunrise_Sunset'])
    f=( data['Visibility(mi)']!="NaN") & ( data['Visibility(mi)']<=10)
    g=( data['Precipitation(in)']!="NaN") & ( data['Precipitation(in)']>=0.2)
    #h=(x!='nan' and x in weather)
    #h=( data['Weather_Condition']!="NaN") & ( data['Weather_Condition'].lower() in weather)
    if(a & i | b | c ):
        if(d & e & f & g ):
            if(type(x)!='float'):
                j=data['Weather_Condition'].lower()=="heavy snow"
                k=data['Weather_Condition'].lower()=="thunderstorm"
                l=data['Weather_Condition'].lower()=="heavy rain"
                m=data['Weather_Condition'].lower()=="heavy rain showers"
                n=data['Weather_Condition'].lower()=="blowing dust"
                if(j | k| l| m | n):
                    hour=(data['Start_Time'])[11:13]
                    #time=datetime.strptime(data["Start_Time"],"%Y-%m-%d %H:%M:%S").strftime("%H")
                    print('%s\t%s' % (hour,1))
