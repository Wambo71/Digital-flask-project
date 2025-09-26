import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();
  const goToProducts = () => {
    navigate("/products");
  };

  return (
    <div className="home-container" style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Welcome to Digital Marketplace</h1>
      <p>Your one stop place for shopping online!!!</p>
      <button onClick={goToProducts}>Go to Products</button>
    </div>
  );
}

export default Home;

