import React, { useState, Fragment } from "react";
import { Button, Form, Grid, Header, Segment } from 'semantic-ui-react'
import { useHistory } from "react-router-dom";
import { postRequest } from "../util/request";

export default ({setLoggedIn}) => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [passError, setPassError] = useState('');
    let history = useHistory();

    const submitSignup = (e) => {
        e.preventDefault();
        if (!validatePassword(password)) {
            console.log('invalid password');
            setPassError('Your password must be at least six characters long and include at least one special character, and one number.')
        } else {
            const usern = username;
            const pass = password;
            const em = email;
            setEmail('');
            setUsername('');
            setPassword('');
            setPassError('');
            postRequest("/users",
                {
                    "username": usern,
                    "email": em,
                    "password": pass
                }
            ).then((json) => {
                console.log(json);
                if (!json.access_token) {
                    setError(json.description);
                } else {
                    setError('');
                    localStorage.setItem('jwt', json.access_token);
                    setLoggedIn(true);
                    history.push("/dashboard");
                }
            });
        } 
    }

    const validatePassword = (password) => {
        console.log("checkin' password!")
        let specialChars = "~!@#$%^&*()_+`{}[];:'<>?/,.";
        let nums = "1234567890";

        let hasNum = false;
        let hasSpec = false;
        for (let char of password) {
            if (specialChars.includes(char)) hasSpec = true;
            if (nums.includes(char)) hasNum = true;
        }
        
        if (password.length <= 6 || hasSpec === false || hasNum === false) {
            return false;
        } else {
            return true;
        }
    }

    const passErrorMessage = (
        <p>{passError}</p>
    )

    const errorDiv = (<div className="signup-error">
        There was a problem with your credentials. Please try again.
    </div>);

    return (
        <Fragment>
            <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
                <Grid.Column style={{ maxWidth: 450 }}>
                    <Header as='h2' color='orange' textAlign='center'>
                        Sign up for Climbing Stats
                    </Header>
                    {error ? errorDiv : <div></div>}
                    <Form onSubmit={(e) => submitSignup(e)}>
                        <Segment raised>
                            <Form.Input 
                                fluid icon='user' 
                                iconPosition='left' 
                                placeholder='Username' 
                                value={username} onChange={(e) => setUsername(e.target.value)} 
                            />
                            <Form.Input 
                                fluid icon='mail' 
                                iconPosition='left' 
                                placeholder='E-mail' 
                                value={email} onChange={(e) => setEmail(e.target.value)} 
                            />
                            {passError ? passErrorMessage : null}
                            <Form.Input
                                fluid
                                icon='lock'
                                iconPosition='left'
                                placeholder='Password'
                                type='password'
                                required
                                value={password} 
                                onChange={(e) => setPassword(e.target.value)}
                            />
                            <Button type="submit" color='orange' fluid size='large'> Sign up </Button>
                        </Segment>
                    </Form>
                </Grid.Column>
            </Grid>
        </Fragment>
    )
};