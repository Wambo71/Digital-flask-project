// App.jsx
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import Products from "./pages/Products";
import ProductDetails from "./pages/ProductDetails";
import Cart from "./pages/Cart";
import Checkout from "./pages/Checkout";
import Login from "./pages/LoginPage";
import SignUp from "./pages/SignUp";
import Profile from "./pages/Profile";
import AddProduct from "./pages/AddProduct";
import ProtectedRoute from "./components/ProtectedRoutes";
import "./App.css";

function App() {
  const [cart, setCart] = useState([]);

  return (
    <Router>
      <NavBar cart={cart} />

      <Routes>
        {/* Public routes */}
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />

        {/* Protected routes */}
        <Route
          path="/products"
          element={
            <ProtectedRoute>
              <Products />
            </ProtectedRoute>
          }
        />
        <Route
          path="/products/:id"
          element={
            <ProtectedRoute>
              <ProductDetails cart={cart} setCart={setCart} />
            </ProtectedRoute>
          }
        />
        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />

        {/* Only sellers can add products */}
        <Route
          path="/add-product"
          element={
            <ProtectedRoute sellerOnly={true}>
              <AddProduct />
            </ProtectedRoute>
          }
        />

        {/* Cart and checkout */}
        <Route path="/cart" element={<Cart cart={cart} />} />
        <Route path="/checkout" element={<Checkout />} />
      </Routes>
    </Router>
  );
}

export default App;
