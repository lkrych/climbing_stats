import React from "react";

import Histogram from "./Histograms";

export default () => {
    return (
        <div>
            <h1>Dashboard coming here</h1>
            {/* Dropdown should send one of the following query params: "week" for week, "month" for month, "year" for year */}
            <Histogram />
        </div>    
    )
};