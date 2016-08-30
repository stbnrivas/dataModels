# Off Street Parking

## Description

A site, off street, intended to park vehicles, managed independently and with suitable
and clearly marked access points (entrances and exits).
If necessary, and for management purposes or to deal with multi-location parking sites,
it can de divided into different zones modelled by the entity type [OffStreetParkingZone](../../OffStreetParkingZone/doc/spec.md) .
In DATEX 2 version 2.3 terminology it corresponds to a *UrbanParkingSite* of type *offStreetParking*. 

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `OffStreetParking`.

+ `layout` : Parking layout(s). If the parking site has different zones with different layouts, this property must have a value per
each different zone's layout. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: All defined by the *ParkingLayoutEnum* of DATEX II version 2.3, for instance `underground`. 
        + Or any other value useful for the application and not covered above.
    + Mandatory

+ `usageScenario` : Usage scenario.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the enumeration *ParkingUsageScenarioEnum* and
    *ParkingDurationEnum* of DATEX II version 2.3.
    For instance, `parkAndRide`.
    + Optional
    
+ `highestFloor` : For multistorey parking sites, highest floor.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: An integer number. 0 is ground level. Upper floors are positive numbers. Lower floor are negative ones. 
    + Optional
    
+ `lowestFloor` : For multistorey parking sites, lowest floor.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: An integer number.
    + Optional
    
+ `location` : Geolocation of the parking site represented by a GeoJSON (Multi)Polygon or Point.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory
    
+ `specialLocation` : If the parking site is at a special location (airport, depatment store, etc.)
it conveys what is such special location.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: All values as per the *ParkingSpecialLocationEnum* defined by
    [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a). Example `airportTerminal`. 
    + Optional

+ `address` : Registered parking site civic address.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Optional

+ `name` : Name given to the parking site.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Optional

+ `description` : Description about the parking site. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `owner` : Parking site's owner.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional
    
 + `ownershipType` : Type of ownership (public, private, mixed ...)
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: Those specified by *OwnershipTypeEnum* of DATEX II version 2.3, for instance `public`.
    + Optional
      
+ `reservationType` : Conditions for reservation.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: Those specified by *ReservationTypeEnum* of DATEX II version 2.3, for instance `optional`.
    + Optional

+ `provider` : Parking site service provider.
    + Normative references: [https://schema.org/provider](https://schema.org/provider)
    + Optional
    
+ `contactPoint` : Parking site contact point.
    + Normative references: [https://schema.org/contactPoint](https://schema.org/contactPoint)
    + Optional

+ `allowedVehicleType` : Vehicle type(s) allowed.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed Values: Those values defined by *VehicleTypeEnum*, [DATEX 2 version 2.3](http://www.datex2.eu/sites/www.datex2.eu/files/DATEXIISchema_2_2_2_1.zip)
    + Optional
   
+ `openingHours` : Opening hours of the parking site.
    + Normative references:  [http://schema.org/openingHours](http://schema.org/openingHours)
    + Optional

+ `totalSpotNumber` : The total number of spots offered globally by this parking site. 
This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number or 0. 
    + Normative references: DATEX 2 version 2.3 attribute *parkingNumberOfSpaces* of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The number of spots available globally, excluding reserved spaces, such as those for disabled people,
long term parkers and so on.
This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`. 
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
        
+ `extraSpotNumber` : The number of extra spots *available*, i.e. free. Extra spots are those reserved for special purposes and usually require
a permit. Permit details will be found at parking group level (entity of type `ParkingGroup`).
This value must aggregate free spots from all groups devoted to special parking.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or
    equal to `totalSpotNumber`. 
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
   
+ `occupancyDetectionType` : Occupancy detection method(s).
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: DATEX II version 2.3 *OccupancyDetectionTypeEnum*
    + Optional
    
+ `status` : Status of the parking site. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Allowed values: Those defined by the following enumerations defined by DATEX II version 2.3 :
        + *ParkingSiteStatusEnum*
        + *ParkingConditionsEnum*
        + *OpeningStatusEnum* 
    + Optional
    
+ `firstAvailableFloor` : Number of the floor closest to the ground which currently has available parking spots.
    + Attribute type: [Number](http://schema.org/Number)
    + Metadata:
        + `dateUpdated` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Allowed values: Stories are numbered between -n and n, being 0 ground floor.
    + Optional

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

+ `maximumAllowedHeight` : Maximum allowed height for vehicles. If there are multiple zones, it will be the minimum height of
all the zones. If there is no height limitation this value must be equal to `null`. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional

+ `acceptedPaymentMethod` : Accepted payment method(s)
    + Normative references: https://schema.org/acceptedPaymentMethod
    + Optional

+ `facilities` : Facilities provided by this parking site.
    + Attributes: List of [Text](http://schema.org/Text)
    + Allowed values: All defined by the *EquipmentTypeEnum* enumeration of DATEX II version 2.3, for instance `toilet`, `payDesk`, etc.
    + Optional
    
+ `security` : Security aspects provided by this parking site.
    + Attributes: List of [Text](http://schema.org/Text)
    + Allowed values: All defined by the *ParkingSupervisionEnum* and *ParkingSecurityEnum* of DATEX II version 2.3.
    + Optional

+ `entrance` : Parking site's entrance(s).
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/doc/spec.md)
    + Optional

+ `exit` : Parking site's exit(s).
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/doc/spec.md)
    + Optional
   
+ `maximumAParkingDuration` : Maximum allowed stay at site.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Seconds
    + Optional

+ `chargeType` : Type of charge performed by the parking site.
Note that this attribute can change dynamically depending on time of day or day of week.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the DATEX II version 2.3 *ChargeTypeEnum* enumeration.
    + Optional
    
+ `image` : A URL containing a photo of this parking site.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

+ `aggregateRating` : Aggregated rating for this parking site. 
    + Normative References: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)
    + Optional

+ `refParkingGroup` : Parking site's identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc. 
    + Attribute type: List of references to [ParkingGroup](../../ParkingGroup/doc/spec.md)
    + Optional
    
+ `refParkingSpot` : Individual parking spots belonging to this offstreet parking site.  
    + Attribute type: List of references to [ParkingSpot](../../ParkingSpot/doc/spec.md)
    + Optional    
    
 + `areaServed` : Area served by this parking. Precise semantics can depend on the application or target city.
 For instance, it can be a neighbourhood, burough or district.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional
    
+ `dateModified` : Last update timestamp of this entity
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional
    

## Examples of use

    {
      "type": "OffStreetParking",
      "id": "porto-ParkingLot-23889",
      "name": "Parque de estacionamento Trindade",
      "location": {
        "coordinates": [-8.60961198807, 41.150691773],
        "type": "Point"
      },
      "allowedVehicleType": ["Car"],
      "totalSpotNumber": 414,
      "availableSpotNumber": 132,
      "address": {
        "streetAddress": "Rua de Fernandes Tomás",
        "addressLocality": "Porto",
        "addressCountry": "Portugal"
      },
      "description": "Municipal car park located near the Trindade metro station and the Town Hall",
      "dateModified": "2016-06-02T09:25:55.00Z"
    }

## Test it with a real service

## Open issues

+ How to model tariffs (use DATEX II version 2.3 as possible input)