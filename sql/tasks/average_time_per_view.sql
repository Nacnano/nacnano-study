SELECT
memberid ,
AVG(timeUsed) AS 'averageTime_minute'
FROM (
SELECT 
msv.memberid ,
msv.duration/60 AS 'timeUsed'
FROM monkeyeveryday.MemberSheetVideo msv
) AS tmp
GROUP BY memberid  
ORDER BY averageTime_minute DESC