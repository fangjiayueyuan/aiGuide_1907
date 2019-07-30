import jieba
import csv
import pandas as pd
import numpy as np

csvFile = csv.reader(open(r'trainingData.csv',encoding="utf-8"))
# 导入医学专有名词字典
# with open(file='./Minedic.txt', mode='r', encoding='utf-8') as f:
#   read = f.readlines()
#
# for line in read:
#   str = line.replace('\t', ' ').rstrip()
#   with open('./Minedic.txt', 'a+', encoding='utf-8')as f1:
#     # print(1)
#     f1.write(str + '\n')



# for item in csvFile:
#   zhuSu = item[1]
#   print(zhuSu)
#   zhenDuan = item[2]
#   segListZhusu = jieba.cut(zhuSu)  # 默认是精确模式
#   print("/".join(segListZhusu))
#   segListZhenDuan = jieba.cut(zhenDuan)  # 默认是精确模式
#   print("/".join(segListZhenDuan))

# 统计类别多少
data_dict = {}
total = 0
for item in csvFile:
    zhenDuan = item[2]
    if zhenDuan not in data_dict:
        data_dict[zhenDuan] = 0
    data_dict[zhenDuan] = data_dict[zhenDuan] + 1
 # 统计标签的总数目
for val in data_dict.values():
    total += val

for item in data_dict:
    print(data_dict[item])
for item in data_dict:
    print(item)
print(total)