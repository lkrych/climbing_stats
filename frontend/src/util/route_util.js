import React from 'react';
import { Route, Redirect, withRouter } from 'react-router-dom';

const Open = ({ component: Component, path, loggedIn, exact }) => (
    <Route 
        path={path}
        exact={exact}
        render={props => 
            !loggedIn ? <Component {...props} /> : <Redirect to="/dashboard" />
        }
    />
);

const Protected = ({ component: Component, path, loggedIn, exact }) => (
    <Route 
        path={path}
        exact={exact}
        render={props =>
            loggedIn ? <Component {...props} /> : <Redirect to="/" />
        }
    />
);

export const OpenRoute = withRouter(Open);
export const ProtectedRoute = withRouter(Protected);



