import { Link } from "react-router-dom";

function ProductCard({ product }) {
  return (
    <div className="card">
      <img src={product.image_url} alt={product.name} className="image" />
      <h3 className="name">{product.name}</h3>
      <p className="price">${product.price}</p>
      <Link to={`/products/${product.id}`}>
        <button className="button">View Details</button>
      </Link>
    </div>
  );
}

export default ProductCard;
