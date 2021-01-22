# selenium结合PhantomJS()访问郑州师范学院OJ平台，统计学生在OJ平台上C语言题目的提交情况
# 写入数据库stuoj的stuquestionbh表中
# 导入selenium的
from selenium import webdriver
# import MySQLdb

from selenium.webdriver.common.by import By
import pymysql

 # db=pymysql.connect("localhost","root","","stuoj")
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='stuoj',
    charset='utf8'
)
cur = conn.cursor()

driver = webdriver.PhantomJS()

def getstuquestions(stuno):#按学号搜索学生通过题目数、挑战题目数
    # 访问郑州师范学院OJ平台的“排名”页面
    driver.get("http://47.95.10.46/ranklist.php")
    # 找到页面上的输入用户名的文本框
    driver.find_element_by_name("keyword").send_keys(stuno)  # 输入学生学号
    button = driver.find_elements_by_xpath("//button[@class='btn btn-default']")[1]  # .click() # 单机搜索按钮
    #  container.row.input-group.input-group-btn.btn.btn-default
    button.click()
    # 找到学生名字、通过题目数、提交数等的超链接
    link1 = driver.find_elements_by_xpath("//div[@class='col-md-12']/table/tbody/tr/td/a")
    i = 0
    link = link1[0]
    link.click()
    # 找到题号的超链接
    timuhaos = driver.find_elements_by_xpath("//div[@class='well collapse in']/a")
    # print(timuhaos)
    for tihaolink in timuhaos:
        # print(tihaolink.text) #输出题号
        # 将学生做的题号插入到数据库
        sql="insert into stuques(stuno,questionbh)values(%s,%s)"
        cur.execute(sql, (stuno, tihaolink.text))
        # print(stuno, tihaolink.text)

def getstudentxuehao():
    banjiids = tuple(range(1, 2))# 各个班级的Id元组
    for banjiid in banjiids:
        print(banjiid)
        sql = "select stuno from student where banjiid =" + str(banjiid)
        cur.execute(sql)
        results = cur.fetchall()  # 用于返回多条数据，得到全部学生学号
        for stuno in results:  # print(result[0])
            # 得到学生完成的题目数
            getstuquestions(stuno)


getstudentxuehao()# 得到所有学生做的题号
cur.close()
driver.close()
# 可以更新学生的完成的题目数
# update student set accept=(select count(*) from stuquestionbh where stuno=student.stuno)

