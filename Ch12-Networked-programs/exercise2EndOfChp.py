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

    count = 0
    while True:
        data = mySock.recv(100)
        if len(data) < 1:
            break
        count += len(data)
        if count < 3000:
            print(data.decode(), end='')
    print("\nCopied data: ",count)
    mySock.close()


if __name__ == '__main__':
    address = input("Enter: ")
    port = 80
    useSocket(address, port)
