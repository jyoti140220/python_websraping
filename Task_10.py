from Task_5 import movie_details
from pprint import pprint

def analyse_language_and_directors():
    directors_dic={}
    for movie in movie_details:
        for director in movie['director']:
            # print(director)
            directors_dic[director]={}
    print(directors_dic)
    for i in range(len(movie_details)):
        for director in directors_dic:
            if director in movie_details[i]['director']:
                for language in movie_details[i]['language']:
                    directors_dic[director][language]=0
    print(directors_dic)
    for i in range(len(movie_details)):
        for director in directors_dic:
            if director in movie_details[i]['director']:
                for language in movie_details[i]['language']:

                    directors_dic[director][language] +=1
    return directors_dic

                            

pprint(analyse_language_and_directors())