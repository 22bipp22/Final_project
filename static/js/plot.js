function initializeViz() {
    // JS object that points at empty div in the html
    let placeholderDiv = document.getElementById("tableauViz");
    let placeholderDiv2 = document.getElementById("tableauViz2");
    // URL of the viz to be embedded
    let url = "http://public.tableau.com/views/off_to_the_races/Offtotheraces";
    let url2 = "http://public.tableau.com/views/race_track/Racetrack";
    // An object that contains options specifying how to embed the viz
    let options = {
      width: '1000px',
      height: '1000px',
      hideTabs: true,
      hideToolbar: true,
    };
    viz = new tableau.Viz(placeholderDiv, url, options);
    viz2 = new tableau.Viz(placeholderDiv2, url2, options);

}
  
initializeViz()