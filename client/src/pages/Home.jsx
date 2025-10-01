import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Welcome to Digital Marketplace</h1>
      <p>Your one stop place for shopping online!!!</p>
      <button className="button" onClick={() => navigate("/signup")}>Go to SignUp</button>
    </div>
  );
}

export default Home;

