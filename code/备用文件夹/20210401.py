# encoding=utf-8

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
            
    
    # 返回图片
    return picture
    


# 保存地址
path = 'G:/FFOutput-1/其它/pic/pic106/'

# 创建文件夹并切换到对应文件夹下面
#os.makedirs(path + title.strip())
#os.chdir(path + title.strip())
os.chdir(path)

theme_url = "http://www.gogogort.info/html/guomosipai/index"
for j in range (1,98):
    if j < 2:
        index_url = theme_url+'.html'
    else:
        index_url = theme_url+"_"+str(j)+'.html'
    
    theme = requests.get(index_url,headers = Hostreferer)
    theme.encoding="gbk"
    print("当前 theme 页访问结果：",theme)
    print("当前 theme 页 url 为：", index_url)
    
    time.sleep(2)

    theme_soup = BeautifulSoup(theme.text,'lxml')
    
    # 创建一个数字作为文件夹的编号
    folder_number = 0
    
    #提取一个大页中每个主题的URL，一下两种方法均可
    #for ul in theme_soup.find_all(attrs={'class':'ulPic'}):
    for ul in theme_soup.find_all(class_='ulPic'):
        
        for li in ul.find_all(name="li"):
            #print(li)
            
            for a in li.select('a'):
                print(a)
                print(a.attrs['href'])

                b = a.attrs['href'].split('.')[0]
                print(b)


                page_url = "http://www.gogogort.info"+b
                #总页数
                page_number = 200   
                
                #获取主题的名字，作为后面的文件夹名
                page = requests.get(page_url+".html",headers = Hostreferer)
                page.encoding="gbk"
                print("当前 Page 页访问结果：",page)
                print("当前 page 页 url 为：", page_url)
                soup_1 = BeautifulSoup(page.text,'lxml')
                page_title = soup_1.find("title")
                #print(page_title.string.split(' - ')[0])
                page_name = clean(page_title.string.split(' - ')[0])
                print("当前页的主题："+page_name)

                # 文件夹编号+1
                folder_number = folder_number + 1

                # 创建以主题为名字的文件夹，并切换到该文件夹下面
                os.makedirs(path + '/' + str(j) + '_' + str(folder_number) +'_'+ page_name)
                os.chdir(path + '/' + str(j) + '_' + str(folder_number) +'_'+ page_name)

                # 遍历该主题下的每一个页面，并保存图片，因为此处页面数没法确定，所以暂时选择200作为上限
                for i in range(1,page_number):
                    #以此获取page页的url并获取网页文件
                    if i <2:
                        url = page_url+'.html'
                    else:
                        url = page_url+'_'+str(i)+".html"
                    
                    page = requests.get(url,headers = Hostreferer)
                    print("当前 page 页 url 为：", url)
                    print("当前 Page 页访问结果：",page)

                    if page.status_code==404:
                        break
                    
                    

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
                                f = open(file_name,'wb')
                                f.write(picture.content)
                                f.close()
                                #time.sleep(5)
                    #time.sleep(5)  
                # 遍历完一个主题，切换至主文件夹 
                os.chdir(path) 
            

                
                    