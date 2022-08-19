SELECT
userId ,
AVG(diff) AS 'averageTime_minute'
FROM (
SELECT 
userId ,
TIMESTAMPDIFF(MINUTE , takenAt, submittedAt) AS diff
FROM my_exam.exam_attempt
HAVING diff >= 0 AND diff <= 185
) AS tmp
GROUP BY userId 
ORDER BY averageTime_minute DESC