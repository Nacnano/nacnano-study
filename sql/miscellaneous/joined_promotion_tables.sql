SELECT
*
FROM
(SELECT
monkeyeveryday.PromotionUsage.memberId ,
monkeyeveryday.PromotionUsage.promotionId ,
monkeyeveryday.PromotionUsage.subscriptionTypeId ,
monkeyeveryday.PromotionUsage.promoCode ,
monkeyeveryday.PromotionUsage.createdtime ,
monkeyeveryday.PromotionUsage.updatedtime ,
monkeyeveryday.PromotionUsage.memberSubscriptionId ,
monkeyeveryday.Promotion.title ,
monkeyeveryday.Promotion.promoType ,
monkeyeveryday.Promotion.config ,
monkeyeveryday.Promotion.starttime ,
monkeyeveryday.Promotion.endtime
FROM monkeyeveryday.PromotionUsage
INNER JOIN monkeyeveryday.Promotion ON monkeyeveryday.PromotionUsage.promoCode=monkeyeveryday.Promotion.promoCode 
) AS joined1
WHERE promoType=3 OR promotype=2
