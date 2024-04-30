Image Ranking Backend Documentation
Introduction

This backend provides functionality for ranking images using the Elo Rating algorithm. It allows users to compare two images and select the preferred one, updating their ratings accordingly.
Technologies Used

    Flask: A micro web framework for Python.
    Flask-SQLAlchemy: Integrates SQLAlchemy with Flask for database management.
    Flask-CORS: Enables Cross-Origin Resource Sharing (CORS) for handling requests from different origins.
    SQLite: A lightweight SQL database engine.

Endpoints
1. /images - GET

    Description: Retrieves two randomly selected images from the database for comparison.
    Request Method: GET
    Response Body Format: JSON
    Response Example:

    json

    {
        "image1": {
            "id": 1,
            "rating": 1400,
            "image": "image1.jpg"
        },
        "image2": {
            "id": 2,
            "rating": 1400,
            "image": "image2.jpg"
        }
    }

2. /results - POST

    Description: Saves the result of a comparison between two images, updating their ratings using the Elo Rating algorithm.
    Request Method: POST
    Request Body Format: JSON

    json

    {
        "winnerImg": {
            "id": 1,
            "rating": 1400,
            "image": "image1.jpg"
        },
        "looserImg": {
            "id": 2,
            "rating": 1400,
            "image": "image2.jpg"
        }
    }

Response Body Format: JSON

json

    {}

3. /leaderboard - GET

    Description: Retrieves the leaderboard showing the top-ranked images.
    Request Method: GET
    Response Body Format: JSON (To be implemented)

Database Schema

    Image
        id: Integer (Primary Key)
        rating: Integer (Default 1400)
        image: String (Path to image file)

Setup and Usage

    Ensure you have Python installed on your system.
    Install the required dependencies by running:

pip install Flask Flask-SQLAlchemy Flask-CORS

Run the backend using the command:

    python app.py

    Access the endpoints using appropriate HTTP requests.

Notes

    The Elo Rating algorithm is used to adjust image ratings based on comparison results.
    Images are randomly selected for comparison to ensure fairness.
    This backend currently uses SQLite for data storage, but it can be easily modified to work with other database systems.

Feel free to adjust and expand upon this documentation as needed for your specific project requirements!
