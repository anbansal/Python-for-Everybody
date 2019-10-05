import json


def useJSON(jsonInput):
    lst = json.loads(jsonInput)
    print("Users count: ", len(lst))
    for user in lst:
        try:
            print("Name: ", user["name"])
            print("ID: ", user["id"])
            print("Attribute: ", user["x"])
        except:
            print("Your XML data does not have one or more property that you are accessing")
            quit(0)


def generateJSON():
    jsonInput = '''
    [
        {
        "name":"Chuck",
        "id":"001",
        "x":"2"
        } ,
        {
        "name":"Brent",
        "id":"009",
        "x":"7"
        }
    ]
    '''

    return jsonInput


if __name__ == '__main__':
    jsonInput = generateJSON()
    useJSON(jsonInput)
