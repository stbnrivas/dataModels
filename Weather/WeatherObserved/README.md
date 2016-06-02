# Weather Observed

Weather observed from the [Spanish National Meteorology Agency](http://aemet.es) (AEMET) is exposed through NGSI v2.
The Weather observed is provided by [weather stations](../../PointOfInterest/WeatherStation) owned by AEMET. 

This folder contains the following script:

`weather_observed.py` .- Contains all the logic to expose the weather observed as an NGSIv2 data model.

Please check data licenses at the original data sources before using this data in an application. 

## Examples of use

```curl http://130.206.83.68:1028/v2/entities?type=WeatherObserved&q=stationCode:2422;country:ES```

```json
{
    "temperature": 9.2,
    "source": "http://www.aemet.es",
    "windDirection": "Este",
    "address": {
      "addressLocality": "Valladolid",
      "addressCountry": "ES"
    },
    "dateObserved": "2016-03-14T16:00:00",
    "pressure": 930,
    "windSpeed": 7,
    "type": "WeatherObserved",
    "relativeHumidity": 0.47,
    "precipitation": 0,
    "pressureTendency": -1.3
}
```