SELECT 
newdate,
attemptcount 
FROM (SELECT
newdate,
COUNT(DISTINCT attemptId) as 'attemptcount'
FROM (
SELECT
attemptId ,
DATE_FORMAT(createdAt, "%Y %m %d") AS 'newdate' 
FROM my_exam.exam_attempt_item
) AS tmp
GROUP BY newdate) AS tmp2
ORDER BY newdate ASC;
