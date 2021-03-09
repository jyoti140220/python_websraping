from Task_5 import movie_details
from pprint import pprint 

list1=[]

def analyse_movies_directors():
    for i in movie_details:
        list1.append(i['director'])
    director_list=list1
    # print(director_list)
    i=0
    duplicate_director_list=[]
    while i<len(director_list):
        j=0
        while j<len(director_list[i]):
            if director_list[i][j] not in duplicate_director_list:
                duplicate_director_list.append(director_list[i][j])
            j=j+1
        i=i+1
    # print(duplicate_director_list)
    i=0
    director_count_list=[]
    while i<len(duplicate_director_list):
        count=0
        for x in movie_details:
            if duplicate_director_list[i] in x['director']:
                count=count+1
        director_count_list.append(count)
        i=i+1
    # print(director_count_list)   
    i=0
    dic={}
    while i<len(duplicate_director_list):
        dic[duplicate_director_list[i]]=director_count_list[i]
        i=i+1
    return dic

pprint(analyse_movies_directors())