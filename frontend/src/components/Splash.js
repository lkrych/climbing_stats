import React, { Fragment } from "react";
import { NavLink } from "react-router-dom";

import { Container, Header } from 'semantic-ui-react';
import { Button, MainHeader, SubHeader, Text } from '../styled/styled_components';

export default ({ setShowSignup }) => {
    return ( 
        <Fragment>
            <div className="background-container">
                <Container fluid >
                    <div className="splash-content">
                        <MainHeader>
                            Reach your climbing goals with Pinnacle
                        </MainHeader>
                        <SubHeader>
                                Simple logging for your gym climbs
                        </SubHeader>
                        <NavLink to="/signup">
                            <Button
                                onClick={() => setShowSignup(false)}>
                                Sign up
                            </Button>
                        </NavLink>
                    </div>
                    <div className="about">
                        <Text>
                            A description of this service.
                        </Text>
                    </div>
                </Container>
            </div>
        </Fragment>
    );
};