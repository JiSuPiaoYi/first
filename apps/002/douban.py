import urllib.request
import urllib.parse


url = 'https://movie.douban.com/j/chart/top_list?type=22&interval_id=100%3A90'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

page = int(input('请输入您要的页码'))

start = (page-1)*20
limit = 20

data = {
    'start': start,
    'limit': limit
}

data = urllib.parse.urlencode(data)

url = url+data

req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)


with open('douban', 'wb') as fw:
    fw.write(res.read())
print(res.read().decode('utf-8'))
