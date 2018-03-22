# import requests
#
# params = {'firstname':'Ryan','lastname':'Mitchell'}
# r =requests.post("http://pythonscraping.com/files/processing.php",data=params)
# print(r.text)

from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()