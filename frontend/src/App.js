import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Nav from "./components/Nav";
import Splash from "./components/Splash";
import Login from "./components/Login";

export default () => {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn}/>
      <Switch>
        <Route exact path="/signup">
          {/* <Login/> need to specify type via props? */}
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