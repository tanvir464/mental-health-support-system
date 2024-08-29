// Patient appointment chart
var papp_value = {
  series: [
    {
      name: "Specialist",
      data: [44, 55, 41, 67, 22, 43, 13, 23, 20, 8, 13, 27],
    },
    {
      name: "Councelor",
      data: [13, 23, 20, 8, 13, 27, 44, 55, 41, 67, 22, 43],
    },
  ],
  chart: {
    type: "bar",
    height: 350,
    stacked: true,
    toolbar: {
      show: true,
    },
    zoom: {
      enabled: true,
    },
  },
  responsive: [
    {
      breakpoint: 480,
      options: {
        legend: {
          position: "bottom",
          offsetX: -10,
          offsetY: 0,
        },
      },
    },
  ],
  plotOptions: {
    bar: {
      horizontal: false,
      borderRadius: 10,
      borderRadiusApplication: "end", // 'around', 'end'
      borderRadiusWhenStacked: "last", // 'all', 'last'
      dataLabels: {
        total: {
          enabled: true,
          style: {
            fontSize: "13px",
            fontWeight: 900,
          },
        },
      },
    },
  },
  xaxis: {
    type: "string",
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  legend: {
    position: "right",
    offsetY: 40,
  },
  fill: {
    opacity: 1,
  },
};

var papp = new ApexCharts(
  document.querySelector("#appointment-chart"),
  papp_value
);
papp.render();

// Patient prescription chart
var prescription_value = {
  series: [
    {
      name: "Prescription",
      data: [31, 40, 28, 51, 42, 109, 100, 23, 17, 78, 38, 50],
    },
  ],
  chart: {
    height: 350,
    type: "area",
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    curve: "smooth",
  },
  xaxis: {
    type: "string",
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  tooltip: {
    x: {
      format: "dd/MM/yy HH:mm",
    },
  },
};

var prescription = new ApexCharts(
  document.querySelector("#prescription-chart"),
  prescription_value
);
prescription.render();

// Patient diagnosis report chart
var dreport_value = {
  series: [14, 23, 21, 17, 15, 10, 12, 17, 21],
  chart: {
    height:350,
    type: 'polarArea',
},
stroke: {
  colors: ['#fff']
},
fill: {
  opacity: 0.8
},
responsive: [{
  breakpoint: 480,
  options: {
    chart: {
      width: 200,
    },
    legend: {
      position: 'bottom'
    }
  }
}]
};

var chart = new ApexCharts(document.querySelector("#dreport-chart"), dreport_value);
chart.render();


// patient event chart
var event_value = {
  series: [
    {
      name: "Event",
      data: [80, 50, 40, 100, 20, 13, 45, 24, 34, 47, 30, 24],
    },
  ],
  chart: {
    height: 350,
    type: "radar",
  },
  yaxis: {
    stepSize: 20,
  },
  xaxis: {
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
};

var events = new ApexCharts(
  document.querySelector("#event-chart"),
  event_value
);
events.render();

// patient card chart
var pcard_value = {
  series: [76, 67],
  chart: {
    height: 390,
    type: "radialBar",
  },
  plotOptions: {
    radialBar: {
      offsetY: 0,
      startAngle: 0,
      endAngle: 270,
      hollow: {
        margin: 5,
        size: "30%",
        background: "transparent",
        image: undefined,
      },
      dataLabels: {
        name: {
          show: false,
        },
        value: {
          show: false,
        },
      },
      barLabels: {
        enabled: true,
        useSeriesColors: true,
        margin: 8,
        fontSize: "16px",
        formatter: function (seriesName, opts) {
          return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex];
        },
      },
    },
  },
  colors: ["#1ab7ea", "#0084ff"],
  labels: ["Psychiatrist", 'Psychologist'],
  responsive: [
    {
      breakpoint: 480,
      options: {
        legend: {
          show: false,
        },
      },
    },
  ],
};

var pcard = new ApexCharts(document.querySelector("#card-chart"), pcard_value);
pcard.render();
