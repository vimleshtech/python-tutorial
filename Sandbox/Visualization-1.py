import numpy as np

import matplotlib.pyplot as plt 

x = np.arange(0,10) 
y = x ^ 2
print(x)
print(y)


#Simple Plot
#plt.plot(x,y)
#plt.show()

##label the axis
#Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
#Simple Plot
plt.plot(x,y)
#plt.show()

#save the graph 
#plt.savefig('out.pdf', format='pdf')



#format and color
# Formatting the line colors
plt.plot(x,y,'y')
# Formatting the line type  
plt.plot(x,y,'.')
plt.show()













