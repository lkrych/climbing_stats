import React, { Fragment } from "react";
import { NavLink } from "react-router-dom";
import { Container, Header, Icon, Button } from 'semantic-ui-react'
import "../../index.css";

export default ({ setShowSignup, mobile }) => {
    return (
        <Fragment>
            <div className="background-container">
                <Container fluid >
                    <h1 className="splash-header-desktop">
                        Climbing Stats
                    </h1>
                    <h2 className="splash-secondary-desktop">
                        Simple logging for your climbs
                    </h2>
                    <NavLink to="/signup">
                        <Button 
                            onClick={() => setShowSignup(false)} 
                            color='orange' 
                            size='huge'
                            style={{
                                marginLeft: '10vw'
                            }}
                        >
                            Sign up
                            <Icon name='right arrow' />
                        </Button>
                    </NavLink>
                </Container>
            </div>
        </Fragment>
    );
};