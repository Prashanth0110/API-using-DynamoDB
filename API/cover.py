from boto3.dynamodb.conditions import Key
import boto3

def get_item(resource_name,id1,id2):
    
    client = boto3.resource('dynamodb', 
    endpoint_url="http://localhost:8000",
    region_name='ap-south-1',
    aws_access_key_id='vy5154',
    aws_secret_access_key='x0ta4')        
    table = client.Table(resource_name)
    response = table.get_item(
        
        Key={
            'FlightLegKey':id1,
            'docType' : id2
        }
    )
    return response

def delete_item(resource_name,id1,id2):
    
    client = boto3.resource('dynamodb', 
    endpoint_url="http://localhost:8000",
    region_name='ap-south-1',
    aws_access_key_id='vy5154',
    aws_secret_access_key='x0ta4')        
    table = client.Table(resource_name)
    response = table.delete_item(
        Key={
            'FlightLegKey': id1,
            'docType' : id2
        }
    )
    return response

def query_item(resource_name):
    
    client = boto3.resource('dynamodb', 
    endpoint_url="http://localhost:8000",
    region_name='ap-south-1',
    aws_access_key_id='vy5154',
    aws_secret_access_key='x0ta4')        
    table = client.Table(resource_name)
    response = table.query(
        KeyConditionExpression=Key('FlightLegKey').eq('UA::0001::1::25MAY22')
    )
    return response    
