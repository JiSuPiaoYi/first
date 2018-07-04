import urllib.request
import urllib.parse
import os

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
# }
# 下载并保存文件
def download(req, page):

    res = urllib.request.urlopen(req)
    dirname = 'tieba'
    filename = '第'+str(page)+'页.html'
    filtepath = os.path.join(dirname, filename)
    with open(filtepath, 'wb') as fw:
        fw.write(res.read())





# 拼接url以及构建请求对象
def build_url(url,page,tname):
    pn = (page-1)*50
    data = {
        'kw': tname,
        'pn': pn,
    }

    data = urllib.parse.urlencode(data)
    url += data
    req = urllib.request.Request(url=url)
    return req



def main():
    start_page = int(input('请输入起始页码：'))

    end_page = int(input('请输入结束页码：'))

    tname = input('请输入贴吧名称：')

    url = 'http://tieba.baidu.com/f?&ie=utf-8&'

    for page in range(start_page, end_page+1):
        # 返回request对象
        req = build_url(url, page, tname)
        download(req, page)



if __name__ == '__main__':
    main()