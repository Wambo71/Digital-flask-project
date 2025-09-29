import { useEffect, useState } from "react";
import ProductCard from "../components/ProductCard";
import "../App.css";

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://digital-flask-project-4.onrender.com")
      .then(res => res.json())
      .then(data => setProducts(data))
      .catch(err => console.error(err));
  }, []);

  if (!products.length) return <p className="loading-text">Loading products...</p>;

  return (
    <div className="products-page">
      <h1 className="products-title">Products</h1>
      <div className="product-grid">
        {products.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
}

export default Products;
