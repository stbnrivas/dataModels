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

What was the air quality observed today at the "Plaza de España" air quality station?

```
curl -S --header 'fiware-service:airquality' --header 'fiware-servicepath:/Spain_Madrid' --header 'x-auth-token:4bc89e757d1841f6a33b02748376edc9' "http://130.206.118.244:1027/v2/entities?type=AirQualityObserved&attrs=measurand,address&q=dateObserved>2016-11-24;stationCode:'28079004'&orderBy=dateObserved&options=keyValues" | python -mjson.tool
```

```json

[{
        "address": {
            "addressCountry": "ES",
            "addressLocality": "Madrid",
            "streetAddress": "Plaza de Espa\u00f1a"
        },
        "id": "Madrid-AmbientObserved-28079004-2016-11-24T01:00:00",
        "measurand": [
            "SO2,2.0,GQ,Sulfur Dioxide",
            "CO,0.3,GP,Carbon Monoxide",
            "NO,20.0,GQ,Nitrogen Monoxide",
            "NO2,57.0,GQ,Nitrogen Dioxide",
            "NOx,88.0,GQ,Nitrogen oxides"
        ],
        "type": "AirQualityObserved"
    }
...
```
