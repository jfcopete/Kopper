import requests

get="GET"
post="POST"
put="PUT"
delete="DELETE"

def template_injection_main(schema,host,headers,cookies,paths):
    url = schema+host
    template_injection_payloads = open('resources/template_injection_payloads.txt','r')
    sqli_lines_injection = template_injection_payloads.readlines()
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
            breaked=False
            for body_value in params:
                for line in sqli_lines_injection:
                    body[body_value]=f"{line}"
                    r=requests.post(url_request,data=body)
                    res=r.text
                    print(r.text)
                    if(line not in res):
                        print(f"[-] Possible TemplateInjection found on {url_request}.")
                        breaked=True
                        break
                if(breaked):
                    break
        elif(method==put):
            url_request=url+enpoint
            print(url_request)
            print(path)
            params=[]
            for param in path['body_params']:
                params.append(param['name'])
            body={}
            breaked=False
            for body_value in params:
                for line in sqli_lines_injection:
                    body[body_value]=f"{line}"
                    r=requests.post(url_request,data=body)
                    res=r.text
                    print(r.text)
                    if(line not in res):
                        print(f"[-] Possible TemplateInjection found on {url_request}.")
                        breaked=True
                        break
                if(breaked):
                    break