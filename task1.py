
import requests
from bs4 import BeautifulSoup
import json
import os





def scrape_top_list():
    if os.path.exists("/home/amisha/Desktop/python12/WEB SCRAPING/TopMovieData.json")==True:
        with open("TopMovieData.json","r") as movieDataFile:
            data=movieDataFile.read()
            final=json.loads(data)
        return final
    else:
        TopMovie_url= "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"

        TopRatedMoviesApi=requests.get(TopMovie_url)

        htmlcontent=TopRatedMoviesApi.content

        soup=BeautifulSoup(htmlcontent,"html.parser")

        tableTag=soup.find("table",class_="table")
        td=tableTag.find_all("tr")
    #    
        top_movie=[]
        for i in td[1:]:
        
            movieRank=i.find("td",class_="bold")
            for rank in movieRank:
                rank=" ".join(movieRank.text.split())
            

            movieRating=i.find("span",class_="tMeterScore")
            for rating in movieRating:
            #     a=(" ".join(movieRating.text.split()))
            #     a.strip()
                a=" ".join(movieRating.text.split())
    
            movieName=i.find("a", class_="unstyled articleLink")
            for name in movieName:
                b=" ".join(movieName.text.split())

                year=b[len(b)-5:len(b)-1]
                # b.strip()
            
            
            reviewsNo=i.find("td",class_="right hidden-xs")
            for reviews in reviewsNo:
                reviews=" ".join(reviewsNo.text.split())
                

            Movie_url=i.find("a",class_="unstyled articleLink")['href']

            Movie_link="https://www.rottentomatoes.com"+Movie_url
        
            allDetails={"movieRank":rank ,"movieYear":year , "movieRating":a , "movieName":b , "reviewsNo":reviews , "movie_link":Movie_link}

            top_movie.append(allDetails)
        
        with open("TopMovieData.json","w") as movieDataFile:
            json.dump(top_movie,movieDataFile,indent=5)
        return top_movie

movies=scrape_top_list()