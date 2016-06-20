# Waste Container Isle

## Description

An area which may contain one or more waste containers. 

## Data Model

+ `type` : `WasteContainerIsle`
+ `location`: Location of the isle represented by a GeoJSON Polygon.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory
  
+ `level`: Isle level (ground, underground, etc.)
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: one Of (`ground`, `underground`)
    + Optional
  
+ `address`: Civic address where the isle is located. 
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional

+ `description`: Description about the isle. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `containers`: List of containers present in the isle.
    + Attribute type: List. 
    + Allowed values. Container's id.
    + Optional


## Example

    {
      "id": "wastecontainerisle:Fleming:1",
      "type": "WasteContainerIsle",
      "location": {
         "type": "Polygon",
         "coordinates": [
          [
            [ -3.164485591715449, 40.62785133667262 ],
            [ -3.164445130316209, 40.627871567372239 ],
            [ -3.164394553567159, 40.627772099765778 ],
            [ -3.164424899616589, 40.62775018317452 ],
            [ -3.164485591715449, 40.62785133667262 ]
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
    
## Test it with a real service

T.B.D.