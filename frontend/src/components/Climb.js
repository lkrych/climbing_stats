import React, { useState, Fragment } from "react";

export default ({type, grade, index, removeFromArray}) => {

    return(
        <Fragment>
            <div onClick={(e) => removeFromArray(e, type, index)}>
                {type == 'boulder' ? `V${grade}` : `5.${grade}`}
            </div>
        </Fragment>
    );
}