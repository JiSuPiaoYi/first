import urllib.request
import urllib.parse


url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

data = {
    'cname': '北京',
    'pid': '',
    'pageIndex': '1',
    'pageSize': '10'

}

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url=url, headers=headers, data=data)

res = urllib.request.urlopen(req)

print(res.read().decode('utf-8'))