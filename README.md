<h1 align='center'> 🎉 New Year Count Down 🎉 </h1>


<p align='center' > New Year CountDown using Python Datetime Module and Flask. </p>

<a href='https://fun-web-projects.herokuapp.com/fun/new-year-countdown'> <h3 align='center'> Live App </h3> </a>

<hr>

## How its work

[Python Function](https://github.com/yogeshwaran01/new-year-countdown-python/blob/d968414a6676486bec02a4c2050b32c22a2217d7/utils.py#L8) returns the day and time 
 for the Next New Year. [Flask route path](https://github.com/yogeshwaran01/new-year-countdown-python/blob/d968414a6676486bec02a4c2050b32c22a2217d7/app.py#L13) return 
 the json of that day and time of the Next Year. [This](https://github.com/yogeshwaran01/new-year-countdown-python/blob/d968414a6676486bec02a4c2050b32c22a2217d7/static/script.js#L1) Javascript Function send the Http Request for that [Flask route path](https://github.com/yogeshwaran01/new-year-countdown-python/blob/d968414a6676486bec02a4c2050b32c22a2217d7/app.py#L13). It gets updated each seconds by running the [Function](https://github.com/yogeshwaran01/new-year-countdown-python/blob/d968414a6676486bec02a4c2050b32c22a2217d7/utils.py#L8) by sending the requests.
 
 ## Website
 
 <a href='https://fun-web-projects.herokuapp.com/fun/new-year-countdown'> Website </a> for the live App
 
 ## Local
 
 ### Web App
 
 ```bash
 git clone https://github.com/yogeshwaran01/new-year-countdown-python
 
 cd new-year-countdown-python
 
 python app.py
 
 ```
 
 ### CLI
 
  ```bash
 git clone https://github.com/yogeshwaran01/new-year-countdown-python
 
 cd new-year-countdown-python
 
 python cli.py
 
 ```
 
 <p align='center'> Made With Python ❤️ </p>
 
