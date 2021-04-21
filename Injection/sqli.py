import requests

get="GET"
post="POST"
put="PUT"
delete="DELETE"

def sqli_main(schema,host,headers,cookies,paths):
    url = schema+host
    for path in paths:
        enpoint=path['endpoint']
        method=path['method']
        if(method==post):
            url_request=url+enpoint
            print(url_request)
            print(path)
            params=[]
            for param in path['body_params']:
                params.append(param['name'])
            body={}
            for body_value in params:
                body[body_value]="'"
            r=requests.post(url_request,data=body)
            res=r.text
            if("SQL" in res):
                print(f"[+] Detected SQLi vulnerability found on {url_request}.")
