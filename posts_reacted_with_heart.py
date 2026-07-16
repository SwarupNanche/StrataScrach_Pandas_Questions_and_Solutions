# ID 10087
# Find all posts which were reacted to with a heart


import pandas as pd

combined_df=pd.merge(facebook_posts,facebook_reactions, on='post_id', how='inner')
combined_df=combined_df[combined_df['reaction']=='heart']
combined_df=combined_df[['post_id','poster_x','post_text','post_keywords','post_date']]
