# Streetlight control cabinet

It represents equipment, usually on street, used to the automated control of a group(s) of streetlights, i.e. one or more circuits.

## Data Model

+ `id` : Entity's unique identifier. 

+ `type` : It must be equal to `StreetlightControlCabinet`.

+ `location` : Control cabinet's location represented by a GeoJSON point. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory

+ `address` : Civic address where the control cabinet is located. 
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Mandatory if `location` is not present.
        
+ `area` : Higher level area to which the cabinet belongs to. It can be used to group per
responsible, district, neighbourhood, etc.
    + Attribute type: [Text](https://schema.org/Text)
    + Optional
    
+ `serialNumber` : Serial number of the control cabinet.
    + Normative References: [https://schema.org/serialNumber](https://schema.org/serialNumber)
    + Optional   

+ `refStreetlightGroup` : Streetlight group(s) controlled. 
    + Attribute type: List of references to entities of type [StreetlightGroup](../../StreetlightGroup/doc/spec.md).
    + Mandatory

+ `brandName` : Name of the cabinet's brand.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/brand](https://schema.org/brand)
    + Optional

+ `modelName` : Name of the cabinet's model.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/model)
    + Optional

+ `manufacturerName` : Name of the cabinet's manufacturer.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/manufacturer)
    + Optional

+ `cupboardMadeOf` : Material the cabinet's cupboard is made of. 
    + Attribute type: [Text](https://schema.org/Text)
    + Allowed values: one Of (`plastic`, `metal`, `concrete`, `other`)
    + Optional

+ `features` : A list of cabinet controller features. 
    + Attribute type: List of [Text](https://schema.org/Text)
    + Allowed Values: Those technical values considered meaningful by applications.
        + `astronomicalClock` .- The control cabinet includes an astronomical clock to deal with switching hours. 
        + `individualControl` .- The control cabinet allows to control street lights individually. 

+ `compliantWith`. A list of standards to which the cabinet controller is compliant with (ex. `IP54`)
    + AttributeType: List of [Text](https://schema.org/Text).
    + Optional
    
+ `annotations` : A field reserved for annotations (incidences, remarks, etc.).
    + Attribute type: List of [Text](https://schema.org/Text)
    + Optional

+ `dateUpdated` : Last update timestamp of this entity.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional

+ `dateServiceStarted` : Date at which the cabinet controller started giving service.
    + Attribute Type: [Date](http://schema.org/Date)
    + Optional

+ `dateLastProgramming` : Date at which there was a programming operation over the cabinet.
    + Attribute Type: [Date](http://schema.org/DateTime)
    + Optional
    
+ `nextActuationDeadline` : Deadline for next actuation to be performed (programming, testing, etc.).
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Optional   

+ `responsible` : Responsible for the cabinet controller, i.e. entity in charge of actuating (programming, etc.). 
    + Attribute type: [Text](http://schema.org/Text)
    + Optional


## Examples of Use

    {
      "id": "streetlightcontrolcabinet:A45HGJK",
      "type": "StreetlightControlCabinet",
      "location": {
        "type": "Point",
        "coordinates": [  -3.164485591715449, 40.62785133667262 ]
      },
      "cupboardMadeOf": "plastic",
      "brandName": "Siemens",
      "modelName": "Simatic S7 1200",
      "refStreetlightGroup": ["streetlightgroup:BG678", "streetlightgroup:789"],
      "compliantWith": ["IP54"],
      "dateLastProgramming": "2016-07-08"
    }


## Test it with a real service


## Open Issues

+ Should we create a `StreetlightControlCabinetModel entity type? 