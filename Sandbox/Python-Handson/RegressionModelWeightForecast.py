import numpy as np
from sklearn.linear_model import LinearRegression


height =[140,155,156,134,143,149]
x = np.array(height).reshape((-1, 1))
print(x)

weight =[51,62,72,45,52,56]
y = np.array(weight)
print(y)


model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)



#prediction
newdata =[]
for i in range(1,4):
          h = int(input('enter height : '))
          newdata.append(h)

          
x_new = np.array(newdata).reshape((-1, 1))
y_new = model.predict(x_new)
print(y_new)








