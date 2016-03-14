# Weather data models

This folder contains all the code that supports NGSIv2 end points for providing weather information.
The following entity types are supported:

* `WeatherObserved` .- Weather observations provided by [AEMET Weather Stations](../PointOfInterest/WeatherStation/README.md)
* `WeatherForecast` .- Weather forecasts provided by [AEMET](http://aemet.es) and [IPMA](http://ipma.pt)
* `WeatherAlarm` .- Weather alarms provided by [MeteoAlarm](http://meteoalarm.eu)

The main script in this folder is `aemet.py` which serves as the main entry point for NGSIv2 weather data. 