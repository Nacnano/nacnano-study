select 
u.phone ,
ph.package_id ,
u.first_name ,
u.last_name ,
u.id ,
ph.created_at ,
ph.channel 
from everyday.public.payment_history ph 
inner join
everyday.public."user" u 
on u.id = ph.user_id 

