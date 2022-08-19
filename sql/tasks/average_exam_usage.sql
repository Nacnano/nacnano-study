SELECT 
userId ,
time_diff/60/60/24 AS time_diff_day ,
taken_count ,
time_diff/taken_count/60/60/24 AS period
FROM (
SELECT
userId ,
TIMESTAMPDIFF(SECOND, firstTime, lastTime) AS time_diff,
taken_count 
FROM (
SELECT
userId ,
MIN(takenAt) AS firstTime,
MAX(takenAt) AS lastTime,
COUNT(id) AS taken_count
FROM
my_exam.exam_attempt
GROUP BY userId 
) AS tmp
HAVING time_diff > 0
) AS tmp2
ORDER BY period ASC