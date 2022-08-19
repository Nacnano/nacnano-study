SELECT 
DataTakenDate.dateTaken ,
DataWatchedDate.user_watched_count , 
DataTakenDate.user_taken_count
FROM (SELECT
dateTaken ,
COUNT(DISTINCT everydayUserId) AS user_taken_count 
	FROM
	(
	SELECT
	my_exam.user.everydayUserId ,
	my_exam.exam_attempt.examId ,
	DATE_FORMAT(takenAt, "%Y %m %d") AS dateTaken 
	FROM
	my_exam.exam_attempt
	INNER JOIN my_exam.user
	ON my_exam.user.id = my_exam.exam_attempt.userId
	) AS mapped_exam
GROUP BY dateTaken
) AS DataTakenDate
INNER JOIN 
	(SELECT
	dateWatched ,
	COUNT(DISTINCT memberId) AS user_watched_count
	FROM 
		(SELECT
		memberId ,
		DATE_FORMAT(createdtime , "%Y %m %d") AS dateWatched
		FROM monkeyeveryday.VideoViewLog
		) AS formattedDate
	GROUP BY dateWatched ) AS DataWatchedDate
	ON DataTakenDate.dateTaken = DataWatchedDate.dateWatched 
