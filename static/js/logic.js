//load in json data 
// loop through data
//This function generates 14 random numbers and loads them into a table on the 
  // webpage. Will need to add functionality to run those horse numbers through the model. 
  function randomRace() {  
    const url = "/dataset";
    d3.json(url).then(function(response) {
      
      let raceData = response
      console.log(raceData)
  
      // horseNumbers = []
  
      // for(let i = 0; i < 14; i++) {
  
      //   randomNumber =  Math.round(Math.random()*(4405 - 1) +1)
      //   horseNumbers[i] = randomNumber  
         
      // }
      
      // Create the Table Header Row
      let webBody = d3.select("body");
      let table = webBody.append("table")
      table.attr("style", "margin: 20px; width: 100%")
         
      
      let thead = table.append("thead")
      let trow = thead.append("tr")
      let header = trow.append("th")
      header.text("Horse Number")
            .attr("style", "width: 20%; text-align: center")
            
      let header2 = trow.append("th")
      header2.text("Race Distance")
            .attr("style", "width: 20%; text-align: center")
            
      let header3 = trow.append("th")
      header3.text("Place Odds")
            .attr("style", "width: 20%; text-align: center")
            
      let header4 = trow.append("th")
      header4.text("Result")
            .attr("style", "width: 20%; text-align: center")
           
      let header5 = trow.append("th")
      header5.text("Winner")
            .attr("style", "width: 20%; text-align: center")
  
    //   // Populate the table data
      let tableBody = table.append("tbody")
     
      
    // Loop through the randomly generated horse numbers to populate the table
      // horseNumbers.forEach((number) => {
        // search through the data for matching horse numbers and populate table with the data found 
        for(let i = 0; i < raceData.length; i++) {
            // if (number == raceData[i].horse_id) {
              let row = tableBody.append('tr');
              let cell = row.append('td');
              cell.text(raceData[i].horse_id)
                  .attr("style", "text-align: center");
              // let cell2 = row.append('td')
              // cell2.text(raceData[i].race_id)
              //     .attr("style", "text-align: center");
              let cell3 = row.append('td')
              cell3.text(raceData[i].distance)
                  .attr("style", "text-align: center");
              let cell4 = row.append('td')
              cell4.text(raceData[i].place_odds)
                  .attr("style", "text-align: center");
              let cell5 = row.append('td')
              cell5.text(raceData[i].race_id)
                  .attr("style", "text-align: center");
              let cell6 = row.append('td')
              // Check to see if the horse won or lost the race and populate accordingly
              if (raceData[i].won == 0) { 
                cell6.text("Lost")
                  .attr("style", "text-align: center");
              }
                else {
                  cell6.text("Won")
                      .attr("style", "text-align: center");
                }
            }
          // }
          let svgWidth = window.innerWidth;
          let svgHeight = "400px";
    
          let imagepath = "../static/data/Generic_track.jpg" 
          webBody.append("img")
                  .attr("width", svgWidth)
                  .attr("height", svgHeight)
                  .attr("src", imagepath)
                  .attr("style", "padding: 50px")
    
          
      });  

     
    
    // });
  
  } 
   


randomRace();