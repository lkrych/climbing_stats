import React, { useState } from "react";
import { NavLink } from "react-router-dom";

export default ({ loggedIn, setLoggedIn, showSignup, setShowSignup }) => {

    const logOut = (e) => {
        e.preventDefault();
        sessionStorage.removeItem('jwt');
        setLoggedIn(false);
    }

    if (loggedIn) {
        return (
            <div> 
                <NavLink to="/"><li>LOGO!</li></NavLink>
                <li>Add Workout</li>
                <li><button onClick={(e) => logOut(e)}> Logout</button></li>
            </div>
        )
    } else {
        return (
            <div>
                <NavLink to="/"><li>LOGO!</li></NavLink>
                <NavLink to={showSignup ? "/signup" : "/login"}><button onClick={() => setShowSignup(!showSignup)}>{showSignup ? "Sign Up" : "Log In"}</button></NavLink>
            </div>
        )
    }
  
};