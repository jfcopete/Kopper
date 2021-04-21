import requests
import random
import time

random.seed(float(time.time()))

def get_random():
    return random.choice(list(range(100)))

def assign_values(type_param):
    if(type_param=='integer'):
        random_var=random.randint(1,100)
        return random_var
    return 0

def idor_main(host,path,method,parameters):
#HTTP mientras averiguo que es un perro esquema
    if(method=='get'):
        schema='http://'
        for param in parameters:
            for x in range(100):
                param_path=assign_values(param['type'])
                print(param_path)
                path_uri=path.replace('{'+param['name']+'}',str(param_path))
                uri_builder=schema+host+path_uri
                request=requests.get(str(uri_builder))
                response_request=request.text
                print(parameters)
                print(uri_builder)
                print(str(response_request))
                print(str(request.status_code))

