#! python3
# 使用多线程爬取顺序排列的图片
# coding=utf-8

# 导入需要的库
import os
import re
import requests
import time
import threading
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

# 设置保存地址并切换到该地址
path = 'G:/FFOutput-1/其它/pic/pic108_/06、晶晶/'
os.chdir(path)

def downpic(startPic, endPic):
    for i in range(startPic,endPic):
        #图片末尾按1、2、3排列
        #pic_url = 'https://pic1.hmpicimage.com/meitui/2021/07/21/b03a347e-4d43-403a-aeb6-c71e3915a904/' + str(i) +'.jpg'
        #图片末尾按001、002、003排列
        pic_url = 'http://p.99gort.in/uploadfile/2018/0127/06/'+str(i).rjust(2,'0')+'.jpg'

        
            
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


# 使用多线程下载
downloadThreads = []                 
for i in range(0, 156, 10):        # 定义图片的起始和终止编号，以及每个线程处理几张图片
    downloadThread = threading.Thread(target=downpic, args=(i, i + 9))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

