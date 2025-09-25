import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import ReviewForm from "../components/ReviewForm";

function ProductDetails() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    // Fetch product from backend API
    fetch(`http://127.0.0.1:5500/api/products/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setProduct(data);
        setReviews(data.reviews || []); // initialize reviews
      })
      .catch((err) => console.error("Error fetching product:", err));
  }, [id]);

  const handleReviewSubmit = (newReview) => {
    setReviews([...reviews, newReview]);
    //  Send review to backend via POST
  };

  if (!product) return <p>Loading...</p>;

  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <button>Add to Cart</button>

      <h3>Reviews:</h3>
      {reviews.length === 0 ? (
        <p>No reviews yet</p>
      ) : (
        reviews.map((review, index) => (
          <p key={index}>
            {review.comment || review} - {review.rating || "N/A"}/5
          </p>
        ))
      )}

      <ReviewForm onSubmit={handleReviewSubmit} />
    </div>
  );
}

export default ProductDetails;
