import React, { useState } from "react";
import { NavLink } from "react-router-dom";

export default ({ loggedIn, showSignup, setShowSignup }) => {

    if (loggedIn) {
        return (
            <div> 
                <li>LOGO!</li>
                <li>Add Workout</li>
                <li>Logout</li>
            </div>
        )
    } else {
        return (
            <div>
                <li>LOGO!</li>
                <NavLink to={showSignup ? "/signup" : "/login"}><button onClick={() => setShowSignup(!showSignup)}>{showSignup ? "Sign Up" : "Log In"}</button></NavLink>
            </div>
        )
    }
  
};