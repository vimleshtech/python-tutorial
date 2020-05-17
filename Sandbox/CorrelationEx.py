'''
Python | Pandas dataframe.corr()
Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric python packages. Pandas is one of those packages and makes importing and analyzing data much easier.

Pandas dataframe.corr() is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.

method : 
pearson : standard correlation coefficient
kendall : Kendall Tau correlation coefficient
spearman : Spearman rank correlation
min_periods : Minimum number of observations required per pair of columns to have a valid result. Currently only available for pearson and spearman correlation

Returns: count :y : DataFrame


'''

# importing pandas as pd 
import pandas as pd 
  
# Making data frame from the csv file 
df = pd.read_csv("data.csv") 
  
# Printing the first 10 rows of the data frame for visualization 
df[:10]

df.corr(method ='pearson')





df.corr(method ='kendall')


'''
The output dataframe can be interpreted as for any cell, row variable correlation with the column variable is the value of the cell. As mentioned earlier, that the correlation of a variable with itself is 1. For that reason all the diagonal values are 1.00.

# fake kendall
k = pd.DataFrame()
k['X'] = np.arange(5)+1
k['Y'] = [7, 5,1, 6, 9]
print k.corr(method='kendall')




import pandas as pd
path = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None,
            names = ['mpg', 'cylinders', 'displacement','horsepower',
            'weight', 'acceleration', 'model_year', 'origin', 'name'],
            na_values='?')





            mpg_data.info()




            mpg_data['mpg'].corr(mpg_data['weight'])


# pairwise correlation
mpg_data.drop(['model_year', 'origin'], axis=1).corr(method='spearman')


odel_year', 'origin'], axis=1).corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)



# plot correlated values
plt.rcParams['figure.figsize'] = [16, 6]

fig, ax = plt.subplots(nrows=1, ncols=3)

ax=ax.flatten()

cols = ['weight', 'horsepower', 'acceleration']
colors=['#415952', '#f35134', '#243AB5', '#243AB5']
j=0

for i in ax:
    if j==0:
        i.set_ylabel('MPG')
    i.scatter(mpg_data[cols[j]], mpg_data['mpg'],  alpha=0.5, color=colors[j])
    i.set_xlabel(cols[j])
    i.set_title('Pearson: %s'%mpg_data.corr().loc[cols[j]]['mpg'].round(2)+' Spearman: %s'%mpg_data.corr(method='spearman').loc[cols[j]]['mpg'].round(2))
    j+=1

plt.show()


            
'''


















