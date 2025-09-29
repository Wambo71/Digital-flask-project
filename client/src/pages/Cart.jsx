import { Link } from "react-router-dom";

function Cart({ cart }) {
  return (
    <div className="container">
      <h2 className="heading">Your Cart</h2>
      {cart.length === 0 ? (
        <p>No items in cart</p>
      ) : (
        <ul>
          {cart.map((item, index) => (
            <li key={index}>
              {item.name} - ${item.price}
            </li>
          ))}
        </ul>
      )}
      <Link to="/checkout">
        <button className="button">Go Checkout</button>
      </Link>
    </div>
  );
}

export default Cart;
