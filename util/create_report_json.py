import json
import os

def create_report_json_main(schema,host,headers,cookies,path,res,vuln) :
    report_json={"schema":schema,"host":host,"headers":headers,"cookies":cookies,"path":path,"response_body":res,"vulnerability":vuln}
    with open(os.getcwd()+"/reports_found/"+vuln+".json","w+") as f:
        json.dump(report_json, f)
    