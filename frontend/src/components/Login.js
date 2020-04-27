import React, { Fragment, useState } from "react";
import { postRequest } from "../util/request";

export default ({ setLoggedIn }) => {
    const [usernameOrEmail, setUsernameOrEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('')

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
                sessionStorage.setItem('jwt', json.access_token);
                setLoggedIn(true);
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
                <label>Username or Email: </label>
                <input type="text" value={usernameOrEmail} onChange={(e) => setUsernameOrEmail(e.target.value)} />
                <br />
                <label>Password: </label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit"> Log In </button>
            </form>
        </Fragment>
    )
};