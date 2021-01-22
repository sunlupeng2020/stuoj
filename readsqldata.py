# 读取MySQL数据库中的数据
import pandas as pd
from sqlalchemy import create_engine
from pandas import DataFrame,Series


# 练习：使用pandas组件读取Mysql数据库中的学生数据
def read_student_oj_info():
    engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/stuoj')
    #result = pd.read_sql('stuchallenged',engine)
    result = pd.read_sql("select stuno,questionid from stuchallenged order by stuno,questionid",engine)
    print(result)


# 练习:用pandas组件将DataFrame数据写入数据库
def write_to_mysql_pd():
    df = DataFrame({"班级":["一年级", "二年级", "三年级", "四年级"],
                    "男生人数":[25, 23, 27, 30],
                    "女生人数":[19, 17, 20, 20]})
    # 创建数据库引擎
    engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/stuoj')
    df.to_sql('lx_studentinfo1', engine)


def read_average_oj_num_by_gender():  # 从数据库中查询B20软工1班学生的学号、性别、做题数量
    engine = create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/stuoj')
    result = pd.read_sql("select gender,avg(accept) from student where banjiid=1 group by gender", engine)
    # result = pd.read_sql("select stuno,gender,accept from student where banjiid=1 order by gender", engine)
    print(result)


if __name__ == '__main__':
    # write_to_mysql_pd()
    read_average_oj_num_by_gender()

