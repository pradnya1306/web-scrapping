
import json
from task1 import scrapp


def decade(group_year):
    yearlist=[]
    for i in group_year:
        i=(i["Year"])
        mod=i%10
        decade1=i-mod
        if decade1 not in yearlist:
            yearlist.append(decade1)
    
    yearlist.sort()

    moviedec={}
    for i in yearlist:

        decade=i+9
        mylist=[]
        for x in group_year:
            a=x["Year"]
            if a>=i and a<=decade:
               mylist.append(x)
        moviedec.update({i:mylist}) 
        
    with open("decade.json","w")as w:
        json.dump(moviedec,w,indent=4)

decade(scrapp)