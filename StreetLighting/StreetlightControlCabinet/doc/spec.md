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
        
+ `areaServed` : Higher level area to which the cabinet belongs to. It can be used to group per
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

+ `dateModified` : Last update timestamp of this entity.
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

+ `workingMode` : Working mode for this cabinet controller.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: 
        + `automatic` : The cabinet controller decides automatically when light groups are switched on and off.
        Manual operation is not allowed. 
        + `manual` : Human intervention is required for switching on and off. 
        + `semiautomatic` : The same as `automatic` but in this case manual intervention is allowed. 
    + Mandatory 

+ `maximumPowerAvailable` : The maximum power available (by contract) for the circuits controlled by this cabinet.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Kilowatts
    + Optional
    
 + `energyConsumed` :  Energy consumed by the circuits controlled since metering started (since `dateMeteringStarted`).
    + Attribute type: [Number](https://schema.org/Number)
    + Default unit: Kilowatts per hour (Kwh).
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `energyCost` : Cost of the energy consumed by the circuits controlled since the metering start date (`dateMeteringStarted`).
    + Attribute type: [Number](https://schema.org/Number)
    + Default currency: Euros. (Other currencies might be expressed using a metadata attribute)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `reactiveEnergyConsumed` : Energy consumed (with regards to reactive power) by circuits
since the metering start date (`dateMeteringStarted`).
    + Attribute type: [Number](https://schema.org/Number)
    + Default unit: KiloVolts-Ampere-Reactive per hour (Kvar).
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `dateMeteringStarted` : The starting date for metering energy consumed.
    + Attribute Type: [DateTime](http://schema.org/DateTime)
    + Mandatory if `powerConsumedAccumulated` is present.     

+ `lastMeterReading` : Value of the last reading obtained from the energy consumed metering system.
    + Attribute type: [Number](https://schema.org/Number)
    + Default unit: Kilowatts per hour.
    + Attribute metadata:
        + `dateUpdated`: Timestamp which reflects the date and time at which the referred reading was obtained.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `meterReadingPeriod` : The periodicity of energy consumed meter readings in days.
    + Attribute Type: [Number](http://schema.org/Number)
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
      "dateLastProgramming": "2016-07-08",
      "maximumPowerAvailable": 10,
      "energyConsumed": 162456,
      "dateMeteringStarted": "2013-07-07",
      "lastMeterReading": 161237,
      "meterReadingPeriod": 60
    }


## Test it with a real service


## Open Issues

+ Should we create a `StreetlightControlCabinetModel` entity type?
+ Should we have the programming parameters as attribute of this entity? Advantage is that if programming is the same
for all the controlled cicuits then there is no need to repeat the same parameters over multiple entities. 