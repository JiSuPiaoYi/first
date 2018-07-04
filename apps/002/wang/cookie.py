import requests

url = 'http://www.renren.com/327550029/profile'

# 直接携带cookies请求url地址
# ---1.cookies放在headers中

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
#     'Cookie': 'anonymid=jj5ojicdidlgua; depovince=GW; jebecookies=1694ba58-8a7a-414c-b891-e1353c4e33d2|||||; _r01_=1; JSESSIONID=abcHaj9D7Bm9F6b6XjGrw; ick_login=7e3e5097-8617-4d42-8349-ed0e9c4c27ac; jebe_key=bfe2dcc9-ce6c-4b0d-b72f-770cf4c6314b%7Ccfcd208495d565ef66e7dff9f98764da%7C1530621537060%7C0%7C1530621542306'
#
# }


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
# cookie字典传给cookies参数
cookie = 'anonymid=jj5ojicdidlgua; depovince=GW; jebecookies=1694ba58-8a7a-414c-b891-e1353c4e33d2|||||; _r01_=1; JSESSIONID=abcHaj9D7Bm9F6b6XjGrw; ick_login=7e3e5097-8617-4d42-8349-ed0e9c4c27ac; jebe_key=bfe2dcc9-ce6c-4b0d-b72f-770cf4c6314b%7Ccfcd208495d565ef66e7dff9f98764da%7C1530621537060%7C0%7C1530621542306'
cookie_dict = {i.split('=')[0]: i.split('=')[-1] for i in cookie.split(';')}
print(cookie_dict)


response = requests.get(url, headers=headers, cookies=cookie_dict)

with open('renren1.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())