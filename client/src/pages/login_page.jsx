// src/pages/Login.jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import axios from "axios";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const LoginSchema = Yup.object().shape({
  email: Yup.string().email("Invalid email").required("Email is required"),
  password: Yup.string().required("Password is required"),
});

const Login = () => {
  const navigate = useNavigate();

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      const res = await axios.post("http://localhost:5500/api/login", values);

      localStorage.setItem("token", res.data.access_token);

      toast.success("Login successful", {
        position: "top-right",
        autoClose: 3000,
      });

      navigate("/profile"); 
    } catch (error) {
      toast.error(
        error.response?.data?.error || "Login failed. Check credentials.",
        {
          position: "top-right",
          autoClose: 3000,
        }
      );
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-50">
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-md">
        <h2 className="text-2xl font-bold text-center mb-6">Login</h2>

        <Formik
          initialValues={{ email: "", password: "" }}
          validationSchema={LoginSchema}
          onSubmit={handleSubmit}
        >
          {({ isSubmitting }) => (
            <Form className="space-y-4">
              <div>
                <label className="block text-gray-700">Email</label>
                <Field
                  type="email"
                  name="email"
                  className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400"
                />
                <ErrorMessage
                  name="email"
                  component="div"
                  className="text-red-500 text-sm"
                />
              </div>

              <div>
                <label className="block text-gray-700">Password</label>
                <Field
                  type="password"
                  name="password"
                  className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400"
                />
                <ErrorMessage
                  name="password"
                  component="div"
                  className="text-red-500 text-sm"
                />
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full bg-green-500 text-white py-2 rounded-lg hover:bg-green-600 transition"
              >
                {isSubmitting ? "Logging in..." : "Login"}
              </button>
            </Form>
          )}
        </Formik>

        <p className="text-center mt-4 text-sm text-gray-600">
          Does not have an account?{" "}
          <span
            onClick={() => navigate("/register")}
            className="text-green-500 cursor-pointer"
          >
            Register
          </span>
        </p>
      </div>
    </div>
  );
};

export default Login;
