SELECT 
  name,
  id,examYear 
FROM my_exam.exam
WHERE id IN (1,2,3,4,5,17,19,20,44,46,56,57,70,89,228,229,230,231,224,225,192,190,136)
ORDER BY examYear ASC
