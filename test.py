from sklearn.preprocessing  import LabelEncoder

le = LabelEncoder()
l_train = [1,2,3,4,5]
le.fit(l_train)
print(le.transform(l_train))
# array([0, 1, 2, 3, 4], dtype=int64)
print(le.transform([2,3,4,5]))
#array([1, 2, 3, 4], dtype=int64)

all_topics = open('./reuters21578/all-topics-strings.lc.txt', 'r')
result = all_topics.read().split('\n')
all_topics.close()
result.pop()
print(result)
print(len(result))
