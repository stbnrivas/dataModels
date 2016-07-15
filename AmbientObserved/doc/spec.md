# Ambient Observed

The formal documentation is currently under development. In the meantime please check examples of use. 

## Examples of use

    {
      "address": {
        "addressCountry": "ES",
        "addressLocality": "Madrid",
        "streetAddress": "Plaza de España"
      },
      "dateCreated": "2016-03-15T13:29:30.894942",
      "id": "Madrid-AmbientObserved-28079004-2016-03-15T11:00:00",
      "location": {
        "type": "geo:point",
        "value": "40.423852777777775,-3.712247222222222"
      },
      "pollutants": {
        "CO": {
          "concentration": 500,
          "description": "Carbon Monoxide"
        },
        "NO": {
          "concentration": 45,
          "description": "Nitrogen Monoxide"
        },
        "NO2": {
          "concentration": 69,
          "description": "Nitrogen Dioxide"
        },
        "NOx": {
          "concentration": 139,
          "description": "Nitrogen oxides"
        },
        "SO2": {
          "concentration": 11,
          "description": "Sulfur Dioxide"
        }
      },
      "precipitation": 0,
      "relativeHumidity": 54,
      "source": "http://datos.madrid.es",
      "stationCode": "28079004",
      "stationName": "Pza. de España",
      "temperature": 12.2,
      "type": "AmbientObserved",
      "validity": {
        "from": "2016-03-15T11:00:00",
        "to": "2016-03-15T12:00:00"
      },
      "windDirection": 186,
      "windSpeed": 0.64
    }