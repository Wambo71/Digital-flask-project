import { useState, useEffect } from "react";

function Profile() {
  const user = JSON.parse(localStorage.getItem("user"));
  const [orders, setOrders] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) {
      setLoading(false);
      return;
    }

    // Fetch user's orders
    fetch(`https://digital-flask-project-4.onrender.com/orders`)
      .then((res) => res.json())
      .then((data) => {
        // Filter orders for this user
        const userOrders = data.filter(
          (order) => order.user_id === user.id
        );
        setOrders(userOrders);
      })
      .catch((err) => console.error("Error fetching orders:", err));

    // Fetch user's reviews
    fetch(`https://digital-flask-project-4.onrender.com/reviews`)
      .then((res) => res.json())
      .then((data) => {
        // Filter reviews for this user
        const userReviews = data.filter(
          (review) => review.user_id === user.id
        );
        setReviews(userReviews);
      })
      .catch((err) => console.error("Error fetching reviews:", err))
      .finally(() => setLoading(false));
  }, [user]);

  if (!user) {
    return (
      <div className="container">
        <h2>Profile Page</h2>
        <p>No user data available. Please log in.</p>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="container">
        <p>Loading profile...</p>
      </div>
    );
  }

  return (
    <div className="container">
      <h2>My Profile</h2>

      {/* User Info Section */}
      <div className="profile-section">
        <h3>Account Information</h3>
        <p><strong>Username:</strong> {user.username}</p>
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>Role:</strong> {user.role || "Buyer"}</p>
      </div>

      {/* Orders Section */}
      <div className="profile-section" style={{ marginTop: "30px" }}>
        <h3>My Orders ({orders.length})</h3>
        {orders.length > 0 ? (
          <div>
            {orders.map((order) => (
              <div
                key={order.id}
                style={{
                  border: "1px solid #ddd",
                  padding: "15px",
                  marginBottom: "15px",
                  borderRadius: "5px",
                }}
              >
                <p><strong>Order ID:</strong> {order.id}</p>
                <p><strong>Product ID:</strong> {order.product_id}</p>
                <p><strong>Quantity:</strong> {order.quantity}</p>
                <p><strong>Total Amount:</strong> ${order.total_amount}</p>
                <p><strong>Status:</strong> {order.status}</p>
                <p>
                  <strong>Date:</strong>{" "}
                  {order.created_at
                    ? new Date(order.created_at).toLocaleDateString()
                    : "N/A"}
                </p>
              </div>
            ))}
          </div>
        ) : (
          <p>You haven't made any orders yet.</p>
        )}
      </div>

      {/* Reviews Section */}
      <div className="profile-section" style={{ marginTop: "30px" }}>
        <h3>My Reviews ({reviews.length})</h3>
        {reviews.length > 0 ? (
          <div>
            {reviews.map((review) => (
              <div
                key={review.id}
                style={{
                  border: "1px solid #ddd",
                  padding: "15px",
                  marginBottom: "15px",
                  borderRadius: "5px",
                }}
              >
                <p><strong>Product ID:</strong> {review.product_id}</p>
                <p><strong>Rating:</strong> {review.rating}/5</p>
                <p><strong>Comment:</strong> {review.comment}</p>
                <p>
                  <strong>Date:</strong>{" "}
                  {review.created_at
                    ? new Date(review.created_at).toLocaleDateString()
                    : "N/A"}
                </p>
              </div>
            ))}
          </div>
        ) : (
          <p>You haven't written any reviews yet.</p>
        )}
      </div>

      {/* Purchase Summary */}
      <div className="profile-section" style={{ marginTop: "30px" }}>
        <h3>Purchase Summary</h3>
        <p>
          <strong>Total Orders:</strong> {orders.length}
        </p>
        <p>
          <strong>Total Spent:</strong> 
          {orders
            .reduce((sum, order) => sum + parseFloat(order.total_amount || 0), 0)
            .toFixed(2)}
        </p>
        <p>
          <strong>Total Reviews Written:</strong> {reviews.length}
        </p>
      </div>
    </div>
  );
}

export default Profile;