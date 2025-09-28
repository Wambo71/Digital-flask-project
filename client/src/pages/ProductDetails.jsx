import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

function ProductDetails({ cart, setCart }) {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5500/products/${id}`)
      .then(res => res.json())
      .then(data => setProduct(data))
      .catch(err => console.error(err));
  }, [id]);

  if (!product) return <p>Loading...</p>;

  const addToCart = () => setCart([...cart, product]);

  return (
    <div className="container">
      <h2 className="heading">{product.name}</h2>
      <img src={product.image_url} alt={product.name} className="image" />
      <p>{product.description}</p>
      <p className="price">{product.price}</p>
      <button className="button" onClick={addToCart}>
        Add to Cart
      </button>
    </div>
  );
}

export default ProductDetails;
