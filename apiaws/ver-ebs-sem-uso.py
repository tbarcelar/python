# carregar as bibliotecas necessárias
import boto3
from pprint import pprint
import dotenv
import os

from pkg_resources import cleanup_resources

# carregar os dados para autenticar que está no arquivo com nome .env
dotenv.load_dotenv()
client = boto3.client('ec2',
                      region_name=os.getenv('AWS_REGION'),
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))



# Carregar a lista dos EBS
volumes_to_delete = list()
volume_detail = client.describe_volumes()

# Fazer Filtro para carregar
if volume_detail['ResponseMetadata']['HTTPStatusCode'] == 200:
    for each_volume in volume_detail['Volumes']:
        
        if len(each_volume['Attachments']) == 0 and each_volume['State'] == 'available':
            volumes_to_delete.append(each_volume['VolumeId'])
            
# imprimir tudo 
print("------------------- EBS sem uso ----------------------------")
pprint(volumes_to_delete)
