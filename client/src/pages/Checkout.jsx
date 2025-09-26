import CheckoutForm from "../components/CheckoutForm";

function Checkout() {
  const handleCheckout = () => {
    // Implement checkout logic here
    alert("Checkout process initiated!");
  };
  return (
    <div>
      <h1>Checkout</h1>
      <CheckoutForm />
      <button type="submit" onClick={handleCheckout}>Place Order</button>

    </div>
  );
}

export default Checkout;
