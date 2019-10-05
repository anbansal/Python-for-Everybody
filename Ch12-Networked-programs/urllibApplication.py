import urllib.request


def useUrllib(address):
    fhand = urllib.request.urlopen(address)
    for line in fhand:
        print(line.decode().strip())


if __name__ == '__main__':
    address = 'http://data.pr4e.org/romeo.txt'
    useUrllib(address)
