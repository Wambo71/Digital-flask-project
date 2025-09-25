import CheckoutForm from "../components/CheckoutForm";

function Checkout() {
  return (
    <div>
      <h1>Checkout</h1>
      
        <CheckoutForm/>
        <button type="submit">Place Order</button>
      
    </div>
  );
}

export default Checkout;
