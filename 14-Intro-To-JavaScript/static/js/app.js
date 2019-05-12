// from data.js
var Data = data;
var submit = d3.select("#filter-btn")
submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  var filteredData = Data.filter(sighting => sighting.datetime === inputValue);

  // Get a reference to the table body
  var tbody = d3.select("#ufo-table>tbody");

  // Console.log the UFO data from data.js
  console.log(Data);

  // Step 5: Use d3 to update each cell's text with
  // UFO sighting values (date/time, city, state, country, shape, durationMinutes, comment)
  filteredData.forEach(function(ufoSighting) {
    console.log(ufoSighting);
    var row = tbody.append("tr");
    Object.entries(ufoSighting).forEach(function([key, value]) {
      console.log(key, value);
      // Append a cell to the row for each value
      // in the UFO sighting object
      var cell = row.append("td");
      cell.text(value);
    });
  })});
