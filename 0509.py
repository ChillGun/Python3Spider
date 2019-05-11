#coding=utf-8

import re
import requests
from bs4 import BeautifulSoup



url = 'https://wtfuck.net/page/2/'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

html = requests.get(url,headers = header)

print(html)

#使用自带的html.parser解析，速度慢但通用
soup = BeautifulSoup(html.text,'lxml')

#获取每个单页的src
for h3 in soup. select('h3'):
    print(h3)
    title = (h3.get_text())
    p= re.compile('"(http.*)"')
    srcs = p.findall(str(h3))
    print(type(srcs))
    
    for src in srcs:
        html_2 = requests.get(src,headers = header)
        soup = BeautifulSoup(html_2.text,'lxml')
        print(html_2.text)


print("-------------/n")

all_a = soup.find_all(attrs={"class":"entry-title"})

for a in all_a:
    print(a)
    title = a.get_text()#提取文本
    
    print(title)
