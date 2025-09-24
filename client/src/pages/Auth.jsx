// src/auth.jsx
import { createContext, useState, useContext } from "react";
import { toast } from "react-toastify";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // login function
  const login = async (credentials) => {
    try {
      const res = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(credentials),
      });

      if (!res.ok) throw new Error("Login failed");

      const data = await res.json();
      setUser(data.user);
      localStorage.setItem("token", data.access_token);

      toast.success("Logged in successfully!");
    } catch (error) {
      toast.error(error.message || "Invalid credentials");
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("token");
    toast.info("You have been logged out");
  };

  const register = async (newUser) => {
    try {
      const res = await fetch("http://localhost:5000/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newUser),
      });

      if (!res.ok) throw new Error("Registration failed");

      const data = await res.json();
      setUser(data.user);
      localStorage.setItem("token", data.access_token);

      toast.success("Account created successfully!");
    } catch (error) {
      toast.error(error.message || "Could not register");
    }
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, register }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
