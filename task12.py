from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from task1 import movies
data1=movies
# print(data1)

def main_fun(data):
    # print(data)
    def scrap_movie_cast(link,movie_name):
        # print(link)
        d1={}
        link_data=requests.get(link)
        # print(link_data)
        soup=BeautifulSoup(link_data.text,'html.parser')
        d1["Name"]=movie_name
        # print(d1)
        table=soup.find('div',class_='castSection')
        # print(table)
        celebrity_link=table.find_all('a',class_='unstyled articleLink')
        celebrity_name=table.find_all('span',class_='characters subtle smaller')
        # print(celebrity_link)
        # print(celebrity_name)
        
        d1={}
        dic={}
        for i in range(len(celebrity_link)):    
            # print(i)        
            Name=celebrity_name[i]['title']
            # print(Name)
            # link="https://www.rottentomatoes.com/"+celebrity_link[i]['href']
            link=celebrity_link[i]['href']
            # print(link)
            cast_id=""
            # print(cast_id)
            id=len(link)-1
            # print(id)

            while id>=0:
                if link[id]!="/":
                    # print(link[id])
                    cast_id+=link[id]
                    # print(cast_id)
                else:
                    break
                id=id-1
            
            cast_id=list(cast_id)
            # print(cast_id)
            cast_id.reverse()
            # print(cast_id)
            cast_id=''.join(cast_id)
            # print(cast_id)
            d1[cast_id]=Name           
        # print(d1)
        dic[movie_name]=d1
        # print(dic)
        return dic
   
    movie_cast_list=[]
    for i in data:
        # print(i)
        for j in i:
            # print(j)
            movie_name=i["movieName"]
            # print(movie_name)
            if j=="movie_link":
                # print( i[j])
                movie_details_dic=scrap_movie_cast(i[j],movie_name) 
                # print(movie_details_dic)
                movie_cast_list.append(movie_details_dic)
                # print(movie_cast_list)
                # movie_filename=str(movie_filename(movie_name))
                with open("movie_cast.json","w") as f:
                    json.dump(movie_cast_list,f,indent=3)
    # print(movie_cast_list)

castdata=main_fun(data1)