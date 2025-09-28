import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

function Login() {
  const navigate = useNavigate();

  const initialValues = { email: "", password: "" };

  const validationSchema = Yup.object({
    email: Yup.string().email("Invalid email").required("Email is required"),
    password: Yup.string().min(4, "Password too short").required("Password is required"),
  });

  const handleSubmit = (values, { setSubmitting }) => {
    console.log("Login data:", values);

    fetch("http://127.0.0.1:5500/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(values),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("Response:", data);
        alert("Login successful (mock)");

        navigate("/products");
      })
      .catch((err) => console.error(err))
      .finally(() => setSubmitting(false));
  };

  return ( 
    <div className="checkout-container">
      <h2 className="checkout-title">Login</h2>
      <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
        {({ isSubmitting }) => (
          <Form className="checkout-form">
            <div>
              <Field type="email" name="email" placeholder="Email" className="form-input"/>
              <ErrorMessage name="email" component="div" style={{ color: "red" }} />
            </div>
            <div>
              <Field type="password" name="password" placeholder="Password" className="form-input"/>
              <ErrorMessage name="password" component="div" style={{ color: "red" }} />
            </div>
            <button type="submit" disabled={isSubmitting} className="submit-btn">
              {isSubmitting ? toast.success("Unable to login") : "Login"}
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default Login;
