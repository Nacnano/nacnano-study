SELECT
AllDate.Datetmp AS Date ,
COALESCE(DataWatchedDate.user_watched_count ,0) AS user_watched_count ,
COALESCE(DataTakenDate.user_taken_count ,0) AS user_taken_count ,
COALESCE(Counted_dataCombined.video_exam_count  ,0) AS user_taken_watched_count,
COALESCE(DataRegister.register ,0) AS register_count
FROM 
(
SELECT
ADDDATE('2021-02-28', INTERVAL id DAY) AS Datetmp
FROM monkeyeveryday.MyPromotion
HAVING Datetmp <= NOW()
) AS AllDate
LEFT JOIN 
	(
	SELECT
	dateTaken ,
	COUNT(DISTINCT everydayUserId) AS user_taken_count 
		FROM
		(
		SELECT
		my_exam.user.everydayUserId ,
		my_exam.exam_attempt.examId ,
		DATE_FORMAT(takenAt, "%Y-%m-%d") AS dateTaken 
		FROM
		my_exam.exam_attempt
		INNER JOIN my_exam.user
		ON my_exam.user.id = my_exam.exam_attempt.userId
		) AS mapped_exam
	GROUP BY dateTaken
	) AS DataTakenDate
ON DataTakenDate.dateTaken = AllDate.Datetmp
LEFT JOIN
	(
	SELECT
	dateWatched ,
	COUNT(DISTINCT memberId) AS user_watched_count
	FROM 
		(
		SELECT
		memberId ,
		DATE_FORMAT(createdtime , "%Y-%m-%d") AS dateWatched
		FROM monkeyeveryday.VideoViewLog
		) AS formattedDate
	GROUP BY dateWatched 
	) AS DataWatchedDate
ON DataWatchedDate.dateWatched = AllDate.Datetmp 
LEFT JOIN 
	(
	SELECT
	dateCombined ,
	COUNT(DISTINCT memberId) AS video_exam_count
	FROM 
		(
		SELECT
		DATE_FORMAT(takenAt, "%Y-%m-%d") AS dateCombined ,
		my_exam.user.everydayUserId AS memberId
		FROM
			my_exam.exam_attempt
			INNER JOIN my_exam.user
			ON my_exam.user.id = my_exam.exam_attempt.userId
			UNION
			SELECT
			DATE_FORMAT(createdTime, "%Y-%m-%d") AS dateCombined ,
			memberId
			FROM
			monkeyeveryday.VideoViewLog
		) AS DataCombined
		GROUP BY dateCombined
	) AS Counted_dataCombined
ON Counted_dataCombined.dateCombined = AllDate.Datetmp 
LEFT JOIN 
	(
	SELECT 
	dateCombined ,
	COUNT(id) AS register
	FROM 
		(
		SELECT
		DATE_FORMAT(createdtime, "%Y-%m-%d") AS dateCombined ,
		id
		FROM monkeyeveryday.Member
		) AS tmp
	GROUP BY dateCombined 
	) AS DataRegister
ON DataRegister.dateCombined = AllDate.Datetmp