# Air Quality Observed

This folder contains scripts that give support to expose air quality observed data as NGSI version 2.

The data provided comes from [air quality stations](../PointOfInterest/AirQualityStation) located in different cities in Spain.

Please check the original data source before making use of this data in an application. 

The following scripts are present:

* `madrid_air_quality_harvest.py`.- A data harvest and harmonization program for official Madrid's Air Quality Data provided
by Madrid's City Council.
* `barcelona_air_quality_harvest.py`.- A data harvest and harmonization program for official Barcelona's Air Quality Data 
provided by Catalonia's Government.
* `madrid_air_quality.py` .- Offers both an NGSIv2 end point and NGSI10 to provide ambient observed data (outdated)
* `ngsi_helper.py` .- Contains helper functions to support the NGSI protocol (outdated)

## Examples of Use

What was the air quality observed today at noon at the "Plaza de España" air quality station?

```
curl -S --header 'fiware-service:airquality' --header 'fiware-servicepath:/Spain_Madrid' --header 'x-auth-token:4bc89e757d1841f6a33b02748376edc9' "http://130.206.118.244:1027/v2/entities?options=keyValues&q=dateObserved:2016-11-28T12:00;stationCode:'28079027'" | python -mjson.tool
```

```json

    [
        {
            "id": "Madrid-AmbientObserved-28079027-2016-11-28T12:00:00",
            "type": "AirQualityObserved",
            "NO": 3,
            "NO2": 11,
            "NOx": 16,
            "O3": 68,
            "address":
            {
                "addressCountry": "ES",
                "addressLocality": "Madrid",
                "streetAddress": "C/. Júpiter, 21 Barajas "
            },
            "dataProvider": "TEF",
            "dateObserved": "2016-11-28T11:00:00.00Z",
            "hour": "12:00",
            "location":
            {
                "type": "Point",
                "coordinates":
                [
                    -3.580030556,
                    40.476927778
                ]
            },
            "measurand":
            [
                "NO,3.0,GQ,Nitrogen Monoxide",
                "NO2,11.0,GQ,Nitrogen Dioxide",
                "NOx,16.0,GQ,Nitrogen oxides",
                "O3,68.0,GQ,Ozone"
            ],
            "source": "http://datos.madrid.es",
            "stationCode": "28079027",
            "stationName": "Barajas Pueblo",
        }
    ]

```
