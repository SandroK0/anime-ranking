from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from random import randint
from ranking_algorithm import EloRating
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Animes.sqlite"

CORS(app)

db = SQLAlchemy(app)


class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.Integer, default=1400)
    image = db.Column(db.String)


def generate_two_randint(lowbar, topbar):
    a = randint(lowbar, topbar)
    b = None
    while True:
        b = randint(lowbar, topbar)
        if b != a:
            break

    return a, b


@app.route('/', methods=['GET', 'POST'])
def index():

    return jsonify("This flask backend server for facemash")


@app.route("/images", methods=['GET'])
def get_images():

    status_code = None
    response_data = {}

    if request.method == "GET":
        size = db.session.query(Anime).count()
        id_1, id_2 = generate_two_randint(1, size)

        anime_1 = db.session.query(Anime).filter_by(id=id_1).first()
        anime_2 = db.session.query(Anime).filter_by(id=id_2).first()

        response_data['anime1'] = {
            "id": anime_1.id, "title": anime_1.title, "rating": anime_1.rating, "image": anime_1.image}
        response_data['anime2'] = {
            "id": anime_2.id, "title": anime_2.title, "rating": anime_2.rating, "image": anime_2.image}

        status_code = 200

    return jsonify(response_data), status_code


@app.route("/results", methods=['POST'])
def save_results():
    data = request.json
    status_code = 200
    response_data = {}

    if request.method == "POST":

        print(data)
        winner_anime = data['result']['winner']
        looser_anime = data['result']['looser']

        winner_id = winner_anime['id']
        looser_id = looser_anime['id']
        winner_rating = winner_anime['rating']
        looser_rating = looser_anime['rating']

        new_winner_rating, new_looser_rating = EloRating(
            int(winner_rating), int(looser_rating))

        winner_anime = db.session.query(Anime).filter_by(id=winner_id).first()
        winner_anime.rating = new_winner_rating
        looser_anime = db.session.query(Anime).filter_by(id=looser_id).first()
        looser_anime.rating = new_looser_rating
        db.session.commit()
    return jsonify(response_data), status_code


@app.route("/leaderboard")
def leaderboard():

    status_code = None
    response_data = None

    data = db.session.query(Anime).order_by(Anime.rating.desc()).all()
    if data:

        response_data = []

        i = 1
        for anime in data:
            anime = {'ranking': i, 'id': anime.id, 'title': anime.title,
                     'rating': anime.rating, 'image': anime.image}

            response_data.append(anime)
            i += 1
        status_code = 200

    else:
        response_data = {"message": "Data not found!"}
        status_code = 404

    return jsonify(response_data), status_code


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
