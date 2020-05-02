import React from "react";
import { NavLink } from "react-router-dom";

export default ({ setShowSignup }) => (
    <div>
        <h1>Splash! Keep track of your climbs.</h1>
        <div>
            <p>Scroll down to see this paragraph about how to use this app. Get started below</p>
            <div>
                <NavLink to="/signup"><button onClick={() => setShowSignup(false)}>Sign Up</button></NavLink>
                <NavLink to="/login"><button onClick={() => setShowSignup(true)}>Log In</button></NavLink>
            </div>
        </div>
    </div>
    

);