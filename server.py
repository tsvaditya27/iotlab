#server
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port=bluetooth.PORT_ANY
server_socket.bind("",port))
server_sock.listen(1)
client socket, address = server_sock.accept()
print "Accepted connection from ", address
while True:
    data = client_sock.recv(1024)
    print "Received: ", data
    client_socket.send(data)
    client_socket.close()
server_socket.close()