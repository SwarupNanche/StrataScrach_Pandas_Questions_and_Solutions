# ID 9653
# Count the number of user events performed by MacBookPro users.
# Output the result along with the event name.
# Sort the result based on the event count in the descending order.


import pandas as pd

playbook_events=playbook_events[playbook_events['device']=='macbook pro']
playbook_events.groupby('event_name').size().reset_index().sort_values(by='event_name',ascending=True)
