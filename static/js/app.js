/// This function puts a random circle to hold SVG area in case
///  we want to use it later. 
function buildPlot() {

 let svgWidth = window.innerWidth;
 let svgHeight = "400px";

 let imagepath = "../static/data/consumption_bar.png" 
 let svg = d3.select("#svg-area").append("img")
    .attr("width", svgWidth)
    .attr("height", svgHeight)
    .attr("src", imagepath);

    
  };

buildPlot();
