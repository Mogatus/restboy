# functions used in RestBoy
import requests

def sendRequest(req):
    print("sending request: " + req.method)
    contents = requests.get(req.url)
    data = contents.text
    print(contents)
    print(data)
    return contents
