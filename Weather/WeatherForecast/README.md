# Weather Forecast

This folder contains a set of scripts which allow to expose a NGSIv2 endpoint intended to provide weather forecasts.

Source of weather forecast are the [Spanish National Meteorology Agency](http://aemet.es) (AEMET) 
and the [Portuguese Institute for Sea and Atmosphere](http://ipma.pt) (IPMA).

The scripts present in this folder are the following:

* `aemet.py` is the main entry point for providing weather information
* `ipma.py` contains the Puython code for getting adn formatting the IPMA data

Please check data licenses at the original data sources before using this data in an application. 

## Examples of use

```
curl http://130.206.83.68:1028/v2/entities?type=WeatherForecast&q=country:PT;addressLocality:Porto
```

```json
  {
    "dayMinimum": {
      "temperature": 6.9
    },
    "feelsLikeTemperature": 14.2,
    "temperature": 15.1,
    "dateCreated": "2016-03-14T08:27:45",
    "windDirection": "W",
    "weatherType": "High clouds",
    "dayMaximum": {
      "temperature": 17.3
    },
    "windSpeed": 10,
    "validity": {
      "to": "2016-03-14T17:00:00",
      "from": "2016-03-14T16:00:00"
    },
    "address": {
      "addressCountry": "PT",
      "addressLocality": "Porto"
    },
    "type": "WeatherForecast",
    "id": "PT-Porto-2016-03-14T16:00:00-2016-03-14T17:00:00",
    "relativeHumidity": 0.59
  }
```  

  
```
curl http://130.206.83.68:1028/v2/entities?type=WeatherForecast&q=postalCode:39001;country:ES
```

```json
{
    "feelsLikeTemperature": 7,
    "dayMinimum": {
      "feelsLikeTemperature": 5,
      "temperature": 7,
      "relativeHumidity": 0.6
    },
    "temperature": 7,
    "dateCreated": "2016-03-14T11:40:02",
    "type": "WeatherForecast",
    "address": {
      "addressCountry": "ES",
      "postalCode": "39001",
      "addressLocality": "Santander"
    },
    "windSpeed": 0,
    "validity": {
      "to": "2016-03-15T00:00:00",
      "from": "2016-03-14T18:00:00"
    },
    "source": "http://www.aemet.es/xml/municipios/localidad_39075.xml",
    "precipitationProbability": 0,
    "dayMaximum": {
      "feelsLikeTemperature": 12,
      "temperature": 12,
      "relativeHumidity": 0.85
    },
    "weatherType": "Despejado",
    "windDirection": "C",
    "id": "39001_ES_2016-03-14_1",
    "relativeHumidity": 0.85
}
```