from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from nltk.corpus import stopwords
import re

def cleanbody(body):
    stopwords_set = set(stopwords.words('english'))
    body = re.sub('\sReuter\n\x03','',body) #postfix of artical
    body = body.replace('\n', ' ').lower().strip()
    result = ' '.join([text for text in body.split() if text not in stopwords_set])
    return result

def getData(result):
    resultDict = {}
    if result.find('topics')==None:
        resultDict['topic'] = ""
    else:
        resultDict['topic'] = [topic.get_text() for topic in result.find('topics').find_all('d')]
    if result.find('body')==None:
        resultDict['body'] = ""
    else:
        resultDict['body'] = result.find('body').get_text()
    return resultDict

def dataToCsv(dataList, outputpath):
    df = pd.DataFrame(dataList)
    df['body'] = df['body'].apply(cleanbody)
    print("Total Retrieved: {0}".format(len(df)))
    df.to_csv(outputpath, index=False)

testResultList = []
trainResultList = []
# file_list = glob('./test/test.sgm')
file_list = glob('./reuters21578/*.sgm')


for filename in file_list:
    print(f'start parsing {filename}')
    file = open(filename, 'rb')
    htmlResults = BeautifulSoup(file, 'html.parser')
    file.close()
    for result in htmlResults.find_all('reuters', lewissplit="TEST", topics="YES"):
        testResultList.append(getData(result))
    for result in htmlResults.find_all('reuters', lewissplit="TRAIN", topics="YES"):
        trainResultList.append(getData(result))
    print('=============done==============')

dataToCsv(trainResultList, './data/train_data.txt')
dataToCsv(testResultList, './data/test_data.txt')