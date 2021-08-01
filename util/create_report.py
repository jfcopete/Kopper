import json
import os
import markdown
import time

def create_report_main(schema,host,headers,cookies,path,res,vuln) :  
    print(str(vuln)+" "+str(path))  
    vulnerability = "# Vulnerability "+vuln +" in "+path["endpoint"]+" \n"
    summary = "## Summary "+"\n"
    tech_details = "### Technical Details"+"\n"
    schema_host_path= "#### Enpoint: "+schema+host+path["endpoint"]+"\n"
    json_md="```"+"\n"
    close_json_md="```"+" \n"
    header_x=""
    for x in headers:
        header_x = header_x+" "+x["name"]+" "+x["value"] + " \n"
    headers_md="#### Headers: "+" \n"

    cookie_x=""
    for x in cookies:
        cookie_x = cookie_x+" "+x["name"]+" "+x["value"] + " \n"
    cookies_md="#### Cookies: "+ " \n"
    response = "#### Response: "+" \n"
    impact="### Impact \n"

    md = markdown.Markdown()
    html = md.convert(vulnerability+summary+tech_details+schema_host_path+headers_md+json_md+header_x+close_json_md+cookies_md+json_md+cookie_x+close_json_md+str(response)+str(res).replace("#", "")+impact)

    with open(os.getcwd()+"/reports_found/"+vuln+" "+str(path["endpoint"]).replace("/", "_")+" "+str(time.time()).split(".")[0]+".html","w+", encoding="utf-8") as f:
        f.write(html)

    