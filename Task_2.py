from Task_1 import scrap_top_list
from pprint import pprint 
year_list=[]
for i in scrap_top_list():
    if i['year'] not in year_list:
        # print(i['year'])
        year_list.append(i['year'])
year_list.sort()
# print(year_list)
movies_dict={i:[] for i in year_list}
# print(movies_dict)
# print(type(movies_dict))
for i in scrap_top_list():
    year=i['year']
    for x in movies_dict:
        if str(x)==str(year):
            movies_dict[x].append(i)
        
pprint(movies_dict)
