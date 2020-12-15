# Major features
1. use two methods svm and naive_bayes with tfidf to classify article
2. article may have multi-topic, so apply two approach
    2-1. split multi-topic to different single topic instance, for example:
        [topic 1, topic 2] article 1 => topic 1 article 1
                                        topic 2 article 1
    
    2-2. delete multi-topic
The result is that delete multi-topic has better performance, no matter use svm or naive_bayes

 3. write predict topic of each article to excel(./data/svm_single_label_result.xls, ./data/nb_single_label_result.xls)
 4. Automatically classifying all test documents in ModApte, and showing evaluation results for classification effectiveness (precision, recall, F-measure, accuracy), show in screen shot: svm.png, naive_bayes.png
# Major difficulties encountered
solution of multi-topic

# Enviroment Setting
## download virtualbox and install ubuntu
please set enough resource to your vm(e.g. memory, cpu..)

below install steps is install in virtual machine
install python, sklearn

# Instructions
1. execute generate_dataset.py to generate ModApte dataset from Reuters21578
2. execute svm_tfidf.py to get classification result (./data/svm_single_label_result.xls)and evaluation score precision, recall, F-measure, accuracy
3. execute naive_bayes_tfidf.py to get classification result(./data/nb_single_label_result.xls) and evaluation score precision, recall, F-measure, accuracy
# team member
109598091 陳逸芳