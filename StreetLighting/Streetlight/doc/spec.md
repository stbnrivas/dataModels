# Streetlight

An entity of type `Streetlight` represents a streetlight composed by a column, one or more arms together
with their corresponding lanterns and lamps.
A `Steeetlight` entity does not contain any attribute corresponding to its structural characteristics.
Such data is captured by entities of type `StreetlightModel`.

## Data Model

+ `id` : Entity's unique identifier. 

+ `type` : It must be equal to `Streetlight`.

+ `location` : Streetlight's location represented by a GeoJSON Point. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory if `address` is not present.
    
+ `address` : Civic address where the streetlight is located. 
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Mandatory if `location` is not present.
    
+ `area` : Higher level area to which the streetlight belongs to. It can be used to group streetlights per
responsible, district, neighbourhood, etc.
    + Attribute type: [Text](https://schema.org/Text)
    + Optional 

+ `circuit` : The circuit to which this streetlight connects to and gets power from.
Typically it will contain an identifier that will allow to obtain more information about such circuit. 
    + Attribute type: [Text](http://schema.org/Text)
    + Optional

+ `refStreetlightModel` : Streetlight's model. 
    + Attribute type : Reference to a [StreetlightModel](../../StreetlightModel/doc/spec.md) entity.
    + Optional

+ `status` : The overall status of this street light. 
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: one Of (`ok`, `defectiveLamp`, `columnIssue`, `brokenLantern`)
        + Or any other value meaningful to the application and not covered by the values above. 
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Mandatory

+ `powerState` : Streetlight's power state.
    + Attribute type: [Text](http://schema.org/Text)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Allowed values: one Of (`on`, `off`, `bootingUp`)
    + Optional
    
+ `refGroup` : Streetlight's group
    + Attribute type : Reference to a [StreetlightGroup](../../StreetlightGroup/doc/spec.md) entity.
    + Optional

+ `dateLastLampChange` : Timestamp of the last change of lamp made.
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
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

+ `timeSwitchingOn` : Regular switching on time for this street light.
    + Attribute Type: [DateTime](http://schema.org/Time)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `timeSwitchingOff` : Regular switching off time for this street light.
    + Attribute Type: [DateTime](http://schema.org/Time)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `controllingMethod` : The method used to control this streetlight.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: one Of (`cabinetController`, `individual`)
    
+ `dateUpdated` : Timestamp of the last update made to this entity
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `dateServiceStarted` : Date at which the streetlight started giving service.
    + Attribute Type: [Date](http://schema.org/Date)
    + Optional
       
+ `color` : Street light structure's color.
    + Attribute type: [Text](https://schema.org/Text)
    + Allowed Values:
        + A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords)
        + A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)
    + See also: [https://schema.org/color](https://schema.org/color)
    + Optional

+ `image` : A URL containing a photo of the streetlight.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional
    
+ `description` : Description about the streetlight. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `annotations` : A field reserved for annotations (incidences, remarks, etc.).
    + Attribute type: List of [Text](https://schema.org/Text)
    + Optional
    
+ `category` : Type of asset which implements the street light (`street lighting`, `street furniture`)

+ `streetLocation` : (`façade`, `sidewalk`)

+ `lanternHeight` : 

## Examples of Use

    {
      "id": "streetlight:guadalajara:4567",
      "type": "Streetlight",
      "location": {
        "type": "Point",
        "coordinates": [  -3.164485591715449, 40.62785133667262 ]
      },
      "area": "Poligono Industrial I",
      "status": "ok",
      "refStreetlightGroup": "streetlightgroup:G345",
      "circuit": "C-456-A467",
    }

## Test it with a real service

## Open Issues
