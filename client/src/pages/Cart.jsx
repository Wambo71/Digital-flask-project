import {Link} from "react-router-dom";

function Cart(){
    return(
        <div>
            <h2>Your cart</h2>
            <p>Items added will appear here</p>

            <Link to="/checkout">
              <button>Go checkout</button>
            </Link>
        </div>
    )
}

export default Cart