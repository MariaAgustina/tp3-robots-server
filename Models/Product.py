import json
from json import JSONEncoder

class Product(object):

    def __init__(self):
        self.thumbnail = ""
        self.title = ""
        self.permalink = ""
        self.price = 0
        self.id = ""
        self.imageData = ""

    def print(self):
        print("Product: " + self.thumbnail + " " + self.title + " " + self.permalink + " " + str(self.price) + " " + self.id)


    def encode(self):
        #TODO: encode image if needed
        return {
            "thumbnail": self.thumbnail,
            "title": self.title,
            "permalink": self.permalink,
            "price": self.price,
            "id": self.id
        }