import requests
from bs4 import BeautifulSoup
import os

Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
}
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}

def get_html(url):#获得页面html代码
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html

def save_img(img_url, count, name):
    req = requests.get(img_url, headers=Picreferer)
    with open(name+'/'+str(count)+'.jpg', 'wb') as f:
        f.write(req.content)

def get_page_name(url):#获得图集最大页数和名称
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('cboxElement')
    title = soup.find('h1', class_="entry-title")
    return span, title


def main():
    old_url = "http://wtfuck.net/freya-haworth-by-mike-chalmers"
    page, name= get_page_name(old_url)
    os.mkdir(name)
    for photo in span:
        print(photo)
        url=photo
        print(name)
        img = requests.get(url)
        file_name = name + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()
    


main()
