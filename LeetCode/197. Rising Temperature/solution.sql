# Write your MySQL query statement below
# select Id
# from Weather a
# left join
# (
#     select DATE_ADD(RecordDate,INTERVAL 1 DAY) as RecordDate, Temperature
#     from Weather
# ) b
# on a.RecordDate = b.RecordDate
# where b.Temperature is not null and a.Temperature > b.Temperature


# SELECT
#     weather.id AS 'Id'
# FROM
#     weather
#         JOIN
#     weather w ON DATEDIFF(weather.RecordDate, w.RecordDate) = 1
#         AND weather.Temperature > w.Temperature
# ;


SELECT wt1.Id 
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND 
      TO_DAYS(wt1.RecordDate)-TO_DAYS(wt2.RecordDate)=1;