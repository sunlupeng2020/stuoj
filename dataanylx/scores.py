# 案例——北京高考分数线统计分析
# 对北京市近年来高考数据进行一些简单的操作，具体分析包括：
# （1）一本文理科与二本文理科最高的分数线是多少，最低的分数线是多少，相差多少分
# （2）今年与去年相比，一本文理科与二本文理科变化了多少分？
# （3）求2006-2018年近13年每科分数线的平均值
import pandas as pd
import numpy as np



def read_and_sort_scores():  # 从excel文件中读取数据并排序
    # df_obj = pd.read_excel('../data/scores.xlsx', header=[0, 1]) 提示不支持xlsx文件
    df_obj1 = pd.read_excel('../data/scores1.xls', header=[0, 1], index_col=[0])
    # 排序
    sorted_obj = df_obj1.sort_index(ascending=False)
    # print(sorted_obj)
    # print(df_obj1)
    return sorted_obj  # 按年度排序的数据


# 获取历年一本、二本文理科最高和最低的分数线及极差
def get_max_min_diff_scores(sorted_obj):
    max = sorted_obj.max()
    min = sorted_obj.min()
    # result1 = sorted_obj["一本分数线", "文科"].ptp()  # .ptp()
    res1 = np.ptp(sorted_obj["一本分数线", "文科"])
    # result2 = sorted_obj["一本本分数线","理科"].ptp()
    res2 = np.ptp(sorted_obj["一本分数线", "理科"])
    # result3 = sorted_obj["二本分数线","文科"].ptp()
    res3 = np.ptp(sorted_obj["二本分数线", "文科"])
    # result4 = sorted_obj["二本分数线","理科"].ptp()
    res4 = np.ptp(sorted_obj["二本分数线", "理科"])
    # print(result1, result2, result3, result4)
    print(res1, res2, res3, res4)
    # print(result1)
    # print(max, min)
    return max


def get_serise_ptp():
    sr = pd.Series([11, 21, 8, 18, 65, 84, 32, 10, 5, 24, 32])
    # Print the series
    print(sr)
    result = np.ptp(sr)
    print(result)


# 比较2018年一本与二本文理科分数线的差值
def fenshuxian_2018_2017():
    sorted_obj1 = read_and_sort_scores()
    # print(sorted_obj1)
    ser_obj1 = sorted_obj1['一本分数线', '文科']
    print(ser_obj1[2018] - ser_obj1[2017])
    ser_obj2 = sorted_obj1['一本分数线', '理科']
    print(ser_obj2[2018] - ser_obj2[2017])
    ser_obj3 = sorted_obj1['二本分数线', '文科']
    print(ser_obj3[2018] - ser_obj3[2017])
    ser_obj4 = sorted_obj1['二本分数线', '理科']
    print(ser_obj4[2018] - ser_obj4[2017])
    # print(ser_obj1)


# 计算2006-—2018年的平均分数线
def mean_fenshuxian_2006_2018():
    sorted_obj1 = read_and_sort_scores()
    return sorted_obj1.describe()


if __name__ == '__main__':
    # sorted_obj1 = read_and_sort_scores()
    # max_obj = get_max_min_diff_scores(sorted_obj1)
    # print(max_obj)
    # print(sorted_obj1)
    # get_serise_ptp()
    # fenshuxian_2018_2017()
    describe = mean_fenshuxian_2006_2018()
    print(describe)
