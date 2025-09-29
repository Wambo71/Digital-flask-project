// src/pages/AddProduct.jsx
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom";

function AddProduct() {
  const navigate = useNavigate();

  const initialValues = {
    name: "",
    description: "",
    price: "",
    stock: "",
    image_url: ""
  };

  const validationSchema = Yup.object({
    name: Yup.string().required("Product name is required"),
    description: Yup.string().required("Description is required"),
    price: Yup.number().typeError("Price must be a number").required("Price is required"),
    stock: Yup.number().typeError("Stock must be a number").required("Stock is required"),
    image_url: Yup.string().url("Must be a valid URL").required("Image URL is required"),
  });

  const handleSubmit = async (values, { setSubmitting, setStatus }) => {
    try {
      const user = JSON.parse(localStorage.getItem("user"));
      if (!user) {
        setStatus("You must be logged in to add a product");
        return;
      }

      // Add seller_id from logged-in user
      const payload = { ...values, seller_id: user.id };

      const res = await fetch("http://127.0.0.1:5500/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        credentials: "include"
      });

      const data = await res.json();

      if (!res.ok) {
        setStatus(data.error || "Failed to add product");
        return;
      }

      alert("Product added successfully!");
      navigate("/products");
    } catch (error) {
      console.error("Add Product error:", error);
      setStatus("Something went wrong. Try again.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="add-product-container">
      <h2>Add Product</h2>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting, status }) => (
          <Form className="add-product-form">
            <div className="form-group">
              <Field type="text" name="name" placeholder="Product Name" className="form-input" />
              <ErrorMessage name="name" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field type="text" name="description" placeholder="Description" className="form-input" />
              <ErrorMessage name="description" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field type="text" name="price" placeholder="Price (e.g., 100)" className="form-input" />
              <ErrorMessage name="price" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field type="text" name="stock" placeholder="Stock" className="form-input" />
              <ErrorMessage name="stock" component="div" className="error-text" />
            </div>

            <div className="form-group">
              <Field type="text" name="image_url" placeholder="Image URL" className="form-input" />
              <ErrorMessage name="image_url" component="div" className="error-text" />
            </div>

            {status && <div className="error-text">{status}</div>}

            <button type="submit" disabled={isSubmitting} className="submit-btn">
              {isSubmitting ? "Adding..." : "Add Product"}
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default AddProduct;
