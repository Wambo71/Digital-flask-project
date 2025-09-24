 import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
 import { ToastContainer } from "react-toastify";
 import "react-toastify/dist/ReactToastify.css";
 import { AuthProvider } from "./auth";
 import NavBar from "./components/NavBar";
 import Home from "./pages/Home";
 import Login from "./pages/Login";
 import Register from "./pages/Register";
 import Profile from "./pages/Profile";

function AppRoutes() {
  return (
    <AuthProvider>
      <Router>
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
        /* Toast container must be global */
        <ToastContainer position="top-right" autoClose={3000} />
      </Router>
    </AuthProvider>
  );
}

export default AppRoutes;
