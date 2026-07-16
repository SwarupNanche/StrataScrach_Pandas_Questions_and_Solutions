# ID 9688
# Find the inspection date and risk category (pe_description) of facilities named 'STREET CHURROS' that received a score below 95.


import pandas as pd

df=los_angeles_restaurant_health_inspections.copy()
df=df[(df['facility_name']=='STREET CHURROS') & (df['score']<95)]
df[['activity_date','pe_description']].head()
