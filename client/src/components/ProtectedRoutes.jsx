import { Navigate } from "react-router-dom";

function ProtectedRoute({ children }) {
  // Check if user exists 
  const user = localStorage.getItem("user");

  // If not logged in then redirect to login
  if (!user) {
    return <Navigate to="/login" />;
  }

  // If logged in then show the page
  return children;
}

export default ProtectedRoute;
