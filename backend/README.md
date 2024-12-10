# Anime Ranking Backend

This is a Flask backend server for the Anime Ranking website. The server provides endpoints to retrieve random pairs of anime images, save user preferences, and display a leaderboard based on anime ratings.

## Prerequisites

Before running the server, make sure you have the following installed:

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask CORS

You can install the dependencies via pip:

```bash
pip install flask flask_sqlalchemy flask_cors

Setup

    Clone this repository:

bash

git clone https://github.com/SandroK0/anime-ranking.git

    Navigate to the project directory:

bash

cd anime-ranking-backend


Usage

    Start the Flask server:

bash

python app.py

    Access the API endpoints:

    Random anime pair: /images (GET)
    Save user preferences: /results (POST)
    Leaderboard: /leaderboard (GET)

API Endpoints
Random Anime Pair

Returns two random anime images for user comparison.

    URL: /images
    Method: GET
    Response: JSON object containing two anime images.

Save User Preferences

Saves the user's preferred anime choice.

    URL: /results
    Method: POST
    Request Body: JSON object containing the winner and loser anime.

    json

    {
      "result": {
        "winner": {"id": 1, "rating": 1500},
        "looser": {"id": 2, "rating": 1400}
      }
    }

    Response: JSON object confirming successful save.

Leaderboard

Displays the leaderboard based on anime ratings.

    URL: /leaderboard
    Method: GET
    Response: JSON array containing anime rankings.
```
