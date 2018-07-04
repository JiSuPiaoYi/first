import requests


url = 'http://fanyi.baidu.com/basetrans'

# 发送post请求，请求体为字典
data = {
    'query': '人生苦短，我用python',
    'from': 'zh',
    'to': 'en'
}

response = requests.post(url, data=data)

print(response)