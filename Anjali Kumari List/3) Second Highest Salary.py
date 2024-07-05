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
SELECT max(Salary) as SecondHighestSalary 
FROM Employee 
WHERE Salary < (SELECT max(Salary) FROM Employee);

=========================
Subquery: (SELECT MAX(Salary) FROM Employee) finds the highest salary in the Employee table.

From our dataset, the highest salary is 300.
Main Query: The main query finds the maximum salary that is less than the highest salary found in the subquery.

It does this by evaluating the WHERE clause: Salary < 300.
This filters the salaries in the Employee table to those less than 300.
Evaluation of the WHERE clause:

Salaries less than 300: 100, 200.
Finding the maximum salary among these filtered salaries:

The maximum of 100 and 200 is 200.
So, the query correctly identifies that the second highest salary is 200 by:

First finding the highest salary (300).
Then finding the maximum salary among those salaries that are less than 300 (100 and 200).
==========================


-- SOLUTION - 3
SELECT max(e2.Salary) as SecondHighestSalary
FROM Employee e1, Employee e2
WHERE e1.Salary > e2.Salary;

=========================
Self-Join: The Cartesian product of the Employee table with itself is created and filtered by e1.Salary > e2.Salary.

Filtering Pairs:

e1: 200 > e2: 100
e1: 300 > e2: 100
e1: 300 > e2: 200
Finding the Maximum Salary among the filtered pairs:

e2.Salaries in the filtered pairs: 100, 100, 200.
The maximum of these salaries is 200.
=======================

'''

# referee_id = NULL : this is not working
# The 'not equal' operator in MySQL is represented by <> or !=.
