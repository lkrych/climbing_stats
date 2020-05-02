import React from "react";
import { NavLink, useHistory } from "react-router-dom";

export default ({ loggedIn, setLoggedIn, showSignup, setShowSignup }) => {
    let history = useHistory();
    const logOut = (e) => {
        e.preventDefault();
        sessionStorage.removeItem('jwt');
        setLoggedIn(false);
        history.push("/")
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