import pandas as pd
import numpy as np
import json
import datetime
from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
import pymysql


everyday_sql_engine = create_engine('postgresql://')
with everyday_sql_engine.connect() as dbConnection:
    df = pd.read_sql('''
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
        where package_id = ''
        order by ph.created_at asc
    ''', dbConnection)

print(df.head())

df.to_csv("updated_data/updated_from_database.csv")
