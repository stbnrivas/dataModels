# Parking Group

## Description

A group of parking spots. Granularity level can vary.
It can be an storey on a parking garage, an specific zone belonging to a big parking lot,  or just a group of spots intended
for parking a certain vehicle type or subject to certain restrictions (disabled, residents, ...).

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `ParkingGroup`.

+ `parkingGroupType` : Type of parking group.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values:
        + All the values specified by the *ParkingTypeOfGroup* enumeration of DATEX II version 2.3.
        + `onstreet` if the parking group belongs to an `OnStreetParking`. 
        + `offstreet` if the parking group belongs to an `OffStreetParking`.
        + Any value not covered by the above enumeration and meaningful for the application.
    + Mandatory

+ `refParkingSite` : Parking site to which this zone belongs to. A group cannot be orphan.
    + Attribute type: Reference to a [OffStreetParking](../../OffStreetParking/doc/spec.md)
    [OnStreetParking](../../OnStreetParking/doc/spec.md) entity. 
    + Mandatory   
   
+ `location` : Geolocation of the parking group represented by a GeoJSON (Multi)Polygon or Point.
If not defined location will be of the parent.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory

+ `address` : Registered parking group civic address.
If not defined address will be of the parent.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional

+ `name` : Name given to the parking group.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Optional

+ `description` : Description about the parking group. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional
      
+ `reservationType` : Conditions for reservation.
If not defined reservation type will be of the parent.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: Those specified by *ReservationTypeEnum* of DATEX II version 2.3, for instance `optional`.
    + Optional

+ `allowedVehicleType` : Vehicle type allowed. If not defined it fallbacks to the group's parent value.
Only one value is allowed here for the sake of cleanness of data models. 
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed Values: Those values defined by *VehicleTypeEnum*, [DATEX 2 version 2.3](http://www.datex2.eu/sites/www.datex2.eu/files/DATEXIISchema_2_2_2_1.zip)
    + Optional
   
+ `areBordersMarked` : Denotes whether parking spots are delimited (with blank lines or similar) or not.
If not defined it fallbacks to the zone's parent value. 
    + Attribute type: [Boolean](https://schema.org/Boolean)
    + Optional

+ `totalSpotNumber` : The total number of spots pertaining to this group. 
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number or 0. 
    + Normative references: DATEX 2 version 2.3 attribute *parkingNumberOfSpaces* of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The number of spots available globally, excluding reserved spaces, such as those for disabled people,
long term parkers and so on.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`. 
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
        
+ `extraSpotNumber` : The number of extra spots *available*, i.e. free. Extra spots are those reserved for special purposes or permit holders
and usually require a permit.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or
    equal to `totalSpotNumber`. 
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    
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

+ `maximumAllowedHeight` : Maximum allowed height for vehicles. If not defined it fallbacks to the value of the zone's parent. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional
    
+ `image` : A URL containing a photo of this parking group.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

+ `refParkingSpot` : Parking spots belonging to this group.
    + Attribute type: List of references to [ParkingSpot](../../ParkingSpot/doc/spec.md)
    + Optional
        
+ `requiredPermits` : Required permit(s) for parking. If not present no permit is needed.
 List semantics is that one of those permits must held in order to park at the zone. If not defined, fallbacks to the parent. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the *PermitTypeEnum* enumeration of DATEX II version 2.3. 
    + Optional
    
+ `chargeType` : Type of charge performed at the parking zone.
Note that this attribute can change dynamically depending on time of day or day of week.
    + Attribute type: List of [Text](http://schema.org/Number)
    + Allowed values: Those defined by the DATEX II version 2.3 *ChargeTypeEnum* enumeration.     
    
+ `maximumAParkingDuration` : Maximum allowed stay.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Seconds
    + Optional
    
+ `dateModified` : Last update timestamp of this entity.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `dateCreated` : Entity's creation date.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional        


## Examples of use

    {
      "id": "daoiz-velarde-1-5-disabled",
      "type": "ParkingGroup",
      "parkingGroupType": ["onstreet", "adjacentSpaces"],
      "refParkingSite": "daoiz-velarde-1-5",
      "description": "Two parking spots reserved for people with disabilities",
      "totalSpotNumber": 2,
      "availableSpotNumber": 0,
      "extraSpotNumber": 1,
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
      "requiredPermits": ["disabledPermit"]
    }

## Test it with a real service


## Open issues

