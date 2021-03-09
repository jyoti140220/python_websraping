from Task_1 import scrap_top_list
from bs4 import BeautifulSoup
from pprint import pprint 
import requests
import os
import json
movie_url_list=[]
movie_name_list=[]

for i in scrap_top_list():
    movie_url_list.append(i['url'])
    movie_name_list.append(i['name'])
# pprint(movie_url_list)
def scrape_movie_details(movies):
    print("************** Movie name:- ",movie_name_list[user-1],"*****************")
    print()
    movie_id=""
    for _id in movies[27:]:
        if '/' not in _id:
            movie_id+=_id
        else:
            break
    file_name=movie_id+'.json'
    # file_name=movie_name_list[user-1]+'.json'

    text=None
    if os.path.exists(file_name):
        f=open(file_name)
        text=f.read()
        text=json.loads(text)
        return text
    if text is None:

        page=requests.get(movies)
        soup=BeautifulSoup(page.text,"html.parser")
        # print(soup)

        title_div=soup.find('div',class_="title_wrapper").h1.get_text()
        # print(title_div)
        movie_name=""
        for i in title_div:
            if '(' not in i:
                movie_name=(movie_name+i)
            else:
                break
        # print(movie_name)

        sub_div=soup.find('div',class_="subtext")
        runtime=sub_div.find('time').get_text().strip()
        runtime_hours=int(runtime[0])*60
        
        # print(sub_div)
       
        if 'min' in runtime:
            # print(runtime[3:].strip('min'))
            runtime_minutes=int(runtime[3:].strip('min'))
            movie_runtime=runtime_hours+runtime_minutes
        else:
            movie_runtime=runtime_hours
        # print(movie_runtime)
        gener=sub_div.find_all('a')
        gener.pop()
        movie_gener=[i.get_text() for i in gener]
        # print(movie_gener)

        summary=soup.find('div',class_="plot_summary")
        movie_bio=summary.find('div',class_="summary_text").get_text().strip()
        # print(movie_bio)

        director=summary.find('div',class_="credit_summary_item")
        director_list=director.find_all('a')
        movie_director=[i.get_text().strip() for i in director_list]

        
        extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
        list_of_divs=extra_details.find_all('div')
        for div in list_of_divs:
            tag_4=div.find_all('h4')
            for text in tag_4:
                # print(text)
                tag_anchor=div.find_all('a')
                # print(tag_anchor)
                if 'Language:' in text:
                    tag_anchor=div.find_all('a')
                    movie_language=[Language.get_text() for Language in tag_anchor]
                elif "Country:" in text:
                    tag_anchor=div.find_all('a')
                    movie_country=''.join([Country.get_text() for Country in tag_anchor])
        
        movie_poster_link=soup.find('div',class_="poster").a['href']
        movie_poster="https://www.imdb.com"+movie_poster_link
        movie_detial_dic={}
        # movie_detial_dic={'name':'','director':'','country':'','language':'','poster_image_url':'','bio':'','runtime':'','genre':''}
        

        movie_detial_dic['name']=movie_name
        movie_detial_dic['director']=movie_director
        movie_detial_dic['country']=movie_country
        movie_detial_dic['language']=movie_language
        movie_detial_dic['poster_image_url']=movie_poster
        movie_detial_dic['bio']=movie_bio
        movie_detial_dic['runtime']=movie_runtime
        movie_detial_dic['genre']=movie_gener

        file1=open(file_name,"w")
        raw=json.dumps(movie_detial_dic)
        file1.write(raw)
        file1.close()
        return movie_detial_dic

 
user=int(input("enter the number of movies: "))
movie_url=movie_url_list[user-1]
pprint(scrape_movie_details(movie_url))
