SELECT 
DATE_FORMAT(ADDDATE('2020-11-12', INTERVAL id DAY), "%Y %m %d") AS Date
FROM monkeyeveryday.MyPromotion
LIMIT 1000