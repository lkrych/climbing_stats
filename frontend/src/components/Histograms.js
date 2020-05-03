import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

export default () => {
    const d3Container = useRef(null); //useRef hook creates a variable that holds on to a value throughout rendering
    const data = [4, 8, 15, 17, 24, 4];

    useEffect(() => {
        if (data && d3Container.current) {
            drawBarChart(data);
        }
    }, [data, d3Container.current])

    const drawBarChart = (data) => {
        const height = 400;
        const width = 600;
        const scale = 5;
        const svgCanvas = d3.select(d3Container.current)
            .append("svg")
            .attr("viewBox", [0, 0, width, height])
            .style("border", "1px solid red");

        svgCanvas.append("g")
            .attr("fill", "orange")
            .selectAll("rect")
            .data(data)
            .join("rect")
                .attr("x", x(0))
                .attr("y", (d, i) => y(i))
                .attr("width", d => x(d) - x(0))
                .attr("height", y.bandwidth());

        svgCanvas.append("g")
            .call(xAxis);

        svgCanvas.append("g")
            .call(yAxis);

        return svgCanvas.node();
        
        // svgCanvas.selectAll("rect")
        //     .data(data).enter()
        //     .append("rect")
        //     .attr("width", 30) //width of bars
        //     .attr("height", (datapoint) => datapoint * scale)
        //     .attr("fill", "orange")
        //     .attr("x", (datapoint, iteration) => iteration * 35)
        //     .attr("y", (datapoint) => canvasHeight - datapoint * scale)
    }

    return (
        <div
            className="d3-container"
            ref={d3Container}
        ></ div>
    )
}