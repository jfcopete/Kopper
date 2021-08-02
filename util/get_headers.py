def get_headers_global(headers):
    aux={}
    for x in headers:
        aux = {x["name"]:x["value"]}
    return aux
    