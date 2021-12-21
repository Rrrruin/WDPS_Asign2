import csv

import pandas as pd
import plotly
import plotly.express as px

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

content_list, score_list = read_data('Data.csv')

# graph about distribute of scores
df = pd.read_csv('Data.csv')
fig = px.histogram(df, x='score')
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Score Distribution')
plotly.offline.plot(fig)

