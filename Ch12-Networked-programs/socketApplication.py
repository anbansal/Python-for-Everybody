import socket


def useSocket(server, port):
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySock.connect((server, port))
    cmd = ('GET http://' + server + '/romeo.txt HTTP/1.0\r\n\r\n').encode()
    # cmd = ('GET http://' + server + 'HTTP/1.0\r\n\r\n').encode()
    mySock.send(cmd)

    while True:
        data = mySock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mySock.close()


if __name__ == '__main__':
    server = 'data.pr4e.org'
    # server = 'facebook.com'
    port = 80
    useSocket(server, port)
