import pandas as pd
from sklearn.linear_model import  LinearRegression

#GUI
from tkinter import *

window = Tk()

Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
                }


data= pd.DataFrame(Stock_Market)
print(data)

x = data[['Interest_Rate','Unemployment_Rate']]
y = data['Stock_Index_Price']


print(x)
print(y)

#train 
obj = LinearRegression()
obj.fit(x,y)
print(obj)
print(obj.intercept_)
print('Coefficients: \n', obj.coef_)




irl = Label(text='Enter IR')
irl.pack()

irt =  Entry()
irt.pack()

url = Label(text='Enter UR')
url.pack()

urt =  Entry()
urt.pack()

msg = Label()
msg.pack()

def predict():
     #######predict
     #ir  =float(input('enter interst rate '))
     #ur = float(input('etner unemployement rate '))

     ir  =float(irt.get())
     ur = float(urt.get())
     
     o = obj.predict([[ir,ur]])
     #print(o)
     msg.configure(text= str(o[0]))
     


     
btn = Button(text='Predict',command=predict)
btn.pack()


window.mainloop()

