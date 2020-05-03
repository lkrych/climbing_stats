import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

export default () => {
    const leftContainer = useRef(null);
    const rightContainer = useRef(null); //useRef hook creates a variable that holds on to a value throughout rendering
    const data = [{ grade: "9", value: 1 }, { grade: "10a", value: 3 }, { grade: "10b", value: 4 }, { grade: "10c", value: 6 }, { grade: "10d", value: 3 }, { grade: "11a", value: 2 }, { grade: "11b", value: 3 }, { grade: "11c", value: 2 }, { grade: "11d", value: 1 }, { grade: "12a", value: 1 }];

    useEffect(() => {
        if (data && rightContainer.current) {
            // drawLeftChart(data);
            drawRightChart(data);  
        }
    }, [data, rightContainer.current])

    //replace this object with a regex function that handles various cases and returns appropriate hex
    const barColors = {
        "9": "#FFC300",
        "10a": "#FFC300",
        "10b": "#FFC300",
        "10c": "#FFC300",
        "10d": "#FFC300",
        "11a": "#FF5733",
        "11b": "#FF5733",
        "11c": "#FF5733",
        "11d": "#FF5733",
        "12a": "#C70039"
    };

    //adapted from the following tutorials: https://observablehq.com/@d3/horizontal-bar-chart#data
    // https://codepen.io/tfaramar/pen/qBOVbQO?editors=1010
    // const drawLeftBarChart = (data) => {
    //     const barHeight = 20;
    //     const margin = ({ top: 10, right: 20, bottom: 30, left: 10 });
    //     const height = Math.ceil((data.length + 0.1) * barHeight) + margin.top + margin.bottom;
    //     const width = 500;

    //     const x = d3.scaleLinear()
    //         .domain([0, d3.max(data, d => d.value)])
    //         .range([margin.left, width - margin.right]);

    //     const y = d3.scaleBand()
    //         .domain(d3.range(data.length))
    //         .rangeRound([margin.top, height - margin.bottom])
    //         .padding(0.1);

    //     const xAxis = g => g
    //         .attr("transform", `translate(0, ${height - margin.bottom})`)
    //         .call(d3.axisBottom(x).ticks(width / 80, data.format))
    //         .call(g => g.select(".domain").remove()); //removes tick line

    //     const yAxis = g => g
    //         .attr("transform", `translate(${margin.left}, 0)`)
    //         .call(d3.axisRight(y).tickFormat(i => data[i].grade).tickSize(0))
    //         .call(g => g.select(".domain").remove());

    //     const format = x.tickFormat(1, data.format);

    //     const svgCanvas = d3.select(rightContainer.current)
    //         .append("svg")
    //         .attr("viewBox", [0, 0, width, height])
    //         .style("border", "1px solid red");

    //     svgCanvas.append("g")
    //         .attr("fill", "orange")
    //         .selectAll("rect")
    //         .data(data)
    //         .join("rect")
    //         .attr("x", x(0))
    //         .attr("y", (d, i) => y(i))
    //         .attr("width", d => x(d.value) - x(0))
    //         .attr("height", y.bandwidth());

    //     // Uncomment the below to add values (floats) to bars
    //     // svgCanvas.append("g")
    //     //     .attr("fill", "red")
    //     //     .attr("text-anchor", "end")
    //     //     .attr("font-family", "san-serif")
    //     //     .attr("font-size", 12)
    //     //     .selectAll("text")
    //     //     .data(data)
    //     //     .join("text")
    //     //         .attr("x", d => x(d.value) + 10)
    //     //         .attr("y", (d, i) => y(i) + y.bandwidth() / 2)
    //     //         .attr("dy", "0.35em")
    //     //         .text(d => format(d.value));

    //     svgCanvas.append("g")
    //         .call(xAxis);

    //     svgCanvas.append("g")
    //         .call(yAxis);

    //     return svgCanvas.node();
    // }


    const drawRightChart = (data) => {
        const barHeight = 20;
        const margin = ({ top: 10, right: 20, bottom: 30, left: 10 });
        const height = Math.ceil((data.length + 0.1) * barHeight) + margin.top + margin.bottom;
        const width = 500;
      
        const x = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.value)])
            .range([margin.left, width - margin.right]);
        
        const y = d3.scaleBand()
            .domain(d3.range(data.length))
            .rangeRound([margin.top, height - margin.bottom])
            .padding(0.1);

        const xAxis = g => g
            .attr("transform", `translate(0, ${height - margin.bottom})`)
            .call(d3.axisBottom(x).ticks(width / 80, data.format).tickSize(4))
            .call(g => g.select(".domain").remove()); //removes tick line

        const yAxis = g => g
            .attr("transform", `translate(${margin.left}, 0)`)
            .call(d3.axisRight(y).tickFormat(i => data[i].grade).tickSize(0))
            .call(g => g.select(".domain").remove()); 

        const svgCanvas = d3.select(rightContainer.current)
            .append("svg")
            .attr("viewBox", [0, 0, width, height])
            .style("border", "1px solid red");

        svgCanvas.append("g")
            .selectAll("rect")
            .data(data)
            .join("rect")
                .attr("x", x(0))
                .attr("y", (d, i) => y(i))
                .attr("fill", d => barColors[d.grade]) //create object to map colors 
                .attr("width", d => x(d.value) - x(0))
                .attr("height", y.bandwidth());

        svgCanvas.append("g")
            .call(xAxis);

        svgCanvas.append("g")
            .call(yAxis)
            .attr("font-family", "sans-serif"); //font style for y-axis grades

        console.log(svgCanvas.node());
        return svgCanvas.node();
    }

    return (
        <div className="d3-container">
            <div ref={leftContainer}></div>
            <div ref={rightContainer}></ div>
        </div>
        
    )
}