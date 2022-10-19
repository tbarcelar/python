import requests
import os
import json
import pandas as pd



headers = {
  'Accept': 'application/json;datetime-format=rfc3339',
  'DD_API_KEY': 'xxxxxxxxxxxx',
  'DD-APPLICATION-KEY': 'xxxxxxxxxxxxxxxxx',

}

payload={
  'filter[timestamp][start]': '2022-08-01T00:00',
  'filter[timestamp][end]' :'2022-08-01T23:00',
  'filter[product_families]': 'infra_hosts',
  'page['limit']' : '500',
  'page[next_record_id]' : '',
}

r2 = requests.get(' https://api.datadoghq.com/api/v2/usage/hourly_usage', headers=headers, params=payload).content 
obj = json.loads(r2)
df = pd.json_normalize(obj['data'])


listagem = df['attributes.measurements'].tolist()
############ agent_host_count
df_finala = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[0], index=[0])
    df_finala = df_finala.append(df1, ignore_index=True)
df_finala['data'] = df['attributes.timestamp']
df_finala = df_finala[['data','usage_type','value']]


############ alibaba_host_count
df_finalb = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[1], index=[0])
    df_finalb = df_finalb.append(df1, ignore_index=True)
df_finalb['data'] = df['attributes.timestamp']
df_finalb = df_finalb[['data','usage_type','value']]


############ apm_azure_app_service_host_count
df_finalc = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[2], index=[0])
    df_finalc = df_finalc.append(df1, ignore_index=True)
df_finalc['data'] = df['attributes.timestamp']
df_finalc = df_finalc[['data','usage_type','value']]


############ apm_host_count
df_finald = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[3], index=[0])
    df_finald = df_finald.append(df1, ignore_index=True)
df_finald['data'] = df['attributes.timestamp']
df_finald = df_finald[['data','usage_type','value']]


############ aws_host_count
df_finale = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[4], index=[0])
    df_finale = df_finale.append(df1, ignore_index=True)
df_finale['data'] = df['attributes.timestamp']
df_finale = df_finale[['data','usage_type','value']]


############ azure_host_count
df_finalf = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[5], index=[0])
    df_finalf = df_finalf.append(df1, ignore_index=True)
df_finalf['data'] = df['attributes.timestamp']
df_finalf = df_finalf[['data','usage_type','value']]


############ container_count
df_finalg = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[6], index=[0])
    df_finalg = df_finalg.append(df1, ignore_index=True)
df_finalg['data'] = df['attributes.timestamp']
df_finalg = df_finalg[['data','usage_type','value']]


############ gcp_host_count
df_finalh = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[7], index=[0])
    df_finalh = df_finalh.append(df1, ignore_index=True)
df_finalh['data'] = df['attributes.timestamp']
df_finalh = df_finalh[['data','usage_type','value']]



############ heroku_host_count
df_finali = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[8], index=[0])
    df_finali = df_finali.append(df1, ignore_index=True)
df_finali['data'] = df['attributes.timestamp']
df_finali = df_finali[['data','usage_type','value']]


############ host_count
df_finalj = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[9], index=[0])
    df_finalj = df_finalj.append(df1, ignore_index=True)
df_finalj['data'] = df['attributes.timestamp']
df_finalj = df_finalj[['data','usage_type','value']]


############ infra_azure_app_service
df_finalk = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[10], index=[0])
    df_finalk = df_finalk.append(df1, ignore_index=True)
df_finalk['data'] = df['attributes.timestamp']
df_finalk = df_finalk[['data','usage_type','value']]


############ opentelemetry_host_count
df_finall = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[11], index=[0])
    df_finall = df_finall.append(df1, ignore_index=True)
df_finall['data'] = df['attributes.timestamp']
df_finall = df_finall[['data','usage_type','value']]


############ vsphere_host_count
df_finalm = pd.DataFrame(columns = ['usage_type','value'])
for i in listagem:
    df1 = pd.DataFrame(i[12], index=[0])
    df_finalm = df_finalm.append(df1, ignore_index=True)
df_finalm['data'] = df['attributes.timestamp']
df_finalm = df_finalm[['data','usage_type','value']]

######## mesclagem
frame1 = df_finala.merge(df_finalb, on='data', how='left')
frame2 = frame1.merge(df_finalc, on='data', how='left')
frame3 = frame2.merge(df_finald, on='data', how='left')
frame4 = frame3.merge(df_finale, on='data', how='left')
frame5 = frame4.merge(df_finalf, on='data', how='left')
frame6 = frame5.merge(df_finalg, on='data', how='left')
frame7 = frame6.merge(df_finalh, on='data', how='left')
frame8 = frame7.merge(df_finali, on='data', how='left')
frame9 = frame8.merge(df_finalj, on='data', how='left')
frame10 = frame9.merge(df_finalk, on='data', how='left')
frame11 = frame10.merge(df_finall, on='data', how='left')
frame12 = frame11.merge(df_finalm, on='data', how='left')



frame12.columns = ['data', 'agent_host_count', 'agent_host_count_value', 'alibaba_host_count', 'alibaba_host_count_value_', 'apm_azure_app_service_host_count', 'apm_azure_app_service_host_count_value', 'apm_host_count', 'apm_host_count_value', 'aws_host_count','aws_host_count_value','azure_host_count', 'azure_host_count_value', 'container_count', 'container_count_value','gcp_host_count', 'gcp_host_count_value', 'heroku_host_count', 'heroku_host_count_value', 'infra_azure_app_service','infra_azure_app_service_value', 'opentelemetry_host_count', 'opentelemetry_host_count_value', 'vsphere_host_count', 'vsphere_host_count_value','usage_type', 'value']

print(frame12 )