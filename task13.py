import os
import json
import requests
from bs4 import BeautifulSoup
from task5 import movie_list
from task1 import scrapp
from task12 import scrape_movie_cast

def  casting_list():
    newlist=[]
    for i in range(10):
        newlist.append(movie_list[i])

    for i in range(10):
        url=scrapp[i]["Movie URL"]
        sd=scrape_movie_cast(url)
        newlist[i]["cast"]=sd
    with open("task13.json","w")as file1:
         json.dump(newlist,file1,indent=4)  
    return newlist 

casting=casting_list()
