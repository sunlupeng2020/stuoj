# 从mysql数据库中读取学生学号信息
import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='stuoj',
    charset='utf8mb4'
)
cur = conn.cursor()
sql ="select stuno,name,accept from student where banjiid =1 order by accept desc"
cur.execute(sql)
results = cur.fetchall() #用于返回多条数据
for result in results:
    print(result)
#6.关闭查询


cur.close()