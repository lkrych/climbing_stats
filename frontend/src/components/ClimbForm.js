import React, { useState, Fragment } from "react";

import { range, rangeWithChars } from "../util/util";

export default ({type, addClimb, climbs}) => {
    const [boulderSelection, setBoulderSelection] = useState(null);
    const [routeSelection, setRouteSelection] = useState(null);

    const createRangeButtonList = (range = [], buttonInput, clickFunction) => {
        return range.map((n) => <button key={n} onClick={(e) => clickFunction(e, n)}>{buttonInput}{n}</button>, range)
    }

    const addBoulder = (e, grade) => {
        e.preventDefault();
        addClimb(climbs => [...climbs, { 'grade': grade }])
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

    const routeRangeChoices = [
        <button key={"5.0-5.9"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.0-5.9")}}>5.0-5.9</button>,
        <button key={"5.10-5.11"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.10-5.11")}}>5.10-5.11</button>,
        <button key={"5.12-5.13"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.12-5.13")}}>5.12-5.13</button>,
        <button key={"5.14-5.15"} onClick={(e) => { e.preventDefault(); setRouteSelection("5.14-5.15")}}>5.14-5.15</button>
    ];

    const letterGrades = ['a','b','c','d'];
    
    const addRoute = (e, grade) => {
        e.preventDefault();

        let numberGrade = null;
        let letterGrade = null;
        if( typeof(grade) == 'string') {
            let letterSplit = grade.split(/([abcd])/);
            if (letterSplit.length > 1) {
                numberGrade = letterSplit[0];
                letterGrade = letterSplit[1];
            }
        } else { // for 5.0-5.9
            numberGrade = grade;
        }
       
        addClimb(climbs => [...climbs, { 'grade': numberGrade, 'letterGrade': letterGrade }]);
    }
    const routeSelectionChoices = {
        "5.0-5.9": createRangeButtonList(range(10, 0), '5.', addRoute),
        "5.10-5.11": createRangeButtonList(rangeWithChars(2, 10, letterGrades), '5.', addRoute),
        "5.12-5.13": createRangeButtonList(rangeWithChars(2, 12, letterGrades), '5.', addRoute),
        "5.14-5.15": createRangeButtonList(rangeWithChars(2, 14, letterGrades), '5.', addRoute),
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

