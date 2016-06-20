# Waste Container Isle

## Description

A geographical area which keeps one or more waste containers. 

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `WasteContainerIsle`. 

+ `location`: Location of the isle represented by a GeoJSON Polygon.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory
  
+ `level`: Level at which the isle is placed (ground, underground, etc.)
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: one Of (`ground`, `underground`)
    + Optional
  
+ `address`: Civic address where the isle is located. 
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional
 
+ `name`: Name given to the isle
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Optional

+ `description`: Description about the isle. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `containers`: List of containers present in the isle.
    + Attribute type: List of references to [WasteContainer](../../WasteContainer/doc/spec.md) entities. 
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
      "name": "Doctor Fleming 5",
      "description": "Container isle located downtown",
      "containers": ["wastecontainer:Fleming:4", "wastecontainer:Fleming:5"] 
    }
    
## Test it with a real service

T.B.D.