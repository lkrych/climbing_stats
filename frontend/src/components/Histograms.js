import React, { useRef, useEffect } from "react";
import * as d3 from "d3";

export default () => {
    const leftContainer = useRef(null);
    const rightContainer = useRef(null); //useRef hook creates a variable that holds on to a value throughout rendering
    
    const routeData = [{ grade: "9", value: 2 }, { grade: "10a", value: 3 }, { grade: "10b", value: 4 }, { grade: "10c", value: 6 }, { grade: "10d", value: 3 }, { grade: "11a", value: 2 }, { grade: "11b", value: 3 }, { grade: "11c", value: 2 }, { grade: "11d", value: 1 }, { grade: "12a", value: 1 }];
    const boulderData = [{ grade: "V3", value: 6 }, { grade: "V4", value: 3 }, { grade: "V5", value: 4 }, { grade: "V6", value: 2 }];
    // format routeData and boulderData as k/v pairs in histogram data passed in

    useEffect(() => {
        if (routeData && rightContainer.current) {   
            drawRightChart(routeData);  
        }
        if (boulderData && leftContainer.current) {
            drawLeftChart(boulderData);
        }
    }, [routeData, rightContainer.current])

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
        "12a": "#C70039",
        "V3": "green"
    };

    //adapted from the following tutorials: https://observablehq.com/@d3/horizontal-bar-chart#data
    // https://codepen.io/tfaramar/pen/qBOVbQO?editors=1010
    const drawLeftChart = (data) => {
        const barHeight = 20;
        const margin = ({ top: 10, right: 5, bottom: 30, left: 20 });
        const height = Math.ceil((data.length + 0.1) * barHeight) + margin.top + margin.bottom;
        const width = 500;

        const x = d3.scaleLinear()
            .domain([d3.max(data, d => d.value), 0])
            .range([margin.left, width - margin.right]);

        const y = d3.scaleBand()
            .domain(d3.range(data.length))
            .rangeRound([margin.top, height - margin.bottom])
            .padding(0.1);

        const xAxis = g => g
            .attr("transform", `translate(0, ${height - margin.bottom})`)
            .call(d3.axisBottom(x).ticks(width / 100, data.format).tickSize(4))
            .call(g => g.select(".domain").remove()); //removes tick line

        const yAxis = g => g
            .attr("transform", `translate(${width - margin.right}, 0)`)
            .call(d3.axisLeft(y).tickFormat(i => data[i].grade).tickSize(0))
            .call(g => g.select(".domain").remove()); 

        const boulderChart = d3.select(leftContainer.current)
            .append("svg")
            .attr("width", width)
            .attr("viewBox", [0, 0, width, height])
            // .style("border", "1px solid red");

        boulderChart.append("g")
            .selectAll("rect")
            .data(data)
            .join("rect")
            .attr("x", d => x(d.value))
            .attr("y", (d, i) => y(i))
            .attr("fill", d => barColors[d.grade]) //create object to map colors 
            .attr("width", d => x(0) - x(d.value))
            .attr("height", y.bandwidth());

        boulderChart.append("g")
            .call(xAxis);

        boulderChart.append("g")
            .call(yAxis)
            .attr("font-family", "sans-serif"); //font style for y-axis grades

        return boulderChart.node();
    }

    const drawRightChart = (data) => {
        const barHeight = 20;
        const margin = ({ top: 10, right: 20, bottom: 30, left: 5 });
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

        const routeChart = d3.select(rightContainer.current)
            .append("svg")
            .attr("width", width)
            .attr("viewBox", [0, 0, width, height])
            // .style("border", "1px solid red");

        routeChart.append("g")
            .selectAll("rect")
            .data(data)
            .join("rect")
                .attr("x", x(0))
                .attr("y", (d, i) => y(i))
                .attr("fill", d => barColors[d.grade]) //create object to map colors 
                .attr("width", d => x(d.value) - x(0))
                .attr("height", y.bandwidth());

        routeChart.append("g")
            .call(xAxis);

        routeChart.append("g")
            .call(yAxis)
            .attr("font-family", "sans-serif"); //font style for y-axis grades

        return routeChart.node();
    }

    return (
        <div className="d3-container">
            <div ref={leftContainer}></div>
            <div ref={rightContainer}></ div>
        </div>
        
    )
}