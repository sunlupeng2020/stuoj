# 读取excel表中的学生名单，写入到mysql数据库中
import xlrd
import pymysql

# 打开excel
wb = xlrd.open_workbook(r'D:\ChromeCoreDownloads\班级名册--B20信息安全.xls')
# 按工作簿定位工作表
sh = wb.sheet_by_name('班级名册')
print(sh.nrows)# 有效数据行数
print(sh.ncols)# 有效数据列数
print(sh.cell(0, 0).value)# 输出第一行第一列的值
# print(sh.row_values(0))# 输出第一行的所有值
# 将数据和标题组合成字典
# print(dict(zip(sh.row_values(0), sh.row_values(1))))
# 遍历excel，打印所有数据
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='stuoj',
    charset='utf8mb4'
)
cur = conn.cursor()
for i in range(1, sh.nrows):
    # print(sh.row_values(i))
    sql = "insert into student(banjiid,stuno,name) values(%s,%s,%s);"# 将学生信息插入数据库的student表
    # sql = 'INSERT INTO test_student_table VALUES(%s,%s,%s);'
    # insert(sql, (2, 'wang', 13))
    key = sh.row_values(i)[0]
    value = sh.row_values(i)[1]
    print(key, value)
    cur.execute(sql, (7, key, value))# 班级id,学号，姓名
# 关闭连接
cur.close()