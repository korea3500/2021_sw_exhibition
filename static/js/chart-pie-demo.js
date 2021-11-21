// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");

var nc = document.getElementById("nc_value").value
var dementia = document.getElementById("dementia_value").value

var temp = '{{ nc_value | tojson | safe }}';

console.log(temp);

dementia = dementia*=1;
nc = nc*=1;
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["dementia", "NC"],
    datasets: [{
      data: [dementia, nc],
      backgroundColor: ['#007bff', '#dc3545'],
    }],
  },
});
