# mongo-engine packages
from mongoengine import *

class Audio(Document):
    id_t = StringField()
    url = StringField()
    title = StringField()

class Gospel(Document):
    id_t = StringField()
    name = StringField()


class Text(Document):
    gospel = ListField(Gospel)
    contemplation = StringField()
    question = ListField(StringField())

class Prayers(Document):
    audio = ListField(Audio)
    text = ListField(Text)



    

    