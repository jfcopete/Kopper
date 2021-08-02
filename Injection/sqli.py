import requests
from util.create_report import create_report_main

get="GET"
post="POST"
put="PUT"
delete="DELETE"

def sqli_main(schema,host,headers,cookies,paths):
    url = schema+host
    sqli_payloads = open('resources/sqli_payload.txt','r')
    sqli_lines_injection = sqli_payloads.readlines()
    for path in paths:
        enpoint=path['endpoint']
        method=path['method']
        if(method==post):
            url_request=url+enpoint
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
                    if("SQL" in res):
                        print(f"[+] Detected SQLi vulnerability found on {url_request}.")
                        create_report_main(schema, host, headers, cookies, path, res, "SQLi_vulnerabilities")
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
                    if("SQL" in res):
                        print(f"[+] Detected SQLi vulnerability found on {url_request}.")
                        breaked=True
                        break
                if(breaked):
                    break
        elif(method==get):
            url_request=url+enpoint
            print(url_request)
            print(path)
            str(url_request)
            breaked=False
            for line in sqli_lines_injection:
                print(line)
                print(url_request)
                r=requests.get(str(url_request).replace("{*}", f"{line}"))
                print(str(url_request).replace("{*}", f"{line}"))
                res=r.text
                if("SQL" in res):
                    print(f"[+] Detected SQLi vulnerability found on {url_request}.")
                    create_report_main(schema, host, headers, cookies, path, res, "SQLi_vulnerabilities")
                    breaked=True
                    break


                