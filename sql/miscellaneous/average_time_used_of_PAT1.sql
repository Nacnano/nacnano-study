SELECT 
  examId ,
  AVG(diffmin) AS `avgdiff`
FROM 
(SELECT
  examId ,
  takenAt ,
  submittedAt ,
  TIMESTAMPDIFF(MINUTE , takenAt , submittedAt) AS `diffmin`
FROM my_exam.exam_attempt
HAVING
diffmin >= 30 AND 
diffmin <= 190 AND examid in (1,2,3,4,5,17,19,20,44,46,56,57,70,89,228,229,230,231,224,225,192,190,136)
) AS tmp
GROUP BY examId
