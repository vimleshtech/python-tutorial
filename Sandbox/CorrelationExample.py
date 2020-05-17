import pandas as pd

path = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None,
            names = ['mpg', 'cylinders', 'displacement','horsepower',
            'weight', 'acceleration', 'model_year', 'origin', 'name'],
            na_values='?')

#print(mpg_data.corr())

out = mpg_data['mpg'].corr(mpg_data['weight'])

print(out)
print(type(out))

#out.to_csv('corr1.csv')

o = mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='spearman')
print(o)







