import React, { useState } from "react";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";

import { OpenRoute, ProtectedRoute } from "./util/route_util";
import Nav from "./components/Nav";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Splash from "./components/Splash";
import Dashboard from "./components/Dashboard";
import WorkoutForm from './components/WorkoutForm';

export default () => {
  const [loggedIn, setLoggedIn] = useState(localStorage?.jwt);
  const [showSignup, setShowSignup] = useState(false); //need to set this as soon as login or signup endpoint is reached

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn} setLoggedIn={setLoggedIn} showSignup={showSignup} setShowSignup={setShowSignup}/>
      <Switch>
        <OpenRoute exact path="/signup" component={Signup} setLoggedIn={setLoggedIn} />
        <OpenRoute exact path="/login" component={Login} setLoggedIn={setLoggedIn} />
        <OpenRoute exact path="/" component={Splash} loggedIn={loggedIn} setShowSignup={setShowSignup} />
        <ProtectedRoute exact path="/dashboard" component={Dashboard} loggedIn={loggedIn} />
        <ProtectedRoute exact path="/workout/create" component={WorkoutForm} loggedIn={loggedIn}/>
        <Redirect to="/" />
      </Switch>
    </BrowserRouter>
  )
};