# mongo-engine packages
from mongoengine import *

class Patrons(Document):
    name = StringField(max_length=240)
    quotes = ListField(StringField())

    

    