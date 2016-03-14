# PointOfInterest

This folder contains all the code related to a harmonized NGSIv2 end point which serves entities of type `PointOfInterest`.

The main entry point the is the poi-server.js. Querying the end point is as easy as

```
http://130.206.83.68:1027/v2/entities?type=PointOfInterest&q=category:Restaurant
```

```json
{
    "id": "porto-poi-24043",
    "type": "PointOfInterest",
    "source": "http://fiware-porto.citibrain.com/docs",
    "category": "Restaurantes",
    "created": "1970-01-01T00:00:00.000Z",
    "updated": "2015-11-12T19:35:42.926Z",
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

The referred end point is providing data from the city of Porto (Portugal) and from AEMET (National Weather Agency from Spain)

Currently the following categories are supported:

* 'WeatherStation',
* 'Restaurant',
* 'Hotel',
* 'ParkingLot'