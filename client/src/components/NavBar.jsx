import { NavLink } from "react-router-dom";

function NavBar() {
  return (
    <nav style={{ display: "flex", gap: "20px", justifyContent: "center", padding: "20px", backgroundColor: "#f0f0f0ff" }}>
      <NavLink to="/dashboard">Dashboard</NavLink>
    </nav>
  );
}

export default NavBar;
