SELECT
dateCombined ,
COUNT(DISTINCT memberId) AS video_exam_count
FROM 
	(
	SELECT
	DATE_FORMAT(takenAt, "%Y %m %d") AS dateCombined ,
	my_exam.user.everydayUserId AS memberId
        FROM
	my_exam.exam_attempt
	INNER JOIN my_exam.user
	ON my_exam.user.id = my_exam.exam_attempt.userId
	UNION
	SELECT
	DATE_FORMAT(createdTime, "%Y %m %d") AS dateCombined ,
	memberId
	FROM
	monkeyeveryday.VideoViewLog
	) AS DataCombined
GROUP BY dateCombined 