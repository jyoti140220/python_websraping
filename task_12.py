# only "Anand" movie k liye

from Task_1 import scrap_top_list
from bs4 import BeautifulSoup
from pprint import pprint 
import requests
import os
import json

def scrape_movie_cast(movie_caste_url ):
    print("************** Movie name:- ","Anand","*****************")
    print()
    movie_id=""
    for _id in movie_caste_url[27:]:
        if '/' not in _id:
            movie_id+=_id
        else:
            break
    file_name=movie_id+"_cast"+'.json'

    text=None
    if os.path.exists(file_name):
        f=open(file_name)
        text=f.read()
        text=json.loads(text)
        return text
    if text is None:
    
        page=requests.get(movie_caste_url )
        soup=BeautifulSoup(page.text,"html.parser")
        
        table_data=soup.find('table',class_='cast_list')
        actors=table_data.find_all('td',class_="")
        cast_list=[]
        for actor in actors:
            actor_dict={}
            imdb_id=actor.find('a').get('href')[6:15]
            name=actor.find('a').get_text().strip()
            actor_dict["Imdb_id"]=imdb_id
            actor_dict["Name"]=name
            cast_list.append(actor_dict)
        file1=open(file_name,"w")
        file2=json.dump(cast_list,file1,indent=6)
        file1.close()
        return cast_list
    
movie_url="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
movie_cast_detials=scrape_movie_cast(movie_url)
pprint(movie_cast_detials)

