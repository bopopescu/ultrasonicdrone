//gloabl SQL 
var h = 0; 

//gets height from server
function getH(str) {
  var xhttp; 
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    h = 1;
  };
  
  //name of server, figure out file typing
  xhttp.open("GET", "getcustomer.asp?q="+str, true);
  xhttp.send();
}

//drawing the chart
var chart = new SmoothieChart(),
    canvas = document.getElementById('smoothie-chart'),
    series = new TimeSeries();

console.time('function');
setInterval(function(){
  //Display: document.getElementById("height") = series[-1]; 
  var t = performance.now(); 
  var n = Math.random().toFixed(2); 
  getH("Hello"); 
  document.getElementById("height").innerHTML = n; 
  document.getElementById("test").innerHTML = h;
  console.timeEnd('function');
  series.append(new Date().getTime(), n);
}, 400); 

chart.addTimeSeries(series, {lineWidth:2,strokeStyle:'#00ffff'});
chart.streamTo(canvas, 500);
var q = performance.now(); 


