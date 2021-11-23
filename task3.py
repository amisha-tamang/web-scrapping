from task1 import movies
import json

def group_by_decade(movies):
    DecadeMovie={}
    list=[]
    for index in movies:
        # print(index)
        num=int(index["movieYear"])%10
        # print(num)
        Decade=int(index["movieYear"])-num
        # print(Decade)
        if Decade not in list:
            list.append(Decade)
    list.sort()
    # print(list)
    for i in list:
        # print(i)
        DecadeMovie[i]=[]
        for x in movies:
            # print(x)
            if int(x["movieYear"])>=i and int(x["movieYear"])<=i+9:
                DecadeMovie[i].append(x)
                # print(DecadeMovie)
    with open("decadeData.json","w") as f:
        json.dump(DecadeMovie,f,indent=4)   
group_by_decade(movies)
