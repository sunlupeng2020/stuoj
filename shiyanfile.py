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
# 班级ID元组
banjiids=tuple(range(1, 8))# 各个班级的Id元组
for banjiid in banjiids:
    print(banjiid)
    sql ="select stuno from student where banjiid ="+str(banjiid)
    cur.execute(sql)
    results = cur.fetchall() #用于返回多条数据
    for result in results:
        print(result[0])
#6.关闭查询
cur.close()

