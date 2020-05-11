import React, { useState, useEffect } from "react";
import { Dropdown } from 'semantic-ui-react'


import Histogram from "./Histograms";
import { getRequest } from "../util/request";
import { getUserId } from '../util/jwt';

export default () => {
    const [dateFilter, setDateFilter] = useState("year");
    const [climbs, setClimbs] = useState([]);
    const [error, setError] = useState('');

    const fetchClimbs = () => {
        const userId = getUserId();
        getRequest(`/user/${userId}/workouts`,
            { "dateFilter": dateFilter }
            ).then(json => {
            console.log("json from fetch", json);
            if (!json || json.status_code != 200) {
                setError('Something bad happened');
            } else {
                // console.log(json);
                // setClimbs(json);
            }
        })
    }

    useEffect(() => fetchClimbs(), [dateFilter]);

    return (
        <div>
            <h1>Dashboard coming here</h1>
            <Dropdown text={`Show Climbs for ${dateFilter}`}> 
                <Dropdown.Menu>
                    <Dropdown.Item text='This Month' onClick={() => setDateFilter('month')} />
                    <Dropdown.Item text='This Year' onClick={() => setDateFilter('year')} />
                </Dropdown.Menu>
            </Dropdown>
            {/* {error ? <div>{error}</div> : null} */}
            {/* Dropdown should send one of the following query params: "week" for week, "month" for month, "year" for year */}
            <Histogram />
        </div>    
    )
};