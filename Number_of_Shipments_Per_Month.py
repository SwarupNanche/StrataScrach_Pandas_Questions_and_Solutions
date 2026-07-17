# ID 2056

# Write a query that will calculate the number of shipments per month. The unique key for one shipment is a combination of shipment_id and sub_id. 
# Output the year_month in format YYYY-MM and the number of shipments in that month.


import pandas as pd

amazon_shipment['year_month']=amazon_shipment['shipment_date'].dt.strftime('%Y-%m')
amazon_shipment['key']=amazon_shipment['shipment_id']+amazon_shipment['sub_id']
final_df=amazon_shipment.groupby('year_month')['key'].count().reset_index()
final_df=final_df.rename(columns={'key':'count'})
