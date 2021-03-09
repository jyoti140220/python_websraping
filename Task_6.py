from Task_5 import movie_details
from pprint import pprint 

list1=[]

def analyse_movies_language():
    for i in movie_details:
        list1.append(i['language'])
    language_list=list1
    # print(language_list)
    i=0
    duplicate_language_list=[]
    while i<len(language_list):
        j=0
        while j<len(language_list[i]):
            if language_list[i][j] not in duplicate_language_list:
                duplicate_language_list.append(language_list[i][j])
            j=j+1
        i=i+1
    # print(duplicate_language_list)
    i=0
    language_count_list=[]
    while i<len(duplicate_language_list):
        count=0
        for x in movie_details:
            if duplicate_language_list[i] in x['language']:
                count=count+1
        language_count_list.append(count)
        i=i+1
    # print(language_count_list)   
    i=0
    dic={}
    while i<len(duplicate_language_list):
        dic[duplicate_language_list[i]]=language_count_list[i]
        i=i+1
    return dic

pprint(analyse_movies_language())