import  requests

# 实例化session
session = requests.session()

# 使用session发送post请求，获取对方报错在本地的cookie
post_url = 'http://www.renren.com/PLogin.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

post_data = {
    'email': 'mr_mao_hacker@163.com',
    'password': 'alarmchime'
}

session.post(post_url,headers=headers,data=post_data)


# 在使用session请求登录后的页面
url = 'http://www.renren.com/PLogin.do'
response = session.get(url,headers=headers)

with open('renren2.html', 'w') as f:
    f.write(response.content.decode())

