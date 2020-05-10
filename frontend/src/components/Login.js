import React, { Fragment, useState } from "react";
import { useHistory } from "react-router-dom";
import { Button, Form, Grid, Header, Segment } from 'semantic-ui-react'

import { postRequest } from "../util/request";

export default ({ setLoggedIn }) => {
    const [usernameOrEmail, setUsernameOrEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    let history = useHistory();

    const submitLogin = (e) => {
        e.preventDefault();

        //clear input
        const username = usernameOrEmail;
        const pass = password;
        setUsernameOrEmail('');
        setPassword('');

        
        postRequest("/login",
            {
                "username": username,
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
    
    const errorDiv = (<div className="login-error">
        There was a problem with your credentials. Please try again.
    </div>);

    return (
        <Fragment>
            <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
                <Grid.Column style={{ maxWidth: 450 }}>
                    <Header as='h2' color='orange' textAlign='center'>
                        Login to your account
                    </Header>
                    {error ? errorDiv : <div></div>}
                    <Form onSubmit={(e) => submitLogin(e)}>
                        <Segment stacked>
                            <Form.Input 
                                fluid icon='user' 
                                iconPosition='left' 
                                placeholder='E-mail address or Username' 
                                value={usernameOrEmail} 
                                onChange={(e) => setUsernameOrEmail(e.target.value)} 
                            />
        
                            <Form.Input
                                fluid
                                icon='lock'
                                iconPosition='left'
                                placeholder='Password'
                                type='password'
                                value={password} 
                                onChange={(e) => setPassword(e.target.value)}
                            />
                            <br />
                            <Button type="submit" color='orange' fluid size='large'> Login </Button>
                        </Segment>
                    </Form>
                </Grid.Column>
            </Grid>
        </Fragment>
    )
};