from js import sex, age, y1, y2, records

import re
def _y_m(age):
    m = re.match('(\d+)歲(\d+)', age)
    return f'{m.group(1)}y{m.group(2)}m__'

table = {}
table['Age__'] = [f'{_y_m(age)}']
table['OD'] = [f'{y1:.2f}']
table['OS'] = [f'{y2:.2f}']

import json
records = json.loads(records)
for record in records:
    if record[18] or record[24]:
        table['Age__'].insert(0, f'{_y_m(record[11])}')
        table['OD'].insert(0, f'{record[18]:.2f}')
        table['OS'].insert(0, f'{record[24]:.2f}')

import pandas as pd
df = pd.DataFrame(table)
df = df.T
df.columns = df.loc['Age__']
df = df.drop(index='Age__')
display(df, target='table')