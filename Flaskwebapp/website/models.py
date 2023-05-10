# defining database tables or schema

from . import db # importing current package (website folder) ie: db object
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):  # schema for the particular user data field.
    id =db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

#note for the lowercase of 'user.id' in line 11 instead of Capital 'User.id' because in python it is a convention to write the classname in Capitals but the sql understands the 'user.id' as 'User.id' where 'User' is a classname (This phenomenon is only valid for foreign key)

# in case for relationship we have to use the Original classname with the Uppecase Character as written in the database schema(here the 'Note')  eg: line 22

class User(db.Model,UserMixin):  # schema of the user sign-up info
    id =db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes_1=db.relationship('Note')
