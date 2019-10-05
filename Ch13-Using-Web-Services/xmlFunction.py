import xml.etree.ElementTree as ET


def useXml(xmlInput):
    xmlStuff = ET.fromstring(xmlInput)
    lst = xmlStuff.findall('users/user')
    print("Users count: ", len(lst))

    for user in lst:
        try:
            print("Name: ", user.find('name').text)
            print("ID: ", user.find('id').text)
            print("Attribute: ", user.get('x'))
        except:
            print("Your XML data does not have one or more property that you are accessing")
            quit(0)


def generateXML():
    xmlInput = '''
        <stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Brent</name>
                </user>
            </users>
        </stuff>
        '''
    return xmlInput


if __name__ == '__main__':
    xmlInput = generateXML()
    useXml(xmlInput)
