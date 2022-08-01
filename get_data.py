# use below script to read the data from server. 
import urllib.request, json 
with urllib.request.urlopen("https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/debts") as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4, sort_keys=True))

import urllib.request, json 
with urllib.request.urlopen("https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payment_plans") as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4, sort_keys=True))

import urllib.request, json 
with urllib.request.urlopen("https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payments") as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4, sort_keys=True))

