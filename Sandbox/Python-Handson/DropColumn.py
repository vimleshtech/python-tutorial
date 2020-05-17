import pandas as pd

data  = pd.DataFrame(data={'eid':[1,2,3,4],'name':['Raman','jatin','divya','Kshitiz']})
print(data)

data = data.drop('name',axis=1)
print(data)




