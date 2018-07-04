import urllib.request
import urllib.parse


# # 有中文的需要编码
# url = 'http://www.baidu.com?name=中国'
# str = urllib.parse.quote(url)
# print(str)
# # http%3A//www.baidu.com%3Fname%3D%E4%B8%AD%E5%9B%BD

# 解码
str = urllib.parse.unquote('http%3A//www.baidu.com%3Fname%3D%E4%B8%AD%E5%9B%BD')
print(str)
# http://www.baidu.com?name=中国