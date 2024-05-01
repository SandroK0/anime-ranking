import { Outlet, useNavigate } from "react-router-dom";
import "./App.css";

function App() {
  const navigate = useNavigate();

  return (
    <div className="App">
      <header
        onClick={() => {
          navigate("/");
        }}
      >
        <div>Anime Ranking</div>
      </header>
      <div className="content">
        <Outlet />
      </div>
    </div>
  );
}

export default App;
