'''去除春雨医生里面的停词'''
import jieba
import jieba.posseg as pseg


def readTxt(filename):
    with open(filename,encoding="utf-8") as file_to_read:
        f = file_to_read.read()
        return f
    # f = f.read()



def main():
    filename = './语料/产科.txt'
    stopwords = readTxt('./stopWords.txt')
    f = readTxt(filename)
    print(f,stopwords)

if __name__ == '__main__':
    main()