import random
import time
import os
import json
from task1 import scrapp
from task4 import scrape_movie_details


def get_movie_list_detailes():
    for i in range(10):
            url=scrapp[i]["Movie URL"][33:]
            url1=scrapp[i]["Movie URL"]
            name=scrapp[i]["Movie Name"]
            filename="/home/pradnya/Desktop/web scraping/"+url+".json"
            randomtime=random.randint(1,3)
                
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
                time.sleep(randomtime)   
                print(data)



                with open(filename,"w") as file:
                    json.dump(data,file,indent=4)
        
print(get_movie_list_detailes())

