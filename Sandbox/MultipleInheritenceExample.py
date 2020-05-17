class calc:
     def add(s,a,b):
          c =a+b
          print(c)

     def sub(s,a,b):
          c = a -b
          print(c)
     def add(s,a,b,c):
          d =a+b+c
          print(d)



class acalc:
     def fact(s,n):
          o =1
          for i in range(1,n+1):
               o*=i

          print(o)
          

     def area(s,a,b):
          c = a * b *3.14
          print(c)

class common(calc,acalc):
     def test(s):
          print('child class')

##
o = common()
#o.add(11,2) #error 
o.add(11,2,444)
o.sub(33,4)

o.fact(5)
o.test()












          








          
     
