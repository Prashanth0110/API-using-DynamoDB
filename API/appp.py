from flask import Flask, request
from botocore.exceptions import ClientError
from website import controller

app = Flask(__name__)
@app.route('/')
def root_route(resource_name = 'bbt-flifo-data1'):
   return 'Table'+'='+ resource_name
 
@app.route('/get/', methods=['GET'])
def get_movie(resource_name = 'bbt-flifo-data1'):
    response = controller.read_from_movie(resource_name)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if ('Item' in response):
            return { 'Item': response['Item'] }
        else:
            return { 'msg' : 'Item not found!' }
    else:
        return {
            'msg': 'error occurred',
            'response': response
        }
 
@app.route('/delete/', methods=['DELETE'])
def delete_movie(resource_name = 'bbt-flifo-data1'):
    response = controller.delete_from_movie(resource_name)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Delete successful',
        }
    else:
        return { 
            'msg': 'error occurred',
            'response': response
        }
 
@app.route('/update/', methods=['PUT'])
def update_movie(resource_name = 'bbt-flifo-data1'):
 
    data = request.get_json()
    response = controller.update_in_movie(resource_name, data)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'                : 'update successful',
            'response'           : response['ResponseMetadata'],
            'ModifiedAttributes' : response['Attributes']
        }
    else:
        return {
            'msg'      : 'error occurred',
            'response' : response
        }  
 
if __name__ == '__main__':
    app.run()