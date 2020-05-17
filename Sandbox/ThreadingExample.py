import time
import threading

def print1():
     #while True:
     for i in range(1,5):          
          #print('perfrom your job')
          print(i)
          #time.sleep(3)
          

def print2():
     for j in range(11,15):
          print(j)
          #time.sleep(3)
          
def print3():
     for j in range(101,105):
          print(j)
          #time.sleep(3)


#print1()
#print2()
t1 = threading.Thread(target=print1,name="process1")          
t2 = threading.Thread(target=print2,name="process2")
t3 = threading.Thread(target=print3,name="process3")

#print()
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

#t1.join(t2) #t2 is dependend  on t1







