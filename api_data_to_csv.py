import time 
import Post
import pandas as pd
from pandas.io.json import json_normalize

data = Post.ct_get_posts(count=100,offset=0,include_history='true',start_date='2021-01-01',end_date='2021-01-02',api_token=Post.token,listIds=1578298)
df = json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False)
