import nltk
from nltk.corpus import stopwords
import string
import pandas as pd
import numpy as np
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
nltk.download('stopwords')

def read_data(path):
    content_list = []
    score_list = []
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        for data in reader:
            content = data[2]
            score = data[3]
            content_list.append(content)
            score_list.append(score)
    return content_list[1:], score_list[1:]


cont_list, sco_list = read_data('Data.csv')
for i in range(len(sco_list)):
    sco_list[i] = int(sco_list[i])
X_train, X_test, y_train, y_test = train_test_split(cont_list, sco_list, test_size=0.15, random_state=22)


def tokenize(content_list):
    punctuation_string = string.punctuation  # for remove punctuation
    stopWords = set(stopwords.words('english'))
    token_content_list = []
    for i in content_list:  # remove punctuation
        for p in punctuation_string:
            i = i.replace(p, '')

        tokens = nltk.word_tokenize(i)
        f_tokens = []

        for w in tokens:  # remove stop words
            if w not in stopWords:
                f_tokens.append(w)
        token_content_list.append(f_tokens)
    return token_content_list


token_content_list = tokenize(cont_list)

vect = CountVectorizer(max_df = 0.8,
                       min_df = 3,
                       token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
                       )

test = pd.DataFrame(vect.fit_transform(cont_list).toarray(), columns=vect.get_feature_names())
nb = MultinomialNB()

X_train_vect = vect.fit_transform(X_train)
nb.fit(X_train_vect, y_train)
train_score = nb.score(X_train_vect, y_train)

X_test_vect = vect.transform(X_test)
print(nb.score(X_test_vect, y_test))