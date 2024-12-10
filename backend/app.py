from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from ranking_algorithm import EloRating
from flask_cors import CORS
from sqlalchemy import func
from math import ceil

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Animes.sqlite"

CORS(app)

db = SQLAlchemy(app)


class Anime(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.Integer, default=1400)
    desc = db.Column(db.String)
    eps = db.Column(db.String)
    years = db.Column(db.String)
    image = db.Column(db.String)


@app.route('/', methods=['GET', 'POST'])
def index():

    return jsonify("This flask backend server for Anime Ranking")


@app.route("/get_match", methods=['GET'])
def get_match():
    try:
        random_animes = Anime.query.order_by(func.random()).limit(2).all()

        if not random_animes:
            return jsonify({"message": "No animes found"}), 404

        anime_list = [{
            "id": anime.id,
            "title": anime.title,
            "rating": anime.rating,
            "desc": anime.desc,
            "eps": anime.eps,
            "years": anime.years,
            "image": request.host_url + anime.image
        } for anime in random_animes]

        return jsonify(anime_list), 200
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@app.route("/save_result", methods=['POST'])
def save_result():
    try:
        data = request.get_json()
        result = data.get("result")

        winner_id = result.get('winner_id')
        loser_id = result.get('loser_id')
        winner = Anime.query.get(winner_id)
        loser = Anime.query.get(loser_id)

        if not winner or not loser:
            return jsonify({"message": "One or both anime not found"}), 404

        Ra = winner.rating
        Rb = loser.rating

        new_Ra, new_Rb = EloRating(Ra, Rb)

        winner.rating = new_Ra
        loser.rating = new_Rb

        db.session.commit()

        return jsonify({
            "message": "Ratings updated successfully",
            "winner_new_rating": new_Ra,
            "loser_new_rating": new_Rb
        }), 200

    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@app.route('/leaderboard', methods=['GET'])
def leaderboard():

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    offset = (page - 1) * per_page

    total_animes = Anime.query.count()
    animes = Anime.query.order_by(Anime.rating.desc()).offset(
        offset).limit(per_page).all()

    leaderboard_data = [
        {
            'id': anime.id,
            'image': request.host_url + anime.image,
            'ranking': index + 1 + offset,
            'rating': anime.rating,
            'title': anime.title
        }
        for index, anime in enumerate(animes)
    ]

    total_pages = ceil(total_animes / per_page)

    return jsonify({
        'totalCount': total_animes,
        'page': page,
        'pageSize': per_page,
        'totalPages': total_pages,
        'items': leaderboard_data
    })


with app.app_context():
    db.create_all()


def create_app():
    return app


if __name__ == "__main__":
    app.run(debug=True)
