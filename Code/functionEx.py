'''
input()
print()
max()
min()
sum()
sort()
append()
remove()
int()
str()
float()

split()
list()

replace()
subString()


a.upper()
a.lower()


'''
a = [444,323,2121,1,2233]
m = max(a)
print(m)

print(min(a))
print(sum(a))

a.sort()
print(a)

## remove
a = [3,4,432,2]
print(a)
a.remove(4)
print(a)

d = a[2]
a.remove(d)
print(a)


####
name = input('enter name ')
col = name.split(' ')
print('first name :',col[0])


l =len(name)

print(l)
for i in range(0,l):
     print(name[i])
     


a = list(name)
print(a)


a.upper()
a.lower()



##replace
name = name.replace('a','dbc')
print(name)

##substring/slicer # ravinder
n = name[2:4]
print(n)

### wap to get count of word from sentence
col = name.split(' ')
print(len(col))

### wapt to get count of particular word from sentence
##count of is?

### wap to convert sentence to proper case
#### this is python program = This Is Python Program














