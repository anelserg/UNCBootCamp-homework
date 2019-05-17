function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  var defaultURL = "/metadata/"+sample
  d3.json(defaultURL).then(function(data){
  // console.log(data)
    // Use d3 to select the panel with id of `#sample-metadata`
    var samplePanelMetadata = d3.select("#sample-metadata")
    
    // Use `.html("") to clear any existing metadata
    samplePanelMetadata.html("")
    
    // Use `Object.entries` to add each key and value pair to the panel
    Object.entries(data).forEach(function([key, value]){
      // console.log(key, value);
      
      samplePanelMetadata.append("p").text(key + ": " + value)
    });
  })
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(`/samples/${sample}`).then(function(data){
    // console.log(data.otu_ids)

    // @TODO: Build a Bubble Chart using the sample data
    var trace1 = {
      type: "bubble",
      name: name,
      x: data.otu_ids,
      y: data.sample_values,
      text: data.otu_labels,
      mode: 'markers',
      marker: {
        size: data.sample_values,
        color: data.otu_ids
      }

    };

    var bubbleData = [trace1];

    var layout = {
      title: `otu_ids`,
      xaxis: {
        autorange: true,
        type: "id"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("bubble", bubbleData, layout);
    

    var idsSliced = data.otu_ids.slice(0, 10)
    var valuesSliced = data.sample_values.slice(0, 10)
    var labelsSliced = data.otu_labels.slice(0, 10)

    // @TODO: Build a Pie Chart
    var trace1 = {
      labels: idsSliced,
      values: valuesSliced,
      type: 'pie',
      text: labelsSliced
    };
      
    var pieData = [trace1];
    
    var layout = {
      title: "'Pie' Chart",
      height: 400,
      width: 500,
    };
    
    Plotly.newPlot("pie", pieData, layout);
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
  })
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
