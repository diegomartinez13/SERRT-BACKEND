setTimeout(function() {
  location.reload();
}, 2000); // Reload the webpage after 1 seconds

// function getLatestData() {
//   fetch('/cardata/simulation').then(response => response.json()).then(data => {
//       document.getElementById("speed").innerText = data.current_speed + 'MPH';
//       document.getElementById("progress-speed").style.width = data.current_speed + '%';
//       document.getElementById("temp").innerText= data.current_temp + '&deg;C';
//       document.getElementById("battery").innerText = data.battery + '%';
//       document.getElementById("progress-battery").style.width = data.battery + '%';
//       document.getElementById("optimal_velocity").innerText = data.optimal_velocity + "MPH";
//       document.getElementById("solar_panel_output").innerText = data.solar_panel_output + "V";
//   }).catch(error => console.error(error));
// }

// $(function () {
// getLatestData();
// setInterval(getLatestData, 5000);
// });