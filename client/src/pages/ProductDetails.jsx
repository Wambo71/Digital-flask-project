import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { Formik, Form, Field } from "formik";

function ProductDetails({ cart, setCart }) {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [isEditing, setIsEditing] = useState(false);

  // Fetch product details
  useEffect(() => {
    fetch(`https://digital-flask-project-4.onrender.com/products/${id}`)
      .then((res) => res.json())
      .then((data) => setProduct(data))
      .catch((err) => console.error("Error fetching product:", err));
  }, [id]);

  // Fetch reviews for the product
  useEffect(() => {
    fetch(`https://digital-flask-project-4.onrender.com/reviews`)
      .then((res) => res.json())
      .then((data) => {
        // Filter reviews for this product
        const productReviews = data.filter(
          (review) => review.product_id === parseInt(id)
        );
        setReviews(productReviews);
      })
      .catch((err) => console.error("Error fetching reviews:", err));
  }, [id]);

  if (!product) return <p>Loading...</p>;

  // Add product to cart
  const addToCart = () => setCart([...cart, product]);

  // Handle UPDATE product
  const handleUpdateProduct = (values) => {
    fetch(`https://digital-flask-project-4.onrender.com/products/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: values.name,
        description: values.description,
        price: parseFloat(values.price),
        stock: parseInt(values.stock),
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setProduct(data);
        setIsEditing(false);
        alert("Product updated successfully!");
      })
      .catch((err) => console.error("Error updating product:", err));
  };

  // Handle DELETE product
  const handleDeleteProduct = () => {
    if (window.confirm("Are you sure you want to delete this product?")) {
      fetch(`https://digital-flask-project-4.onrender.com/products/${id}`, {
        method: "DELETE",
      })
        .then((res) => {
          if (res.ok) {
            alert("Product deleted successfully!");
            navigate("/products"); // Redirect to products page
          }
        })
        .catch((err) => console.error("Error deleting product:", err));
    }
  };

  // Handle submitting a review
  const handleReviewSubmit = (values, { resetForm }) => {
    const newReview = {
      user_id: 1, // Replace with actual logged-in user ID
      product_id: parseInt(id),
      rating: parseInt(values.rating),
      comment: values.reviewText,
    };

    fetch(`https://digital-flask-project-4.onrender.com/reviews`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newReview),
    })
      .then((res) => res.json())
      .then((data) => {
        setReviews([...reviews, data]);
        resetForm();
        alert("Review submitted successfully!");
      })
      .catch((err) => console.error("Error submitting review:", err));
  };

  return (
    <div className="container">
      {!isEditing ? (
        // View Mode
        <>
          <h2 className="heading">{product.name}</h2>
          <img src={product.image_url} alt={product.name} className="image" />
          <p>{product.description}</p>
          <p className="price">${product.price}</p>
          <p>Stock: {product.stock}</p>

          <div style={{ marginTop: "20px" }}>
            <button className="button" onClick={addToCart}>
              Add to Cart
            </button>
            <br></br>
            <button className="button" onClick={() => setCart([])}>
              Clear Cart
            </button>
            <br></br>
            <button className="button" onClick={() => setIsEditing(true)}>
              Update Product
            </button>
            <br></br>
            <button
              className="button"
              onClick={handleDeleteProduct}
              style={{ backgroundColor: "#d9534f" }}
            >
              Delete Product
            </button>
          </div>
        </>
      ) : (
        // Edit Mode
        <div className="edit-form">
          <h3>Edit Product</h3>
          <Formik
            initialValues={{
              name: product.name,
              description: product.description,
              price: product.price,
              stock: product.stock || 0,
            }}
            onSubmit={handleUpdateProduct}
          >
            {() => (
              <Form>
                <div>
                  <label>Name:</label>
                  <Field name="name" type="text" required />
                </div>
                <br></br>
                <div>
                  <label>Description:</label>
                  <Field name="description" as="textarea" required />
                </div>
                <br></br>
                <div>
                  <label>Price:</label>
                  <Field name="price" type="number" step="0.01" required />
                </div>
                <br></br>
                <div>
                  <label>Stock:</label>
                  <Field name="stock" type="number" required />
                </div>
                <br></br>
                <div>
                  <label>Image URL:</label>
                  <Field name="image_url" type="textarea" required />
                </div>
                <button type="submit" className="button" >
                  Save Changes
                </button>
                <br></br>
                <button
                  type="button"
                  className="button"
                  onClick={() => setIsEditing(false)}
                >
                  Cancel
                </button>
              </Form>
            )}
          </Formik>
        </div>
      )}

      {/* Reviews Section */}
      <div className="reviews" style={{ marginTop: "40px" }}>
        <h3>Customer Reviews</h3>
        {reviews.length > 0 ? (
          <ul>
            {reviews.map((review) => (
              <li key={review.id} style={{ marginBottom: "15px" }}>
                <strong>Rating: {review.rating}/5</strong>
                <p>{review.comment}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No reviews yet. Be the first to write one!</p>
        )}
      </div>

      {/* Review Form */}
      <div className="review-form" style={{ marginTop: "30px" }}>
        <h4>Write a Review</h4>
        <Formik
          initialValues={{ rating: "5", reviewText: "" }}
          onSubmit={handleReviewSubmit}
        >
          {() => (
            <Form>
              <div>
                <label>Rating:</label>
                <Field as="select" name="rating" required>
                  <option value="5">5 - Excellent</option>
                  <option value="4">4 - Good</option>
                  <option value="3">3 - Average</option>
                  <option value="2">2 - Poor</option>
                  <option value="1">1 - Terrible</option>
                </Field>
              </div>
              <div>
                <Field
                  as="textarea"
                  name="reviewText"
                  placeholder="Write your review..."
                  required
                  style={{ width: "100%", minHeight: "100px", marginTop: "10px" }}
                />
              </div>
              <button type="submit" className="button" style={{ marginTop: "10px" }}>
                Submit Review
              </button>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
}

export default ProductDetails;