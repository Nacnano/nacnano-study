SELECT 
CASE
	WHEN dataWatch.memberId IS NULL THEN dataExam.memberId 
	ELSE dataWatch.memberId
END AS MemberId,
watch_count ,
taken_count 
FROM
	(
	SELECT
	memberId ,
	COUNT(id) AS watch_count
	FROM
	monkeyeveryday.MemberSheetVideo
	GROUP BY memberId 
	) AS dataExam
LEFT JOIN 
	(
	SELECT 
	everydayUserId AS memberId ,
	COUNT(takenAt) AS taken_count
	FROM
		(
		SELECT
		my_exam.user.everydayUserId,
		my_exam.exam_attempt.examId ,
		takenAt 
		FROM
		my_exam.exam_attempt
		INNER JOIN my_exam.user
		ON my_exam.user.id = my_exam.exam_attempt.userId
		) AS mapped_exam
	GROUP BY everydayUserId 
	) AS dataWatch
ON dataWatch.memberId  = dataExam.memberId 
UNION
SELECT 
CASE
	WHEN dataExam.memberId IS NULL THEN dataWatch.memberId 
	ELSE dataExam.memberId
END AS MemberId,
watch_count ,
taken_count 
FROM
	(
	SELECT
	memberId ,
	COUNT(id) AS watch_count
	FROM
	monkeyeveryday.MemberSheetVideo
	GROUP BY memberId 
	) AS dataExam
RIGHT JOIN 
	(
	SELECT 
	everydayUserId AS memberId ,
	COUNT(takenAt) AS taken_count
	FROM
		(
		SELECT
		my_exam.user.everydayUserId,
		my_exam.exam_attempt.examId ,
		takenAt 
		FROM
		my_exam.exam_attempt
		INNER JOIN my_exam.user
		ON my_exam.user.id = my_exam.exam_attempt.userId
		) AS mapped_exam
	GROUP BY everydayUserId 
	) AS dataWatch
ON dataWatch.memberId  = dataExam.memberId 
ORDER BY MemberId 