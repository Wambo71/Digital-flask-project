import React, { useEffect, useState } from "react";

function Cart() {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5500/api/orders") 
      .then((res) => res.json())
      .then((data) => setCart(data))
      .catch((err) => console.error("Error fetching cart:", err));
  }, []);

  return (
    <div>
      <h1>My Cart</h1>
      {cart.length > 0 ? (
        cart.map((order) => (
          <div
            key={order.id}
            style={{
              border: "1px solid #ddd",
              margin: "10px 0",
              padding: "15px",
              borderRadius: "6px",
            }}
          >
            <h2>Order #{order.id}</h2>
            <p>Status: {order.status}</p>
            <p>Total: ${order.total_amount}</p>

            <h3>Items:</h3>
            <ul>
              {order.order_items.map((item) => (
                <li key={item.id}>
                  {item.product?.name} — {item.quantity} × ${item.price}
                </li>
              ))}
            </ul>
          </div>
        ))
      ) : (
        <p>Your cart is empty.</p>
      )}
    </div>
  );
}

export default Cart;
