//load in json data 
// loop through data
//This function generates 14 random numbers and loads them into a table on the 
  // webpage. Will need to add functionality to run those horse numbers through the model. 
function randomRace() {  
  // const url = "/api/button";
  // d3.json(url).then(function(response) {
    
    horseNumbers = []

    for(let i = 0; i < 14; i++) {

      randomNumber =  Math.round(Math.random()*(4405 - 1) +1)
      horseNumbers[i] = randomNumber
      console.log(randomNumber);
    // expected output: a number from 0 to <1
       
    }
    
    // Create the Table Header Row
    let webBody = d3.select("body");
    let table = webBody.append("table")
    let thead = table.append("thead")
    let trow = thead.append("tr")
    let header = trow.append("th")
    header.text("Horse Number")

    // Populate the table data
    let tableBody = table.append("tbody")
    horseNumbers.forEach((number) => {
        console.log(number);
        let row = tableBody.append('tr');
        let cell = row.append('td');
        cell.text(number);
        
    });   

} 
 






