from urllib import request

import requests

from retrying import retry

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

@retry(stop_max_attempt_number=3)   # 让被装饰的函数反复执行三次，三次全报错才会报错
def _parse_url(url):
    print('#'*50)
    response =requests.get(url,headers=headers,timeout=10)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    # url1 = 'www.baidu.com'
    # print(parse_url(url1))
    print(parse_url(url)[:100])