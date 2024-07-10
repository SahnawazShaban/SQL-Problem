"""
178. Rank Scores
Medium
Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 
Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

The result format is in the following example.

Example 1:
Input: 
Scores table:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
Output: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
"""

# Solution 

# Write your MySQL query statement below

'''
SELECT s1.score, 
        (SELECT COUNT(DISTINCT s2.score) 
        FROM Scores s2
        WHERE s1.score <= s2.score) AS 'rank'
FROM Scores s1
ORDER BY s1.score DESC;

-----------------------------

SELECT s.Score, count(distinct t.score) Rank
FROM Scores s JOIN Scores t ON s.Score <= t.score
GROUP BY s.Id
ORDER BY s.Score desc

------------------------------

select score,dense_rank() over (order by score desc) as 'rank' from Scores;


-------------------------------


SELECT s1.score, 
       (SELECT COUNT(*) 
        FROM Scores s2 
        WHERE s2.score = s1.score AND s2.id <= s1.id) AS 'rank'
FROM Scores s1
ORDER BY s1.score DESC, s1.id;

OUTPUT:
| score | rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 2    |
| 3.85  | 1    |
| 3.65  | 1    |
| 3.65  | 2    |
| 3.65  | 3    |
| 3.5   | 1    |

'''

# The 'not equal' operator in MySQL is represented by <> or !=.


