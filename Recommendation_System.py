# ID 2081
# You are given the list of Facebook friends and the list of Facebook pages that users follow. 
# Your task is to create a new recommendation system for Facebook. For each Facebook user, find pages that this user doesn't follow but at least one of their friends does. 
# Output the user ID and the ID of the page that should be recommended to this user.


import pandas as pd

df=pd.merge(users_friends,users_pages, how='inner',left_on='friend_id',right_on='user_id')
users_pages['key']=users_pages['user_id'].astype(str)+users_pages['page_id'].astype(str)
df['key']=df['user_id_x'].astype(str)+df['page_id'].astype(str)
df[~df['key'].isin(users_pages['key'])][['user_id_x','page_id']]
