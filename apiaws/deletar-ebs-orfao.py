# carregar as bibliotecas necessárias
import boto3
from pprint import pprint
import dotenv
import os

from pkg_resources import cleanup_resources

# carregar os dados para autenticar que está no arquivo .env
dotenv.load_dotenv()
client = boto3.client('ec2',
                      region_name=os.getenv('AWS_REGION'),
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))



# Carregar  a lista dos EBS
volumes_to_delete = list()
volume_detail = client.describe_volumes()

# Fazer Filtro para carregar todos os ebs
if volume_detail['ResponseMetadata']['HTTPStatusCode'] == 200:
    for each_volume in volume_detail['Volumes']:
        
        print("Working for volume with volume_id: ", each_volume['VolumeId'])
        print("State of volume: ", each_volume['State'])
        print("Attachment state length: ", len(each_volume['Attachments']))
        print(each_volume['Attachments'])
        print("------------------- Proximo EBS ----------------------------")
        # carregar os ebs não atachados 
        if len(each_volume['Attachments']) == 0 and each_volume['State'] == 'available':
            volumes_to_delete.append(each_volume['VolumeId'])

# imprimir tudo 
pprint(volumes_to_delete)
# 
#  Deletar os ebs orfãos
for each_volume_id in volumes_to_delete:
    try:
        print("Deleting Volume with volume_id: " + each_volume_id)
        response = client.delete_volume(
            VolumeId=each_volume_id
        )
    except Exception as e:
        print("Issue in deleting volume with id: " + each_volume_id + "and error is: " + str(e))

# Esperar a confirmação que foi deletado
waiter = client.get_waiter('volume_deleted')
try:
    waiter.wait(
        VolumeIds=volumes_to_delete,
    )
    print("Successfully deleted all volumes")
except Exception as e:
    print("Error in process with error being: " + str(e))