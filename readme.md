1.
1) Use Python to get the result from 3 URLs. To save some time, I downloaded them into json file and stored in the same folder. 
2) In debts and payment_plans, there are ids that are matched. So we can merge debts and payment_plans together.
3) In the result of 2), we will add another column, we will call it "is_in_payment_plan", if the debt_id is not None, then we will give that boolean as "Yes", otherwise give it "No".

I also see "or the payment plan is completed", at this point, I think if the amount to pay is 0, then it should be No. The data set is not perfect enough, but I have to take this into consideration. 

2. 
Tend to get this resolved after other problems resolved.

3. 
Remaining amount will be the amount to payment minus the sum of payment that are having same debt_id.
The reason the amount not equal to amount to pay is because signing up for payment plan allow them to pay a reduced amount.

4. 
The next payment due date will be calculated based on the latest payment date + frequency, as long as remaining balance is bigger than 0

If no "is_in_payment_plan", or no remaining balance, then null.

Outside the schedule also count, and does not change anything.