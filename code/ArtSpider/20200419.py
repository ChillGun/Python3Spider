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
path = 'E:/pic2/'

# 创建文件夹并切换到对应文件夹下面
#os.makedirs(path + title.strip())
#os.chdir(path + title.strip())
os.chdir(path)

for i in range(99,200):
    #以此获取page页的url并获取网页文件
    src = 'http://p.gg99rt.net/uploadfile/2020/0412/07/'+str(i)+".jpg"
    print("当前图片 url：", src)
    #picture = requests.get(pic_['src'],headers = header)
    
    try:
        picture = requests.get(src,headers = Hostreferer, timeout=(3.05,27))
        print(picture.status_code)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
        
    #获取图片名
    file_name = src.split(r'/')[-1]
    file_name = clean(file_name)

    #保存图片
    f = open(file_name,'wb')
    f.write(picture.content)
    f.close()
