import React, { useState, Fragment } from "react";

import { range, rangeWithChars } from "../util/util";

export default ({type, addClimb, climbs}) => {
    const [boulderSelection, setBoulderSelection] = useState(null);
    const [routeSelection, setRouteSelection] = useState(null);

    const createRangeButtonList = (range = [], buttonInput, clickFunction) => {
        return range.map((n) => <button key={n} onClick={(e) => clickFunction(e, n)}>{buttonInput}{n}</button>, range)
    }

    const addBoulderOrRoute = (e, grade) => {
        e.preventDefault();
        addClimb(climbs => [...climbs, grade])
    }

    const boulderSelectionChoices = {
        "V0-V5": createRangeButtonList(range(6, 0), 'V', addBoulderOrRoute),
        "V6-V10": createRangeButtonList(range(5, 6), 'V', addBoulderOrRoute),
        "V11-V16": createRangeButtonList(range(6, 11), 'V', addBoulderOrRoute),
    }

    const boulderRangeChoices = [
        <button key={"V0-V5"} onClick={(e) => { e.preventDefault(); setBoulderSelection("V0-V5")}}>V0-V5</button>,
        <button key={"V6-V10"} onClick={(e) => { e.preventDefault(); setBoulderSelection("V6-V10")}}>V6-V10</button>,
        <button key={"V11-V16"} onClick={(e) => { e.preventDefault(); setBoulderSelection("V11-V16")}}>V11-V16</button>
    ];

    const routeRangeChoices = [
        <button key={"5.0-5.9"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.0-5.9")}}>5.0-5.9</button>,
        <button key={"5.10-5.11"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.10-5.11")}}>5.10-5.11</button>,
        <button key={"5.12-5.13"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.12-5.13")}}>5.12-5.13</button>,
        <button key={"5.14-5.15"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.14-5.15")}}>5.14-5.15</button>
    ];

    const letterGrades = ['a','b','c','d'];
    

    const routeSelectionChoices = {
        "5.0-5.9": createRangeButtonList(range(10, 0), '5.', addBoulderOrRoute),
        "5.10-5.11": createRangeButtonList(rangeWithChars(2, 10, letterGrades), '5.', addBoulderOrRoute),
        "5.12-5.13": createRangeButtonList(rangeWithChars(2, 12, letterGrades), '5.', addBoulderOrRoute),
        "5.14-5.15": createRangeButtonList(rangeWithChars(2, 14, letterGrades), '5.', addBoulderOrRoute),
    }


    return(
        <Fragment>
            <h4>Add a {type}</h4>
            { type == "boulder" ? boulderRangeChoices : routeRangeChoices }
            <br></br>
            { boulderSelection ? boulderSelectionChoices[boulderSelection] : null }
            { routeSelection ? routeSelectionChoices[routeSelection] : null}
        </Fragment>
    );
}

