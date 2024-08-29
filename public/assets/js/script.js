$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
    $("#content").toggleClass("active");
  });

  $(".more-button,.body-overlay").on("click", function () {
    $("#sidebar,.body-overlay").toggleClass("show-nav");
  });
});

// Quill Text Editor
const quill = new Quill("#editor", {
  theme: "snow",
});

// Radial
var options = {
  series: [44, 55, 67, 83],
  chart: {
    height: 350,
    type: "radialBar",
  },
  plotOptions: {
    radialBar: {
      dataLabels: {
        name: {
          fontSize: "22px",
        },
        value: {
          fontSize: "16px",
        },
        total: {
          show: true,
          label: "Total",
          formatter: function (w) {
            return 249;
          },
        },
      },
    },
  },
  labels: ["Apples", "Oranges", "Bananas", "Berries"],
};

var chart = new ApexCharts(document.querySelector("#chart3"), options);
chart.render();
