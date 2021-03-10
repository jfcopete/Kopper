import json
from BrokenAccessControl.idor import idor_main
data = {}
with open ('./swagger-data/api-docs.json','r') as f:
    data = json.load(f)
host=data['host']

paths_get=[]

for path in data['paths']:
    # for get request while implementing next methods or actions
    if ('{' in path and '}' in path):
        #print(path)
        paths_get.append(path)
        #print(data['paths'][path].values())
        if('get' in data['paths'][path]):
            method='get'
            path_request=path
            params_request=data['paths'][path]['get']['parameters']
            #name_request=data['paths'][path]['get']['parameters']['name']
            #in_request=data['paths'][path]['get']['parameters']['in']
            #required_request=data['paths'][path]['get']['parameters']['required']
            #type_request=data['paths'][path]['get']['parameters']['type']
            #format_request=data['paths'][path]['get']['parameters']['format']
            idor_main(str(host),path_request,method,params_request)
            
            



