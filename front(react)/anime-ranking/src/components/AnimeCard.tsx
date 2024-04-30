import { anime } from "../Types";
import "./AnimeCard.css"

export default function Image(props: {
  anime: anime;
  handleClick: (winner: number) => void;
}) {
  const { anime, handleClick } = props;

  return (
    <div className="anime-card">
      <img
        src={`http://localhost:5000/${anime.image}`}
        onClick={() => handleClick(anime.id)}
        height={320}
      ></img>
      <div>{anime.title}</div>
    </div>
  );
}
