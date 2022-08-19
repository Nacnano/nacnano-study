SELECT 
id AS memberId ,
mobile,
ExamPeriodData.exam_period ,
VideoPeriodData.video_period ,
VideoProgressData.avg_progress ,
ExamPeriodData.taken_count ,
ExamPeriodData.time_diff_day AS exam_timediff,
VideoPeriodData.watch_count ,
VideoPeriodData.time_diff_day AS watch_timediff ,
VideoProgressData.video_watched AS number_of_video_watched
FROM monkeyeveryday.Member
LEFT JOIN 
	(
	SELECT 
	memberId  ,
	time_diff/60/60/24 AS time_diff_day ,
	taken_count ,
	time_diff/taken_count/60/60/24 AS exam_period
	FROM 
		(
		SELECT
		memberId  ,
		TIMESTAMPDIFF(SECOND, firstTime, lastTime) AS time_diff,
		taken_count 
		FROM 
			(
			SELECT
			my_exam.user.everydayUserId AS memberId ,
			MIN(takenAt) AS firstTime,
			MAX(takenAt) AS lastTime,
			COUNT(my_exam.exam_attempt.id) AS taken_count
			FROM
			my_exam.exam_attempt
			INNER JOIN 
			my_exam.user
			ON my_exam.user.id = my_exam.exam_attempt.userId 
			GROUP BY userId 
			) AS tmp
			HAVING time_diff >= 0
		) AS tmp2
	) AS ExamPeriodData
ON monkeyeveryday.Member.id = ExamPeriodData.memberId 
LEFT JOIN
	(
	SELECT 
	memberId ,
	time_diff/60/60/24 AS time_diff_day ,
	watch_count ,
	time_diff/watch_count/60/60/24 AS video_period
	FROM 
		(
		SELECT
		memberId ,
		TIMESTAMPDIFF(SECOND, firstTime, lastTime) AS time_diff,
		watch_count 
		FROM 
			(
			SELECT
			memberId ,
			MIN(createdtime) AS firstTime,
			MAX(createdtime) AS lastTime,
			COUNT(id) AS watch_count
			FROM
			monkeyeveryday.VideoViewLog
			GROUP BY memberId 
			) AS tmp
			HAVING time_diff >= 0
		) AS tmp2
	) AS VideoPeriodData
ON monkeyeveryday.Member.id = VideoPeriodData.memberId
LEFT JOIN
	(
	SELECT 
	memberId ,
	AVG(progress) AS avg_progress ,
	COUNT(id) AS video_watched
	FROM MemberSheetVideo
	GROUP BY memberId 
	) VideoProgressData
ON monkeyeveryday.Member.id = VideoProgressData.memberId 
ORDER BY memberId 