import React, { Fragment, useState } from "react";
import { useHistory } from "react-router-dom";
import { Button, Input, Label } from 'semantic-ui-react'

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
            {error ? errorDiv : <div></div>}
            <form onSubmit={(e) => submitLogin(e)}>
                <Label>Username or Email: </Label>
                <Input type="text" value={usernameOrEmail} onChange={(e) => setUsernameOrEmail(e.target.value)} />
                <br />
                <Label>Password: </Label>
                <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <br />
                <Button type="submit"> Log In </Button>
            </form>
        </Fragment>
    )
};