import { useEffect, useState } from "react";
import ProductCard from "../components/ProductCard";

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5500/api/products")
      .then(res => res.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Products</h1>
      <div style={{ display: "flex", flexWrap: "wrap" }}>
        {products.map(p => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
}

export default Products;
