# 得到学生挑战的题目及次数
from selenium import webdriver
from lxml import etree
import re
import pymysql

driver = webdriver.PhantomJS()
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='stuoj',
    charset='utf8mb4'
)
cur = conn.cursor()

url = 'http://47.95.10.46/ranklist.php'



# 班级ID元组
banjiids=tuple(range(1, 2))# 各个班级的Id元组
for banjiid in banjiids:
    print(banjiid)
    sql ="select stuno from student where banjiid ="+str(banjiid)
    cur.execute(sql)
    results = cur.fetchall() #用于返回多条数据
    for stuno in results:
        driver.get(url)
        # 找到页面上的输入用户名的文本框
        driver.find_element_by_name("keyword").send_keys(stuno)  # 输入学生学号
        button = driver.find_elements_by_xpath("//button[@class='btn btn-default']")[1]  # .click() # 单击搜索按钮
        #  container.row.input-group.input-group-btn.btn.btn-default
        button.click()
        # print(result[0])
        link1 = driver.find_elements_by_xpath("//div[@class='col-md-12']/table/tbody/tr/td/a")
        # i = 0
        link = link1[2]# 挑战题目链接
        link.click()
#6.关闭查询
cur.close()