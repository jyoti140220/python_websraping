from Task_1 import scrap_top_list
from pprint import pprint 

year_list=[]
for i in scrap_top_list():
    if i['year'] not in year_list:
        year_list.append(i['year'])
year_list.sort()
# print(year_list)
list1=[]
dic_1={}
for index in year_list:
    mod=index%10
    decade=index-mod
    if decade not in list1:
        list1.append(decade)
        dic_1[decade]=[]
# print(list1)
# print(dic_1)
for x in dic_1:
    for i in scrap_top_list():
        h=str(x)
        j=str(i['year'])
        if h[-2]==j[-2]:
            dic_1[x].append(i)
pprint(dic_1)
