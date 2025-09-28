import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import ReviewForm from "../components/ReviewForm";

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

  const addToCart = () => {
    setCart([...cart, product]);
    toast.success("Item added to cart!");
  };

  const addreviews = () => {
    <ReviewForm />
  }

  return (
    <div className="container">
      <h2 className="heading">{product.name}</h2>
      <img src={product.image_url} alt={product.name} className="image" />
      <p>{product.description}</p>
      <p className="price">{product.price}</p>
      <h3>Reviews:</h3>
        {product.reviews.map((review, index) => (
          <li key={index}>
            <strong>{review.author}</strong> {review.comment}
          </li>
        ))}
      <button className="button" onClick={addreviews}>Add review</button> <br />
      <button className="button" onClick={addToCart}>
        Add to Cart
      </button>
      {toast.info("Product added to Cart")}
    </div>
  );
}

export default ProductDetails;
