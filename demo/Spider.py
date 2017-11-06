# -*- coding: utf-8 -*-
'''
Created on 2017年11月3日

@author: Jeff Yang
'''
import os
import requests
from urllib.request import urlretrieve

def get_url(day=0):
    """参数值0为今天，1为昨天，-1为明天"""
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=" + str(day) + "&n=1&nc=1509675905008&pid=hp&video=1"
    return url

def get_img(url, path="D://wallpaper/"):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
    html = requests.get(url)
    content = html.json()
    src = "https://www.bing.com" + content['images'][0]['url']
    urlretrieve(src, path + content['images'][0]['enddate'] + '.jpg')
#     return content['images'][0]['enddate'] + '.jpg'
   
def show_img(url):
    html = requests.get(url)
    content = html.json()
    src = "https://www.bing.com" + content['images'][0]['url']
    req = requests.get(src)
    return req.content,content['images'][0]['enddate'] + '.jpg'
    
if __name__ == '__main__':  
    get_img(get_url())  
