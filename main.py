import json
data = {}
with open ('./swagger-data/api-docs.json','r') as f:
    data = json.load(f)
print(data)
host=data['host']
print(host)