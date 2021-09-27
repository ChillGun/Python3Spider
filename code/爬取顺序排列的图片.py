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
    'Referer':'https://diskgirl.com/images/5f6d106a94dbb221944af7e7'
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
            
    
    # 返回图片
    return picture
    


# 保存地址
path = 'G:/FFOutput-1/其它/pic/pic108_/07、国模左曦/'

# 创建文件夹并切换到对应文件夹下面
#os.makedirs(path + title.strip())
#os.chdir(path + title.strip())
os.chdir(path)



# 保存图片 url
# for pic_ in soup_1.select('img'):
for i in range(1,92):
    #图片末尾按1、2、3排列
    #pic_url = 'https://pic1.hmpicimage.com/meitui/2021/07/21/b03a347e-4d43-403a-aeb6-c71e3915a904/' + str(i) +'.jpg'
    #图片末尾按001、002、003排列
    pic_url = 'http://p.99gort.cc/uploadfile/2018/0316/06/'+str(i).rjust(2,'0')+'.jpg'

    
        
    # #获取图片名
    file_name = pic_url.split(r'/')[-1]
    file_name = clean(file_name)

    #保存图片
    if file_name != 'slt.jpg':
        if file_name != 'nopic_small.gif':
            print("当前图片 url：", pic_url)
            picture = get_picture(pic_url)
            f = open(file_name,'wb')
            f.write(picture.content)
            f.close()
            # time.sleep(5)
#time.sleep(5)         
        