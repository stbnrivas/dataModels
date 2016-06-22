# Off Street Parking

## Description

A site, off street, intended to park vehicles, managed independently and with suitable
and clearly marked access points (entrances and exits).
If necessary, and for management purposes or to deal with multi-location parking sites,
it can de divided into different zones modelled by the entity type [../../OffStreetParkingZone/spec.md](OffStreetParkingZone).
In DATEX 2 version 2.3 terminology it corresponds to a **UrbanParkingSite* of type *offStreetParking**. 

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

+ `areBordersMarked` : Denotes whether parking spots are delimited (with blank lines or similar) or not.
    + Attribute type: [Boolean](https://schema.org/Boolean)
    + Optional

+ `totalSpotNumber` : The total number of spots offered by the parking site, aggregating data from all its zones (if defined).
This can be difficult to be measured at those parking locations on which spots are not clearly limited by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number.
    + Normative references: DATEX 2 version 2.3 attribute `parkingNumberofSpaces` of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The total number of spots available, aggregating all its zones (if defined).
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
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/spec.md)
    + Optional

+ `exit` : Parking site's exit(s).
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/spec.md)
    + Optional
   
+ `maximumAParkingDuration` : Maximum allowed stay at site.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Seconds
    + Optional

+ `requiredPermits` : Required permit(s) for parking at the site. If this property is not present no permit is needed.
 List semantics is that one of those permits must held in order to park at the site. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the *PermitTypeEnum* enumeration of DATEX II version 2.3. 
    + Optional    

+ `chargeType` : Type of charge performed by the parking site.
Note that this attribute can change dynamically depending on time of day or day of week.
    + Attribute type: List of [Text](http://schema.org/Number)
    + Allowed values: Those defined by the DATEX II version 2.3 *ChargeTypeEnum* enumeration.
    + Optional
    
+ `image` : A URL containing a photo of this parking site.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

+ `aggregateRating` : Aggregated rating for this parking site. 
    + Normative References: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)
    + Optional

+ `parkingZones` : Parking site's identified zones. A zone can correspond to a complete storey, a group of spots, etc. 
    + Attribute type: List of references to [OffStreetParkingZone](../../OffStreetParkingZone/spec.md)
    + Optional

# Test it with a real service

# Open issues

+ How to model tariffs