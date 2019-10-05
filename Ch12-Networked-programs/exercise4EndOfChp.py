import urllib.request
from bs4 import BeautifulSoup
import re
import ssl


def useUrllib(address):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    fhand = urllib.request.urlopen(address,context=ctx)
    html = fhand.read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('p')
    count = 0
    for tag in tags:
        # print('TAG: ',tag)
        # print('URL: ', tag.get('href',None))
        # print('Contents: ',tag.contents[0])
        # print('Attrs: ',tag.attrs)
        count += 1
    print(address,"contains",count,"references to paragraph!!!")


if __name__ == '__main__':
    address = input("Enter: ")
    useUrllib(address)
