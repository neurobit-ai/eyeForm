from js import sex, x, y1, y2

import pickle
with open('data_to_plot.pkl', 'rb') as f:
    data_to_plot = pickle.load(f)

import matplotlib.pyplot as plt
def plot(sex):
    morf = data_to_plot.loc[sex].loc[3:16]
    MorF = {'男': 'Male', '女': 'Female'}[sex]
    plt.xticks(range(3, 17))
    plt.yticks(range(20, 30))
    plt.fill_between(morf.index, morf['<lambda_4>'], morf['<lambda_3>'], color='red', alpha=0.6, label='90~100%')
    plt.fill_between(morf.index, morf['<lambda_3>'], morf['<lambda_2>'], color='orange', alpha=0.6, label='75~90%')
    plt.fill_between(morf.index, morf['<lambda_2>'], morf['<lambda_1>'], color='yellow', alpha=0.6, label='50~75%')
    plt.fill_between(morf.index, morf['<lambda_1>'], morf['<lambda_0>'], color='lightgreen', alpha=0.6, label='0~50%')
    plt.legend(loc='lower right')
    plt.title(f'Axial Length Growth in {MorF} Taiwanese Children', fontsize=14)
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Axial Length', fontsize=14)

plot(sex)
if y1:
    plt.scatter(x, y1, color='red')
if y2:
    plt.scatter(x, y2, color='blue')
plt