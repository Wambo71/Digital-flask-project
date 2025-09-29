import { NavLink, useParams } from "react-router-dom";
import { useEffect } from "react";
import { toast } from "react-toastify";
import { useState } from "react";
import ProductCard from "../components/ProductCard";

function Home() {
  const [visibleCount, setVisibleCount] = useState(4);
  const [products, setProducts] = useState([]);
  const displayedProducts = products.slice(0, visibleCount);

  useEffect(() => {
      fetch(`http://127.0.0.1:5500/products`)
        .then(res => res.json())
        .then(data => setProducts(data))
        .catch(err => console.error(err));
    }, []);
  
  const handleViewMore = () => {
    setVisibleCount(products.length);
    toast.info("All products are now displayed!");
  }
  return (
    <div className="home-container" style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Welcome to Digital Marketplace</h1>
      <p>Your one stop place for shopping online!!!</p>

      <div className="nav-links">
      <NavLink to="/dashboard" className="nav-link">Dashboard</NavLink>
      </div>

      <div className="product-grid">
        {displayedProducts.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
      {visibleCount < products.length && (
        <button className="button" onClick={handleViewMore}>
          View More
        </button>
      )}
    </div>
  );
}

export default Home;

