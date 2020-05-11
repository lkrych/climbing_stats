import React, { useState, useEffect } from "react";
import { Dropdown } from 'semantic-ui-react'


import Histogram from "./Histograms";
import { getRequest } from "../util/request";
import { getUserId } from '../util/jwt';
import { explodeClimbsObject } from '../util/util';

export default () => {
    const [dateFilter, setDateFilter] = useState("year");
    const [routes, setRoutes] = useState([]);
    const [boulders, setBoulders] = useState([]);
    const [error, setError] = useState('');

    const fetchClimbs = () => {
        const userId = getUserId();
        getRequest(`/user/${userId}/workouts`,
            { "dateFilter": dateFilter }
            ).then(json => {
            if (!json || json.status_code != 200) {
                setError('Something bad happened');
            } else {
                let routes = {};
                let boulders = {};
                json.workouts.forEach(w => {
                    w.climbs.forEach(c => {
                        if (c.type == "boulder") {
                            if (`V${c.grade}` in boulders) {
                                boulders[`V${c.grade}`] += 1;
                            } else {
                                boulders[`V${c.grade}`] = 1;
                            }
                        } else {
                            if (!c.letter_grade){
                                if (`${c.grade}` in routes) {
                                    routes[`${c.grade}`] += 1;
                                } else {
                                    routes[`${c.grade}`] = 1;
                                }
                            } else {
                                if (`${c.grade}${c.letter_grade}` in routes) {
                                    routes[`${c.grade}${c.letter_grade}`] += 1;
                                } else {
                                    routes[`${c.grade}${c.letter_grade}`] = 1;
                                }
                            }
                        }
                    });
                });
                setBoulders(explodeClimbsObject(boulders, "boulder"));
                setRoutes(explodeClimbsObject(routes));
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
            <Histogram routeData={routes} boulderData={boulders}/>
        </div>    
    )
};