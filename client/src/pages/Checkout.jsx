import CheckoutForm from "../components/CheckoutForm";
import { toast } from "react-toastify";

function Checkout() {
  return (
    <div>
      <h1>Checkout</h1>
      <CheckoutForm />
      {true ? (
        toast.success("Checkout successful!")
      ) : (
        toast.error("Checkout failed. Please try again.")
      )}
    </div>
  );
}

export default Checkout;
