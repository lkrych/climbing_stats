import React, { useState, Fragment } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { Button, Form, Segment, Header, Grid, Divider, Icon } from 'semantic-ui-react'


import AddClimbs from "./AddClimbs";
import { postRequest } from '../util/request';
import { getUserId } from '../util/jwt';

export default () => {
    const [date, setDate] = useState(new Date());
    const [boulders, setBoulders] = useState([]);
    const [routes, setRoutes] = useState([]);
    const [message, setMessage] = useState('');

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
                    date: date.getTime() / 1000, //for proper timestamp
                    boulders,
                    routes
                }
            ).then((json) => {
                console.log(json);
                if (json.status_code == 200) {
                    setBoulders([]);
                    setRoutes([]);
                    setMessage('Your workout was added!')
                    setDate(new Date())
                } else {
                    setMessage(json.msg);
                }
            });
    }

    

    return (
        <Fragment>
            <Grid textAlign='center' style={{ height: '100vh'}} verticalAlign='middle'>
                <Grid.Column style={{ maxWidth: '85vw' }}>
                    { message ? <div>{message}</div> : null }
                    <Header as='h2' color='orange' textAlign='left'>
                        Enter your climbs
                    </Header>
                    <Form onSubmit={(e) => submitWorkout(e)}>
                        <Segment raised textAlign='left'>
                            <Icon size="big" name="calendar" color='orange'/>
                            <DatePicker
                                selected={date}
                                onChange={(e) => handleDateChange(e)}
                            />
                            <Divider></Divider>
                            <AddClimbs
                                boulders={boulders}
                                setBoulders={setBoulders}
                                routes={routes}
                                setRoutes={setRoutes}
                                removeFromArray={removeFromArray}
                            />
                            <Divider></Divider>
                            <Button type="submit" color='orange' size='large'> Enter Workout </Button>
                        </Segment>
                    </Form>
                </Grid.Column>

            </Grid>
        </Fragment>  
    )
};