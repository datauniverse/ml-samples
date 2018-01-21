# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:25:24 2017

@author: abhil
"""

import pandas as pd

data = {
    'id': [1,2,3,4,5,6,7,8],
    'name': ['Keith','Josh','Robin','Raja','Tridip','Arijit','Amit','Dev'],
    'manager_id': [0,1,1,2,0,5,5,6]
}
df = pd.DataFrame.from_dict(data)
"""
ID    Name     MgrID
 1    Keith    0
 2    Josh     1
 3    Robin    1
 4    Raja     2
 5    Tridip   0
 6    Arijit   5
 7    Amit     5
 8    Dev      6
"""

target_id = [8]

def recurse(data_frame, identities):
    if len(identities) == 0:
        return pd.DataFrame.empty
    elif len(identities) == 1:
        return data_frame[data_frame['id'] == identities[0]]
    return recurse(data_frame, data_frame[data_frame['id'].isin(identities)]['manager_id'])

df_res = recurse(df, target_id)

"""
df_result = df[df['id'] == target_id]

result_ids = df_result['manager_id'].values

for ids in result_ids:
    df_subresult = df[df['id'] == ids]
    df_result = df_result.append(df_subresult)
"""
print(df_res)