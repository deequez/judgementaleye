from flask import Flask, render_template, redirect, request, url_for, flash, session, g
from model import session as db_session, User, Rating


app = Flask(__name__)
app.secret_key = 'goldFishesAreDelicious'

@app.before_request
def get_user_id():
    g.user_id = session.get("user_id") 

@app.teardown_request
def remove_session(exception=None):
    db_session.remove()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signin", methods=["POST"])
def signin():
    email =         request.form["email"]
    password =      request.form["password"]
    
    try:
        user = db_session.query(User).filter_by(email=email, password=password).one()
    except:
        flash("That is an invalid login.", "error")
        return redirect(url_for("index"))

    session["user_id"] = user.id
    return redirect(url_for("signed_in_landing"))

@app.route("/register", methods=["POST"])
def register():
    email =         request.form["email"]
    password =      request.form["password"]
    age =           request.form["age"]
    gender =        request.form["gender"]
    zipcode =       request.form["zipcode"]
    
    user_exists = db_session.query(User).filter_by(email=email).first()

    if user_exists:
        flash("Email already in use.", "error")
        return redirect(url_for("index"))

    user_object = User(age=age, gender=gender, zipcode=zipcode, 
                        email=email, password=password)
    db_session.add(user_object)
    db_session.commit()
    db_session.refresh(user_object)
    session["user_id"] = user_object.id
    return redirect(url_for("signed_in_landing"))

@app.route("/users")
def signed_in_landing():
    users = db_session.query(User).all()
    return render_template("users.html", users=users)

@app.route("/user/<int:id>/movies")
def view_movies(id):
    ratings = db_session.query(Rating).filter_by(user_id=id).all()
    return render_template("movies.html", ratings=ratings, id=id)

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)