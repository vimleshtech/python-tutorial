import mysql.connector as c

#establish the connection between python and my sql server database 
con = c.connect(host="localhost",user="root",password="root",database="mylearning2")
#execute sql command
cur = con.cursor()
     
def show():
     cur.execute("select * from users;")
     out = cur.fetchall()

     for r in out:
          print(r)

def save():
     eid = input('enter id :')
     name = input('enter name :')
     
     #cur.execute("insert into users(id,name) values(100,'ayush')")
     cur.execute("insert into users(id,name) values("+eid+",'"+name+"')")
     con.commit() #to push/save data to database(insert,delete,update)
     print('Record is saved in DB')


save()
show()




