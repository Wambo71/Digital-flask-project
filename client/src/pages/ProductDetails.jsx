import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { Formik, Form, Field } from "formik";

function ProductDetails({ cart, setCart }) {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [reviews, setReviews] = useState([]);

  //  Fetch product details
  useEffect(() => {
    fetch(`http://127.0.0.1:5500/products/${id}`)
      .then((res) => res.json())
      .then((data) => setProduct(data))
      .catch((err) => console.error(err));
  }, [id]);

  //  Fetch reviews for the product
  useEffect(() => {
    fetch(`http://127.0.0.1:5500/reviews?productId=${id}`)
      .then((res) => res.json())
      .then((data) => setReviews(data))
      .catch((err) => console.error(err));
  }, [id]);

  if (!product) return <p>Loading...</p>;

  //  Add product to cart
  const addToCart = () => setCart([...cart, product]);

  // Handle submitting a review using Formik
  const handleReviewSubmit = (values, { resetForm }) => {
    const newReview = {
      productId: id,
      text: values.reviewText,
    };

    // POST to backend (JSON Server )
    fetch(`http://127.0.0.1:5500/reviews`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newReview),
    })
      .then((res) => res.json())
      .then((data) => {
        // Update the list of reviews in the UI
        setReviews([...reviews, data]);
        resetForm(); // clear the form
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="container">
      
      <h2 className="heading">{product.name}</h2>
      <img src={product.image_url} alt={product.name} className="image" />
      <p>{product.description}</p>
      <p className="price">${product.price}</p>
      <button className="button" onClick={addToCart}>
        Add to Cart
      </button>

      {/*  Reviews Section */}
      <div className="reviews">
        <h3>Reviews</h3>
        {reviews.length > 0 ? (
          <ul>
            {reviews.map((review) => (
              <li key={review.id}>{review.text}</li>
            ))}
          </ul>
        ) : (
          <p>No reviews yet. Be the first to write one!</p>
        )}
      </div>

      {/*  Formik Review Form */}
      <div className="review-form">
        <h4>Write a Review</h4>
        <Formik
          initialValues={{ reviewText: "" }}
          onSubmit={handleReviewSubmit}
        >
          {() => (
            <Form>
              <Field
                as="textarea"
                name="reviewText"
                placeholder="Write your review..."
                required
                
              />
              <button type="submit">Submit Review</button>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
}

export default ProductDetails;
