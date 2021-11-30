
from task1 import scrapp
from task4 import scrape_movie_details
import pprint
import json

def get_movie_list_details(movies):
    mylist=[]
    # detail_list=[]
    for j in movies:
        mylist.append(j)
        # if j["Movie Rank"]== "10.":
            # break
    # print(mylist)
    url_namelist={}
    
    for j in mylist:
        url_namelist.update({j["Movie URL"]:j["Movie Name"]})

    # print(urllist)
    detail_list=[]
    for link,name in url_namelist.items():
        a=scrape_movie_details(link,name)
        detail_list.append(a)

    

    with open ("movie_url.json","w") as file:
       json.dump(detail_list,file,indent=4)

    return detail_list



movie_list=(get_movie_list_details(scrapp))