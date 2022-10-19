
import requests
import os
import json
import pandas as pd

headers = {
  'Accept': 'application/json;datetime-format=rfc3339',
  'DD_API_KEY': 'xxxxxxxxx',
  'DD-APPLICATION-KEY': 'xxxxxxxxxx',

}

payload={
  'filter[timestamp][start]': '2022-08-01T00:00',
  'filter[timestamp][end]' :'2022-08-01T23:00',
  'filter[product_families]': 'serverless',
  'page' : 'next_record_id',
}

r2 = requests.get(' https://api.datadoghq.com/api/v2/usage/hourly_usage', headers=headers, params=payload).content 

obj = json.loads(r2)
df = pd.json_normalize(obj['data'])
listagem = df['attributes.measurements'].tolist()

### serverless func_count

serverless = pd.DataFrame(columns = ['value'])
for serve in listagem:
    df1 = pd.DataFrame(serve[0], index=[0])
    serverless = serverless.append(df1, ignore_index=True)
serverless['data'] = df['attributes.timestamp']
serverless = serverless[['data','value']]
serverless.columns=['data',  'serverless_func_count']

######## serverless invocations_sum

serverless1 = pd.DataFrame(columns = ['value'])
for serve1 in listagem:
    df1 = pd.DataFrame(serve1[1], index=[0])
    serverless1 = serverless1.append(df1, ignore_index=True)
serverless1['data'] = df['attributes.timestamp']
serverless1 = serverless1[['data','value']]
serverless1.columns=['data',  'serverless_invocations_sum']

######## mesclagem

frame1 =  serverless.merge(serverless1, on='data', how='left')

print(frame1)