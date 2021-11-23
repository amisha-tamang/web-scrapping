import requests
from bs4 import BeautifulSoup
import json

def scrap_movie_details( Movie_link): 
    # TopMovie=[]                       
    MovieDetails={}
    LinkData=requests.get( Movie_link)
    soup=BeautifulSoup(LinkData.text,"html.parser")
    # print(soup)
    MovieDetails["name"]=soup.find("h1").text
    # print(MovieDetails)
    main=soup.find("ul",class_="content-meta info")
    # print(main)
    all=main.find_all("li",class_="meta-row clearfix")
    # print(all)
    for i in all:
        # print(i)
        MovieDetails[i.find("div",class_="meta-label subtle").text.strip()]=(i.find("div",class_="meta-value")).text.strip()
        print(MovieDetails)
    # with open("BlackPantherMovieDeatail.json","w") as f:
    #     json.dump(MovieDetails,f,indent=4)   

scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")



