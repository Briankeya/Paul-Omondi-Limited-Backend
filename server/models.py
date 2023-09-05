from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships
from sqlalchemy_serializer import SerializerMixin
import datetime

db = SQLAlchemy()

# Users Table
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_names = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    phone_number = db.Column(db.String)
    hashed_password = db.Column(db.String)
    confirm_hashed_password = db.Column(db.String)

# Projects Table
class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    images_url = db.Column(db.String)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))

# Team Members Table
class TeamMember(db.Model, SerializerMixin):
    __tablename__ = 'team_members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Colum6mn(db.String(100), nullable=False)
    bio = db.Column(db.String)
    image_url = db.Column(db.String(200))

# Services Table
class Service(db.Model, SerializerMixin):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    overview = db.Column(db.Text)
    description = db.Column(db.Text)

# Contact Table
class Contact(db.Model, SerializerMixin):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Testimonials Table
class Testimonial(db.Model, SerializerMixin):
    __tablename__ = 'testimonials'
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Blogs Table
class Blogs(db.MOdel, SerializerMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)






