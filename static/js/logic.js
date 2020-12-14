//load in json data 
// loop through data
//This function generates 14 random numbers and loads them into a table on the 
  // webpage. Will need to add functionality to run those horse numbers through the model. 
function randomRace() {  
  const url = "/dataset";
  d3.json(url).then(function(response) {
    
    let raceData = response
    console.log(raceData)

    horseNumbers = []

    for(let i = 0; i < 14; i++) {

      randomNumber =  Math.round(Math.random()*(4405 - 1) +1)
      horseNumbers[i] = randomNumber
      
       
    }
    
    // Create the Table Header Row
    let webBody = d3.select("body");
    let table = webBody.append("table")
    let thead = table.append("thead")
    let trow = thead.append("tr")
    let header = trow.append("th")
    header.text("Horse Number")
    let header2 = trow.append("th")
    header2.text("Race Distance")
    let header3 = trow.append("th")
    header3.text("Place Odds")
    let header4 = trow.append("th")
    header4.text("Result")
    let header5 = trow.append("th")
    header5.text("Winner")

  //   // Populate the table data
    let tableBody = table.append("tbody")
  //   raceData.forEach((horse) => {
  //     // console.log(ufoSighting);
  //     let row = tableBody.append('tr');
  //     Object.entries(horse).forEach(([key, value]) => {
  //         let cell = row.append('td');
  //         cell.text(value);
  //     });
  // });
    
    
    // horseNumbers.forEach((number) => {
        // for(let i = 0; i < response.length; i++) {
        //   if (number == response[i].horse_id) {
        //     let row = tableBody.append('tr');
        //     let cell = row.append('td');
        //     cell.text(number);
        //   }
        // }

    //     console.log(number);
    //     let row = tableBody.append('tr');
    //     let cell = row.append('td');
    //     cell.text(number);
        
    // });  
  
  });

} 
 






