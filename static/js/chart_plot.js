// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
let max_value;

var col_name = document.getElementById("column").value

var normal_value = document.getElementById("normal_column").value
var normal_instance = document.getElementById("normal_instance").value
var other_value = document.getElementById("other_column").value
var other_instance = document.getElementById("other_instance").value
console.log(other_instance.split(", "))
console.log(other_instance.split(', '))

// function getCookie(cookieName){
//   var cookieValue=null;
//   if(document.cookie){
//       var array=document.cookie.split((escape(cookieName)+'='));
//       if(array.length >= 2){
//           var arraySub=array[1].split(';');
//           cookieValue=unescape(arraySub[0]);
//       }
//   }
//   return cookieValue;
// }

// var normal_name = json.loads(getCookie("normal_value_index"))
// var normal_count = getCookie("normal_value_counts")
// var other_name = getCookie("other_value_index")
// var other_count = getCookie("other_value_counts")

console.log(normal_value)
console.log(normal_instance)
console.log(other_value)
console.log(other_instance)

var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: normal_value.slice(1, -1).split(", "),
    datasets: [{
      label: "Normal",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      // data: [dementia, nc],
      data: normal_instance.slice(1, -1).split(", "),
    }],
  },
  options: {
    scales: {
      xAxes: [{
        // time: {
        //   unit: 'month'
        // },
        gridLines: {
          display: false
        },
        // ticks: {
        //   maxTicksLimit: 6
        // }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          // max: normal_instance[0],
          
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: true
    }
  }
});

var ctx2 = document.getElementById("myBarChart2");

// var pie_nc = document.getElementById("nc_value").value
// var pie_dementia = document.getElementById("dementia_value").value

var temp = '{{ nc_value | tojson | safe }}';

console.log(temp);

// dementia = dementia*=1;
// nc = nc*=1;
var myLineChart = new Chart(ctx2, {
  type: 'bar',
  data: {
    labels: other_value.slice(1, -1).split(", "),
    datasets: [{
      label: "Dementia",
      backgroundColor: "#dc3545",
      borderColor: "#dc3545",
      // data: [dementia, nc], 
      data: other_instance.slice(1, -1).split(", "),
    }],
  },
  options: {
    scales: {
      xAxes: [{
        // time: {
        //   unit: 'month'
        // },
        gridLines: {
          display: false
        },
        // ticks: {
        //   maxTicksLimit: 6
        // }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          // max: normal_instance[0],
          
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: true
    }
  }
});

// var myPieChart = new Chart(pie_plot, {
//   type: 'pie',
//   data: {
//     labels: other_value.slice(1, -1).split(", "),
//     datasets: [{
//       // data: [pie_dementia, pie_nc],
//       data: other_instance.slice(1, -1).split(", "),
//       // backgroundColor: ['#007bff', '#dc3545'],
//     }],
//   },
//   options: {
//     legend : {
//       display: true
//     }
//   }
// });
