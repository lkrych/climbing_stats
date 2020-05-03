import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Nav from "./components/Nav";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Splash from "./components/Splash";
import Dashboard from "./components/Dashboard";
import WorkoutForm from './components/WorkoutForm';

export default () => {
  const [loggedIn, setLoggedIn] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

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
        <Route exact path="/">
          <Splash setShowSignup={setShowSignup} />
        </Route>
        <Route exact path="/dashboard">
          <Dashboard />
        </Route>
        <Route exact path="/workout/create">
          <WorkoutForm />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};