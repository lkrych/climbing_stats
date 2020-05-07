import React from "react";
import { NavLink } from "react-router-dom";
import { Button } from 'semantic-ui-react'

export default ({ setShowSignup }) => (
    <div>
        <h1>Splash! Keep track of your climbs.</h1>
        <div>
            <p>Scroll down to see this paragraph about how to use this app. Get started below</p>
            <div>
                <NavLink to="/signup"><Button onClick={() => setShowSignup(false)}>Sign Up</Button></NavLink>
                <NavLink to="/login"><Button onClick={() => setShowSignup(true)}>Log In</Button></NavLink>
            </div>
        </div>
    </div>
    

);