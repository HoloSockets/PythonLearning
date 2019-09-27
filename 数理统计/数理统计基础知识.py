# -*- coding:utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings

sns.set(style='darkgrid')
mpl.rcParams['font.family'] = 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False
warnings.filterwarnings('ignore')

# 加载鸢尾花数据集
iris = load_iris()
# print(iris.data[:10], iris.target[:10])
# print(iris.feature_names, iris.target_names)

# 将鸢尾花数据与对应的类型合并，组合完成记录
data = np.concatenate([iris.data, iris.target.reshape(-1, 1)], axis=1)
data = pd.DataFrame(data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type'])
data.sample(10)
# print(data.sample(10))

'''
1.频数和概率
'''
# # 计算鸢尾花数据中，每个类别出现的频数
# # frequency = data['type'].value_counts()
# # print('type of frequency:', type(frequency))
# # print(frequency)
# # # 计算每个类别出现的频率，通常使用百分比表示
# # percentage = frequency * 100 / len(data)
# # print('type of percentage:', type(percentage))
# # print(percentage)
# #
# # frequency.plot(kind='bar')
# # plt.show()

'''
2.集中趋势
均值、中位数、众数
数值变量（均值、中位数）
类别变量（众数）
正态分布下，均值、中位数、众数三者相同
偏态分布下，均值、中位数、众数三者不相同（左偏分布 均值-中位数-众数 右偏分布 众数-中位数-均值）
均值容易受极端值的影响
中位数与众数不受极端值的影响，相对稳定
众数在一组数据中可能不唯一
'''
# # 计算花萼长度的均值
# mean = data['sepal_length'].mean()
# # 计算花萼长度的中位数
# median = data['sepal_length'].median()
# # 计算花萼长度的众数
# s = data['sepal_length'].value_counts()
# mode = s.keys()[0]
# print(mean, median, mode)
#
# sns.distplot(data['sepal_length'])
# plt.axvline(mean, ls='-', color='r', label='均值')
# plt.axvline(median, ls='-', color='g', label='中位数')
# plt.axvline(mode, ls='-', color='indigo', label='众数')
# plt.legend()
# plt.show()

'''
扩展
分位数
不一定会是数据集中的元素
'''
# # 分位数是数据集中的元素
# x = np.arange(10, 19)
# n = len(x)
# q1_index = 1 + (n - 1) * 0.25
# q2_index = 1 + (n - 1) * 0.5
# q3_index = 1 + (n - 1) * 0.75
# print(q1_index, q2_index, q3_index)
#
# index = np.array([q1_index, q2_index, q3_index]).astype(np.int32)
# index -= 1
# print(x[index])
#
# plt.figure(figsize=(15, 4))
# plt.xticks(x)
# plt.plot(x, np.zeros(len(x)), ls='', marker='D', ms=15, label='元素值')
# plt.plot(x[index], np.zeros(len(index)), ls='', marker='X', ms=15, label='四分位值')
# plt.legend()
# plt.show()

# # 中位数不是数据集中的元素
# x = np.arange(10, 20)
# n = len(x)
# q1_index = 1 + (n - 1) * 0.25
# q2_index = 1 + (n - 1) * 0.5
# q3_index = 1 + (n - 1) * 0.75
# print(q1_index, q2_index, q3_index)
#
# index = np.array([q1_index, q2_index, q3_index])
# left = np.floor(index).astype(np.int32) - 1
# right = np.ceil(index).astype(np.int32) - 1
# weight, _ = np.modf(index)
# q = x[left] * (1 - weight) + x[right] * weight
# print(q)
#
# plt.figure(figsize=(15, 4))
# plt.xticks(x)
# plt.plot(x, np.zeros(len(x)), ls='', marker='D', ms=15, label='元素值')
# plt.plot(q, np.zeros(len(q)), ls='', marker='X', ms=15, label='四分位值')
# for v in q:
#     plt.text(v, 0.01, s=v, fontsize=15)
# plt.legend()
# plt.show()

# Numpy中计算分位数
x = [1, 3, 10, 15, 18, 20, 21, 23, 40]
print(np.quantile(x, [0.25, 0.5, 0.75]))
x = [1, 3, 10, 15, 18, 20, 23, 40]
print(np.quantile(x, [0.25, 0.5, 0.75]))

# Pandas中计算分位数
x = [1, 3, 10, 15, 18, 20, 21, 23, 40]
s = pd.Series(x)
print(s.describe())
print(s.describe()[4])
print(s.describe()['25%'])
print(s.describe().iloc[4])
# print(s.describe()loc['25%'])
print(s.describe().ix[4])
# print(s.describe()ix['25%'])

