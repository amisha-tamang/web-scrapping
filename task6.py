

import json

def  get_list_details():

    file1=open("AllMovieDetals.json","r")
    h=json.load(file1)
    # print(h)
    list=[]
    for i in h:
        # print(i)
        # print(i["Original Language"])
        if i["Original Language:"]not in list:
            list.append(i["Original Language:"])
            # print(list)
    dict={}
    list1=[]
    for g in list:
        # print(g)
        i=0
        count=0
        while i<len(h):
            # print(i)
            if g==h[i]["Original Language:"]:
                count+=1
            i+=1
        dict.update({g:count})
        # print(dict)
    list1.append(dict)
    # print(list1)
    with open("LanguageData.json","w")as file:
        json.dump(list1,file,indent=4)

get_list_details()






