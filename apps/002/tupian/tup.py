import re
import os
import urllib.request

def getHtml(url):
    res = urllib.request.urlopen(url)  #打开url地址
    html = res.read().decode('utf-8')  #读取url页面数据
    return html

def getImg(html):
    reg = r'src=".+?\.jpg"'
    imgre = re.compile(reg)
    # imglist = re.findall(imgre, html)
    imglist = imgre.findall(html)     # 第二种findall方式

    imgurllist = []
    for imgurl in imglist:
        src = re.compile(r'com(\/.+\.jpg)')
        imgsrc = src.findall(imgurl)
        imgurllist.append('http://img.mukewang.com'+imgsrc[0])

    x = 0
    for imgurl in imgurllist:
        path = os.path.abspath('.')
        urllib.request.urlretrieve(imgurl, path + '/image/%s.jpg' % x)
        x += 1

    return imgurllist

html = getHtml("http://www.imooc.com/course/list")
imgurllist = getImg(html)
print(imgurllist)