#coding:utf-8
import sys
import requests
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
    file = open(filename,'a',encoding="utf-8")
    for i in range(len(data_list)):
        s = str(data_list[i]).replace('[', '').replace(']', '').replace("                   ",'')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '')   # 去除单引号，逗号，每行末尾追加换行符
        s = s.replace(" ","")
        file.write(s)
    file.close()
    print("保存文件成功")

def main():
    depth = 101
    file_name = ('./语料/产科.txt')
    start_url = 'https://www.chunyuyisheng.com/pc/qalist/clinicno_21/?high_quality=1'
    re_wen = re.compile(r'(?<=<i class="ask-tag">)[\s\S]*?(?=</a>)')
    re_da = re.compile(r'(?<=<div class="qa-item qa-item-answer">)[\s\S]*?(?=</div>)')
    for i in range(1, depth):
        url = start_url + '&page=' + str(i)+"#hotqa"
        html = getHTMLText(url)
        result_a=re_wen.findall(html)
        result_b=re_da.findall(html)
        for j in range (len(result_a)):
            result_a[j] = result_a[j].replace("   ", "").replace(r"</i>", ':').replace("\n", "").replace("\t","")
            result_b[j] = result_b[j].replace('<i class="ask-tag answer-tag">', "").replace("<span class='s-hl'>",'').replace("</span>", "").replace("\t", '').replace(r"</i>", ':').replace(" ", "\n")+"\n"
            saveData(file_name, result_a[j])
            saveData(file_name, result_b[j])
        for j in range(len(result_b)):
            print(str(i)+":"+result_a[j]+result_b[j])
main()

