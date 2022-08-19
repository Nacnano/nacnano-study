import numpy as np
import pandas as pd
import json
import datetime
from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
import pymysql

package_id = ''
everyday_username = ""
everyday_password = ""

everyday_sql_engine = create_engine('postgresql://')

with everyday_sql_engine.connect() as dbConnection:
    df_payment_history = pd.read_sql(f'''
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
            where package_id = '{package_id}'
            ''', dbConnection)

print(df_payment_history.head())

# SOLVE BY USING UNICODE + %
