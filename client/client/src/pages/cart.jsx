import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Cart() {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5500/api/cart")
      .then(res => res.json())
      .then(data => setCart(data));
  }, []);

  return (
    <div>
      <h1>My Cart</h1>
      {cart.map(item => (
        <div key={item.id}>
          <p>{item.product_name} x {item.quantity}</p>
        </div>
      ))}
      <Link to="/checkout">
        <button>Checkout</button>
      </Link>
    </div>
  );
}

export default Cart;
