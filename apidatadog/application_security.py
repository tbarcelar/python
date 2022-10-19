
import requests
import os
import json
import pandas as pd

headers = {
  'Accept': 'application/json;datetime-format=rfc3339',
  'DD_API_KEY': 'xxxxxxxxxxx',
  'DD-APPLICATION-KEY': 'xxxxxxxxxxxxxxx',

}

payload={
  'filter[timestamp][start]': '2022-08-01T00:00',
  'filter[timestamp][end]' :'2022-08-01T23:00',
  'filter[product_families]': 'application_security',
  'page' : 'next_record_id',
}

r2 = requests.get(' https://api.datadoghq.com/api/v2/usage/hourly_usage', headers=headers, params=payload).content 

obj = json.loads(r2)
df = pd.json_normalize(obj['data'])
listagem = df['attributes.measurements'].tolist()

security = pd.DataFrame(columns = ['value'])
for security1 in listagem:
    df1 = pd.DataFrame(security1[0], index=[0])
    security = security.append(df1, ignore_index=True)
security['data'] = df['attributes.timestamp']
security = security[['data','value']]
security.columns=['data',  'application_security']

print(security)