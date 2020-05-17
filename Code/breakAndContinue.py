for i in range(1,10):
     if i % 3 == 0:
          break
     
     print(i)

for i in range(1,10):
     if i % 3 == 0:
          continue 
     
     print(i)

#################

data = []
ch = 'y'
while ch == 'y':
     ch = input('enter 1 for add element, 2 show elemetns , 3 for exist ')

     if ch == '1':
          d = input('enter data ')
          data.append(d)
          ch  = 'y'
          
     elif ch == '2':
          print(data)
          ch = 'y'
          
     elif ch =='3':
          break
     else:
          print('invalid choice...please enter again !!!!')
          ch ='y'
          continue
     
     





          
     
     
     
