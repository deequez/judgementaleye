import model
import csv

"""
1. open a file
2. read a line
3. parse a line
4. create an object
5. add the object to a session
6. commit
7. repeat until done 
"""


def load_users(session):
    with open('seed_data/u.user', 'rb') as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            id, age, gender, occupation, zipcode = row
            id = int(id)
            age = int(age)
            user_object = model.User(id=id, age=age, zipcode=zipcode)
            session.add(user_object)
            session.commit()


def load_movies(session):
    with open('seed_data/u.item', 'rb') as f:
        reader = csv.reader(f, delimiter = "|")
        for row in reader:
            id, name, released_on, imdb_url = int(row[0]), row[1], row[2], row[3]
            movie_obect = model.Movie(id=id, name=name, released_on=released_on, 
                            imdb_url=imdb_url)
            session.add(movie_obect)
            session.commit()


def load_ratings(session):
    with open('seed_data/u.data', 'rb') as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            user_id, movie_id, rating = int(row[0]), int(row[1]), int(row[2])
            rating_object = model.Rating(user_id=user_id, movie_id=movie_id, rating=rating)
            session.add(rating_object)
            session.commit()


def main(session):
    # load_users(session)
    load_movies(session)
    load_ratings(session)


if __name__ == "__main__":
    s = model.connect()
    main(s)
