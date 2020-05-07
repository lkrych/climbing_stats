import React from "react";
import { NavLink, useHistory, useLocation } from "react-router-dom";
import { Button } from 'semantic-ui-react'

export default ({ loggedIn, setLoggedIn, showSignup, setShowSignup }) => {
    let history = useHistory();
    let location = useLocation();

    const logOut = (e) => {
        e.preventDefault();
        localStorage.removeItem('jwt');
        setLoggedIn(false);
        history.push("/")
    }

    const goToWorkout = (e) => {
      e.preventDefault();
      console.log(location.pathname);
      history.push('/workout/create')  
    };

    const addWorkoutLink = (<li>
                            <Button onClick={(e) => goToWorkout(e)}>Add Workout</Button>
                        </li>);

    if (loggedIn) {
        return (
            <div> 
                <NavLink to="/"><li onClick={() => setShowSignup(false)}>LOGO!</li></NavLink>
                { location.pathname == "/workout/create" ? null : addWorkoutLink }
                <li>
                    <Button onClick={(e) => logOut(e)}> Logout</Button>
                </li>
            </div>
        )
    } else {
        return (
            <div>
                <NavLink to="/"><li onClick={() => setShowSignup(false)}>LOGO!</li></NavLink>
                <NavLink to={showSignup ? "/signup" : "/login"}><Button size='tiny' onClick={() => setShowSignup(!showSignup)}>{showSignup ? "Sign Up" : "Log In"}</Button></NavLink>
            </div>
        )
    }
  
};