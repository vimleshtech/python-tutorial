#dependence or association is any statistical relationship, whether causal or not, between two random variables or bivariate data. Correlation is any of a broad class of statistical relationships involving dependence.
# how close two variables are to having a linear relationship with each other.
#[‘arrow’, ‘under’, ‘interior’, ‘theta’, ‘amb’, ‘slice’, ‘delta’, ‘pi’, ‘height’, ‘nu’, ‘night’, ‘dataset’, ‘length’, ‘twi’, ‘x’, ‘wind’, ‘y’, ‘rho’, ‘alpha’]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://www.dropbox.com/s/4jgheggd1dak5pw/data_visualization.csv?raw=1', index_col=0)
corr = data.corr()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)

fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)


ax.set_xticks(ticks)
plt.xticks(rotation=90)

ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)

plt.show()
