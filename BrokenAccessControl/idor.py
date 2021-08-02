import requests
import random
import time
from util.create_report import create_report_main
from util.get_headers import get_headers_global

get="GET"
post="POST"
put="PUT"
delete="DELETE"

random.seed(float(time.time()))

def get_random():
    return random.choice(list(range(100)))

def assign_values(type_param):
    if(type_param=='integer'):
        random_var=random.randint(1,100)
        return random_var
    return 0

def idor_main(schema,host,headers,cookies,paths):
    for path in paths:
        url = schema+host
        enpoint=path['endpoint']
        method=path['method']
        url_request=url+enpoint
        names_payload = open('resources/names_payload.txt','r')
        names_lines_injection = names_payload.readlines()
        if(method==get):
            str(url_request)
            breaked=False
            for x in range(100):
                integer_random=str(assign_values("integer"))
                r=requests.get(str(url_request).replace("{*}", integer_random),headers=get_headers_global(headers))
                res=r.text
                print(str(url_request).replace("{*}", integer_random))
                if(integer_random in res):
                        print(f"[+] Detected Broken Acces Control found on {url_request}.")
                        create_report_main(schema, host, headers, cookies, path, res, "Broken Access Control Vulnerability")
                        breaked=True
                        break
        elif(method==put):
            for x in range(100):
                integer_random2=str(assign_values("integer"))
                params=[]
                for param in path['body_params']:
                    params.append(param['name'])
                body={}
                print(str(params))
                breaked=False
                for body_value in params:
                    for line in names_lines_injection:
                        body[body_value]=f"{line}"
                print(str(body))
                r=requests.put(str(url_request).replace("{*}", integer_random2),headers=get_headers_global(headers),data=body)
                print(str(url_request).replace("{*}", integer_random2))
                res=r.text
                if(r.status_code==200 or r.status_code==201 or r.status_code==202):
                    print(f"[+] Detected Broken Access Control vulnerability found on {url_request}.")
                    create_report_main(schema, host, headers, cookies, path, res, "Broken Access Control")
                    breaked=True
                    break

                    

