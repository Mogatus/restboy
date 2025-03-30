# Class for handling requests

class Request:

    def __init__(self, name, method, url, body):
        self.name = name
        self.method = method
        self.url = url
        self.body = body

        