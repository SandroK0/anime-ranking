import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import Home from "./Pages/Home.tsx";
import {
  Route,
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import Leaderboard from "./Pages/Leaderboard.tsx";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<App />}>
      <Route index element={<Home></Home>}></Route>
      <Route path="leaderboard" element={<Leaderboard></Leaderboard>}></Route>
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <RouterProvider router={router}></RouterProvider>
);
