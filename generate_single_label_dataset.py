from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from nltk.corpus import stopwords
import re

def cleanbody(body):
    stopwords_set = set(stopwords.words('english'))
    body = body.replace('\n', ' ').lower().strip()
    body = body[0:-9] #postfix of artical
    result = ' '.join([text for text in body.split() if text not in stopwords_set])
    return result

def getData(result):
    resultDictList = []
    body = ""
    if result.find('body')!=None:
        body = result.find('body').get_text()
    else:
        return
    if result.find('topics')==None or len([topic.get_text() for topic in result.find('topics').find_all('d')]) > 1:
        return
    else:
        resultDict = {}
        resultDict['topic'] = result.find('topics').get_text()
        resultDict['body'] = body
        resultDictList.append(resultDict)
    return resultDictList

def dataToCsv(dataList, outputpath):
    df = pd.DataFrame(dataList)
    df['body'] = df['body'].apply(cleanbody)
    print("Total Retrieved: {0}".format(len(df)))
    df.to_csv(outputpath, index=False)

testResultList = []
trainResultList = []
# file_list = glob('./test/test.sgm')
file_list = sorted(glob('./reuters21578/*.sgm'))
for filename in file_list:
    print(f'start parsing {filename}')
    file = open(filename, 'rb')
    htmlResults = BeautifulSoup(file, 'html.parser')
    file.close()
    for result in htmlResults.find_all('reuters', lewissplit="TEST", topics="YES"):
        if getData(result) == None:
            continue
        else:
            for r in getData(result):
                testResultList.append(r)
    for result in htmlResults.find_all('reuters', lewissplit="TRAIN", topics="YES"):
        if getData(result) == None:
            continue
        else:
            for r in getData(result):
                trainResultList.append(r)
    print('=============done==============')

dataToCsv(trainResultList, './data/train_data_single_label.txt')
dataToCsv(testResultList, './data/test_data_single_label.txt')
df_train = pd.read_csv('./data/train_data_single_label.txt').dropna()
df_train.to_csv('./data/train_data_single_label.xls', index=False)
df_test = pd.read_csv('./data/test_data_single_label.txt').dropna()
df_test.to_csv('./data/test_data_single_label.xls', index=False)