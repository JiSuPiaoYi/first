import urllib.parse
import urllib.request

kw = input('请输入您要搜的内容：')
kw = urllib.parse.quote(kw)
url = 'http://www.baidu.com/s?wd='+kw
# print(url)
# # exit()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}


# 构建请求对象
req = urllib.request.Request(url=url, headers=headers)
# 发送请求
res = urllib.request.urlopen(req)

# 数据的读写保存
# with open('china.html','wb') as fw:
#     fw.write(res.read())

with open('meinv.html', 'w', encoding='utf-8') as fw:
    fw.write(res.read().decode('utf-8'))