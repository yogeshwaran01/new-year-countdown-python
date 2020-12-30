function Countdown() {
    const request = new XMLHttpRequest();
    request.open("GET", "/time");
    request.send();
    request.onreadystatechange = (e) => {
        data = JSON.parse(request.responseText)
        document.getElementById('days').innerHTML = data[0];
        document.getElementById('hours').innerHTML = data[1];
        document.getElementById('minutes').innerHTML = data[2];
        document.getElementById('secs').innerHTML = data[3]
    }
};
window.onload = function() {
    setInterval(Countdown, 100);
  };
