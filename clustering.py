import jieba
import wordcloud

import pandas as pd

import pandas as pd

headers = ["department","lei","chapter","chtitle","article","arttitle","content"]
data = pd.read_csv("lei_output.csv",names=headers)

data.head()
for item in data['content']:
    print(item)