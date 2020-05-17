'''
\  ->  \\
\  ->   /
\   -> r 
'''
f = open(r'C:\Users\vkumar15\Desktop\Log\fileex.txt','r')

#print(f)

#print(f.read())
#print(f.readline())

d = f.readlines()
#print(d)

#print row count

print('row count :', len(d))


#word count
wc  = 0
for l in d :#f.readlines():
          col  = l.split(' ')
          wc = wc+ len(col)


print('word count :',wc)

          
     
      

#print(d[6])
f.close()

# wirte /append 

#a = open(r'C:\Users\vkumar15\Desktop\Log\fileex1.txt','a')

#a.write("this is ");
#a.close()


