from google_play_scraper import Sort,reviews
import pandas as pd

result, continuation_token = reviews(
    'com.fantome.penguinisle',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=500
)


name_list = []
score_list = []
content_list = []

for i in result:
    name_list.append(i['userName'])
    content_list.append(i['content'])
    score_list.append(i['score'])

dic = {'UserName':name_list, 'content':content_list, 'score':score_list}
df = pd.DataFrame(dic)
df.to_csv('data.csv')