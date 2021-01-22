# 创建两层索引结构的Series对象、三层结构的DataFrame对象等
import numpy as np
import  pandas as pd
from pandas import DataFrame,Series
from pandas import MultiIndex


# 创建三层结构的DataFrame对象等
def createseries():
    mulitindex_series = pd.Series([15848,13472,12073.8,7813,7446,6444,15230,8269],
                                  index=[['河北省','河北省','河北省','河北省','河南省','河南省','河南省','河南省'],
                                         ['石家庄市','唐山市','邯郸市','秦皇岛市','郑州市','开封市','洛阳市','新乡市']])
    print(mulitindex_series)

    # 创建有两层结构的DataFrame对象
    multiindex_df = DataFrame({'占地面积':[15848,13472,12073.8,7813,7446,6444,15230,8269]},
                              index=[['河北省','河北省','河北省','河北省','河南省','河南省','河南省','河南省'],
                                         ['石家庄市','唐山市','邯郸市','秦皇岛市','郑州市','开封市','洛阳市','新乡市']])
    print(multiindex_df)

# 通过from_tuples()方法创建MultiIndex对象
def createmultiindexfromtuples():
    # 创建包含多个元组的列表
    list_tuples = [('A','A1'),('A','A2'),('B','B1'),('B','B2'),('B','B3')]
    # 根据元祖列表创建一个MultiIndex对象
    multi_index = MultiIndex.from_tuples(tuples=list_tuples,names=['外层索引','内层索引'])
    # print(multi_index)
    # 创建一个DataFrame对象
    values = [[1,2,3],[8,5,7],[4,7,7],[5,5,4],[4,9,9]]
    df_indexs = pd.DataFrame(data=values,index = multi_index)
    print(df_indexs)


# 通过数组创建MultiIndex对象
def create_multi_index_from_array():
    multi_array = MultiIndex.from_arrays(arrays = [['A', 'A', 'B', 'B', 'B'],
                                                  ['A1', 'A2', 'B1', 'B2', 'B3']],
                                         names = ['外层索引','内层索引'])
    values = np.array([[1,2,3],[8,5,7],[4,7,7],[5,5,4],[4,9,9]])
    df_array = DataFrame(data = values, index=multi_array)
    print(df_array)


# 通过from_product()方法创建Multiindex对象, 从多个集合的笛卡尔乘积中创建MultiIndex对象
def create_multi_index_from_product():
    numbers = [0,1,2]
    colors = ['green', 'purple']
    multi_product = pd.MultiIndex.from_product(iterables=[numbers,colors],names=['number','color'])
    print(multi_product)
    values = np.array([[7,5],[6,6],[3,1],[5,5],[4,5],[5,3]])
    df_procut = DataFrame(data=values,index=multi_product)
    print(df_procut)


# 层次化索引操作
def series_index():
    ser_obj = Series([50,60,40,94,63,101,200,56,45],
                     index=[['小说','小说','小说',
                             '散文随笔','散文随笔','散文随笔',
                             '传记','传记','传记'],
                            ['高山上的小邮局','失踪的总统','绿毛水怪',
                             '皮囊','浮生六记','自在独行',
                             '梅西','老舍自传','库里传']])
    print(ser_obj)
    # 选取子集操作
    print(ser_obj['小说'])
    # 交换子集操作
    ser_obj2 = ser_obj.swaplevel()
    print(ser_obj2)
    # print(ser_obj)
    # 排序分层


def

if __name__ == '__main__':
    # create_multi_index_from_array()
    # create_multi_index_from_product()
    series_index()



