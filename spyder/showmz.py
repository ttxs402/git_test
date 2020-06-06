#%%
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
#%%
all_url = 'https://www.showmeizi.com/'
#http请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
'referer':"https://www.showmeizi.com/"}
#此请求头破解盗链
start_html = requests.get(all_url,headers = headers)
#%%
start_html.text
#%%
soup = BeautifulSoup(start_html.text,"html.parser")
all_page = soup.find_all('a',target='_blank')
#%%
href = []
for i in all_page:
    href.append(i['href'])
href_fin = [i for i in href if 'detail' in i]

#%%
dirPath = "E://Python//girl_images//"
#%%
same_url = 'https://www.showmeizi.com'
for j in href_fin[3:20]:
    ul = same_url+j
    start_html = requests.get(ul, headers = headers)
    soup = BeautifulSoup(start_html.text,"html.parser")
    file_name = soup.find('title').get_text().split('-')[0].strip().replace(' ','')#获取文件夹名字
    if os.path.exists(dirPath+file_name):
        print('已经保存过了')
        continue
    os.makedirs(dirPath+file_name)
    os.chdir(dirPath+file_name)
    all_url = soup.find_all('img')
    for i in all_url[0:-1]:
        url_fin = same_url + i['data-src'].replace(' ','%20')
        print(url_fin)
        image = requests.get(url_fin, timeout=7,headers = headers)
        filePath = os.path.join(dirPath+file_name, url_fin.split('/')[-1])
        f = open(filePath, 'wb')
        f.write(image.content)
        f.close()



#%%heisi
all_hs = 'https://www.showmeizi.com/category/heisi'
start_html = requests.get(all_hs,headers = headers)

#%%
start_html.text
# %%
soup = BeautifulSoup(start_html.text,"html.parser")
soup

# %%
all_page = soup.find_all('a',target='_blank')

# %%
href = []
for i in all_page:
    href.append(i['href'])
href_fin = [i for i in href if 'detail' in i]

# %%
href_fin
# %%
href = []
all_hs = 'https://www.showmeizi.com/category/heisi'
for i in range(1,15):
    new_url = all_hs+'/?currentPage='+str(i)
    start_html = requests.get(new_url,headers = headers)
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_page = soup.find_all('a',target='_blank')
    for i in all_page:
        href.append(i['href'])


# %%
dirPath = "E://Python//girl_images//hs//"

# %%
same_url = 'https://www.showmeizi.com'
for j in href[30:35]:
    ul = same_url+j
    start_html = requests.get(ul, headers = headers)
    soup = BeautifulSoup(start_html.text,"html.parser")
    file_name = soup.find('title').get_text().split('-')[0].strip().replace(' ','')#获取文件夹名字    
    if os.path.exists(dirPath+file_name):
        print('已经保存过了')
        continue
    os.makedirs(dirPath+file_name)
    os.chdir(dirPath+file_name)
    all_url = soup.find_all('img')
    for i in all_url[0:-1]:
        url_fin = same_url + i['data-src'].replace(' ','%20')
        print(url_fin)
        image = requests.get(url_fin, timeout=7,headers = headers)
        filePath = os.path.join(dirPath+file_name, url_fin.split('/')[-1])
        f = open(filePath, 'wb')
        f.write(image.content)
        f.close()
    
#%%
