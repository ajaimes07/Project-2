// Plot the default route once the page loads
var defaultURL = "/severeweather";
d3.json(defaultURL), function (severeweatherdata) {
  var data = [severeweatherdata];
  var layout = { margin: { t: 30, b: 100 } };
  Plotly.plot("bar", data, layout);
};
// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("bar", "x", [newdata.x]);
  Plotly.restyle("bar", "y", [newdata.y]);
}
