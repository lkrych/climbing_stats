import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

export default (props) => {
    const d3Container = useRef(null); //useRef hook creates a variable that holds on to a value throughout rendering

    useEffect(() => {
        // if (props.data && d3Container.current) {
        //     const svg = d3.select(d3Container.current);


        // }
    }, [props.data, d3Container.current])

    return (
        <svg
            className="d3-container"
            width={500}
            height={400}
            ref={d3Container}
        />
    )
}