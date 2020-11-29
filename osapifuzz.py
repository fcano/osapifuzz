import yaml
import sys
import requests

class Operation:
    pass

fin = open(sys.argv[1], 'r')

api = yaml.safe_load(fin)

operations = []

for path in api['paths']:
    if 'get' in api['paths'][path].keys():
        operation = Operation()
        operation.url = path
        operation.method = 'get'
        if 'operationId' in api['paths'][path]['get'].keys():
            operation.operationId = api['paths'][path]['get']['operationId']
        operations.append(operation)
    if 'post' in api['paths'][path].keys():
        operation = Operation()
        operation.url = path
        operation.method = 'post'
        if 'operationId' in api['paths'][path]['post'].keys():
            operation.operationId = api['paths'][path]['post']['operationId']
        operations.append(operation)        

for operation in operations:
    if operation.method == 'get':
        r = requests.get(url=operation.url)
    if operation.method == 'post':
        r = requests.post(url=operation.url)
