import React, { useState, Fragment } from "react";

import { range } from "../util/util";
import AddClimbs from "./AddClimbs";

export default ({type, addClimb, climbs}) => {
    const [boulderSelection, setBoulderSelection] = useState(null);
    const [routeSelection, setRouteSelection] = useState(null);
    const [letterGradeSelection, setLetterGradeSelection] = useState(null);

    const createRangeButtonList = (range = [], buttonInput, clickFunction) => {
        return range.map((n) => <button key={n} onClick={(e) => clickFunction(e, n)}>{buttonInput}{n}</button>, range)
    }

    const addBoulder = (e, grade) => {
        e.preventDefault();
        addClimb(...climbs, grade)
    }

    const addRoute = (e, grade) => {
        e.preventDefault();
        addClimb(...climbs, `${grade}${letterGradeSelection}`);
    }

    const boulderSelectionChoices = {
        "V0-V5": createRangeButtonList(range(6, 0), 'V', addBoulder),
        "V6-V10": createRangeButtonList(range(5, 6), 'V', addBoulder),
        "V11-V16": createRangeButtonList(range(6, 11), 'V', addBoulder),
    }

    const boulderRangeChoices = [
        <button key={"V0-V5"} onClick={(e) => { e.preventDefault(); setBoulderSelection("V0-V5")}}>V0-V5</button>,
        <button key={"V6-V10"} onClick={(e) => { e.preventDefault(); setBoulderSelection("V6-V10")}}>V6-V10</button>,
        <button key={"V11-V16"} onClick={(e) => { e.preventDefault(); setBoulderSelection("V11-V16")}}>V11-V16</button>
    ];

    const routeSelectionChoices = {
        "5.0-5.9": createRangeButtonList(range(9, 0), '5.', addRoute),
        "5.10-5.12": createRangeButtonList(range(3, 10), '5.', addRoute),
        "5.13-5.15": createRangeButtonList(range(3, 13), '5.', addRoute),
    }

    const routeRangeChoices = [
        <button key={"5.0-5.9"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.0-5.9")}}>5.0-5.9</button>,
        <button key={"5.10-5.12"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.10-5.12")}}>5.10-5.12</button>,
        <button key={"5.13-5.15"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.13-5.15")}}>5.13-5.15</button>
    ];

    const letterGradeSelectionChoices = [
        <button key={"a"} onClick={(e) => { e.preventDefault(); setRouteSelection("a")}}>a</button>,
        <button key={"b"} onClick={(e) => { e.preventDefault(); setRouteSelection("b")}}>b</button>,
        <button key={"c"} onClick={(e) => { e.preventDefault(); setRouteSelection("c")}}>c</button>,
        <button key={"d"} onClick={(e) => { e.preventDefault(); setRouteSelection("d")}}>d</button>
    ]



    return(
        <Fragment>
            <h4>Add a {type}</h4>
            { type == "boulder" ? boulderRangeChoices : routeRangeChoices }
            <br></br>
            { boulderSelection ? boulderSelectionChoices[boulderSelection] : null }
            { routeSelection ? routeSelectionChoices[routeSelection] : null}
            <br></br>
            { routeSelection && routeSelection != "5.0-5.9" ? letterGradeSelectionChoices : null}
        </Fragment>
    );
}

