"""
Problem: Identify High-Average Payment Funds

You are given two tables: funds and coupon_payments.

funds table:

id (integer): The unique identifier for each fund.
name (string): The name of the fund.
coupon_payments table:

fund_id (integer): The identifier that references the id from the funds table.
payment (decimal): The payment amount made to the fund.
Write a SQL query to find all funds where the average payment is greater than 500. The output should include the following columns:

name: The name of the fund.
total_payments: The total number of payments made to the fund.
min_payment: The minimum payment made to the fund.
max_payment: The maximum payment made to the fund.
avg_payment: The average payment made to the fund.
Order the results by name in ascending order.

Example Output:

name	          |total_payments	min_payment	  max_payment	avg_payment
ABC Growth Fund	  |    7	          111.54	    948.93	      548.96
XYZ Balanced Fund |	   8	          106.52	    770.69	      559.94

"""


# Solution 

# Write your MySQL query statement below

'''
SELECT 
    f.name, 
    COUNT(c.payment) AS total_payments, 
    MIN(c.payment) AS min_payment, 
    MAX(c.payment) AS max_payment, 
    AVG(c.payment) AS avg_payment
FROM 
    funds f 
LEFT JOIN 
    coupon_payments c ON f.id = c.fund_id
GROUP BY 
    f.name, f.id
HAVING 
    avg_payment > 500;

'''
