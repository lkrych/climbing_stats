import React, { useState, Fragment } from "react";
import { Button, Input, Label } from 'semantic-ui-react'

import ClimbForm from "./ClimbForm";
import Climb from "./Climb";

export default ({boulders, setBoulders, routes, setRoutes, removeFromArray}) => {
    const [showBoulderForm, setShowBoulderForm] = useState(false);
    const [showRouteForm, setShowRouteForm] = useState(false);

    const toggleBoulderForm = (e) => {
        e.preventDefault();
        setShowBoulderForm(!showBoulderForm);
    }

    const toggleRouteForm = (e) => {
        e.preventDefault();
        setShowRouteForm(!showRouteForm);
    }

    return(
        <Fragment>
            <div>
                Boulders: {boulders.map((b, i) => <Climb key={i} type="boulder" grade={b} index={i} removeFromArray={removeFromArray} /> )}
            </div>
            <div>
                Routes: {routes.map((r, i) => <Climb key={i} type="route" grade={r} index={i} removeFromArray={removeFromArray}/>)}
            </div>
            <br></br>
            <Button onClick={(e) => toggleBoulderForm(e)}>
                Add Boulder
            </Button>
            {showBoulderForm ? <ClimbForm type="boulder" addClimb={setBoulders} climbs={boulders} /> : null}
            <br></br>
            <Button onClick={(e) => toggleRouteForm(e)}>
                Add Route
            </Button>
            {showRouteForm ? <ClimbForm type="route" addClimb={setRoutes} climbs={routes} /> : null}
        </Fragment>
    );
}