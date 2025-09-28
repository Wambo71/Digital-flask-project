import { Formik, Form, Field } from "formik";
import * as Yup from "yup";

// Validation schema
const ReviewSchema = Yup.object().shape({
  review: Yup.string().required("Review cannot be empty"),
});

function ReviewForm({ onSubmit }) {
  return (
    <div className="container">
      <h4 className="heading">Leave a Review</h4>
      <Formik
        initialValues={{ review: "" }}
        validationSchema={ReviewSchema}
        onSubmit={(values, { resetForm }) => {
          console.log("Review submitted:", values.review);
          if (onSubmit) onSubmit(values.review);
          resetForm();
        }}
      >
        {({ errors, touched }) => (
          <Form className="form">
            <Field
              as="textarea"
              name="review"
              placeholder="Write your review..."
              className={`textarea ${errors.review && touched.review ? "textareaError" : ""}`}
            />
            {errors.review && touched.review && (
              <div className="error">{errors.review}</div>
            )}

            <button type="submit" className="button">
              Submit
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default ReviewForm;
