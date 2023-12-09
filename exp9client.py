import socket
def mpm():
    #establish connection with host
    host = '127.0.0.1'
    port = 6000
    #create socket object
    s = socket.socket()
    #connect host to port
    s.connect((host, port))
    
    print("Connection Established!")
    while True:
        try:
            print()
            x = input("Enter New Message: ")
            #encode and send message to server
            y = x.encode('ascii')
            s.send(y)
            print()
            #revieve response from server,decode ascii
            data = s.recv(1024)
            d = data.decode('ascii')
            print('Server:', d)
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            s.send("Connection from Client terminated!".encode('ascii'))
            break


mpm()
