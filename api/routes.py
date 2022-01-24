# flask packages
from flask_restful import Api

# project resources
from api.event import EventsApi, EventApi
from api.patron import PatronsApi, PatronApi
from api.monastery import MonasteriesApi, MonasteryApi
from api.prayer import PrayersApi, PrayerApi

def create_routes(api: Api):
    """Adds resources to the api.

    :param api: Flask-RESTful Api Object

    :Example:

        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")

    """
    '''
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')



    api.add_resource(MealsApi, '/meal/')
    api.add_resource(MealApi, '/meal/<meal_id>')

    '''

    api.add_resource(EventsApi, '/events/')
    api.add_resource(EventApi, '/event/<event_id>')
    api.add_resource(PatronsApi, '/patrons/')
    api.add_resource(PatronApi, '/patron/<event_id>')  ##/draw/   zrobić losowanie patrona
    api.add_resource(MonasteriesApi, '/monasteries/')
    api.add_resource(MonasteryApi, '/monastery/<event_id>')
    api.add_resource(PrayersApi, '/prayers/')
    api.add_resource(PrayerApi, '/prayer/<event_id>')
