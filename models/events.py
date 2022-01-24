# mongo-engine packages
from mongoengine import *

class Event_Type(Document):
    id_t = StringField()
    name = StringField()
    color_code = StringField()

class Location(Document):
    name = StringField()
    address = StringField()
    lat = StringField()
    lng = StringField()

class Events(Document):
    id_e = StringField() #IntField(required=True)
    title = StringField(max_length=240)
    link = StringField() #URLField() 
    description = StringField()
    start_date = StringField() #DateTimeField()
    end_date = StringField() #DateTimeField()
    event_type = ListField(Event_Type)
    location = ListField(Location)

    

    