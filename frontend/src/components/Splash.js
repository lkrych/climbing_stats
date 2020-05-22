import React, { Fragment } from "react";
import { NavLink } from "react-router-dom";

import { Container, Header } from 'semantic-ui-react';
import { Button, MainHeader } from '../styled/styled_components';

export default ({ setShowSignup }) => {
    return ( 
        <Fragment>
            <div className="background-container">
                <Container fluid >
                    <MainHeader>
                        Reach your climbing goals with Pinnacle
                    </MainHeader>
                    <h2 className="splash-secondary-desktop">
                        Simple logging for your climbs
                    </h2>
                    <NavLink to="/signup">
                        <Button 
                            onClick={() => setShowSignup(false)}>
                            Sign up
                        </Button>
                    </NavLink>
                </Container>
            </div>
        </Fragment>
    );
};