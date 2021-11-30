import json
import requests
from task1 import scrapp
import os
from task4 import scrape_movie_details


def scrape_new_movie_details(url2):
    for i in scrapp:
        if i["Movie URL"]==url2:
            url=i["Movie URL"][33:]
            url1=i["Movie URL"]
            name=i["Movie Name"]
    filename="/home/pradnya/Desktop/web scraping/"+url+".json"

        
    file=os.path.exists(filename)
        # # print(file)
    if file==True:
        print(" it is exists")
        with open(filename,"r")as m:
            details=json.load(m)
            print(details)
    else:
        print("it is not exists")
        data=scrape_movie_details(url1,name)   
        print(data)



        with open(filename,"w") as file:
            json.dump(data,file,indent=4)


url2=scrapp[5]["Movie URL"]
# print(url2)
scrape_new_movie_details(url2)