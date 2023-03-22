from datetime import datetime

from sqlalchemy import (
    Column, String, Integer, DateTime, Text, ForeignKey
)


from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    lastname = Column(String(50))
    nickname = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)





class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, default=datetime.now)

class Articles(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(70), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey("authors.id"))

    def __repr__(self):
        return f"Article({self.title})"

    def __repr__(self):
        return f"User({self.nickname}"
