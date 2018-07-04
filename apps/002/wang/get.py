import requests


url = 'http://www.baidu.com'
# 发送get请求，请求url地址对应的响应
response = requests.get(url)

# 获取网页的html字符串
# response.encoding = 'utf-8'

# 把响应的二进制字节流转化为str类型
response.content.decode()
print(response.text)


'''
获取网页源码的正确打开方式
1 .response.content.decode()
2 .response.content.decode('gbk')
3 .response.text

发送带header请求
    是为了模拟浏览器，获取和浏览器一模一样的内容

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

使用超时参数
-request.get(url,headers=headers,timeout=3)
3秒内必须返回响应，否则回报错

from

'''



