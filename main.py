import json
from BrokenAccessControl.idor import idor_main
from Injection.xss import xss_main
from Injection.sqli import sqli_main
from Injection.template_injection import template_injection_main

data = {}
paths_get=[]
            
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
#sqli_main(schema,host,headers,cookies,paths)

#Calling XSS Module
#xss_main(schema, host, headers, cookies, paths)

#Calling Template Injection Module
#template_injection_main(schema, host, headers, cookies, paths)

#Calling Idor Module
idor_main(schema, host, headers, cookies, paths)