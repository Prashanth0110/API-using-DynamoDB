import boto3

def get_single_item(resource_name):
        client = boto3.resource('dynamodb', 
        endpoint_url="http://localhost:8000",
        region_name='ap-south-1',
        aws_access_key_id='yhsebe',
        aws_secret_access_key='mv8du8')

        table = client.Table(resource_name)

        response = table.get_item(
            
            Key={
                'Departure': 'SFO',
                'LclDepDtm' : '06MAY22T14:10'
            }
        )
        
        return (response['Item'])

print(get_single_item('bbt-flifo-data1'))