import "./Home.css";
import axios, { AxiosResponse } from "axios";
import { anime, match } from "../Types";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import AnimeCard from "../components/AnimeCard";

interface result {
  winner: anime;
  looser: anime;
}

function Home() {
  const [match, setMatch] = useState<match | null>(null);

  const getImageMatch = () => {
    axios
      .get("http://localhost:5000/images")
      .then((response: AxiosResponse) => {
        setMatch(response.data);
        console.log(response.data);
      });
  };

  const sendResults = (result: result) => {
    axios.post("http://localhost:5000/results", { result }).then(() => {
      getImageMatch();
    });
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (match) {
        if (e.key === "ArrowRight") {
          let result: result = {
            winner: match.anime2,
            looser: match.anime1,
          };
          sendResults(result);
        } else if (e.key === "ArrowLeft") {
          let result: result = {
            winner: match.anime1,
            looser: match.anime2,
          };
          sendResults(result);
        }
      }
    };
    document.addEventListener("keydown", handleKeyDown);

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [match]);

  useEffect(() => {
    getImageMatch();
  }, []);

  const handleClick = (winnerId: number) => {
    let result: result;

    if (winnerId === match?.anime1.id) {
      result = {
        winner: match.anime1,
        looser: match.anime2,
      };
      sendResults(result);
    } else if (winnerId === match?.anime2.id) {
      result = {
        winner: match.anime2,
        looser: match.anime1,
      };
      sendResults(result);
    }
  };

  return (
    <div className="Home">
      <div className="main">
        {match && (
          <div className="match">
            <AnimeCard
              anime={match.anime1}
              handleClick={handleClick}
            ></AnimeCard>
            <AnimeCard
              anime={match.anime2}
              handleClick={handleClick}
            ></AnimeCard>
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
