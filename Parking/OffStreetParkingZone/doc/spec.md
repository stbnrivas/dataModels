# Off Street Parking Zone

## Description

An off street parking zone. Granularity level can vary.
It can be an storey on a parking garage, an specific zone belonging to a big parking lot,  or just a group of spots intended
for parking a certain vehicle type.

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `OffStreetParkingZone`.

+ `parkingZoneType` : Type of parking zone.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values:
        + All the values specified by the *ParkingTypeOfGroup* enumeration of DATEX II version 2.3.
        + Any value not covered by the above enumeration and meaningful for the application.
    + Mandatory

+ `parkingSite` : Parking site to which this zone belongs to. A zone cannot be orphan and must always belong to an `OffStreetParking`.
    + Attribute type: Reference to a [OffStreetParking](../../OffStreetParking/doc/spec.md) entity. 
    + Mandatory

+ `layout` : Parking zone layout. If not defined layout will be of the parent *OffStreetParking*. Only one layout is
allowed for zones, in order to enable clean data models and definitions. 
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: Those defined *ParkingLayoutEnum* of DATEX II version 2.3.     
    + Mandatory
   
+ `location` : Geolocation of the parking zone represented by a GeoJSON (Multi)Polygon or Point.
If not defined location will be of the parent *OffStreetParking*.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory

+ `address` : Registered parking zone civic address.
If not defined address will be of the parent *OffStreetParking*.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional

+ `name` : Name given to the parking zone.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Optional

+ `description` : Description about the parking zone. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional
      
+ `reservationType` : Conditions for reservation.
If not defined reservation type will be of the parent *OffStreetParking*.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: Those specified by *ReservationTypeEnum* of DATEX II version 2.3, for instance `optional`.
    + Optional

+ `allowedVehicleType` : Vehicle type allowed. If not defined it fallbacks to the zone's parent value.
Only one value is allowed here for the sake of cleanness of data models. 
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed Values: Those values defined by *VehicleTypeEnum*, [DATEX 2 version 2.3](http://www.datex2.eu/sites/www.datex2.eu/files/DATEXIISchema_2_2_2_1.zip)
    + Optional
   
+ `areBordersMarked` : Denotes whether parking spots are delimited (with blank lines or similar) or not.
If not defined it fallbacks to the zone's parent value. 
    + Attribute type: [Boolean](https://schema.org/Boolean)
    + Optional

+ `totalSpotNumber` : The total number of spots offered by this zone.
This can be difficult to be measured at those parking locations on which spots are not clearly limited by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number.
    + Normative references: DATEX 2 version 2.3 attribute `parkingNumberofSpaces` of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The total number of spots available at this zone.
This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0.
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `occupancyDetectionType` : Occupancy detection method(s). If not defined it fallbacks to the value of the zone's parent. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: DATEX II version 2.3 *OccupancyDetectionTypeEnum*
    
+ `parkingMode` : Parking mode(s). If not defined it fallbacks to the value of the zone's parent. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the DATEX II version 2.3 *ParkingModeEnum* enumeration, for instance `perpendicularParking`. 
    + Optional

+ `averageSpotWidth` : The average width of parking spots. If not defined it fallbacks to the value of the zone's parent. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `averageSpotLength` : The average length of parking spots. If not defined it fallbacks to the value of the zone's parent. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `maximumAllowedHeight` : Maximum allowed height for vehicles at this zone. If not defined it fallbacks to the value of the zone's parent. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `entrance` : Zone entrance(s). If not defined, entrances will be those of the parking site this zone belongs to. 
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/doc/spec.md)
    + Optional

+ `exit` : Zone exit(s). If not defined, exists will be those of the parking site this zone belongs to.
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/doc/spec.md)
    + Optional
    
+ `image` : A URL containing a photo of this parking zone.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

+ `parkingSpots` : Parking spots belonging to this zone.
    + Attribute type: List of references to [ParkingSpot](../../ParkingSpot/doc/spec.md)
    + Optional
    
+ `status` : Status of the parking zone. 
    + Attribute type: [Text](http://schema.org/Text)
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Allowed values: Those defined by the following enumerations defined by DATEX II version 2.3 :
        + *ParkingSiteStatusEnum*
    + Optional
    
+ `requiredPermits` : Required permit(s) for parking at the zone. If not present no permit is needed.
 List semantics is that one of those permits must held in order to park at the zone. If not defined, fallbacks to the parent. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the *PermitTypeEnum* enumeration of DATEX II version 2.3. 
    + Optional
    
 
+ `maximumAParkingDuration` : Maximum allowed stay at zone.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Seconds
    + Optional
    
+ `dateUpdated` : Last update timestamp of this entity
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional    


## Examples of use

## Test it with a real service

## Open issues

+ Attributes allowed on this entity vs OffStreetParking.
