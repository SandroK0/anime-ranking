# Anime Ranking [(view)](http://35.246.196.216/)

Anime Ranking is a web application that allows users to rank their favorite anime by comparing them in pairs. The application utilizes an Elo rating algorithm to dynamically adjust anime ratings based on user preferences, resulting in a leaderboard of the top-ranked anime.

## Screenshots

![home](/Home.png "Home Page")
![leaderboard](/leaderboard.png "Leaderboard Page")
![Alt text](/animation.gif)


## Technologies Used

- **Frontend**:

  - HTML/CSS
  - Typescript
  - React.js

- **Backend**:
  - Python
  - Flask
  - SQLite


## Run Using Docker

### Prerequisites

- Docker
- Docker Compose

### Building and Running the Application

1. Clone this repository:

   ```
    git clone https://github.com/SandroK0/anime-ranking.git
    cd anime-ranking
   ```

2. Build the Docker containers:

   ```
   docker-compose build
   ```

3. Start the application:

   ```
   docker-compose up
   ```

4. Access the application in your web browser at `http://localhost:3000` (or the appropriate port if you've configured it differently).

To stop the application, press `Ctrl+C` in the terminal where it's running, or run:

```
docker-compose down
```


## Setup

1. Clone this repository:

bash
    
    git clone https://github.com/SandroK0/anime-ranking.git

2. Navigate to the project directory:![alt text](<Screenshot from 2024-12-10 20-48-24.png>) ![alt text](<Screenshot from 2024-12-10 20-48-32.png>)

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

