#selenium结合PhantomJS()访问百度，输出新闻标题
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")
data = driver.find_element_by_id("wrapper").text
print(data)
print(driver.title)