# 自定义请求
import urllib.request
url = 'http://www.baidu.com'
# res = urllib.request.urlopen(url=url)
# # print(res.getheaders())

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
# 构建请求
req = urllib.request.Request(url=url, headers=headers)

# 发送请求
res = urllib.request.urlopen(req)

print(res.read.decode('utf-8'))