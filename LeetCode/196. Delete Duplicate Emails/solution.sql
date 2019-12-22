# Write your MySQL query statement below
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

# DELETE FROM Person WHERE
# Id NOT IN (SELECT MIN(p.Id) FROM (SELECT * FROM Person) p
# Group by p.Email);

# DELETE FROM Person WHERE Id NOT IN 
# (SELECT * FROM(
#     SELECT MIN(Id) FROM Person GROUP BY Email) as p);