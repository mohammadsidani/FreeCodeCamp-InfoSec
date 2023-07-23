import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.56.1'
host = socket.gethostname()
port = 444

serversocket.bind(('192.168.56.1', port))
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("Received connection from %s " % str(address))
    
    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()