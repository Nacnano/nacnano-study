SELECT
countnum AS 'Downloads',
COUNT(DISTINCT userId) AS 'Count'
FROM 
(SELECT 
  userId ,
  COUNT( DISTINCT examId) AS 'countnum'
FROM my_exam.`exam_attempt`
GROUP BY userId) AS tmp
GROUP BY countnum
