import socket
#gethostname() , bind(), listen() , accept(), send(), close()

s = socket.socket()         # Create a socket object

host = socket.gethostname() # Get local machine name

port = 1234               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port


s.listen(50)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   
   c.send('Thank you for connecting'.encode())
   c.close()                # Close the connection

print('end ')



