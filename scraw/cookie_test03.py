# -*- coding:UTF-8 -*-
import requests
from selenium import webdriver

# if __name__ == '__main__':
#     url = 'https://www.baidu.com/'
#     headers = {'Upgrade-Insecure-Requests':'1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate, sdch, br',
#     'Accept-Language':'zh-CN,zh;q=0.8',
#     }
#     s = requests.Session()
#     req = s.get(url=url,headers=headers)
#     print(s.cookies)

if __name__ == '__main__':
    url = 'http://pythonscraping.com'
    driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())