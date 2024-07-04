"""
176. Second Highest Salary
Medium
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.
 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

"""


# Solution 

# Write your MySQL query statement below

'''
-- SOLUTION - 1
SELECT IFNULL((SELECT DISTINCT Salary 
                FROM Employee
                ORDER BY Salary DESC
                LIMIT 1,1), NULL) AS SecondHighestSalary;


-- SOLUTION - 2
select max(Salary) as SecondHighestSalary from Employee 
where Salary < (select max(Salary) from Employee)


-- SOLUTION - 3
select max(e2.Salary) as SecondHighestSalary
from Employee e1, Employee e2
where e1.Salary > e2.Salary
'''

# referee_id = NULL : this is not working
# The 'not equal' operator in MySQL is represented by <> or !=.
