### DIGITAL MARKETPLACE PROJECT

 ### OVERVIEW
 This is a full-stack digital marketplace application built with React (frontend) and a backend API (Flask/JSON server). Users can browse products, view details, add items to their cart, submit reviews, and proceed to checkout. Authentication is included for protected routes like Profile and Dashboard.

 ### FEATURES
### product catalog
-View all products in a grid layout

-Click on a product to see detailed information

### shopping cart
-Add products to cart

-Remove items from cart

-Navigate to checkout page

### user Authenitication
-Login form with validation

-Protected routes for Dashboard and Profile

-Redirects after successful login

### product reviews
-Submit reviews for products

-Display reviews on product detail page

### responsive design
-Styled using global CSS in App.css

-Product grid adapts to screen size

### TECHNOLOGIES
### FRONTEND
-React

-React Router DOM

-Formik & Yup for forms & validation

### BACKEND
-Flask (or JSON server for mock API)

-REST API endpoints:

 -GET /products → fetch all products

 -GET /products/:id → fetch product details

 -POST /api/login → authenticate user

 -POST /api/cart → (optional) add product to cart

### STYLING
-Global CSS in App.css

-Flexbox & grid layouts for responsiveness

### INSTALLATIONS
### clone the repository
-bash=git clone https://github.com/your-username/digital-marketplace.git
-bash=cd digital-marketplace

### install frontend dependencies
-cd client
-npm install

### start frontend
-npm start

### start backend
-cd backend
-python app.py





### USAGE
1.Visit http://localhost:5500 in your browser.

2.Navigate to Products to browse items.

3.Click View Details to see product information.

4.Add items to Cart and go to Checkout.

5.Use the Login page to authenticate and access protected routes.

### AUTHOR
wambui karanja,2025
