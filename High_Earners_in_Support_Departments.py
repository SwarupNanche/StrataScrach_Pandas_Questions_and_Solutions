 # ID 2167

# The HR team is reviewing compensation packages for employees in support functions. 
# They want to identify high earners in the HR and Admin departments for a salary benchmarking study.
# Find all employees who earn more than $80,000 and work in either the HR or Admin department. Return first name, last name, department, and salary.


import pandas as pd

df=techcorp_workforce[(techcorp_workforce['salary']>80000) & (techcorp_workforce['department'].isin(['HR','Admin']))]
df[['first_name', 'last_name', 'department','salary']]
