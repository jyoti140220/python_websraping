import requests
from pprint import pprint 
from bs4 import BeautifulSoup

url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")


def scrap_top_list():
    main_div=soup.find('div', class_='lister')
    tbody=main_div.find('tbody', class_='lister-list')
    trs=tbody.find_all('tr')
    
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]

    for tr in trs:
        position=tr.find('td', class_='titleColumn').get_text().strip()
        rank=''
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)

        title=tr.find('td', class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=tr.find('td', class_="titleColumn").span.get_text()
        year_of_realease.append(year)

        imdb_rating=tr.find('td', class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)

        link=tr.find('td' , class_="titleColumn").a['href']
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)

    top_list=[]
    i=0
    while i<len(movie_ranks):
        d1={}
        d1["name"]=str(movie_name[i])
        d1["year"]=int(year_of_realease[i][1:5])
        d1["position"]=int(movie_ranks[i])
        d1["rating"]=float(movie_ratings[i])
        d1["url"]=movie_urls[i]
        top_list.append(d1)
        i=i+1
    return top_list
# pprint(scrap_top_list())







