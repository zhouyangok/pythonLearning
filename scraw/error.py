# -*- coding: UTF-8 -*-

from urllib import request
from urllib import  error

if __name__ == "__main__":
    #url 不存在
    # url = "http://ww.hjiji.com/"
    # req = request.Request(url)
    # try:
    #     response = request.urlopen(req)
    #     html = response.read().decode('utf-8')
    #     print(html)
    # except error.URLError as e:
    #     print(e.reason)

    # 一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)