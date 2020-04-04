import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Nav from "./components/Nav";
import Splash from "./components/Splash";

export default () => {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn}/>
      <Switch>
        <Route to="/">
          <Splash />
        </Route>
      </Switch>
    </BrowserRouter>
  )
};