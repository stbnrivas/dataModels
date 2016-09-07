# Parking Group

## Description

A group of parking spots. Granularity level can vary.
It can be an storey on a parking garage, an specific zone belonging to a big parking lot,  or just a group of spots intended
for parking a certain vehicle type or subject to certain restrictions (disabled, residents, ...).
For the sake of simplicity only one vehicle type per parking group is allowed. Similarly, one required permit is only allowed
per group type. 

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `ParkingGroup`.

+ `category` : Parking Group's category. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values:
        + `onstreet` if the parking group belongs to an `OnStreetParking`. 
        + `offstreet` if the parking group belongs to an `OffStreetParking`.
        + (`adjacentSpaces`, `nonAdjacentSpaces`, `completeFloor`, `statisticsOnly`,
           `vehicleTypeSpaces`, `particularConditionsSpaces`)
        + (`onlyDisabled`, `onlyResidents`, `onlyLoadUnload`, `onlyWithPermit`, `forELectricalCharging`)
        + (`free`, `feeCharged`)
        + (`blueZone`, `greenZone`)
        + Any value not covered by the above enumeration and meaningful for the application.
    + Mandatory

+ `refParkingSite` : Parking site to which this zone belongs to. A group cannot be orphan. A group cannot have subgroups.
    + Attribute type: Reference to an [OffStreetParking](../../OffStreetParking/doc/spec.md) or to an
    [OnStreetParking](../../OnStreetParking/doc/spec.md) entity. 
    + Mandatory
    
+ `allowedVehicleType` : Vehicle type allowed (a parking group only allows one vehicle type). 
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed Values: The following values defined by *VehicleTypeEnum*
    [DATEX 2 version 2.3](http://www.datex2.eu/sites/www.datex2.eu/files/DATEXIISchema_2_2_2_1.zip) :
        + (`agriculturalVehicle`, `bicycle`, `bus`, `car`, `caravan`,
           `carWithCaravan`, `carWithTrailer`, `constructionOrMaintenanceVehicle`, `lorry`, `moped`, `motorcycle`,
           `motorcycleWithSideCar`, `motorscooter`, `tanker`, `trailer`, `van`, `anyVehicle`)
    + Mandatory
       
+ `location` : Geolocation of the parking group represented by a GeoJSON (Multi)Polygon or Point.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Optional

+ `address` : Registered parking group civic address. 
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional

+ `name` : Name given to the parking group.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Optional

+ `description` : Description about the parking group. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `maximumAParkingDuration` : Maximum allowed stay encoded as a ISO8601 duration.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional

+ `chargeType` : Type of charge performed when parking on any of the spots pertaining to this group.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Some of those defined by the DATEX II version 2.3 *ChargeTypeEnum* enumeration:
        + (`flat`, `minimum`, `maximum`, `additionalIntervalPrice` `seasonTicket` `temporaryPrice` `firstIntervalPrice`,
        `annualPayment`, `monthlyPayment`, `free`, `other`)
        + Any other application-specific
    + Optional
    
+ `requiredPermit` : This attribute captures what permit is needed to park in any of the spots of this group. For the
sake of simplicity only one permit can be associated to a parking group. When a permit is composed by more than one item
they can be combined by separating them with a ",". For instance "residentPermit,disabledPermit" stays that both
a resident and a disabled permit are needed to park. 
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: The following, defined by the *PermitTypeEnum* enumeration of DATEX II version 2.3.
        + oneOf (`employeePermit`, `studentPermit`, `fairPermit`, `governmentPermit`,  `residentPermit`, `specificIdentifiedVehiclePermit`,
        `disabledPermit`, `visitorPermit`, `blueZonePermit` `careTakingPermit` `carpoolingPermit` `carSharingPermit` `emergencyVehiclePermit`
        `maintenanceVehiclePermit`, `roadWorksPermit`, `taxiPermit`)
        + Any other application-specific
    + Optional   

+ `reservationType` : Conditions for reservation.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: The following specified by *ReservationTypeEnum* of DATEX II version 2.3:
        + one Of (`optional`, `mandatory`, `notAvailable`, `partly`).
    + Optional
   
+ `areBordersMarked` : Denotes whether parking spots are delimited (with blank lines or similar) or not.
    + Attribute type: [Boolean](https://schema.org/Boolean)
    + Optional

+ `totalSpotNumber` : The total number of spots pertaining to this group. 
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number or 0. 
    + Normative references: DATEX 2 version 2.3 attribute *parkingNumberOfSpaces* of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The number of spots available in this group.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`. 
    + Metadata:
        + `timestamp` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
            
+ `occupancyDetectionType` : Occupancy detection method(s).
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: The following from DATEX II version 2.3 *OccupancyDetectionTypeEnum*:
        + (`none`, `balancing`, `singleSpaceDetection`, `modelBased`, `manual`)
        + Or any other application-specific
    + Optional
    
+ `parkingMode` : Parking mode(s).
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the DATEX II version 2.3 *ParkingModeEnum* enumeration:
        + (`perpendicularParking`, `parallelParking`, `echelonParking`)
    + Optional

+ `averageSpotWidth` : The average width of parking spots. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `averageSpotLength` : The average length of parking spots. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `maximumAllowedHeight` : Maximum allowed height for vehicles. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `maximumAllowedWidth` : Maximum allowed width for vehicles. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional
    
+ `image` : A URL containing a photo of this parking group.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

+ `refParkingSpot` : Parking spots belonging to this group.
    + Attribute type: List of references to [ParkingSpot](../../ParkingSpot/doc/spec.md)
    + Optional
        
## Examples of use

    {
      "id": "daoiz-velarde-1-5-disabled",
      "type": "ParkingGroup",
      "category": ["onstreet", "adjacentSpaces", "onlyDisabled"],
      "refParkingSite": "daoiz-velarde-1-5",
      "description": "Two parking spots reserved for people with disabilities",
      "totalSpotNumber": 2,
      "availableSpotNumber": 1,
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
      "requiredPermit": ["disabledPermit"]
    }

## Test it with a real service


## Open issues

