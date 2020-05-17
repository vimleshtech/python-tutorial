class calc:
     def add(s,a,b):
          c =a+b
          print(c)

     def sub(s,a,b):
          c = a -b
          print(c)

class tax(calc):
     def compute(s,sal):
          msal =sal*.40 + sal*.20 + sal
          ysal = msal *12
          if ysal<300000:
               print('non taxable income')
          else:
               print('taxable income')


class convert(tax): # multi level
     def convertToWord(s,n):

          w =['zero','one','two']
          if n<3:
               print(w[n])
          else:
               print('logic is not present')
               

##create object of child class
'''
o = tax()
o.add(111,2)
o.sub(333,44)
o.compute(44555)
'''
#create object of child 2 level
c =convert()
c.add(11,34)
c.compute(4444)
c.convertToWord(1)





             
