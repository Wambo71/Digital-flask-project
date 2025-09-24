import { NavLink } from "react-router-dom";

function NavBar() {
  return (
    <nav className="navbar">
      <NavLink to="/">Home</NavLink>
      <NavLink to="/products">Products</NavLink>
      <NavLink to="/cart">Cart</NavLink>
      <NavLink to="/login">Login</NavLink>
      <NavLink to="/profile">Profile</NavLink>
    </nav>
  );
}

export default NavBar;
