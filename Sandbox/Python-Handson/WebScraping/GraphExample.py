
import pandas as p
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cols = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = p.read_csv(url, names=cols)

print(df.shape)
#df.plot()
#df.plot(kind='line',subplots=True, layout=(2,2))
df.plot(kind='line',subplots=True)
plt.show()







