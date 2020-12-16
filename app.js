/// This function puts a random circle to hold SVG area in case
///  we want to use it later. 
function buildPlot() {

 let svgWidth = window.innerWidth;
 let svgHeight = "100px";

 let svg = d3.select("#svg-area").append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

  
    let chartGroup = svg.append("g")
          .attr("transform", "translate(10, 10)");


    chartGroup.selectAll("circle")
        .data("10")
        .enter()
        .append("circle")
        .attr("cx", "50")
        .attr("cy", "50")
        .attr("r", "40")
        .attr("stroke", "red")
        .attr("stroke-width", "2")
        .attr("opacity", "25%")

    
  };

buildPlot();
