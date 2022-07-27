import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False )
    password = Column(Integer, nullable=False)

class Follower(Base):
    __tablename__ = 'followers'
    followed_user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    following_user_id = Column(Integer, ForeignKey('users.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    created_by_user = Column(Integer, ForeignKey('users.id'))
    caption = Column(String(150))
    likes = Column(Integer)
    created_time = Column(String(20), nullable=False)

class PostMedia(Base):
    __tablename__ = 'post_media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    media_file = Column(String(100)) # should be VARBINARY


class LikedPost(Base):
    __tablename__ = 'liked_posts'
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comment = Column(String(150))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_time = Column(String(20), nullable=False)
    comment_reply_to = Column(String(150), ForeignKey('comments.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e