import json
import datetime

from textwrap import indent


# set the result as a dict
res = {}

for file in ["problemFour.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
            id = item['id']
            res[id] = {}
            res[id]['id'] = id
            if 'remaining' in item:
                remaining= item['remaining']
                res[id]['remaining'] = remaining


for file in ["payments.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
           debt_id = item['debt_id']
           date = item['date']
           res[debt_id]['debt_id'] = debt_id
           res[debt_id]['date'] = date

for file in ["payment_plans.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
           debt_id = item['debt_id']
           installment_frequency = item['installment_frequency']
           res[debt_id]['debt_id'] = debt_id
           res[debt_id]['installment_frequency'] = installment_frequency


    # if 'amount' in item:
    #             amount= item['amount']
    #             res[id]['amount'] = amount
    # if 'amount_to_pay' in item:
    #             amount_to_pay = item['amount_to_pay']
    #             res[id]['amount_to_pay'] = amount_to_pay
    # if 'amount' in item:
    #     res[id]['remaining'] = amount_to_pay - amount

#   {
#     "id": 2,
#     "remaining": 607.6700000000001,
#     "debt_id": 2,
#     "date": "2020-08-08",
#     "installment_frequency": "BI_WEEKLY"

for key in res:
    item = res[key]
    id = item['id']
    res[id] = {}
    res[id]['id'] = id
    if 'remaining' in item:
        remaining = item['remaining']
        res[id]['remaining'] = remaining
    if 'date' in item:
        latestpaymentdate = item['date']
        res[id]['latestpaymentdate'] = latestpaymentdate
    if 'installment_frequency' in item:
        installment_frequency = item['installment_frequency']
        res[id]['installment_frequency'] = installment_frequency
    
    if 'remaining' in item:
        if installment_frequency == 'BI_WEEKLY':
            # date1 = str(datetime.datetime(date))
            day1 = json.dumps(latestpaymentdate, default=str)
            day1 = day1[1:]
            day1 = day1[:-1]
            
            res[id]['next_payment_due_date'] = datetime.datetime.strptime(day1, "%Y-%m-%d") + datetime.timedelta(days=14)

        elif installment_frequency == 'WEEKLY':
            # date1 = str(datetime.datetime(date))
            day1 = json.dumps(latestpaymentdate, default=str)
            day1 = day1[1:]
            day1 = day1[:-1]
            
            res[id]['next_payment_due_date'] = datetime.datetime.strptime(day1, "%Y-%m-%d") + datetime.timedelta(days=7)
    






# plus_one_hour = datetime.datetime.strptime(date, "%Y-%M-%D") + datetime.timedelta(days=7)
# print(plus_one_hour.strftime("%H:%M:%S"))


reslist = []

for k in res:
    reslist.append(res[k])



    
new_json = json.dumps(reslist, indent = 2, default=str)
print(new_json)
