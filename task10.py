
import json

with open("AllMovieDetals.json","r") as f:
    data=f.read()
    data1=json.loads(data)
    # print(data1)
def language_and_directores(movies_list):
    DirectorList=[]
    for movies in movies_list:
        # print(movies)
        if movies["Director:"] not in DirectorList:
            DirectorList.append(movies["Director:"])
    # print(DirectorList)
    final={}
    for i in DirectorList:
        # print(i)
        count_dic={}
        lang=[]
        for director in movies_list:
            # print(director)
            if i == director["Director:"]:
                if director["Original Language:"] not in lang:
                    count_dic[director["Original Language:"]]=1
                    lang.append(director["Original Language:"])
                    # print(lang)
                else:
                    count_dic[director["Original Language:"]]+=1
        final[i]=count_dic
        with open("DirectorByLanguage.json","w") as f:
            json.dump(final,f,indent=4)
    return(final)

(language_and_directores(data1))

      