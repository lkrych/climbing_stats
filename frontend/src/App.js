import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Nav from "./components/Nav";

export default () => {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <BrowserRouter>
      <Nav loggedIn={loggedIn}/>
      <Switch>
        <Route>

        </Route>
      </Switch>
    </BrowserRouter>
  )
};