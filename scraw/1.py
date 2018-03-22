# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    req = "http://fanyi.baidu.com"
    response = request.urlopen(req)
    html = response.read()
    url = response.geturl()
    info = response.info()
    code = response.getcode()
    # charset = chardet.detect(html)
    html = html.decode("utf-8")
    print(html)
    print('**********************************************')
    print(url)
    print('**********************************************')
    print(info)
    print('**********************************************')
    print(code)