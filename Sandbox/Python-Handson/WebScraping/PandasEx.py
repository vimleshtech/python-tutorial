import pandas as pd

#list 
eid =[1,2,3,4,5]
name =['ayush','jatin','ayush','monika','ayush']


#conert list to dataframe/table
data={'empcode':eid,'name':name}

df= pd.DataFrame(data)
print(df)#print all data 

#
print(df.columns) #print column list
print(df['name']) #print one column
print(df[['name','empcode']]) #print one column


#sorting
print(df.sort_values('name',ascending=True))
print(df.sort_values('name',ascending=False))


#show top given rows
print(df.head(2))


#show buttom given rows
print(df.tail(3))

#rename the columns
df.columns = ['eid','employee name']
print(df)


#distribuation / group by
print(df.groupby('employee name').size()) #count


#write data to excel or csv file
#df.to_csv('myemp_data1.csv',index=False) #comma seperate version
#print('data is save to file')


#convert dataframe to list
data = df.values
print(type(data))

print(data[0:2,])  #read first 2 rows and all columns



print(data[:,1]) #all rows and one column










