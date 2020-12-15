import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

# data preprocessing: dropna
data_train = pd.read_csv('./data/train_data_1on1.xls')
data_test = pd.read_csv('./data/test_data_1on1.xls')
# data_train = pd.read_csv('./data/train_data_single_label.xls')
# data_test = pd.read_csv('./data/test_data_single_label.xls')

# data_train = data_train.dropna()
train_y = data_train['topic']
train_x = data_train['body']

# data_test = data_test.dropna()
test_y = data_test['topic']
test_x = data_test['body']

# label encoding all topic and transform test_y, train_y
label_encoder = LabelEncoder()
topics_file = open('./reuters21578/all-topics-strings.lc.txt', 'r')
topic_list = topics_file.read().split('\n')
topics_file.close()
topic_list.pop()

label_encoder.fit(topic_list)
vec_y_train = label_encoder.transform(train_y)
data_train['label_encoding'] = vec_y_train

vec_y_test = label_encoder.transform(test_y)
data_test['label_encoding'] = vec_y_test

# building pipeline
start_time = time.time()
# method 1
svm_classify = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('svc', SVC())])
svm_classify = svm_classify.fit(train_x, vec_y_train)
prediction = svm_classify.predict(test_x)

def transferPrediction2Label(prediction):
    transfered = []
    for p in prediction:
        transfered.append(topic_list[p])
    return transfered

data_test.insert(1,'label_predict',transferPrediction2Label(prediction))

end_time = time.time()
print('spend time: ', str(end_time-start_time))
data_test.to_csv('./data/svm_single_label_result.xls', index=False)

# f1_score
print('f1 macro: ',metrics.f1_score(vec_y_test, prediction, average='macro'))
print('f1 micro: ',metrics.f1_score(vec_y_test, prediction, average='micro'))
print('f1 weighted: ',metrics.f1_score(vec_y_test, prediction, average='weighted'))
# precision_score
print('precision macro: ', metrics.precision_score(vec_y_test, prediction, average='macro'))
print('precision micro: ', metrics.precision_score(vec_y_test, prediction, average='micro'))
print('precision weighted: ', metrics.precision_score(vec_y_test, prediction, average='weighted'))
# recall_score
print('recall macro: ', metrics.recall_score(vec_y_test, prediction, average='macro'))
print('recall micro: ', metrics.recall_score(vec_y_test, prediction, average='micro'))
print('recall weighted: ', metrics.recall_score(vec_y_test, prediction, average='weighted'))