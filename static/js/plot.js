function initializeViz() {
    // JS object that points at empty div in the html
    let placeholderDiv = document.getElementById("tableauViz");
    // URL of the viz to be embedded
    let url = "https://prod-useast-b.online.tableau.com/t/22bipp22/views/tableau_practice/Obesity?:showAppBanner=false&:display_count=n&:showVizHome=n&:origin=viz_share_link";
    // An object that contains options specifying how to embed the viz
    let options = {
      width: '600px',
      height: '600px',
      hideTabs: true,
      hideToolbar: true,
    };
    viz = new tableau.Viz(placeholderDiv, url, options);
  }
  
initializeViz()