# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# large = 22; med = 16; small = 12
# params = {'axes.titlesize': large,
#           'legend.fontsize': med,
#           'figure.figsize': (16, 10),
#           'axes.labelsize': med,
#           'axes.titlesize': med,
#           'xtick.labelsize': med,
#           'ytick.labelsize': med,
#           'figure.titlesize': large}
# plt.rcParams.update(params)
# plt.style.use('seaborn-whitegrid')
# sns.set_style("white")
# # %matplotlib inline
#
# # Version
# print(mpl.__version__)  # >> 3.0.2
# print(sns.__version__)  # >> 0.9.0




# Import Dataset
df = pd.read_csv("相关系数矩阵.txt")

# Plot
ax = plt.figure(figsize=(12,10), dpi= 80)
labels = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
sns.heatmap(df.corr(), xticklabels=labels, yticklabels=labels, cmap='RdYlGn', center=0, annot=True)
plt.tick_params(bottom=False, left=False, labeltop=True, labelbottom=False)

# plt.yticks([0., 1000000., 2000000., 3000000., 4000000., 5000000.,6000000., 7000000., 8000000.],
#            ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
# Decorations
plt.title('Relevance graph', weight='bold', fontsize=16)

plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.show()












