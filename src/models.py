import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Biker(Base):
    __tablename__ = "biker"
    id = Column(Integer, primary_key = True)
    bikername = Column(String, unique = True)
    firstname = Column(String)
    lastname = Column(String) 
    email = Column(String,unique=True)

class Helper(Base):
    __tablename__ = "helper"
    id = Column(Integer, primary_key = True)
    biker_id = Column(Integer, ForeignKey("biker.id"))
    biker = relationship(Biker)
    taller_id = Column(Integer, ForeignKey("taller.id"))
    taller = relationship(Taller)


class Taller(Base):
    __tablename__ = "taller"
    id = Column(Integer, primary_key = True)
    tallername = Column(String, unique = True)
    name = Column(String)
    email = Column(String,unique=True)

class Blog(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    biker_id = Column(Integer, ForeignKey("biker.id"))
    biker = relationship(Biker)
    taller_id = Column(Integer, ForeignKey("taller.id"))
    taller = relationship(Taller)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey("biker.id"))
    user = relationship(User)
    blog_id = Column(Integer, ForeignKey("blog.id"))
    blog = relationship(Blog)
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e