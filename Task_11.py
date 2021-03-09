from Task_5 import movie_details
from pprint import pprint


def analyse_movies_genre():
    dic={}
    for movie in movie_details:
        for genre in movie['genre']:
            dic[genre]=0
    genre_dic={}
    for x in dic:
        c=0
        for y in range(len(movie_details)):
            for i in movie_details[y]['genre']:
                if x==i:
                    c=c+1
        genre_dic[x]=c
    return genre_dic
pprint(analyse_movies_genre())
