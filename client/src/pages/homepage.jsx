import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Welcome to My Shop</h1>
      <p>Your one stop place for shopping online!!!</p>
      <button onClick={() => navigate("/products")}>Go to Products</button>
    </div>
  );
}

export default Home;

