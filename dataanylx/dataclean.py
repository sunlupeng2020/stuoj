# 数据清洗练习
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from numpy import NaN
import matplotlib.pyplot as plt


# 判断数据为空或不可用(缺失)
def isnull_use():
    series_obj = Series([1, None, NaN])
    print(pd.isnull(series_obj))
    print(pd.notnull(series_obj))

# 填充缺失值或空值
def fill_nan_use():
    df_obj=pd.DataFrame({'A': [1, 2, 3, NaN],
                        'B': [NaN, 4, NaN, 6],
                        'C': ['a', 7, 8, 9],
                        'D': [NaN, 2, 3, NaN]})
    df_filled = df_obj.fillna('66.0')
    df_filled2 = df_obj.fillna({'A': 4.0, 'B': 5.0})
    df_ffiled = df_obj.fillna(method='ffill')   # 前向填充，用同列中前面的数据替换后面的空值
    print(df_obj)
    print(df_ffiled)
    # print("填充后：")
    # print(df_filled)
    # print(df_filled2)
    # print(df_ffiled)


#删除空值或缺失值的行或列
def dropna_use():
    df_obj = pd.DataFrame({'类别':['小说','散文随笔','青春文学','传记'],
                           '书名':[np.nan,'《皮囊》','《旅程结束时》','老舍自传'],
                           '作者':['老舍',None,'张其鑫','老舍']})
    print(df_obj)
    print(df_obj.dropna())


# 重复值的处理duplicated函数和drop_duplicated函数
def dupli_use():
    person_info = pd.DataFrame({'id': [1, 2, 3, 4, 4, 5],
                                'name': ['小铭', '小月月', '彭岩', '刘华', '刘华', '周华'],
                                'age': [18, 18, 29, 58, 58, 36],
                                'height': [180, 180, 185, 175, 175, 178],
                                'gender': ['女', '女', '男', '男', '男', '男']})
    du_serise = person_info.duplicated(keep=False)  # 检测重复值
    print(du_serise)
    droped_pi = person_info.drop_duplicates()  # 删除重复值，多行只保留一行
    print(droped_pi)


# 基于3σ 原则，检测一组数据中是否存在异常值
def three_sigma(ser1):
    mean_value = ser1.mean()  # 求平均值
    std_value = ser1.std()  # 求标准差
    # 设置规则：位于[u-3σ,u+3σ]区间的数据是正常的，不在这个区间的数据为异常的
    # 一旦发现有异常值，就标注为True，否则标注为False
    rule = (mean_value-3*std_value > ser1) | (mean_value+3*std_value < ser1)
    # 返回异常值的位置索引
    index = np.arange(ser1.shape[0])[rule]
    outrange = ser1.iloc[index]
    return outrange


def exeption_value_deal():  # 异常值处理函数
    # 读取数据
    file = open(r'../data/example_data.csv')  # 读取数据文件
    df = pd.read_csv(file)
    # print(df)
    exeption_value = three_sigma(df['A'])
    print(exeption_value)  # 输出数据的索引和值


def box_check_exept():  # 箱型检测异常值
    df = pd.DataFrame({'A': [1, 2, 3, 4],
                       'B': [2, 3, 5, 2],
                       'C': [1, 4, 7, 4],
                       'D': [1, 5, 30, 3]})
    # print(df.boxplot(column=['A','B','C','D']))
    df.boxplot(column=['A', 'B', 'C', 'D'])
    # plt.boxplot(df)
    # plt.show()  # 显示箱型图


# 异常值替换
def exception_value_replace():
    df = pd.DataFrame({'菜谱名': ['红烧肉','铁板鱿鱼','小炒肉','干煸鸭掌','酸菜鱼'],
                       '价格': [38,25,26,388,35]})
    df1 = df.replace(to_replace=388,value=38.8)
    print(df1)


def trans_data_type_1():
    """显示DataFrame中的数据类型

    """
    df = pd.DataFrame({'A': [5,6,7],'B':[3,2,1]},dtype='int')
    print(df.dtypes)


def trans_data_type_2():
    pass


if __name__ == '__main__':
    # isnull_use()
    # fill_nan_use()
    # dropna_use()
    # dupli_use()
    # exeption_value_deal()
    # box_check_exept()
    # exception_value_replace()
    trans_data_type_1()
