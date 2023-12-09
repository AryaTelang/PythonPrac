import socket


def mpm():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket()
    s.bind((host, port))
    #sets socket to listen mode, 1 connection
    s.listen(1)
    print("Waiting for connection...")
    #accept connection from client, c is socket for communication
    c, addr = s.accept()
    print("Connection Established!")
    print("Client Address:", addr)
    while True:
        try:    
            print()
            data = c.recv(1024)
            d = data.decode('ascii')
            print("Client:", d)
            print()
            #server response
            x = input("Enter New Message: ")
            y = x.encode('ascii')
            c.send(y)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            break
mpm()