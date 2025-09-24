// src/pages/Profile.jsx
import { useEffect, useState } from "react";
import { useAuth } from "../auth";
import { toast } from "react-toastify";

function Profile() {
  const { user } = useAuth();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        const res = await fetch("http://localhost:5000/api/profile", {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!res.ok) throw new Error("Failed to load profile");

        const data = await res.json();
        setProfile(data);
      } catch (error) {
        toast.error(error.message || "Something went wrong");
      }
    };

    fetchProfile();
  }, []);

  if (!user) {
    return <p>Please log in to see your profile.</p>;
  }

  if (!profile) {
    return <p>Loading profile...</p>;
  }

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">
        {profile.user.username}'s Profile
      </h1>
      <p>Email: {profile.user.email}</p>

      <h2 className="text-xl font-semibold mt-6">My Products</h2>
      <ul className="list-disc ml-6">
        {profile.products.map((p) => (
          <li key={p.id}>
            {p.name} – ${p.price} (Stock: {p.stock})
          </li>
        ))}
      </ul>

      <h2 className="text-xl font-semibold mt-6">My Orders</h2>
      <ul className="list-disc ml-6">
        {profile.orders.map((o) => (
          <li key={o.id}>
            Order #{o.id} – {o.status} – ${o.total_amount}
          </li>
        ))}
      </ul>

      <h2 className="text-xl font-semibold mt-6">My Reviews</h2>
      <ul className="list-disc ml-6">
        {profile.reviews.map((r) => (
          <li key={r.id}>
            {r.rating}★ on {r.product.name}: "{r.comment}"
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Profile;
