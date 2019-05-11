import requests #导入requests库
import re #写正则表达式要导入的
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
res = requests.get('https://wtfuck.net/freya-haworth-by-mike-chalmers') #像目标url地址发送get请求，返回一个response对象
print(res.text) #r.text是http response的网页HTML
res.encoding='utf-8' #把获取到的源代码格式改为utf-8，避免汉子乱码
html=res.text
 
chapter_photo_list=re.findall(r'<img class="alignnone size-full wp-image-114809".*?srcset="(.*?)100w,',html)
print(chapter_photo_list)
 
#os.mkdir('D:\BeautifulPicture')  #创建文件夹
os.chdir('D:\')   #切换路径至上面创建的文件夹
for chapter_photo in chapter_photo_list:
    print(chapter_photo)
    url=chapter_photo
    name=re.findall(r'photo-(.*?)-',chapter_photo)[0]
    print(name)
    img = requests.get(url)
    file_name = name + '.jpg'
    print('开始保存图片')
    f = open(file_name, 'ab')
    f.write(img.content)
    print(file_name, '图片保存成功！')
    f.close()
