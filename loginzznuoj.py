# 登陆郑州师范学院OJ平台
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

def loginzznuoj(username,password): # 根据用户名和密码登陆
    # username = 'slp'
    # password = 'slp123456'
    loginurl = 'http://47.95.10.46/loginpage.php'
    driver = webdriver.PhantomJS()
    driver.get(loginurl)
    driver.find_element_by_name("username").send_keys(str(username))
    driver.find_element_by_name("password").send_keys(str(password))
    driver.find_element_by_tag_name("button").click()
    try:
        WebDriverWait(driver,10).until(EC.title_is("ZZNUOJ"))
    finally:
        pass
