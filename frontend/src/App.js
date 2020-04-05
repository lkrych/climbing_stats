import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Nav from "./components/Nav";
import Signup from "./components/Signup";

export default () => {
  const [loggedIn, setLoggedIn] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn} showSignup={showSignup} setShowSignup={setShowSignup}/>
      <Switch>
        <Route>
            <Signup />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};