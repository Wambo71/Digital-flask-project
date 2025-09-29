import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom";

function SignUp() {
  const navigate = useNavigate();

  const initialValues = {
    username: "",
    email: "",
    password: "",
    role: "buyer" // default role
  };

  const validationSchema = Yup.object({
    username: Yup.string().required("Username is required"),
    email: Yup.string().email("Invalid email").required("Email is required"),
    password: Yup.string().min(4, "Password too short").required("Password is required"),
    role: Yup.string().oneOf(["buyer", "seller"]).required("Role is required")
  });

  const handleSubmit = async (values, { setSubmitting, setStatus }) => {
    try {
      const res = await fetch("https://digital-flask-project-4.onrender.com/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(values),
        credentials: "include",
      });

      const data = await res.json();
      if (!res.ok) {
        setStatus(data.error || "Failed to sign up");
        return;
      }

      alert("Signup successful!");
      navigate("/login");
    } catch (error) {
      console.error(error);
      setStatus("Something went wrong");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="signup-form-container">
      <h2>Sign Up</h2>
      <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
        {({ isSubmitting, status }) => (
          <Form>
            <div className="form-group">
              <Field name="username" placeholder="Username" className="form-input" />
              <ErrorMessage name="username" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field name="email" placeholder="Email" className="form-input" />
              <ErrorMessage name="email" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field type="password" name="password" placeholder="Password" className="form-input" />
              <ErrorMessage name="password" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field as="select" name="role" className="form-input">
                <option value="buyer">Buyer</option>
                <option value="seller">Seller</option>
              </Field>
              <ErrorMessage name="role" component="div" className="error-text" />
            </div>

            {status && <div className="status-text">{status}</div>}

            <button type="submit" disabled={isSubmitting}>
              {isSubmitting ? "Signing up..." : "Sign Up"}
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default SignUp;
