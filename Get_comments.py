import os
import pandas as pd
import glob

csv_list = glob.glob('Data/*.csv')

for i in csv_list:
    fr = open(i, 'rb').read()
    with open ('comments.csv', 'ab') as f:
        f.write(fr)