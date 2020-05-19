import React, { Fragment } from "react";
import { Button } from 'semantic-ui-react'

export default ({type, grade, index, removeFromArray}) => {
    let style = '';
    let display = '';
    if (type == 'boulder') {
        display = `V${grade}`;
        style = `V${grade} color-button-text button-margin`;
    } else {
        display = `5.${grade}`;
        style = `five-${grade} color-button-text button-margin`;
    }
    return(
        <Fragment>
            <Button 
                className={style} 
                size="tiny"
                onClick={(e) => removeFromArray(e, type, index)}>
                {display}
            </Button>
        </Fragment>
    );
}