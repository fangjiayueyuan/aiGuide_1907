
import re
import pandas as pd

csv_file = pd.read_csv(open('zs2zd.csv',encoding='gbk')).values

r1 = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
# print(csv_file)
for person in csv_file:
    # print(person)
    zhusu = person[0]
    jianyaobs = person[1]
    # linchuangzdId = person[2][0:6]
    linchuangzd = person[2][7:]     #将临床诊断中的特殊字符过滤
    print(re.sub(r1,'',linchuangzd))

    df1 = pd.DataFrame()