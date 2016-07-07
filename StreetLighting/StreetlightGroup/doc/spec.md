# Streetlight group

An entity of type `StreetlightGroup` represents a group of streetlights which belong to the same circuit and which are controlled
by a common automated system. This entity type is mainly useful when the streetlight system is controlled by groups and not individually. 

## Data Model

+ `id` : Entity's unique identifier. 

+ `type` : It must be equal to `StreetlightGroup`.

+ `location` : Streetlight's group location represented by a GeoJSON (multi)geometry. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory
        
+ `area` : Higher level area to which the streetlight group belongs to. It can be used to group per
responsible, district, neighbourhood, etc.
    + Attribute type: [Text](https://schema.org/Text)
    + Optional 

+ `circuit` : The circuit to which the streetlights belonging to this group connect to and gets power from.
Typically it will contain an identifier that will allow to obtain more information about such circuit. 
    + Attribute type: [Text](http://schema.org/Text)
    + Optional

+ `powerState` : Streetlight group's power state.
    + Attribute type: [Text](http://schema.org/Text)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Allowed values: one Of (`on`, `off`, `bootingUp`)
    + Optional
    
+ `refCabinetController` : Streetlight group's cabinet controller
    + Attribute type : Reference to a [StreetlightCabinetController](../../StreetlightCabinetController/doc/spec.md) entity.
    + Mandatory
    
+ `dateLastSwitchingOn` : Timestamp of the last switching on.
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `dateLastSwitchingOff` : Timestamp of the last switching off.
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `timeSwitchingOn` : Regular switching on time.
    + Attribute Type: [DateTime](http://schema.org/Time)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `timeSwitchingOff` : Regular switching off time.
    + Attribute Type: [DateTime](http://schema.org/Time)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `dateUpdated` : Timestamp of the last update made to this entity
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Optional
        
+ `description` : Description about the streetlight group. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `annotations` : A field reserved for annotations (incidences, remarks, etc.).
    + Attribute type: List of [Text](https://schema.org/Text)
    + Optional

+ `refStreetlight` : List of streetlight entities belonging to this group. 
    + Attribute type: List of references to entities fo type [Streetlight](../../Streetlight/doc/spec.md)
    + Allowed values: There must topographical integrity between the location of the group and the individual streetlights.  
    + Optional
    
## Examples of Use

    {
      "id": "streetlightgroup:mycity:A12",
      "type": "StreetlightGroup",
      "location": {
        "type": "MultiLineString",
        "coordinates": [
          [ [100.0, 0.0], [101.0, 1.0] ],
          [ [102.0, 2.0], [103.0, 3.0] ]
        ]
      },
      "area": "Poligono Industrial I",
      "circuit": "C-456-A467",
      "dateLastSwitchingOn":  "2016-07-07T19:59:06.618Z",
      "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",
      "refCabinetController": "cabinetcontroller:CC45A34",
      "timeSwitchingOn":  "19:00",
      "timeSwitchingOff": "08:00"
    }

## Test it with a real service


## Open Issues