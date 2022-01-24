# mongo-engine packages
from mongoengine import *

class Monasteries(Document):
    id_e = StringField() #IntField(required=True)
    name = StringField(max_length=240)
    province = StringField() #URLField() 
    monastery_kind = StringField()
    description = StringField() #DateTimeField()
    monastery_call = StringField() #DateTimeField()
    address = StringField()
    lat = StringField()
    lng = StringField()
    events = ListField(StringField())
    pictures = ListField(StringField())

    

    