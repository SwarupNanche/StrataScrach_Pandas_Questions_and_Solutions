# ID 9915

# Find the customers with the highest daily total order cost between 2019-02-01 and 2019-05-01. 
# If a customer had more than one order on a certain day, sum the order costs on a daily basis. 
# Output each customer's first name, total cost of their items, and the date. 
# If multiple customers tie for the highest daily total on the same date, return all of them.


import pandas as pd

orders=orders[orders['order_date'].between('2019-02-01','2019-05-01',inclusive='both')]
df=pd.merge(orders,customers,how='inner',left_on='cust_id',right_on='id').reset_index()
df['daily_total_order_cost']=df.groupby(['cust_id','order_date'])['total_order_cost'].transform('sum')
df=df.sort_values(by=['order_date','daily_total_order_cost','first_name'],ascending=[True,False,True])
df=df[['order_date','daily_total_order_cost','first_name']]
df['max_daily_total_order_cost']=df.groupby('order_date')['daily_total_order_cost'].transform('max')
max_daily_cost=df[df['daily_total_order_cost']==df['max_daily_total_order_cost']][['order_date','max_daily_total_order_cost','first_name']]
