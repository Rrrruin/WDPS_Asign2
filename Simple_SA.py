import pandas as pd
import re
import emoji
from textblob import TextBlob
from snownlp import SnowNLP
import nltk


def remove_emoji(text, replace=" "):
    return re.sub(emoji.get_emoji_regexp(), replace, text)


def judge_english(text):
    return all(ord(c) < 128 for c in text)


reader = pd.read_csv('Data.csv', engine='python', sep='\t', error_bad_lines=False)

# 非英文处理
for i in range(len(reader['content'])):
    print(type(reader['content'][i]))
    t_str = remove_emoji(reader['content'][i])
    if not judge_english(t_str):
        reader = reader.drop(index=[i])
reader.reset_index(drop=True, inplace=True)

# 评论中对引用台词的处理

test_df = reader['content']
text_list = test_df.to_list()


score_list = []
for text in text_list:
    s = TextBlob(text)
    score = s.sentences[0].sentiment
    score_list.append(score)

# for text in text_list:
#     s = SnowNLP(text)
#     score = s.sentiments
#     score_list.append(score)

reader['score'] = score_list
reader.to_excel('snow_result.xlsx')



