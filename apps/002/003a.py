import json
import urllib.request
import urllib.parse

url = 'http://fanyi.baidu.com/sug/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

kw = input('请输入要查询的词:')

data = {
    'kw': kw
}
# 编码动作
data = urllib.parse.urlencode(data).encode('utf-8')
# 构建请求
req = urllib.request.Request(url=url, headers=headers, data=data)
# 发送请求
res = urllib.request.urlopen(req)
# 读取响应数据
result = res.read().decode('utf-8')
# 把json字符串转为python对象
json_obj = json.loads(result)


#把python对象转为json字符串
str = json.dumps(json_obj, ensure_ascii=False)
# print(result)

# 进行写入操作
with open('static/fy1.json', 'w', encoding='utf-8') as fw:
    fw.write(str)
