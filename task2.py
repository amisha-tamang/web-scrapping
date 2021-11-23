from task1 import*
import json
# movies=scrape_top_list()

def group_by_year(movies):
    # print(movies)
    years=[]
    for i in movies: 
        # print(i)
        if i["movieYear"] not in years:
            # print(years)
            years.append(i["movieYear"])
            years.sort()
            # print(years)
    movie_dict={i:[]for i in years}
    # print(movie_dict)
    for k in movies:
        year1=k["movieYear"]
        # print(year)
        for x in movie_dict:
            if str(x)==str(years):
            # print(x)
                movie_dict[x].append(k)
                # print(movie_dict[x])
    with open("YearMovieData.json","w") as F:
        json.dump(movie_dict,F,indent=4)
year=group_by_year(movies)