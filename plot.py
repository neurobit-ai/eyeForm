from js import sex, age, y1, y2, records, suggestion, localStorage, report

import pandas as pd

import pickle
with open('data_to_plot.pkl', 'rb') as f:
    db_version, slope_groupby, stacked_area = pickle.load(f)[report]

import matplotlib.pyplot as plt
def plot(sex, report):
    area = stacked_area.loc[sex].loc[3:16]
    MorF = {'男': 'Male', '女': 'Female'}[sex]
    if report == '軸長':
        plt.fill_between(area.index, area['P100'], area['P90'], color='red', alpha=0.6, label='90~100%')
        plt.fill_between(area.index, area['P90'], area['P75'], color='orange', alpha=0.6, label='75~90%')
        plt.fill_between(area.index, area['P75'], area['P50'], color='yellow', alpha=0.6, label='50~75%')
        plt.fill_between(area.index, area['P50'], area['P0'], color='lightgreen', alpha=0.6, label='0~50%')
    if report == '球面度數':
        plt.fill_between(area.index, area['P50'], area['P100'], color='lightgreen', alpha=0.6, label='50~100%')
        plt.fill_between(area.index, area['P25'], area['P50'], color='yellow', alpha=0.6, label='25~50%')
        plt.fill_between(area.index, area['P10'], area['P25'], color='orange', alpha=0.6, label='10~25%')
        plt.fill_between(area.index, area['P0'], area['P10'], color='red', alpha=0.6, label='0~10%')
    plt.title(f"Trend of {MorF} Children in Taiwan", fontsize=12)

risk = [...] * 4
risk[0] = f'{report}在年齡正常範圍內，屬無/少風險，建議一年定期檢查，無潛在近視發展狀況。'
risk[1] = f'{report}稍長於年齡正常範圍，屬低風險，建議一年定期檢查，需改變生活型態及減少外在環境影響。'
risk[2] = f'{report}長於年齡正常範圍，屬中風險，建議半年回診檢查，需改變生活型態及減少外在環境影響（例：電腦及手機使用時間需要注意並適度休息、戶外活動需要配戴太陽眼鏡防藍光、UV），並搭配葉黃素或魚油服用。'
risk[3] = f'{report}甚長於年齡正常範圍，屬高風險，有極高近視惡化發展可能，建議3個月回診檢查，需改變生活型態及減少外在環境影響（例：電腦及手機使用時間需要注意並適度休息、避免坐姿不正，戶外活動需要配戴太陽眼鏡防藍光、UV），搭配葉黃素或魚油服用，並搭配積極治療控制。'
Risk = {}

import re
def x(age):
    m = re.match('(\d+)歲(\d+)', age)
    return int(m.group(1)) + int(m.group(2)) / 12

if round(x(age)) in range(3, 17):
    if report == '軸長':
        p0, p50, p75, p90, p100 = stacked_area.loc[sex].loc[round(x(age))]
        for y, eye in (y1, '右眼'), (y2, '左眼'):
            if y < p50:
                display(f'{eye}{risk[0]}', target='advice')
                localStorage.setItem(eye, 0)
            elif y < p75:
                display(f'{eye}{risk[1]}', target='advice')
                localStorage.setItem(eye, 1)
            elif y < p90:
                display(f'{eye}{risk[2]}', target='advice')
                localStorage.setItem(eye, 2)
            else:
                display(f'{eye}{risk[3]}', target='advice')
                localStorage.setItem(eye, 3)
    if report == '球面度數':
        p100, p50, p25, p10, p0 = stacked_area.loc[sex].loc[round(x(age))]
        for y, eye in (y1, '右眼'), (y2, '左眼'):
            if y > p50:
                display(f'{eye}{risk[0]}', target='advice')
                localStorage.setItem(eye, 0)
            elif y > p25:
                display(f'{eye}{risk[1]}', target='advice')
                localStorage.setItem(eye, 1)
            elif y > p10:
                display(f'{eye}{risk[2]}', target='advice')
                localStorage.setItem(eye, 2)
            else:
                display(f'{eye}{risk[3]}', target='advice')
                localStorage.setItem(eye, 3)
else:
    display('該年齡收案不足，無法提供具有統計意義之危險度分級。', target='advice')
    localStorage.setItem('右眼', '')
    localStorage.setItem('左眼', '')

plot(sex, report)
if y1:
    plt.scatter(x(age), y1, color='red', label='OD')
if y2:
    plt.scatter(x(age), y2, color='blue', label='OS')
if y1 and slope_groupby[sex].get(suggestion):
    plt.scatter(x(age) + 1, y1 + slope_groupby[sex][suggestion], color='red', label='OD in 1 yr', marker='*')
if y2 and slope_groupby[sex].get(suggestion):
    plt.scatter(x(age) + 1, y2 + slope_groupby[sex][suggestion], color='blue', label='OS in 1 yr', marker='*')

import json
records = json.loads(records)
od, os = (18, 24) if report == '軸長' else (15, 21)
for record in records:
    if record[od]:
        plt.scatter(x(record[11]), record[od], color='red', marker='.')
    if record[os]:
        plt.scatter(x(record[11]), record[os], color='blue', marker='.')

plt.legend(loc='lower right')
plt.xticks(range(3, 17 if x(age) + 1 <= 16 else int(x(age)) + 2))
plt.yticks(range(20, 30) if report == '軸長' else range(-8, 7))
plt.xlabel('Age', fontsize=12)
plt.ylabel('Axial Length' if report == '軸長' else 'SPH', fontsize=12)
plt.margins(0)
if report == '軸長':
    plt.text(x(age) + 1, 18.8 if sex=='女' else 19.2, f'{db_version}', horizontalalignment='right', fontsize=8)
if report == '球面度數':
    plt.text(x(age) + 1, -8.5 if sex=='女' else -10.5, f'{db_version}', horizontalalignment='right', fontsize=8)
display(plt, target='plot')