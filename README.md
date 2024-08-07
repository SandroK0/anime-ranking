# Anime Ranking

Anime Ranking is a web application that allows users to rank their favorite anime by comparing them in pairs. The application utilizes an Elo rating algorithm to dynamically adjust anime ratings based on user preferences, resulting in a leaderboard of the top-ranked anime.

## Screenshots

![home](/Home.png "Home Page")
![leaderboard](/leaderboard.png "Leaderboard Page")

## Technologies Used

- **Frontend**:

  - HTML/CSS
  - Typescript
  - React.js

- **Backend**:
  - Python
  - Flask
  - SQLite

## Setup

1. Clone this repository:

bash
    
    git clone https://github.com/SandroK0/anime-ranking.git

2. Navigate to the project directory:

bash

    cd anime-ranking

3. Install dependencies:

bash

    # For frontend (assuming using npm)
    cd frontend
    npm install

    # For backend (assuming using pip)
    cd /backend
    pip install -r requirements.txt


4. Start the frontend and backend servers:


# Frontend
bash
    
    cd ../frontend
    npm run dev

# Backend
bash

    cd ../backend
    flask run

5. Access the application in your web browser:

url

    http://localhost:5173  # Frontend
    http://localhost:5000  # Backend

