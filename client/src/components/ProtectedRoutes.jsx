// components/ProtectedRoute.jsx
import { Navigate } from "react-router-dom";

function ProtectedRoute({ children, sellerOnly = false }) {
  const userString = localStorage.getItem("user");
  const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";
  const user = userString ? JSON.parse(userString) : null;

  // Not logged in or user missing
  if (!isLoggedIn || !user) {
    return <Navigate to="/login" replace />;
  }

  // Seller-only page
  if (sellerOnly && user.role !== "seller") {
    alert("Only sellers can access this page");
    return <Navigate to="/" replace />;
  }

  return children;
}

export default ProtectedRoute;
