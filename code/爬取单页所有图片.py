# coding=utf-8

# 导入需要的库
import os
import re
import requests
import time
from bs4 import BeautifulSoup



# 设置headers，网站会根据这个判断你的浏览器及操作系统
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
        }
Hostreferer = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer':'http://www.gogogort.com/'
               }

# 文件名处理函数，去掉文件或文件名中不允许的符号
def clean(text):
    kws = ['/','\\',':','*','"','<','>','|','？','?']
    for kw in kws:
        text = text.replace(kw,'')
    return text


# 图片保存函数，输入图片的url，即可得到图片及图片名
def get_picture(picture_url):
    
    # 尝试下载图片
    try:
        picture = requests.get(picture_url,headers = Hostreferer, timeout=(3.05,27))
        print("当前图片访问状态：",picture.status_code)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.MissingSchema as e:
        print(e)
        picture = requests.NullHandler
            
    
    # 返回图片
    return picture
    


# 保存地址
path = 'G:/FFOutput-1/其它/pic/pic108_/04、测试'

# 创建文件夹并切换到对应文件夹下面
#os.makedirs(path + title.strip())
#os.chdir(path + title.strip())
os.chdir(path)

page_url = "https://www.guomose.top/index.php?s=photo&c=show&id=529"

    
page = requests.get(page_url,headers = Hostreferer)
print("当前 Page 页访问结果：",page)
print("当前 page 页 url 为：", page_url)


# 解析 page 页
soup_1 = BeautifulSoup(page.text,'lxml')

# 获取 theme 页中的图片 url
for pic_ in soup_1.select('img'):

    
        
    # #获取图片名
    file_name = pic_['src'].split(r'/')[-1]
    file_name = clean(file_name)

    #保存图片
    if file_name != 'slt.jpg':
        if file_name != 'nopic_small.gif':
            print("当前图片 url：", pic_['src'])
            picture = get_picture(pic_['src'])
            if picture != requests.NullHandler:
                f = open(file_name,'wb')
                f.write(picture.content)
                f.close()
            #time.sleep(5)
#time.sleep(5)         
        