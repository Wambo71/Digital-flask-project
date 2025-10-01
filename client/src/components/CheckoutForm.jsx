import { Formik, Form, Field } from "formik";
import * as Yup from "yup";

// Validation schema
const CheckoutSchema = Yup.object().shape({
  name: Yup.string().required("Required"),
  address: Yup.string().required("Required"),
  payment: Yup.string().required("Required"),
});

function CheckoutForm() {
  return (
    <div className="checkout-container">
      <h4 className="checkout-title">Checkout Form</h4>
      <Formik
        initialValues={{ name: "", address: "", payment: "" }}
        validationSchema={CheckoutSchema}
        onSubmit={(values, { resetForm }) => {
          console.log("Order placed:", values);
          alert("Order placed successfully!");
          resetForm();
        }}
      >
        {({ errors, touched }) => (
          <Form className="checkout-form">
            <div className="form-group">
              <label>Name:</label>
              <Field name="name" className="form-input" />
              {errors.name && touched.name ? (
                <div className="error-text">{errors.name}</div>
              ) : null}
            </div>

            <div className="form-group">
              <label>Address:</label>
              <Field name="address" className="form-input" />
              {errors.address && touched.address ? (
                <div className="error-text">{errors.address}</div>
              ) : null}
            </div>

            <div className="form-group">
              <label>Payment Method:</label>
              <Field as="select" name="payment" className="form-input">
                <option value="">Select</option>
                <option value="credit">Credit Card</option>
                <option value="paypal">PayPal</option>
                <option value="mpesa">Mpesa</option>
                <option value="cash">Cash on Delivery</option>
              </Field>
              {errors.payment && touched.payment ? (
                <div className="error-text">{errors.payment}</div>
              ) : null}
            </div>

            <button type="submit" className="submit-btn">
              Place Order
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default CheckoutForm;
