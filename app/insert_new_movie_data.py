#Importing the modules

import requests

import json

import os

import pandas as pd
#Ask for movie title

movies = pd.read_csv('ml-1m/movies.dat', sep='::', engine='python')

apikey = 'e760129c'

# movie_name = 'toy story'

# year = '1995'

director_list = []
actor_list = []

for i in range(0,movies['ID'].count()):
	# movies['ID'].count()
	movie_name = movies['MovieName'][i]
	movie_title =  movie_name[0:-7]
	movie_year = movie_name[-5:-1]
	print('i=' + str(i) + ',title = '+ movie_title + ',year = ' + movie_year)

	movie_url = "http://www.omdbapi.com/?" + "t=" + movie_title + "&y=" + movie_year + "&apikey=" + apikey

	try:
		r = requests.get(movie_url)
		movie_info_dic = json.loads(r.text)
		director = movie_info_dic['Director']
		actor = movie_info_dic['Actors']
	except:
		director = ''
		actor = ''

	
	
	print(',director = ' + director)

	director_list.append(director)
	actor_list.append(actor)

movies['Director'] = director_list
movies['Actors'] = actor_list
	
#867
# movies['Director'] = director_list


# col_name = movies.columns.tolist()          # 将数据框的列名全部提取出来存放在列表里
# print(col_name)
 
# col_name.insert(3,'Director')           # 在列索引为2的位置插入一列,列名为:Director，刚插入时不会有值，整列都是NaN
# movies = movies.reindex(columns=col_name)       # DataFrame.reindex() 对原行/列索引重新构建索引值
 
# movies['Director'] = director_list



# responce = requests.get("http://www.imdbapi.com", 
#               params={'t': movie_name, 'y': year, 'apikey': apikey}, 
#               headers={'User-Agent': 'My User-Agent'})




