import React, { useState } from "react";
import { postRequest } from "../util/request";

export default () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const submitLogin = (e) => {
        e.preventDefault();
        postRequest("/auth",
            {
                username,
                password
            }
        ).then((json) => {
            console.log(json);
        });
    }

    return (
        <form onSubmit={(e) => submitLogin(e)}>
            <label>Username: </label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
            <br />
            <label>Password: </label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit"> Log In </button>
        </form>
    )
};