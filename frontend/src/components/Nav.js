import React, { useState } from "react";
import { Link } from "react-router-dom";

export default ({ loggedIn }) => {

    const [showSignup, setShowSignup] = useState(false);

    if (loggedIn) {
        return (
            <div> 
                <li>Add Workout</li>
                <li>Logout</li>
            </div>
        )
    } else {
        return (
            <div>
                <li><button onClick={() => setShowSignup(!showSignup)}>{showSignup ? "Sign Up" : "Log In"}</button></li>
            </div>
        )
    }
  
};