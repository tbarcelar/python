
import requests
import json
import pandas as pd

headers = {
  'Accept': 'application/json;datetime-format=rfc3339',
  'DD_API_KEY': 'xxxxxxxxxxx',
  'DD-APPLICATION-KEY': 'xxxxxxxxxxxx',

}

payload={
  'start_hr':'2022-08-01T00',
  'end_hr': '2022-08-30T23',

}

### ingested spans
r2 = requests.get('https://api.datadoghq.com/api/v1/usage/ingested-spans', headers=headers, params=payload).content 
obj = json.loads(r2)
igspan = pd.json_normalize(obj['usage'])
#print(igspan)

### indexed spans
r2 = requests.get('https://api.datadoghq.com/api/v1/usage/indexed-spans', headers=headers, params=payload).content 
obj = json.loads(r2)
indexspan = pd.json_normalize(obj['usage'])
#print(indexspan)

######## mesclagem

frames = [igspan, indexspan ]
  
result = pd.concat(frames)

print(result)
