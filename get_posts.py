import time 
import Post
import pandas as pd
from pandas.io.json import json_normalize

i = 0
page = {'Init'}

while True:
	data = Post.ct_get_posts(count=100,offset=i,include_history='true',start_date='2021-01-01',end_date='2021-01-02',api_token=Post.token,listIds=1578298)
	try:
		page = data['result']['pagination']['nextPage']
		f=open("Leg_"+str(i)+'.json','w')
		f.write("%s" %data)
		f.close()
		print(i)
		i += 100
		time.sleep(13)
	except:
		page = data['result']
		f=open("Leg_"+str(i)+'.json','w')
		f.write("%s" %data)
		f.close()
		break

"""
#data = Post.ct_get_posts(start_date='2020-01-01',end_date='2020-01-31',api_token=Post.token,listIds=1577627)
#f=open("NTU"+str(i)+'.json','w')
#f.write("%s" %data)
#f.close()
#print(i)
#time.sleep(15)

#print(data)
"""