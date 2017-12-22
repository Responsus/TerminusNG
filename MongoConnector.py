
from flask_mongoengine import MongoEngine
import pymongo
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user

class MongoConnector(object):
    def __init__(self):
        self.client = pymongo.MongoClient("127.0.0.1")
        self.db = self.client["terminus"]

    def get_connection(self):
        return self.db

db = MongoEngine()

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    name = db.StringField()
    skills = db.StringField()
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    phone = db.StringField()
    is_manager = db.BooleanField(default=True)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])
    clients = db.ListField()

class Projects(db.Document, UserMixin):
    manager_id = db.ObjectIdField()
    name = db.StringField()
    manager = db.StringField()
    client = db.StringField()
    objective = db.StringField()
    as_is = db.StringField()
    to_be = db.StringField()
    start_date = db.StringField()
    end_date = db.StringField()
    status = db.IntField()
    budget = db.FloatField()


user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security()
