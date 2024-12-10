import axios from "axios";
import "./Leaderboard.css";
import { useEffect, useState } from "react";
import { anime } from "../Types";
import { API_URL } from "../config";

interface animeLeaderboard extends anime {
  ranking: number;
}

export default function Leaderboard() {
  const [images, setImages] = useState<animeLeaderboard[]>([]); // Store all fetched items
  const [page, setPage] = useState(1); // Current page
  const [isLoading, setIsLoading] = useState(false); // Loading state
  const [hasMore, setHasMore] = useState(true); // Check if more data is available

  const getLeaderboardData = async (currentPage: number) => {
    if (isLoading || !hasMore) return;

    setIsLoading(true);
    try {
      const response = await axios.get(`${API_URL}/leaderboard`, {
        params: {
          page: currentPage,
          per_page: 50,
        },
      });
      if (response.status === 200) {
        setImages((prevImages) => [...prevImages, ...response.data.items]);
        setHasMore(response.data.items.length > 0);
      }
    } catch (error) {
      console.error("Error fetching leaderboard data:", error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    getLeaderboardData(page); // Fetch leaderboard data for the current page
  }, [page]);

  const handleScroll = () => {
    const scrollHeight = document.documentElement.scrollHeight;
    const scrollTop = document.documentElement.scrollTop;
    const clientHeight = document.documentElement.clientHeight;

    // Load more data when the user scrolls near the bottom
    if (scrollTop + clientHeight >= scrollHeight - 200 && !isLoading && hasMore) {
      setPage((prevPage) => prevPage + 1);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, [isLoading, hasMore]);

  return (
    <div className="Leaderboard">
      <div className="cards-container">
        {images.map((anime, index) => (
          <div key={index} className="card">
            <div className="ranking">#{anime.ranking}</div>
            <img src={anime.image} alt={anime.title} className="anime-image" />
            <h3 className="title">{anime.title}</h3>
            <div className="rating">Rating: {anime.rating}</div>
          </div>
        ))}
      </div>
      {isLoading && <div className="loading">Loading...</div>}
      {!hasMore && <div className="end-message">You've reached the end!</div>}
    </div>
  );
}
