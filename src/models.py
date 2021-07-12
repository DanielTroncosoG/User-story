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
    author_id = Column(Integer, ForeignKey("biker.id"))
    biker = relationship(Biker)    

class Blog(Base):
    __tablename__ = "Blog"
    id = Column(Integer, primary_key = True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey("biker.id"))
    biker = relationship(Biker)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    biker_id = Column(Integer, ForeignKey("biker.id"))
    biker = relationship(Biker)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey("biker.id"))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e