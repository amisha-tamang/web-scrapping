import json 

def analyse_movies_directors():

   with open("task5 AllMovieDetals.json","r") as file:
        data=file.read()
        g=json.loads(data)
        # print(g)
        list1=[]
        list2=[]
        list3=[]
        for i in g:
            # print(i)
            a=i["Genre:"].split()
            # print(a)
            for i in a:
                # print(i)
                if i[-1]==",":
                    i=i[:-1]
                    # print(i)
                    list3.append(i)
                    # print(i)
        for i in list3:
            # print(i)
            if i not in list1:
                # print(i)
                # if len(i)>1:
                    # print(i)
                   list1.append(i)
        # print(list1)
        dict={}
        for l in list1:
            # print(l)
            i=0
            count=0
            while i<len(list3):
                # print(i)
                if l==list3[i]:
                    count+=1
                i=i+1
            dict.update({l:count})
        # print(dict)
        list2.append(dict)
        # print(list2)
        with open("MovieGenreData.json","w") as f:
            json.dump(list2,f,indent=4)

analyse_movies_directors()










