
'''
json
数据交换的格式
把json字符串转化为python类型
-json.loads (json字符串)


-json.dumps
    -把python类型转化为字符串
'''

import json
import requests

url = 'https://'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    'Referer:https://m.douban.com/tv/america'
}