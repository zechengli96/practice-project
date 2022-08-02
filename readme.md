
# Python Data Management Tool For TrueAccord

PDMT is a small program written in python to display and adjust the debt paying situation. 

## Installation and Prerequisite

Basic knowledge of command line tool in Windows and Mac. 

Download and Install [python](https://www.python.org/downloads/) to install.

## Usage

```python

# open up a command line and find a suitable place
git clone https://github.com/zechengli96/practice-project.git 

# cd into the project
(base) lizecheng@Lis-MacBook-Pro Desktop % cd practice-project

# problem 1

python problemOne.py

# problem 3

python problemThree.py

# problem 4

python problemFour.py

# problem 2

cd problemTwo 

python test_problemOne.py

python test_problemThree.py

python test_problemFour.py

```

## Result Explanation
1) Above is the step of running the program. 
If I have more time, I would make it more readable, or make a front end website to display the process so the readme will be redundant. 

2) Detailed time usage:
- *1* hours to read and structure the json data initially, and then during the coding, I spent about another *1* hour to think the ability to scale and testing method. 
- *1.5* hours to code on problem 1,3,4. 
- *1* hour to review the method I use, and what can I do better.
- *1* hour to write the readme documentation. 

Total time, *5.5* hours in a week.

3)  A description of your process and approach, including what you think you would have done differently given more time.
- First, I use python to get the JSON file from URL provided, to save further time, I copied and pasted the file into json files in the folder. If I have more time or resource, I will make a website to display the json content and give user the right to click and play with it. And I reviewed all of the data from those URLs. Think these three json file as a database from TrueAccord's debt management system, we have debts, payment plans and payments. Which payment plans is like a middle point that connecting debts and payments. payment plans and debts using id as a foreign key and id for debts is primary key, debt_id is the foreign key to connect payment plans and payments ( which we assume one payment plan only have one debt_id),debt_id is also the primary key for payment plans and payments. And this as a whole could be actually a lot easier if is a database with these three tables, we can join all these together and create some new fields, and do some further operation with it. But because of the limitation on the format has to be easy to access by all the pals, I guess json is the best way to test candidates' ability.

- For the question 1, use the command I provide to show the result. Where if inside the payment_plans.json, if there is a id that is in both payment_plans.json and debts.json, then we will have a field called "is_in_payment_plan" and it is YES, otherwise it will be NO. 

- For the question 2, I did not finish it perfectly. Here are the reasons:
1）I think this question 2 should be question 4 or question 1, we either need to think about testing when we finish all or parallel 2) My first thought is use the random JSON generator to generate some random JSON, and then use those to replace the original file. But I find if I have to write to make sure the payments amount is close to debt amount, there are some extra functions I need to write, and I feel like there should be a good library to use, but I am lacking those knowledges. 3) If I'd have more time, I will put all of the data into a SQL db server, and then the whole process will be a lot easier, it will basic be a select statement with some joins. 4) Maybe use machine learning library to fake some testing data. 5) Testing data is not well prepared so it make the remaining amount to a negative amount.

- For the question 3, use the command I provide to show the result. remaining will be the amount to pay minus sum of all of payments that is in the same debt_id. This part is a little bit tricky, but still a basic Leetcode question and data structure skill.

- For the question 4, use the command I provide to show the result. next payment date will only show if there is a payment plan and the remaining is bigger than 0. And on the latest payment date, plus 7 if payment freq is weekly, 14 if bi-weekly.

Final thoughts:
Overall this is a very good practice for back end engineer, it covers data structure basic, dict, language basic syntax, and programming mindset, testing method experience. 

If I have more time, I would build this into a web application, with the front end of 3 json file displaying, letting user to edit the json file themselves, problem 1, 3, 4 with button to click.

For the problem 2, I strongly suggest using real world data, because if I'd write some function to fake the payments' sum equal to a debt, end of the day all of the data will show the same pattern, and those are not good data, unless your random is really close to nature random. For instance, you need to pay 1000 dollars, then you write a payment which is around 500 dollars and you want to pay them back in 2 times, you could write something like a+b = 1000, a is 500+-10, b is 500+-10. And all of the data will look alike. 

And if I have more time, I will use database to store these data and just write the result out in a SQL query, and fetch the data into the front end.





## License
[MIT](https://choosealicense.com/licenses/mit/)
