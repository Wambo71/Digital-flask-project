import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function ProductDetails() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5500/api/products/${id}`)
      .then(res => res.json())
      .then(data => setProduct(data));
  }, [id]);

  if (!product) return <p>Loading...</p>;

  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>

      <h3>Reviews:</h3>
      {product.reviews?.map(review => (
        <p key={review.id}>{review.comment} - {review.rating}/5</p>
      ))}

      <form>
        <h3>Add Review</h3>
        <textarea placeholder="Write review" />
        <button type="submit">Submit Review (login required)</button>
      </form>
    </div>
  );
}

export default ProductDetails;
