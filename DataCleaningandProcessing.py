import os

import string
import json, csv
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_columns", None)

fileJsonPath = "/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/Clothing_Shoes_and_Jewelry_Rating_catergory_30k.json"

with open(fileJsonPath, encoding='utf-8', errors='ignore') as json_data:
     data = json.load(json_data, strict=False)

fileCsvPath = "/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/BertDataSet.csv"

from contextlib import nullcontext
with open(fileCsvPath, 'w', newline='') as csv_file:
    fieldnames = ["asin","overall","reviewerID","reviewText", "summary"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for r in data:
      #print(r)
      writer.writerow({'asin': str(r['asin']),'overall': str(r['overall']),'reviewerID': str(r['reviewerID']),'reviewText': str(r['reviewText']), 'summary': str(r['summary'])})


df = pd.read_csv ('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/BertDataSet.csv')


df = df.dropna()

df['ReviewTag'] = np.where(df['overall'] < 3, 'Negative' , 'Positive')
df = df.sort_values(by=['ReviewTag'])
df.head()
with open('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/Data_with_Review_tag.csv', 'w') as csv_file:
    df.to_csv(path_or_buf=csv_file)
df4 = df[df['ReviewTag']=='Positive']

with open('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/positive_data.txt', 'w') as csv_file:
    df4.to_csv(path_or_buf=csv_file)

df5 = df[df['ReviewTag']=='Negative']

with open('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/negative_data.csv', 'w') as csv_file:
    df5.to_csv(path_or_buf=csv_file)


curr_word = None
curr_count = 0

for row in df['ReviewTag']:
	word = row 
	count = 1
	
	if word == curr_word:
		curr_count += count
	else:
		if curr_word:
			print('{0}\t{1}'.format(curr_word, curr_count))
	
		curr_word = word
		curr_count = count

if curr_word == word:
	print('{0}\t{1}'.format(curr_word, curr_count))

df['ReviewTag'].value_counts()

df2= df.groupby('asin')
df3 = df2['ReviewTag'].value_counts()
print(df3)

with open('/Users/shalinidhamodharan/Documents/UHCL_DS/Spring2023/Big_Data/Project/bigdataproject/Project_Final/csv_data.txt', 'w') as csv_file:
    df3.to_csv(path_or_buf=csv_file)
