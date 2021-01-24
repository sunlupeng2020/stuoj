# 数据清洗练习
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from numpy import NaN

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


if __name__ == '__main__':
    # isnull_use()
    # fill_nan_use()
    # dropna_use()
    dupli_use()

