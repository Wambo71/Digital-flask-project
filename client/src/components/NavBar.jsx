import { NavLink } from "react-router-dom";

function NavBar() {
  return (
    <nav className="navbar">
      <NavLink to="/" className="nav-link">Home</NavLink>
      <NavLink to="/signup" className="nav-link">Sign up</NavLink>
      <NavLink to="/login" className="nav-link">Login</NavLink>
      <NavLink to="/products" className="nav-link">Products</NavLink>
      <NavLink to="/add-product" className="nav-link">Add Products</NavLink>
      <NavLink to="/cart" className="nav-link">Cart</NavLink>
      <NavLink to="/profile" className="nav-link">Profile</NavLink>
    </nav>
  );
}

export default NavBar;
