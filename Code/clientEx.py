import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name

print(host)

port = 12345                # Reserve a port for your service.


s.connect(('127.0.0.1', port))

print (s.recv(1024))


s.close                     
