import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { toast } from "react-toastify";

const ReviewSchema = Yup.object().shape({
  review: Yup.string().required("Review cannot be empty"),
});


const submitReview = async (review, token) => {
  const response = await fetch("http://127.0.0.1:5000/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`, 
    },
    body: JSON.stringify({ review }),
  });

  if (!response.ok) {
    throw new Error("Failed to submit review");
  }

  return response.json();
};

function ReviewForm() {
  return (
    <div className="container">
      <h4 className="heading">Leave a Review</h4>

      <Formik
        initialValues={{ review: "" }}
        validationSchema={ReviewSchema}
        onSubmit={async (values, { resetForm }) => {
          const token = localStorage.getItem("token");

          if (!token) {
            toast.error("You must be logged in to leave a review!");
            return;
          }

          try {
            const data = await submitReview(values.review, token);
            toast.success("Review submitted successfully!");
            console.log("Review submitted:", data);

            resetForm();
          } catch (err) {
            toast.error(err.message || "Error submitting review");
            console.error(err);
          }
        }}
      >
        {({ isSubmitting }) => (
          <Form className="form">
            <Field
              as="textarea"
              name="review"
              placeholder="Write your review..."
              className="textarea"
            />
            <ErrorMessage
              name="review"
              component="div"
              className="error"
            />

            <button
              type="submit"
              disabled={isSubmitting}
              className="button"
            >
              {isSubmitting ? "Submitting..." : "Submit"}
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default ReviewForm;
