# RateChart
This project is for saving rate, date and demonstrate data in line chart with rate(USD to UAH) to date   

Back-end:
  - Django was used like main framework
  - SQLite as a database 

Front-end:
  - Chart.js as a library for chart 
  - Bootstrap5 is for design 
 
In site you can see two form fields:
  - Decimal field, where we should input currency rate USD to UAH (rate cannot be less than 0.01)
  - Date field

When you submit your rate and date, chart is updating. And than you can see you rate on line chart ordered by date 
