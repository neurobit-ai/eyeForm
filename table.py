from js import sex, age, y1, y2, records

import re
def x(age):
    m = re.match('(\d+)歲(\d+)', age)
    return int(m.group(1)) + int(m.group(2)) / 12

table = {}
table['OD'] = [f'{y1:.2f}']
table['OS'] = [f'{y2:.2f}']
table['Age'] = [f'{x(age):.1f}']

import json
records = json.loads(records)
for record in records[::-1]:
    if record[18] or record[24]:
        table['OD'].insert(0, f'{record[18]:.2f}')
        table['OS'].insert(0, f'{record[24]:.2f}')
        table['Age'].insert(0, f'{x(record[11]):.1f}')

import pandas as pd
df = pd.DataFrame(table)
df = df.T
df.columns = len(df.columns) * ['.......']
df