#!/usr/bin/env python3

import sys as s

total_state=None
total_count=0
present_count=0
present_state=None
present_city=None

for l in s.stdin:
    l=l.strip()
    state,city,count= l.split(" ~ ")  #["state",["city",1]]
    #state=state_list[0]
    #x=state_list[1]
    #city_1=x.split("#")     #["city",1]
    #city=city_1[0]
    #count=city_1[1]

    try:
        state=(str)(state)
        city=(str)(city)
        count=(int)(count)
    except Exception:
        continue
    temp_sate= present_state==state
    temp_city= present_city==city

    if(temp_city & temp_sate):
        present_count=present_count+1
    else:
        if(present_city!=None):
            print(present_city,present_count)
        present_state=state
        present_city=city
        present_count=count

    if(total_state!=state):
        if(total_state!=None):
            print(total_state,total_count)
            total_count=0
        total_state=state
        print(state)

    total_count+=1
final= present_city==city
if(final):
    print(present_city,present_count)

print(total_state,total_count)
