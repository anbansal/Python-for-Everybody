import socket


def useSocket(address, port):
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server = (address.split('/'))[2]
        mySock.connect((server, port))
    except:
        print("Could not connect to the address", server)
        exit()
    cmd = ('GET ' + address + ' HTTP/1.0\r\n\r\n').encode()
    mySock.send(cmd)

    while True:
        data = mySock.recv(100)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mySock.close()


if __name__ == '__main__':
    address = input("Enter: ")
    port = 80
    useSocket(address, port)
