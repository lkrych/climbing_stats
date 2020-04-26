import React, { useState } from "react";
import { postRequest } from "../util/request";

export default () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const submitSignup = (e) => {
        e.preventDefault();
        postRequest("/users",
            {
                username,
                email,
                password
            }
        ).then((json) => {
            // For Tati to do
            console.log(json);
        });
    }

    return (
        <form onSubmit={(e) => submitSignup(e)}>
            <label>Username: </label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
            <br />
            <label>Email: </label>
            <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
            <br />
            <label>Password: </label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit"> Sign Up </button>
        </form>
    )
};