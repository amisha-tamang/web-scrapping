
import json 

def final(text):
    return " ".join(text.split())
   

def analyse_movies_directors():

    with open("AllMovieDetals.json","r") as file:
        data=file.read()
        l=json.loads(data)
        # print(l)
    list=[]
    for i in l:
        f=final(i["Director:"])
        # print(f)
        if f not in list:
            list.append(f)
            # print(list)
    dict1={}
    list1=[]
    for j in list:
        # print(j)
        i=0
        count=0
        while i<len(l):
            # print(i)
            if j==final(l[i]["Director:"]):
                count+=1
            i+=1
        dict1[j]=count
       
        # print(dict1).strip()y 
    # # # print(list1)
    with open("DirectorName.json","w")as f:
        json.dump(dict1,f,indent=4)

analyse_movies_directors()

 







 