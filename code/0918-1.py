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
path = 'E:/20200918下载/pic30_秦雪/'

# 创建文件夹并切换到对应文件夹下面
#os.makedirs(path + title.strip())
#os.chdir(path + title.strip())
os.chdir(path)

page_url = "http://www.9grt.net/html/yazhou/5028"
page_number = 133   #总页数
for i in range(132,page_number):
    #以此获取page页的url并获取网页文件
    if i <2:
        url = page_url+'.html'
    else:
        url = page_url+'_'+str(i)+".html"
    
    page = requests.get(url,headers = Hostreferer)
    print("当前 Page 页访问结果：",page)
    print("当前 page 页 url 为：", url)

    # 解析 page 页
    soup_1 = BeautifulSoup(page.text,'lxml')

    # 获取 theme 页中的图片 url
    for pic_ in soup_1.select('img'):
        
        
            
        # #获取图片名
        file_name = pic_['src'].split(r'/')[-1]
        file_name = clean(file_name)

        #保存图片
        if file_name != 'slt.jpg' :
            print("当前图片 url：", pic_['src'])
            picture = get_picture(pic_['src'])
            f = open(file_name,'wb')
            f.write(picture.content)
            f.close()
        
        