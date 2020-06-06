#%%
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
#%%
all_url = 'http://www.mzitu.com'


#http请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
'referer':"http://www.mzitu.com"}
#此请求头破解盗链



start_html = requests.get(all_url,headers = headers)
#%%
start_html.text

#%%
#保存地址
path = 'E:/vscode_workspace/git_study/spyder/'

#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser")
page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text
#%%

#%%
same_url = 'http://www.mzitu.com/page/'
for n in range(9,int(10)+1):
    ul = same_url+str(n)
    start_html = requests.get(ul, headers = headers)
    soup = BeautifulSoup(start_html.text,"html.parser")
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')
    for a in all_a:
        title = a.get_text() #提取文本
        if(title != ''):
            print("准备扒取："+title)

            #win不能创建带？的目录
            if(os.path.exists(path+title.strip().replace('?',''))):
                    #print('目录已存在')
                    flag=1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag=0
            os.chdir(path + title.strip().replace('?',''))#改变工作路径
            href = a['href']
            html = requests.get(href,headers = headers)
            mess = BeautifulSoup(html.text,"html.parser")
            pic_max = mess.find_all('span')
            pic_max = pic_max[9].text #最大页数
            if(flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
            for num in range(1,int(pic_max)+1):
                try:
                    pic = href+'/'+str(num)
                    html = requests.get(pic,headers = headers)
                    mess = BeautifulSoup(html.text,"html.parser")
                    pic_url = mess.find('img',alt = title)
                    print(pic_url['src'])
                    #exit(0)
                    html = requests.get(pic_url['src'],headers = headers)
                    file_name = pic_url['src'].split(r'/')[-1]
                    f = open(file_name,'wb')
                    f.write(html.content)
                    f.close()
                except Exception as e:
                    print(e)
            print('完成')
    print('第',n,'页完成')

# %%
for i in [1,2,0,3,1]:
    try:
        print(1/i)
    except Exception as e:
        print(e)


# %%
