import React, { useState, Fragment } from "react";

import ClimbForm from "./ClimbForm";

export default ({boulders, setBoulders, routes, setRoutes}) => {
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
            <p>
                Boulders: {boulders.map(b => `V${b.grade}`)}
            </p>
            <p>
                Routes: {routes.map(r => `5.${r.grade}${r.letterGrade}`)}
            </p>
            <br></br>
            <button onClick={(e) => toggleBoulderForm(e)}>
                Add Boulder
            </button>
            {showBoulderForm ? <ClimbForm type="boulder" addClimb={setBoulders} /> : null}
            <br></br>
            <button onClick={(e) => toggleRouteForm(e)}>
                Add Route
            </button>
            {showRouteForm ? <ClimbForm type="route" addClimb={setRoutes} /> : null}
        </Fragment>
    );
}