#constructor and deconstructor example
class employee:

     def __init__(self):
          print(self,'  object is created ')
          self.eid =0
          self.ename =''
          self.gender=''
          self.basic =0

     def newemp(self):
          self.eid =int(input('enter eid :'))
          self.ename =input('enter name :')
          self.gender=input('enter gender :')
          self.basic =int(input('enter basic sal '))

     def compute(self):
          self.hra = self.basic*.40
          self.da = self.basic*.20
          self.msal = self.basic+ self.hra + self.da
          self.ysal = self.msal*12
          if self.ysal <=300000:
               self.tax = 0
          elif self.ysal <=500000:
               self.tax = (self.ysal-300000)*.05
          elif self.ysal <=1000000:
               self.tax = 10000+(self.ysal-500000)*.20
          else:
               self.tax = 110000+(self.ysal-1000000)*.30


     def show(self):
               print('eid :',self.eid)
               print('name :',self.ename)
               print('m sal:',self.msal)
               print('y sal:',self.ysal)
               print('tax:',self.tax)

     def __del__(s):
          print(s, ' object is dealloacted')



o = employee()
o.newemp()
o.compute()
o.show()
del o
