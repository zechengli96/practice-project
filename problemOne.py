import json
from textwrap import indent


# set the result as a dict
res = {}

# read the content inside the debts.json file
for file in ["debts.json"]:
    with open(file) as f:
        # load the content into data, load meaning it is not string, if is string use loads
        data = json.load(f)
        # travesal the data, the data right now is a list of dict.
        for item in data:
        # inside each dict we set up a variable for the res dict, it is based on item_id.
            item_id = item['id']
            amount = item['amount']
            res[item_id] = {}
            res[item_id]['id'] = item_id
            res[item_id]['amount'] = amount
            res[item_id]['is_in_payment_plan'] = "no"


for file in ["payment_plans.json"]:
    with open(file) as f:
        data = json.load(f)
        for item in data:
            # print(item)
            # inside this file, create ids
            item_id = item['id']
            amount_to_pay = item['amount_to_pay']
            debt_id = item['debt_id']
            installment_amount = item['installment_amount']
            installment_frequency = item['installment_frequency']
            start_date = item['start_date']
            res[item_id]['amount_to_pay'] = amount_to_pay
            res[item_id]['debt_id'] = debt_id
            res[item_id]['installment_amount'] = installment_amount
            res[item_id]['installment_frequency'] = installment_frequency
            res[item_id]['start_date'] = start_date
            res[item_id]['is_in_payment_plan'] = "yes"

            if amount_to_pay == 0:
                res[item_id]['is_in_payment_plan'] = "no"

            

reslist = []

for k in res:
    reslist.append(res[k])



    
new_json = json.dumps(reslist, indent = 2)
print(new_json)
