import "./Home.css";
import axios, { AxiosResponse } from "axios";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import AnimeCard from "../components/AnimeCard";
import { result } from "../Types";
import { API_URL } from "../config";

function Home() {
  const [match, setMatch] = useState<any>(null);
  const [animationClass, setAnimationClass] = useState<string>("");

  const getImageMatch = () => {
    axios.get(`${API_URL}/get_match`).then((response: AxiosResponse) => {
      setMatch(response.data);
      setAnimationClass("match-in"); // Start animation for new pair
      setTimeout(() => setAnimationClass(""), 600); // Reset animation class after it finishes
    });
  };

  const sendResults = (result: result) => {
    setAnimationClass("match-up"); // Start animation for old pair
    setTimeout(() => {
      axios.post(`${API_URL}/save_result`, { result }).then(() => {
        getImageMatch();
      });
    }, 600); // Delay fetching new data until the animation is complete
  };

  const chooseWinner = (left_or_right: string) => {
    if (!match) return;

    let result: result | null = null;

    switch (left_or_right) {
      case "Right":
        result = {
          winner_id: match[1].id,
          loser_id: match[0].id,
        };
        break;
      case "Left":
        result = {
          winner_id: match[0].id,
          loser_id: match[1].id,
        };
        break;
      default:
        return;
    }

    if (result) {
      sendResults(result);
    }
  };


  useEffect(() => {
    getImageMatch();
  }, []);

  return (
    <div className="Home">
      <div className="main">
        <p>Click on your favourite Anime!</p>
        {match && (
          <div className={`match ${animationClass}`}>
            <AnimeCard
              anime={match[0]}
              chooseWinner={chooseWinner}
              left_or_right="Left"
            />
            <AnimeCard
              anime={match[1]}
              chooseWinner={chooseWinner}
              left_or_right="Right"
            />
          </div>
        )}
      </div>
      <p>
        Check out the
        <Link to="leaderboard" style={{ color: "blue" }}>
          {" "}
          leaderboard{" "}
        </Link>
        to see the top-ranked animes!
      </p>
    </div>
  );
}

export default Home;
