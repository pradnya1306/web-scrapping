
from task1  import scrapp
import json


def group_by_year(movie):

    year_list=[]
    for i in movie:
        if i["Year"] not in year_list:
            year_list.append(i["Year"])
    
    mydict={}
    for p in year_list:
        # print(p)
        movie_list=[]
        for j in movie:
            if j["Year"]==p:
                movie_list.append(j)
        mydict.update({p:movie_list})

    with open("movies_by_year.json","w")as file:
        json.dump(mydict,file,indent=4)
    return mydict
    
group=group_by_year(scrapp)
