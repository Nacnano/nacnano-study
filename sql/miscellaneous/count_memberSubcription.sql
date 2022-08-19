SELECT
memberId ,
COUNT(schedultId) AS cnt
FROM
monkeyeveryday.MemberSubscription
GROUP BY memberId 
ORDER BY cnt DESC