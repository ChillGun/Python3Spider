# encoding=utf-8

# 导入需要的库
import os
import re
#import requests
import time
#from bs4 import BeautifulSoup

# 保存地址
path = 'C:/Learn6/'

# 创建文件夹并切换到对应文件夹下面
for i in range(0,3):
    dirname = str(i)
    os.makedirs(path + '/' + dirname)
    os.chdir(path + '/' + dirname)
    os.makedirs(path + '/' + dirname + '/' + '测试')

os.chdir(path)