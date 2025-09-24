import { Link } from "react-router-dom";

function ProductCard({ product }) {
  return (
    <div style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
      <h3>{product.name}</h3>
      <p>Price: ${product.price}</p>
      <Link to={`/products/${product.id}`}>
        <button>View Details</button>
      </Link>
    </div>
  );
}

export default ProductCard;
