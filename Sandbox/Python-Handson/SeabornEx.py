import pandas
import matplotlib.pyplot as plt
import seaborn as sns


df = pandas.read_csv(r'C:\Users\vkumar15\Desktop\Desktop - Raman\Python-Batch-20thMay\data\restaurants_list.csv')
print(df)

#df.plot(kind='box')
#plt.show()
print(df.columns)

#Category_Item
#Rating
#Rating_Score


#df.boxplot(by ='Category_Item', column =['Rating_Score'], grid = False)

sns.set_style("whitegrid")   
#sns.boxplot(x = 'Rating', y = 'Rating_Score', data = df) 

#sns.lineplot(x = 'Rating', y = 'Rating_Score', data = df)

sns.countplot(x = 'Rating', data = df)
plt.show()




