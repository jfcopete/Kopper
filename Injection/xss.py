import requests
from util.create_report import create_report_main
from util.get_headers import get_headers_global

get="GET"
post="POST"
put="PUT"
delete="DELETE"

def xss_main(schema,host,headers,cookies,paths):
    url = schema+host
    xss_payloads = open('resources/xss_payloads.txt','r')
    xss_lines_injections = xss_payloads.readlines()
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
                for line in xss_lines_injections:
                    body[body_value]=f"{line}"
                    r=requests.post(url_request,data=body)
                    res=r.text
                    print(r.text)
                    if(line in res):
                        print(f"[-] Possible XSS found on {url_request}.")
                        create_report_main(schema, host, headers, cookies, path, res, "XSS vulnerability")
                        breaked=True
                        break
                if(breaked):
                    break
        elif(method==put):
            url_request=url+enpoint
            print(url_request)
            params=[]
            for param in path['body_params']:
                params.append(param['name'])
            body={}
            breaked=False
            for body_value in params:
                for line in xss_lines_injections:
                    body[body_value]=f"{line}"
                r=requests.post(url_request,data=body)
                res=r.text
                if(line in res):
                    print(f"[-] Possible XSS found on {url_request}.")
                    create_report_main(schema, host, headers, cookies, path, res, "XSS vulnerability")
                    breaked=True
                    break
        elif (method==get):
            url_request=url+enpoint
            str(url_request)
            breaked=False
            for line in xss_lines_injections:
                r=requests.get(str(url_request).replace("{*}", f"{line}"),headers=get_headers_global(headers))
                res=r.text
                print(str(url_request).replace("{*}", f"{line}"))
                if(line in res):
                        print(f"[-] Possible XSS found on {url_request}.")
                        create_report_main(schema, host, headers, cookies, path, res, "XSS Vulnerability")
                        breaked=True
                        break
                