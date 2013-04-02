from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import sessionmaker, relationship, backref


engine = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id =            Column(Integer, primary_key = True)
    age =           Column(String(15))
    gender =        Column(String(15))
    zipcode =       Column(String(15))
    email =         Column(String(64), nullable=True)
    password =      Column(Integer, nullable=True)


class Movie(Base):
    __tablename__= "movies"

    id =            Column(Integer, primary_key= True)
    name=           Column(String(64))
    released_on=    Column(Date)
    imdb_url=       Column(String(128))


class Rating(Base):
    __tablename__= "ratings"

    id =            Column(Integer, primary_key= True)
    movie_id =      Column(Integer, ForeignKey('movies.id'))
    user_id =       Column(Integer, ForeignKey('users.id'))
    rating =        Column(Integer, nullable=False)

    user = relationship("User", backref="ratings")
    movie = relationship("Movie", backref="ratings")

### End class declarations

def create_db():
    Base.metadata.create_all(engine)

def connect():
    global engine
    global session
    engine = create_engine("sqlite:///ratings.db", echo=True)
    session = sessionmaker(bind=engine)

    return session() 


def main():
    """In case we need this for something"""
    connect()
    # if db hasn't already been created call the following:
    # create_db()
    

if __name__ == "__main__":
    main()
