import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Nav from "./components/Nav";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Splash from "./components/Splash";

export default () => {
  const [loggedIn, setLoggedIn] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn} showSignup={showSignup} setShowSignup={setShowSignup}/>
      <Switch>
        <Route exact path="/signup">
          <Signup />
        </Route>
        <Route exact path="/login">
          <Login/>
        </Route>
        <Route exact path="/">
          <Splash />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};