import React from 'react';
import { Route, Redirect, withRouter } from 'react-router-dom';

const Open = ({ component: Component, loggedIn, ...rest }) => {
    return (<Route
        loggedIn={loggedIn}
        {...rest}
        render={props =>
            !loggedIn ? <Component {...rest} {...props} /> : <Redirect to="/dashboard" />
        }
    />)
};

const Protected = ({ component: Component, loggedIn, ...rest }) => (
    <Route 
        loggedIn={loggedIn}
        {...rest}
        render={props =>
            loggedIn ? <Component {...rest} {...props} /> : <Redirect to="/" />
        }
    />
);

export const OpenRoute = withRouter(Open);
export const ProtectedRoute = withRouter(Protected);



