# Point Of interest

This folder contains all the code related to a harmonized NGSIv2 end point.

Such endpoint serves entities of type `PointOfInterest`. Data comes from different sources:

* from the city of Porto (Portugal)

The scripts present in this folder are:

* `poi-server.js`. Main entry point of the endpoint.
* `oporto-ost.js`. Contains all the logic needed to interact with [OST Platform](https://www.ost.pt/)

Please check licenses before using this data in an application. 

Currently the following categories are supported:

* ```OffStreetParking```:          ```418```
* ```Restaurant```:                ```347```
* ```Hotel```:                     ```436```
* ```Museum```:                    ```311```
* ```Beach```:                     ```113```
* ```TouristInformationCenter```:  ```439```


## Examples of use 

```
curl http://130.206.83.68:1027/v2/entities?type=PointOfInterest&q=category:347
```

```json
{
    "id": "porto-poi-24043",
    "type": "PointOfInterest",
    "source": "http://fiware-porto.citibrain.com/docs",
    "category": ["347"],
    "dateCreated": "1970-01-01T00:00:00.000Z",
    "dateModified": "2015-11-12T19:35:42.926Z",
    "location": {
      "type": "Point",
      "coordinates": [
        -8.6207602,
        41.1492753
      ]
    },
    "description": "Space with simple lines, a modern and minimalist decor ... "
}
```
