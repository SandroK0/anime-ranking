import axios from "axios";
import "./Leaderboard.css";
import { useEffect, useState } from "react";
import { anime } from "../Types";

interface animeLeaderboard extends anime {
  ranking: number;
}

export default function Leaderboard() {
  const [images, setImages] = useState<animeLeaderboard[] | null>(null);

  const getLeaderboardData = async () => {
    const response = await axios.get("http://localhost:5000/leaderboard");
    if (response.status === 200) {
      setImages(response.data);
    }
  };

  useEffect(() => {
    getLeaderboardData();
  }, []);

  return (
    <div className="Leaderboard">
      <div className="table-cont">
        <table>
          <thead>
            <tr>
              <th>Ranking</th>
              <th>Image</th>
              <th>Title</th>
              <th>Rating</th>
            </tr>
          </thead>
          <tbody>
            {images &&
              images.map((anime, index) => (
                <tr key={index}>
                  <td>{anime.ranking}</td>
                  <td>
                    <img
                      src={`http://localhost:5000/${anime.image}`}
                      width={100}
                    ></img>
                  </td>
                  <td>{anime.title}</td>
                  <td>{anime.rating}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
