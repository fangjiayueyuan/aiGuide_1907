# 皮肤
import requests
import json
from bs4 import BeautifulSoup
import bs4
import re
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "
def saveData(filename,data_list):
    file = open(filename,'a')
    for i in range(len(data_list)):
        s = str(data_list[i]).replace('[', '').replace(']', '').replace("                   ",'')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')   # 去除单引号，逗号，每行末尾追加换行符
        s = s.replace(" ","")
        file.write(s)
    file.close()
    print("保存文件成功")

def main():
    depth = 10
    start_url = 'https://www.chunyuyisheng.com/pc/qalist/clinicno_4/?query_str=%E6%A2%85%E6%AF%92&page=1&high_quality=1'
    infoList = []
    re_wen = re.compile(r'(?<=<i class="ask-tag">)[\s\S]*?(?=</a>)')
    re_da = re.compile(r'(?<=<div class="qa-item qa-item-answer">)[\s\S]*?(?=</div>)')
    file_name = ('./ask001.txt')


    for i in range(1, depth):
        url = start_url + '&page=' + str(i)
        html = getHTMLText(url)
        result_a=re_wen.findall(html)
        result_b=re_da.findall(html)

        for i in range (len(result_a)):
            result_a[i]=result_a[i].replace("   ","").replace(r"</i>",':').replace("\n","").replace("\t","")+"\n"
            saveData(file_name, result_a[i])
        for i in range(len(result_b)):
            result_b[i] = result_b[i].replace('<i class="ask-tag answer-tag">', "").replace("<span class='s-hl'>",'').replace("</span>", "").replace(" ","").replace(r"</i>",":").replace("\t","")+"\n"
            saveData(file_name, result_b[i])
        for i in range(len(result_b)):
            print(str(i)+":"+result_a[i]+result_b[i])

main()
