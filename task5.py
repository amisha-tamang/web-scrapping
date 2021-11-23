from task1 import*
import json
from  bs4 import BeautifulSoup
import requests
scrapped= scrape_top_list()
# print(scrapped)
def get_movie_list_details(movies):
    j=1
    list1=[]
    while j<len(movies):
        # print(j)
        NewMovieUrl=movies[j]["movie_link"]
        # print(NewMovieUrl)
        Url=NewMovieUrl
        AllDetailsUrl=requests.get(Url)
        # print(j,MovieUrl)
        soup=BeautifulSoup(AllDetailsUrl.text,"html.parser")
        # print(soup)
        main=soup.find("ul",class_="content-meta info")
        # print(main)
        all=main.find_all("li",class_="meta-row clearfix")
        # print(all)
        MyDict={}
        for i in all:
            # print(i)
            MyDict[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.strip()
            # print(MyDict)
        list1.append(MyDict)
        j=j+1
    with open("AllMovieDetals.json","w") as f:
        json.dump(list1,f,indent=3)
        
MovieDetails=get_movie_list_details(scrapped)