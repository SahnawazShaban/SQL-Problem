"""
177. Nth Highest Salary
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
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Example 2:
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+

"""


# Solution 

# Write your MySQL query statement below

'''
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

SET N=N-1;

  RETURN (
      SELECT DISTINCT salary FROM Employee ORDER BY salary DESC 
      LIMIT 1 OFFSET N      
  );
END


----------------------------=============---------------------

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET N-1;

'''

# referee_id = NULL : this is not working
# The 'not equal' operator in MySQL is represented by <> or !=.
