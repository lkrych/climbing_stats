import React from "react";
import { NavLink, useHistory, useLocation } from "react-router-dom";

import { Menu, Icon } from 'semantic-ui-react';
import { Button } from '../styled/styled_components';

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
      history.push('/workout/create')  
    };

    const homeLink = (
        <NavLink to="/">
            <span className="climbing-orange">
                <i 
                    className="fas fa-mountain fa-lg"
                    onClick={() => setShowSignup(false)}>
                </i>

            </span>
        </NavLink>
    );

    const addWorkoutLink = (
        <Button onClick={(e) => goToWorkout(e)} color='orange' fluid size='large'>
            <Icon name='add circle' />
            Add Workout
        </Button>
    );

    if (loggedIn) {
        return (
            <Menu > 
                <Menu.Item>
                    {homeLink}
                </Menu.Item>
                <Menu.Menu position='right'>
                    <Menu.Item>
                        { location.pathname == "/workout/create" ? null : addWorkoutLink }
                    </Menu.Item>
                    <Menu.Item>
                        <Button onClick={(e) => logOut(e)}> Logout</Button>
                    </Menu.Item>
                </Menu.Menu>
            </Menu>
        )
    } else {
        return (
            <Menu 
                style={{
                    margin: 0
                }}
            >
                <Menu.Item>
                    {homeLink}
                </Menu.Item>
                
                <Menu.Menu position='right'>
                    <Menu.Item>
                        <NavLink to={showSignup ? "/signup" : "/login"}>
                            <Button onClick={() => setShowSignup(!showSignup)}>
                                {showSignup ? "Sign Up" : "Log In"}
                            </Button>
                        </NavLink>
                    </Menu.Item>
                </Menu.Menu>
                
            </Menu>
        )
    }
  
};