SELECT 
dateCombined ,
COUNT(id) AS register
FROM (
	SELECT
	DATE_FORMAT(createdtime, "%Y %m %d") AS dateCombined ,
	id
	FROM monkeyeveryday.Member
	) AS tmp
GROUP BY dateCombined 