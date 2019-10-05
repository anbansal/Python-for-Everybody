import socket


def useSocket(host, port):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host, port))
    cmd = ('GET http://' + host + '/cover3.jpg HTTP/1.0\r\n\r\n').encode()
    mysocket.sendall(cmd)
    count = 0
    picture = b""

    while True:
        data = mysocket.recv(5120)
        if len(data) < 1:
            break
        count += len(data)
        print(len(data), count)
        picture += data
    mysocket.close()
    pos = picture.find(b"\r\n\r\n")
    print("Header Count:", pos)
    print(picture[:pos].decode())

    picture = picture[pos + 4:]
    fhand = open("picture.jpg", "wb")
    fhand.write(picture)
    fhand.close()


if __name__ == '__main__':
    host = 'data.pr4e.org'
    port = 80
    useSocket(host, port)
