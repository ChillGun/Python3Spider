import requests
from bs4 import BeautifulSoup
import os

Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://wtfuck.net'
}
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}

def get_page_name(url):#获得图集最大页数和名称
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('cboxElement')
    title = soup.find('h1', class_="entry-title")
    return len(span), title.text, span

def get_html(url):#获得页面html代码
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html

def get_img_url(url, name):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find('img', alt= name)
    return img_url['src']

def save_img(img_url, count, name):
    req = requests.get(img_url, headers=Picreferer)
    with open(name+'/'+str(count)+'.jpg', 'wb') as f:
        f.write(req.content)

def main():
    old_url = "http://wtfuck.net/freya-haworth-by-mike-chalmers"
    page, name, span= get_page_name(old_url)
    os.mkdir(name)
    for i in range(1,int(page)+1):
        img_url = span[i].get(src)
        #print(img_url)
        save_img(img_url, i, name)
        print('保存第' + str(i) + '张图片成功')
main()