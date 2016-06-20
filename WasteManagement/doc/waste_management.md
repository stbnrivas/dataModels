# Waste Management

## Waste Container Isle

An area which may contain one or more waste containers. 

+ `type` : `WasteContainerIsle`
+ `location`: Location of the isle represented by a GeoJSON Polygon.
  + Attribute type: `geo:json`.
  + Normative References: [geojson](https://tools.ietf.org/html/draft-ietf-geojson-03)
  + Mandatory
  
+ `level`:
  + Attribute type: [Text](http://schema.org/Text)
  + Allowed values: one Of (`ground`, `underground`)
  + Optional
  
+ `address`: Civic address where the isle is located. 
  + Normative References: [address](https://schema.org/address)
  + Optional

+ `description`:
  + Normative References: [description](https://schema.org/description)
  + Optional

+ `containers`:
  + List of containers present in the aisle.
  + Attribute type: List. 
  + Allowed values. Container's id.
  + Optional


### Example

    {
      "id": "wastecontaineraisle:Fleming:1",
      "type": "WasteContainerIsle",
      "location": {
         "type": "Polygon",
         "coordinates": [
          [
            [], [], [], []
          ]  
         ]
      },
      "address": {
         "streetAddress" : "Calle Dr. Fleming, 5",
         "addressLocality": "Guadalajara",
         "addressCountry": "ES"
      },
      "level": "ground",
      "description": "Container isle located downtown",
      "containers": ["wastecontainer:Fleming:4", "wastecontainer:Fleming:5"] 
    }
    
### Test it with a real service

