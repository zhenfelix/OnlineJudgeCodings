# Write your MySQL query statement below

# select Request_at Day, 1-round(sum(if(Status="completed",1,0))/count(*),2) "Cancellation Rate"
# from Trips
# where Request_at >= "2013-10-01" and Request_at <= "2013-10-03"
# and Client_Id in (select Users_Id from Users where Banned= "No") and Driver_Id in (select Users_Id from Users where Banned= "No")
# group by Request_at

SELECT Request_at as Day,
       ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips
WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
      AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
GROUP BY Request_at;