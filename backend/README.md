# Anime Ranking API Documentation

## Overview
This Flask backend serves an Anime Ranking application that allows users to compare and rank anime based on an Elo rating system.

## Endpoints

### 1. Root Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a simple server status message
- **Curl Example:**
  ```bash
  curl http://localhost:5000/
  ```
- **Response:**
  ```json
  "This flask backend server for Anime Ranking"
  ```

### 2. Get Match
- **URL:** `/get_match`
- **Method:** `GET`
- **Description:** Retrieves two random anime for comparison
- **Curl Example:**
  ```bash
  curl http://localhost:5000/get_match
  ```
- **Response:** Array of two anime objects
  ```json
  [
    {
      "id": "anime_id",
      "title": "Anime Title",
      "rating": 1400,
      "desc": "Anime description",
      "eps": "Number of episodes",
      "years": "Year of release",
      "image": "full_image_url"
    }
  ]
  ```

### 3. Save Result
- **URL:** `/save_result`
- **Method:** `POST`
- **Description:** Updates anime ratings after a comparison
- **Curl Example:**
  ```bash
  curl -X POST http://localhost:5000/save_result \
       -H "Content-Type: application/json" \
       -d '{
         "result": {
           "winner_id": "winning_anime_id",
           "loser_id": "losing_anime_id"
         }
       }'
  ```
- **Request Body:**
  - `winner_id`: ID of the winning anime
  - `loser_id`: ID of the losing anime
- **Response:**
  ```json
  {
    "message": "Ratings updated successfully",
    "winner_new_rating": 1420,
    "loser_new_rating": 1380
  }
  ```

### 4. Leaderboard
- **URL:** `/leaderboard`
- **Method:** `GET`
- **Description:** Retrieves paginated leaderboard of anime sorted by rating
- **Query Parameters:**
  - `page` (optional, default: 1): Page number
  - `per_page` (optional, default: 10): Number of items per page
- **Curl Example:**
  ```bash
  curl "http://localhost:5000/leaderboard?page=1&per_page=10"
  ```
- **Response:**
  ```json
  {
    "totalCount": 100,
    "page": 1,
    "pageSize": 10,
    "totalPages": 10,
    "items": [
      {
        "id": "anime_id",
        "image": "full_image_url",
        "ranking": 1,
        "rating": 1600,
        "title": "Top Ranked Anime"
      }
    ]
  }
  ```

## Error Handling
- All endpoints return appropriate HTTP status codes
- Error responses include a `message` and potentially an `error` field describing the issue

## Rating System
The API uses an Elo rating system to dynamically adjust anime ratings based on comparison results. Initial rating is set to 1400.