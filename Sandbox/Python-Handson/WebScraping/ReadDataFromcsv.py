#read data from csv or excel file

import pandas as p
import matplotlib.pyplot as plt

data= p.read_csv(r'C:\Users\vkumar15\Desktop\restaurants_list.csv')
print(data)


print(data.shape) #show row and col count


#get count of negative and postive value

print(data.groupby('Rating').size())
print(data.groupby('Rating').sum()['Rating_Score'])
print(data.groupby('Rating').max()['Rating_Score'])
print(data.groupby('Rating').min()['Rating_Score'])


data.plot(kind='line')
plt.show()


'''
id name
2  a
1  a 

sum() group by name
a = 3


'''


