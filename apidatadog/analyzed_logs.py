
import requests
import os
import json
import pandas as pd

headers = {
  'Accept': 'application/json;datetime-format=rfc3339',
  'DD_API_KEY': 'xxxxxxxxxxx',
  'DD-APPLICATION-KEY': 'xxxxxxxxxx',

}

payload={
  'filter[timestamp][start]': '2022-08-01T00:00',
  'filter[timestamp][end]' :'2022-08-01T23:00',
  'filter[product_families]': 'analyzed_logs',
  'page' : 'next_record_id',
}

r2 = requests.get(' https://api.datadoghq.com/api/v2/usage/hourly_usage', headers=headers, params=payload).content 

obj = json.loads(r2)
df = pd.json_normalize(obj['data'])
listagem = df['attributes.measurements'].tolist()

############ analyzed_logs

df1 = pd.DataFrame(columns = ['value'])
for i in listagem:
    df2 = pd.DataFrame(i[0], index=[0])
    df1 = df1.append(df2, ignore_index=True)
df1['data'] = df['attributes.timestamp']
df1 = df1[['data','value']]
df1.columns=['data', 'analyzed_logs']
print(df1)