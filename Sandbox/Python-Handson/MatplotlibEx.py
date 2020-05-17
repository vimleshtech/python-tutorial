import pandas 
import matplotlib.pyplot as plt



data  = pandas.DataFrame(data={'eid':[1,2,3,4],
                               'name':['Raman','jatin','divya','Kshitiz']
                               ,'sal':[10,20,30,40]
                               ,'age':[22,26,19,29]})



#example 1
#data.plot()
#plt.show()



#example 2
#data.plot(kind='line')
#data.plot(kind='box')
#data.plot(kind='bar')

#data.plot(kind='bar',subplots=True) #show seperate graph for every numeric col
#data.plot(kind='bar',subplots=True,layout=(1,3))
#data.plot(kind='bar',subplots=True,layout=(1,3))

data.hist()
plt.show()


