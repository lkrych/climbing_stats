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
  const [loggedIn, setLoggedIn] = useState(false);
  const [showSignup, setShowSignup] = useState(false); //need to set this as soon as login or signup endpoint is reached

  console.log("AM I LOGGED IN?", loggedIn);
  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn} setLoggedIn={setLoggedIn} showSignup={showSignup} setShowSignup={setShowSignup}/>
      <Switch>
        <Route exact path="/signup">
          <Signup setLoggedIn={setLoggedIn} />
        </Route>
        <Route exact path="/login">
          <Login setLoggedIn={setLoggedIn} />
        </Route>
        <OpenRoute exact path="/" component={Splash} loggedIn={loggedIn} setShowSignup={setShowSignup} />
        <ProtectedRoute exact path="/dashboard" component={Dashboard} loggedIn={loggedIn} />
        <ProtectedRoute exact path="/workout/create" component={WorkoutForm} loggedIn={loggedIn}/>
        <Redirect to="/" />
      </Switch>
    </BrowserRouter>
  )
};