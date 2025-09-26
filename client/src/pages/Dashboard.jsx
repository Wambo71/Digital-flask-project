import { NavLink } from "react-router-dom";

function Dashboard(){
    return(
        <div className="dashboard-container" style={{ textAlign: "center", marginTop: "50px", gap: "20px", display: "flex", flexDirection: "column", alignItems: "center" }}>
            <h1 className="text-2xl font-bold">Dashboard</h1>
            <nav>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/products">Products</NavLink>
                <NavLink to="/cart">Cart</NavLink>
                <NavLink to="/login">Login</NavLink>
            </nav>
        </div>
    )
}

export default Dashboard;