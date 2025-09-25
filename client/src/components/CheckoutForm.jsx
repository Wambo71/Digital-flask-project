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
    <div>
      <h4>Checkout Form</h4>
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
          <Form>
            <div>
              <label>Name:</label>
              <Field name="name" />
              {errors.name && touched.name ? (
                <div style={{ color: "red" }}>{errors.name}</div>
              ) : null}
            </div>

            <div>
              <label>Address:</label>
              <Field name="address" />
              {errors.address && touched.address ? (
                <div style={{ color: "red" }}>{errors.address}</div>
              ) : null}
            </div>

            <div>
              <label>Payment Method:</label>
              <Field as="select" name="payment">
                <option value="">Select</option>
                <option value="credit">Credit Card</option>
                <option value="paypal">PayPal</option>
                <option value="cash">Cash on Delivery</option>
              </Field>
              {errors.payment && touched.payment ? (
                <div style={{ color: "red" }}>{errors.payment}</div>
              ) : null}
            </div>

            <button type="submit" style={{ marginTop: "10px" }}>
              Place Order
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default CheckoutForm;
