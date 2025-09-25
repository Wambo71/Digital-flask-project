import { Formik, Form, Field } from "formik";
import * as Yup from "yup";

// Validation schema
const ReviewSchema = Yup.object().shape({
  review: Yup.string().required("Review cannot be empty"),
});

function ReviewForm({ onSubmit }) {
  return (
    <div>
      <h4>Leave a Review</h4>
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
          <Form>
            <Field
              as="textarea"
              name="review"
              placeholder="Write your review..."
              style={{ width: "100%", height: "80px" }} 
            />

            {/* Validation error */}
            {errors.review && touched.review ? (
              <div style={{ color: "red" }}>{errors.review}</div>
            ) : null}

            <button type="submit" style={{ marginTop: "10px" }}>
              Submit
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default ReviewForm;
