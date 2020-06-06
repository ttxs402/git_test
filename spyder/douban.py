#%%
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
#%%
all_url = 'https://movie.douban.com/top250/'
#http请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'referer':"https://movie.douban.com/top250"}
#此请求头破解盗链
start_html = requests.get(all_url,headers = headers)
#%%
base_url = 'https://movie.douban.com/top250'
#%%
movie_list = []
for i in range(0,10):
    url_new = base_url+'?start='+str(i*25)+'&filter='
    start_html = requests.get(url_new,headers = headers)
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find_all('div',attrs = {'class':'hd'})

    for i in all_a:
        movie_list.append(i.find('a').find('span').text)


# %%
filename = 'write_data.txt'
with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write(str(movie_list))
# %%
