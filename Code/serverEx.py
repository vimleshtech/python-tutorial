import socket
#gethostname() , bind(), listen() , accept(), send(), close()

s = socket.socket()         # Create a socket object

host = socket.gethostname() # Get local machine name
print(host)

port = 12345                # Reserve a port for your service.
s.bind(('127.0.0.1', port))        # Bind to the port



s.listen(1)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   
   c.send('Thank you for connecting')
   c.close()                # Close the connection

print('end ')



