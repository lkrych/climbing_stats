import React, { useState, Fragment } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

import AddClimbs from "./AddClimbs";
import { postRequest } from '../util/request';
import { getUserId } from '../util/jwt';

export default () => {
    const [date, setDate] = useState(new Date());
    const [boulders, setBoulders] = useState([]);
    const [routes, setRoutes] = useState([]);

    const handleDateChange = date => {
        setDate(date)
    };

    const removeFromArray = (e, type, index) => {
        e.preventDefault();
        if (type == "route") {
            const copyRoutes = [...routes]
            copyRoutes.splice(index, 1)
            setRoutes(copyRoutes)
        } else {
            const copyBoulders = [...boulders]
            copyBoulders.splice(index, 1)
            setBoulders(copyBoulders)
        }
    }

    const submitWorkout = (e) => {
        e.preventDefault();
        const userId = getUserId();
        postRequest(`/user/${userId}/workouts`,
                {
                    date,
                    boulders,
                    climbs
                }
            ).then((json) => {
                console.log(json);
                if (json.status_code == 200) {
                    
                } else {
                    
                }
            });
    }

    

    return (
        <Fragment>
            <h2>Enter your climbs</h2>
            <form onSubmit={(e) => submitWorkout(e)}>
                <label>Date: </label>
                <DatePicker
                    selected={date}
                    onChange={(e) => handleDateChange(e)}
                />
                <AddClimbs
                    boulders={boulders}
                    setBoulders={setBoulders}
                    routes={routes}
                    setRoutes={setRoutes}
                    removeFromArray={removeFromArray}
                />
                <br />
                
            </form>
        </Fragment>  
    )
};