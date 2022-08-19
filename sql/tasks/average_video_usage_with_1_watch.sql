SELECT 
memberId ,
time_diff/60/60/24 AS time_diff_day ,
watch_count ,
time_diff/watch_count/60/60/24 AS period
FROM (
SELECT
memberId ,
TIMESTAMPDIFF(SECOND, firstTime, lastTime) AS time_diff,
watch_count 
FROM (
SELECT
memberId ,
MIN(createdtime) AS firstTime,
MAX(createdtime) AS lastTime,
COUNT(id) AS watch_count
FROM
monkeyeveryday.MemberSheetVideo
GROUP BY memberId 
) AS tmp
HAVING time_diff = 0
) AS tmp2
ORDER BY period  ASC