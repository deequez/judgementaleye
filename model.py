from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session


engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                        autocommit=False,
                                        autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id =            Column(Integer, primary_key = True)
    age =           Column(String(15))
    gender =        Column(String(15))
    zipcode =       Column(String(15))
    email =         Column(String(64), nullable=True)
    password =      Column(Integer, nullable=True)

    def __repr__(self):
        return "<User('%s', '%s', '%s', '%s')>" % (self.id, self.age, self.gender, self.zipcode)


class Movie(Base):
    __tablename__= "movies"

    id =            Column(Integer, primary_key= True)
    name=           Column(String(64))
    released_on=    Column(Date, nullable=True)
    imdb_url=       Column(String(128))

    def __repr__(self):
        return "<Movie('%s', '%s', '%s', '%s')>" % (self.id, self.name, self.released_on,
                        self.imdb_url)

class Rating(Base):
    __tablename__= "ratings"

    id =            Column(Integer, primary_key= True)
    user_id =       Column(Integer, ForeignKey('users.id'))
    movie_id =      Column(Integer, ForeignKey('movies.id'))
    rating =        Column(Integer, nullable=False)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))

    def __repr__(self):
        return "Rating<('%s', '%s', '%s', '%s')>" % (self.id, self.user_id, self.movie_id,
                        self.rating)

### End class declarations

def create_db():
    Base.metadata.create_all(engine)


def main():
    """In case we need this for something"""
    pass
    # if db hasn't already been created call the following:
    # create_db()
    

if __name__ == "__main__":
    main()
