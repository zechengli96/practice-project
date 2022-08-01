import json
from textwrap import indent

res = {}

for file in ["problemThree.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
            id = item['id']
            res[id] = {}
            res[id]['id'] = id

for file in ["problemThree.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
            if 'amount_to_pay' in item:
                id = item['id']
                
                amount_to_pay = item['amount_to_pay']
                res[id]['amount_to_pay'] = amount_to_pay
                
                

# {
#       "id": 3,
#       "amount": 12938,
#       "is_in_payment_plan": "yes",
#       "amount_to_pay": 4312.67,
#       "debt_id": 3,
#       "installment_amount": 1230.085,
#       "installment_frequency": "WEEKLY",
#       "start_date": "2020-08-01"
#     },           
for file in ["payments.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
           debt_id = item['debt_id']
           amount = item['amount']
           date = item['date']
           res[debt_id]['debt_id'] = debt_id
           res[debt_id]['date'] = date
           

     
           if 'amount' not in res[debt_id]:
               res[debt_id]['amount'] = 0
               res[debt_id]['amount'] += amount
           else:
               res[debt_id]['amount'] += amount


                
           
           






for key in res:
    item = res[key]
    id = item['id']
    res[id] = {}
    res[id]['id'] = id
    if 'amount' in item:
                amount= item['amount']
                res[id]['amount'] = amount
    if 'amount_to_pay' in item:
                amount_to_pay = item['amount_to_pay']
                res[id]['amount_to_pay'] = amount_to_pay
    if 'amount' in item:
        res[id]['remaining'] = amount_to_pay - amount
    

reslist = []

for k in res:
    reslist.append(res[k])


new_json = json.dumps(reslist, indent = 2)
print(new_json)






