import json
from BrokenAccessControl.idor import idor_main
from Injection.xss import xss_main
from Injection.sqli import sqli_main
from Injection.template_injection import template_injection_main
data = {}
with open ('./api-data/api-docs.json','r') as f:
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
            #idor_main(str(host),path_request,method,params_request)
            #xss_main(str(host),path_request,method,params_request)
            

#Reads the config api information
with open ('./api-data/config.json','r') as f:
    data = json.load(f)

#Get the schema information
schema = data['schema']

#Get the host information
host=data['host']

#Get the headers information
headers=data['headers']

#Get the cookies information
cookies=data['cookies']

#Get the paths information
paths=data['paths']

#Calling Sqli Module
sqli_main(schema,host,headers,cookies,paths)

#Calling XSS Module
xss_main(schema, host, headers, cookies, paths)

#Calling Template Injection Module
template_injection_main(schema, host, headers, cookies, paths)