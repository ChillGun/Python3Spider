# coding=utf-8

# 导入需要的库
import os
import re
import requests
from bs4 import BeautifulSoup



# 设置headers，网站会根据这个判断你的浏览器及操作系统
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
        }
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'https://wtfuck.net/'
               }

# 文件名处理函数，去掉文件或文件名中不允许的符号
def clean(text):
    kws = ['/','\\',':','*','"','<','>','|','？','?']
    for kw in kws:
        text = text.replace(kw,'')
    return text

# 保存地址
path = 'E:/资料/python爬图/pic55/'

# 创建文件夹并切换到对应文件夹下面
#os.makedirs(path + title.strip())
#os.chdir(path + title.strip())
os.chdir(path)

for i in range(0,25):
    #以此获取page页的url并获取网页文件
    url = 'http://www.9900rt.com/html/yazhou/2015/0115/1696_'+str(i)+".html"
    page = requests.get(url,headers = Hostreferer)
    print("当前 Page 页访问结果：",page)
    print("当前 page 页 url 为：", url)

    # 解析 page 页
    soup = BeautifulSoup(page.text,'lxml')

    # 获取 theme 页中的图片 url
    for pic_ in soup.select('img'):
        print("当前图片 url：", pic_['src'])
        #picture = requests.get(pic_['src'],headers = header)
        
        try:
            picture = requests.get(pic_['src'],headers = Hostreferer, timeout=(3.05,27))
            print(picture.status_code)
        except requests.exceptions.ConnectTimeout as e:
            print(e)
        except requests.exceptions.Timeout as e:
            print(e)
        except requests.exceptions.ConnectionError as e:
            print(e)
            
        #获取图片名
        file_name = pic_['src'].split(r'/')[-1]
        file_name = clean(file_name)

        #保存图片
        f = open(file_name,'wb')
        f.write(picture.content)
        f.close()
