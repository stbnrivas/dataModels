# On Street Parking

## Description

A site, open space zone, on street, (metered or not) with direct access from a road, intended to park vehicles.
In DATEX 2 version 2.3 terminology it corresponds to a *UrbanParkingSite* of type *onStreetParking*. 

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `OnStreetParking`.

+ `usageScenario` : Usage scenario.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the enumeration *ParkingUsageScenarioEnum* and
    *ParkingDurationEnum* of DATEX II version 2.3.
    For instance, `parkAndRide`.
    + Optional
    
+ `parkingZoneType` : Type of parking zone.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values:
        + All the values specified by the *ParkingTypeOfGroup* enumeration of DATEX II version 2.3.
        + Any value not covered by the above enumeration and meaningful for the application.
    + Mandatory    
       
+ `location` : Geolocation of the parking site represented by a GeoJSON (Multi)Polygon.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory
    
+ `address` : Registered parking site civic address.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional

+ `name` : Name given to the parking zone.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Optional

+ `description` : Description about the parking zone. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `allowedVehicleType` : Vehicle type allowed.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed Values: Those values defined by *VehicleTypeEnum*, [DATEX 2 version 2.3](http://www.datex2.eu/sites/www.datex2.eu/files/DATEXIISchema_2_2_2_1.zip)
    + Optional
   
+ `openingHours` : Opening hours of the parking zone for the general public.
This property allows to capture load / unload zones or any other zone
which can be subject to restrictions at certain times or week days. 
    + Normative references:  [http://schema.org/openingHours](http://schema.org/openingHours)
    + Optional

+ `areBordersMarked` : Denotes whether parking spots are delimited (with blank lines or similar) or not.
    + Attribute type: [Boolean](https://schema.org/Boolean)
    + Optional

+ `totalSpotNumber` : The total number of spots offered by the parking zone.
This can be difficult to be measured at those parking locations on which spots are not clearly limited by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number.
    + Normative references: DATEX 2 version 2.3 attribute `parkingNumberofSpaces` of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The total number of spots available.
This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0.
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `occupancyDetectionType` : Occupancy detection method(s).
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: DATEX II version 2.3 *OccupancyDetectionTypeEnum*
        
+ `parkingMode` : Parking mode(s)
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the DATEX II version 2.3 *ParkingModeEnum* enumeration, for instance `perpendicularParking`. 
    + Optional

+ `averageSpotWidth` : The average width of parking spots.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `averageSpotLength` : The average length of parking spots.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `acceptedPaymentMethod` : Accepted payment method(s)
    + Normative references: https://schema.org/acceptedPaymentMethod
    + Optional
 
+ `maximumAParkingDuration` : Maximum allowed stay at site.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Seconds
    + Optional

+ `requiredPermits` : Required permit(s) for parking at the zone. If this property is not present no permit is needed.
 List semantics is that one of those permits must held in order to park at the site. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the *PermitTypeEnum* enumeration of DATEX II version 2.3. 
    + Optional    

+ `chargeType` : Type of charge performed at the parking zone.
Note that this attribute can change dynamically depending on time of day or day of week.
    + Attribute type: List of [Text](http://schema.org/Number)
    + Allowed values: Those defined by the DATEX II version 2.3 *ChargeTypeEnum* enumeration. 
    
+ `image` : A URL containing a photo of this parking site.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

+ `parkingSpots` : Individual spots belonging to this on street parking site.  
    + Attribute type: List of references to [ParkingSpot](../../ParkingSpot/doc/spec.md)
    + Optional
    
+ `dateModified` : Last update timestamp of this entity
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `areaServed` : Area served by this onstreet parking. Precise semantics can depend on the application or target city.
 For instance, it can be a neighbourhood, burough or district.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional    
  
## Examples of use

    {
      "id": "santander:daoiz_velarde_1_5",
      "type": "OnStreetParking",
      "allowedVehicleType": "Car",
      "availableSpotNumber": 1,
      "dateModified": "2016-06-02T09:25:55.00Z",
      "location": {
        "type": "Polygon",
        "coordinates": [
          [
            [-3.80356167695194, 43.46296641666926 ],
            [-3.803161973253841,43.46301091092682 ],
            [-3.803147082548618,43.462879859445884],
            [-3.803536474744068,43.462838666196674],
            [-3.80356167695194, 43.46296641666926]
          ]
        ]
      },
      "totalSpotNumber": 6,
      "areaServed": "Zona Centro"
    }


## Test it with a real service

## Open issues

+ How to model tariffs