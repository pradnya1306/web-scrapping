
import requests
from bs4 import BeautifulSoup
import json
from task1 import scrapp 


def scrape_movie_details(url1,name):
    url=(url1)
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    tag=soup.find("ul",class_="content-meta info")
    sub=tag.find_all("li",class_="meta-row clearfix")
    
    mydic={}
    mydic["name"]=name
    for i in sub:

        key=i.find("div",class_="meta-label subtle").text.strip()
        # print(key)
        values=(i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip())
        # print(values)
        mydic[key]=values
    
                
    with open("one_movie.json","w")as file:
        json.dump(mydic,file,indent=4)
    return mydic

for i in scrapp:
    url2=scrapp[0]["Movie URL"]
    name=scrapp[0]["Movie Name"]

print(url2)
(scrape_movie_details(url2,name))
