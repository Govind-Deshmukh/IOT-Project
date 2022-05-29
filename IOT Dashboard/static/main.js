var chartTemperatue;
var chartHumidity;

function requestData() {
  // Ajax call to get the Data from Flask
  var requests = $.get("/datafromiotapp");
  
  console.log("Requesting data from Flask");
  console.log(requests);

  var tm = requests.done(function (result) {
    // Temperature
    var seriesTemperature = chartTemperatue.series[0],
      shiftTemperature = seriesTemperature.data.length > 20;

    // Humidity
    var seriesHumidity = chartHumidity.series[0],
      shiftHumidity = seriesTemperature.data.length > 20;

    // Add the Point
    // Time Temperature\
    var data1 = [];
    data1.push(result[0]);
    data1.push(result[1]);

    // Add the Point
    // Time Humidity
    var data2 = [];
    data2.push(result[0]);
    data2.push(result[2]);

    chartTemperatue.series[0].addPoint(data1, true, shiftTemperature);
    chartHumidity.series[0].addPoint(data2, true, shiftHumidity);
    $(".sensor1").text("");
    $(".sensor1").text("Temperature : " + Math.round(data1[1]));

    $(".sensor2").text("");
    $(".sensor2").text("Humidity : " + Math.round(data2[1]));

    // call it again after one second
    setTimeout(requestData, 500);
  });
}

$(document).ready(function () {
  // --------------Chart 1 ----------------------------
  chartTemperatue = new Highcharts.Chart({
    chart: {
      renderTo: "data-temperature",
      defaultSeriesType: "area",
      events: {
        load: requestData,
      },
    },
    title: {
      text: "Temperature",
    },
    xAxis: {
      type: "datetime",
      tickPixelInterval: 150,
      maxZoom: 20 * 1000,
    },
    yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
        text: "Value",
        margin: 80,
      },
    },
    series: [
      {
        color: "#c23d23",
        lineColor: "#303030",
        name: "Temperature",
        data: [],
      },
    ],
  });
  // --------------Chart 1 Ends - -----------------

  chartHumidity = new Highcharts.Chart({
    chart: {
      renderTo: "data-humidity",
      defaultSeriesType: "area",
      events: {
        load: requestData,
      },
    },
    title: {
      text: "Humidity",
    },
    xAxis: {
      type: "datetime",
      tickPixelInterval: 150,
      maxZoom: 20 * 1000,
    },
    yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
        text: "Value",
        margin: 80,
      },
    },
    series: [
      {
        lineColor: "#1d82b8",
        name: "Humidity",
        data: [],
      },
    ],
  });
});
