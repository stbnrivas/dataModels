# Streetlight group

An entity of type `StreetlightGroup` represents a group of streetlights which belong to the same circuit and which are normally controlled
together by the same automated system (cabinet controller). 

## Data Model

+ `id` : Entity's unique identifier. 

+ `type` : It must be equal to `StreetlightGroup`.

+ `location` : Streetlight's group location represented by a GeoJSON (multi)geometry. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory
        
+ `areaServed` : Higher level area to which the streetlight group belongs to. It can be used to group per
responsible, district, neighbourhood, etc.
    + Normative References: [https://schema.org/areaServed](https://schema.org/areaServed)
    + Optional 

+ `circuitId` : The circuit to which the streetlights belonging to this group connect to and gets power from.
Typically it will contain an identifier that will allow to obtain more information about such circuit. 
    + Attribute type: [Text](http://schema.org/Text)
    + Optional
    
+ `circuitFrequency` : The working frequency of the circuit.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Hertz
    + Optional

+ `powerState` : Streetlight group's power state.
    + Attribute type: [Text](http://schema.org/Text)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Allowed values: one Of (`on`, `off`, `low`, `bootingUp`)
    + Optional
    
+ `refStreetlightCabinetController` : Streetlight group's cabinet controller
    + Attribute type : Reference to a [StreetlightCabinetController](../../StreetlightCabinetController/doc/spec.md) entity.
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

+ `switchingOnHours` : Switching on hours. It is used normally to set special schedules for certain dates. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Subproperties:
        + `from` : Starting date (it can be yearless). 
            + Type: [Date](https://schema.org/Date)
        + `to` : Ending date (it can be yearless)
            + Type: [Date](https://schema.org/Date)
        + `hours` : Hours. 
            + Normative References: Value must be compliant with [https://schema.org/openingHours](https://schema.org/openingHours)
    + Attribute metadata:
        + `dateUpdated` : Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
        
+ `switchingMode` : Switching mode. 
    + Attribute Type: List of [Text](http://schema.org/Text)
    + Allowed values: (`night-ON`, `night-OFF`, `night-LOW`, `always-ON`, `day-ON`, `day-OFF`, `day-LOW`)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `illuminanceLevel` : Relative illuminance level setting for the group.
    + Attribute Type: [Number](http://schema.org/Number)
    + Allowed values: A number between 0 and 1.
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
        
+ `activeProgramId` : Identifier of the active program for this streetlight group.
    + Attribute type: [Text](https://schema.org/Text)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional 
    
+ `dateModified` : Timestamp of the last update made to this entity.
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
    + Allowed values: There must topographical integrity between the location of the group and of the individual streetlights.  
    + Optional
    
+ `totalActivePower` : Active power currently consumed by this group of streetlights (counting all phases).
    + Attribute Type: [Number](http://schema.org/Number)
    + Default unit: KiloWatts. 
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `totalReactivePower` : Reactive power currently consumed by this group of streetlights (counting all phases).
    + Attribute Type: [Number](http://schema.org/Number)
    + Default unit: KiloVolts-Ampere-Reactive (Kvar). 
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `activePower` : Active power consumed by the circuit per phase. The actual values will be conveyed
by subproperties which name will be equal to the name of each of the circuit's alternating
current phases, typically R, S, T. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Default unit: Kilowatts
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `reactivePower` : Reactive power of the circuit. The actual values will be conveyed
by subproperties which name will be equal to the name of each of the circuit's alternating
current phases, typically R, S, T. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Default unit: KiloVolts-Ampere-Reactive (Kvar)
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional    
    
+ `energyConsumed` : Energy consumed by the corresponding circuit since the metering start date (`dateMeteringStarted`).
    + Attribute type: [Number](https://schema.org/Number)
    + Default unit: Kilowatts per hour (Kwh).
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `reactiveEnergyConsumed` : Energy consumed (counting reactive power) by the corresponding circuit
since the metering start date (`dateMeteringStarted`).
    + Attribute type: [Number](https://schema.org/Number)
    + Default unit: KiloVolts-Ampere-Reactive per hour (Kvar).
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `energyCost` : Cost of the energy consumed by the corresponding circuit since the metering start date (`dateMeteringStarted`).
    + Attribute type: [Number](https://schema.org/Number)
    + Default currency: Euros. (Other currencies might be expressed using a metadata attribute)
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
    
+ `powerFactor` : Power factor of the circuit associated to this group of streetlights.
    + Attribute Type: [Number](http://schema.org/Number)
    + Allowed values: A number between -1 and 1.
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
    
+ `cosPhi` : "Cosin of phi" parameter of the circuit associated to this group of streetlights.
    + Attribute Type: [Number](http://schema.org/Number)
    + Allowed values: A number between -1 and 1.
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional
   
+ `intensity` : Electric intensity of the circuit. The actual values will be conveyed
by one subproperty per circuit's alternating current phase.  The name of each subproperty
will be equal to the phase name, typically `R`, `S`, `T`. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Default unit: Ampers
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `voltage` : Electric tension of the circuit. The actual values will be conveyed
by one subproperty per circuit's alternating current phase.  The name of each subproperty
will be equal to the phase name, typically `R`, `S`, `T`. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Default unit: Volts
    + Attribute metadata:
        + `dateUpdated`: Timestamp when the last update of the attribute happened.
            + Type: [DateTime](http://schema.org/DateTime)
    + Optional

+ `thdrVoltage` : Total harmonic distortion (R) of the circuit's voltage. The actual values will be conveyed
by one subproperty per circuit's alternating current phase.  The name of each subproperty
will be equal to the phase name, typically `R`, `S`, `T`. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Allowed values: A number between 0 and 1
    + Optional

+ `thdrIntensity` : Total harmonic distortion (R) of the circuit's intensity. The actual values will be conveyed
by one subproperty per circuit's alternating current phase.  The name of each subproperty
will be equal to the phase name, typically `R`, `S`, `T`. 
    + Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    + Allowed values: A value between 0 and 1
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
      "powerStatus": "off", 
      "areaServed": "Calle Comercial Centro",
      "circuit": "C-456-A467",
      "dateLastSwitchingOn":  "2016-07-07T19:59:06.618Z",
      "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",
      "refStreetlightCabinetController": "cabinetcontroller:CC45A34",
      "switchingOnHours": [
        {
          "from" :  "--11-30",
          "to" :    "--01-07",
          "hours" : "Mo,Su 16:00-02:00",
          "description": "Christmas"
        }
      ],
      "intensity": {
         "R": 20.1,
         "S": 14.4,
         "T": 22
      },
      "reactivePower": {
        "R": 45,
        "S": 43.5,
        "T": 42
      }
    }

## Test it with a real service


## Open Issues

+ Do we really need metering attributes on this entity? Is metering only going to be done at Cabinet level? 
