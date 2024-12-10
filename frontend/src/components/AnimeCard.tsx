import { anime } from "../Types";
import "./AnimeCard.css"; // You can style the card by creating this file

interface AnimeCardProps {
  anime: anime;
  chooseWinner: (left_or_right: string) => void;
  left_or_right: string;
}

export default function AnimeCard(props: AnimeCardProps) {
  const { anime } = props;
  return (
    <div
      className="anime-card"
      onClick={() => props.chooseWinner(props.left_or_right)}
    >
      <img className="anime-card-image" src={anime.image} alt={anime.title} />
      <div className="anime-card-info">
        <h2 className="anime-card-title">{anime.title}</h2>
        <div className="anime-card-details">
          <span className="anime-card-rating">Rating: {anime.rating}</span>
          <p className="anime-card-desc">{anime.desc}</p>
          <span className="anime-card-episodes">Episodes: {anime.eps}</span>
          <span className="anime-card-year">Year(s): {anime.years}</span>
        </div>
      </div>
    </div>
  );
}
