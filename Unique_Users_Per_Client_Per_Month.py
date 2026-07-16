# -- ID 2024
# -- Write a query that returns the number of unique users per client for each month. 
# -- Assume all events occur within the same year, so only month needs to be be in the output as a number from 1 to 12

import pandas as pd

fact_events['month_num']=fact_events['time_id'].dt.month
final_df=fact_events.groupby(['client_id','month_num'])['user_id'].nunique()
final_df.head()
