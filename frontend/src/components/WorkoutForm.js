import React, { useState, Fragment } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { Button, Form, Segment, Header, Grid, Divider, Icon, TextArea } from 'semantic-ui-react';

import { CharCount } from '../styled/styled_components';
import AddClimbs from "./AddClimbs";
import { postRequest } from '../util/request';
import { getUserId } from '../util/jwt';

export default () => {
    const [date, setDate] = useState(new Date());
    const [boulders, setBoulders] = useState([]);
    const [routes, setRoutes] = useState([]);
    const [message, setMessage] = useState('');
    const [notes, setNotes] = useState('');
    //pass props to char count to turn red at 300 chars

    const handleDateChange = date => {
        setDate(date)
    };

    const handleNotesChange = e => {
        setNotes(e.currentTarget.value);
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
    };



    const submitWorkout = (e) => {
        e.preventDefault();
        const userId = getUserId();
        postRequest(`/user/${userId}/workouts`,
                {
                    date: date.getTime() / 1000, //for proper timestamp
                    boulders,
                    routes,
                    notes
                }
            ).then((json) => {
                if (json.status_code == 200) {
                    setBoulders([]);
                    setRoutes([]);
                    setNotes('');
                    setMessage('Your workout was added!')
                    setDate(new Date())
                } else {
                    setMessage(json.msg);
                }
            });
    }

    const exceedChars = notes.length > 300;

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
                            <TextArea placeholder='How was your workout?' value={notes} onChange={(e) => handleNotesChange(e)}/>
                            <CharCount exceedChars={exceedChars}>{notes.length} out of 300</CharCount>
                            <Divider></Divider>
                            <Button disabled={exceedChars} type="submit" color='orange' size='large'> Enter Workout </Button>
                        </Segment>
                    </Form>
                </Grid.Column>

            </Grid>
        </Fragment>  
    )
};