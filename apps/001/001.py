import urllib.request
# url = 'http://www.baidu.com'
# 发送请求
# res = urllib.request.urlopen(url=url)

# 读取文件并解码
# result = res.read().decode('utf-8')

# print(result)
# 下载并保存到本地
# urllib.request.urlretrieve(url=url, filename='baidu.html')


# 图片
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531122472&di=451eb09dc0ad5ed565d76da8c7517e90&imgtype=jpg&er=1&src=http%3A%2F%2Fimg5.zdface.com%2F006yCHQygy1fji19zzsljj30m80etdgu.jpg'
res = urllib.request.urlopen(url=url)
result = res.read()
urllib.request.urlretrieve(url=url, filename='meinv1.jpg')
