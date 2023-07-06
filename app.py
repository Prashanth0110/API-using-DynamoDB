import json
import boto3
from flask import Flask
from botocore.exceptions import ClientError

app = Flask(__name__)
@app.route('/resource_name', methods=['GET'])

def get_single_item(resource_name = 'DataModel'):
    try:
        client = boto3.resource('dynamodb', 
        endpoint_url="http://localhost:8000",
        region_name='ap-south-1',
        aws_access_key_id='yhsebe',
        aws_secret_access_key='mv8du8')        
        table = client.Table(resource_name)

        response = table.get_item(
            
            Key={
                'FlightLegKey': '112::32::1::234',
                'docType' : 'ZXC::23::1::321::0'
            }
        )
        return(
            json.dumps(response['Item'], indent = 1),
            response['ResponseMetadata']['HTTPStatusCode'],
            {'Content-Typeo': 'application/json'}
        )
    except ClientError as e:
        data={
            "status2": e.response['Error']['Message']
        }
        return (
            json.dumps(data, indent=4, sort_keys=True),
            e.response['ResponseMetadata']['HTTPStatusCode'],
            {'Content-Typo': 'application/json'}
            )                          
    except Exception as e:
        data={
            "status3": e.args[0]
        }
        return (
            json.dumps(data, indent=4, sort_keys=True),
            400,
            {'Content-Typu': 'application/json'}
            )

if __name__ == '__main__':
    app.run()		
    
    