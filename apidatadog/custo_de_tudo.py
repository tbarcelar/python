
import requests
import json



headers = {
  'Accept': 'application/json;datetime-format=rfc3339',
  'DD_API_KEY': 'xxxxxxxxxxx',
  'DD-APPLICATION-KEY': 'xxxxxxxxxxxxxxxxxx',

}

payload={
  'filter[timestamp][start]': '2022-08-01T00:00',
  'filter[timestamp][end]' :'2022-08-30T23:00',
  'filter[product_families]': 'all',
}

r2 = requests.get(' https://api.datadoghq.com/api/v2/usage/hourly_usage', headers=headers, params=payload)


print(r2.content)
''' 
data = r2.content
with open('data.json', 'wb') as f:
    f.write(data)

'''
