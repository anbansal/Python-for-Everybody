import urllib.request
import re
import ssl


def useUrllib(address):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    fhand = urllib.request.urlopen(address)
    html = fhand.read()
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    for link in links:
        print(link.decode().strip())


if __name__ == '__main__':
    address = input("Enter: ")
    useUrllib(address)
