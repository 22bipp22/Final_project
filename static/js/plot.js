function initializeViz() {
    // JS object that points at empty div in the html
    let placeholderDiv = document.getElementById("tableauViz");
    // URL of the viz to be embedded
    let url = "http://public.tableau.com/views/Top10StationsDashboard_16062498361870/Top10Stations";
    // An object that contains options specifying how to embed the viz
    let options = {
      width: '1000px',
      height: '1000px',
      hideTabs: true,
      hideToolbar: true,
    };
    viz = new tableau.Viz(placeholderDiv, url, options);
  }
  
initializeViz()