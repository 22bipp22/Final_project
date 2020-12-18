//load in json data 
// loop through data
//This function generates 14 random numbers and loads them into a table on the 
  // webpage. Will need to add functionality to run those horse numbers through the model. 
  function randomRace() {  
    const url = "/dataset";
    d3.json(url).then(function(response) {
      
      let raceData = response
      console.log(raceData)
      
      let sortedRace = raceData.sort((a, b) => parseFloat(a.finish_time) - parseFloat(b.finish_time));

      console.log(sortedRace)
      // horseNumbers = []
  
      // for(let i = 0; i < 14; i++) {
  
      //   randomNumber =  Math.round(Math.random()*(4405 - 1) +1)
      //   horseNumbers[i] = randomNumber  
         
      // }
      
      // Create the Table Header Row
      let webBody = d3.select("body");

      let declareWinner = d3.select("#winner")
      if (sortedRace[0].horse_id == 3992) {
      
        declareWinner.text("CONGRATULATIONS!! Your horse is the WINNER!")
                    .attr("style", "text-align: center; width: 100%")

      }
      else {

        declareWinner.text("Horse Number " + sortedRace[0].horse_id + " is the WINNER!")
                    .attr("style", "text-align: center; width: 100%")

      }

      let table = webBody.append("table")
      table.attr("style", "margin: 20px; width: 100%")
         
      
      let thead = table.append("thead")
      let trow = thead.append("tr")
      let header = trow.append("th")
      header.text("Place")
            .attr("style", "width: 33.3%; text-align: center")
            
      let header2 = trow.append("th")
      header2.text("Horse Number")
            .attr("style", "width: 33.3%; text-align: center")
            
      let header3 = trow.append("th")
      header3.text("Finish Time")
            .attr("style", "width: 33.3%; text-align: center")
  
    //   // Populate the table data
      let tableBody = table.append("tbody")
     
      let places = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th"]
    
      // Iterate through the sorted horse race data to display the race results in the order they placed
        for(let i = 0; i < sortedRace.length; i++) {

            
          let row = tableBody.append('tr');
          
          let cell = row.append('td');
          cell.text(places[i])
              .attr("style", "text-align: center");
            
          let cell2 = row.append('td')
          if (sortedRace[i].horse_id == 3992) {
                  
            cell2.text("Your horse")
                .attr("style", "text-align: center");

          }
          else {
            cell2.text(sortedRace[i].horse_id)
                .attr("style", "text-align: center");
          }

          let cell3 = row.append('td')
          cell3.text(sortedRace[i].finish_time)
              .attr("style", "text-align: center");
          
             
          }
           
          let svgWidth = window.innerWidth;
          let svgHeight = "400px";
    
          let imagepath = "../static/data/Generic_track.jpg" 
          webBody.append("img")
                  .attr("width", svgWidth)
                  .attr("height", svgHeight)
                  .attr("src", imagepath)
                  .attr("style", "padding: 50px")
    
          
      });  

     
    
    
  
  } 
   


randomRace();