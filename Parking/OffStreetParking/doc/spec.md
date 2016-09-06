# Off Street Parking

## Description

A site, off street, intended to park vehicles, managed independently and with suitable
and clearly marked access points (entrances and exits).
If necessary, and for management purposes or to deal with multi-location parking sites,
it can be divided into different zones modelled by the entity type [ParkingGroup](../../ParkingGroup/doc/spec.md) .
In DATEX 2 version 2.3 terminology it corresponds to a *UrbanParkingSite* of type *offStreetParking*. 

## Data Model

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `OffStreetParking`.
   
+ `dateCreated` : Entity's creation timestamp
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional

+ `dateModified` : Last update timestamp of this entity
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `location` : Geolocation of the parking site represented by a GeoJSON (Multi)Polygon or Point.
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/draft-ietf-geojson-03](https://tools.ietf.org/html/draft-ietf-geojson-03)
    + Mandatory if `address` is not defined.
    
+ `address` : Registered parking site civic address.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Mandatory if `location` is not defined.
    
+ `name` : Name given to the parking site.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Mandatory

+ `category` : Parking site's category. The purpose of this field is to allow to tag, generally speaking, off street parking entities.
Particularities and detailed descriptions should found under the corresponding specific attributes.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values:
        + (`public`, `private`, `urbanDeterrentParking`, `garage`,
           `shortTerm`, `mediumTerm`, `longTerm`,
           `free`, `feeCharged`,
           `staffed`, `guarded`, `barrierAccess`, `gateAccess`, `freeAccess`, 
           `underground`, `ground`,
           `disabledAccessible`,
           `forResidents`, `forDisabled`, `forCustomers`, `forVisitors`, `forEmployees`)
        + Other application-specific
    + Mandatory
    
+ `allowedVehicleType` : Vehicle type(s) allowed. The first element of this array *MUST* be the principal vehicle type allowed i.e. the one used
for reporting the `availableSpotNumber` attribute. Free spot numbers of other allowed vehicle types will be
reported under the attribute `extraSpotNumber` and specific entities of type *ParkingGroup*. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed Values: The following values defined by *VehicleTypeEnum*, [DATEX 2 version 2.3](http://www.datex2.eu/sites/www.datex2.eu/files/DATEXIISchema_2_2_2_1.zip):
        + (`agriculturalVehicle`, `bicycle`, `bus`, `car`, `caravan`,
           `carWithCaravan`, `carWithTrailer`, `constructionOrMaintenanceVehicle`, `lorry`, `moped`, `motorcycle`, `motorcycleWithSideCar`,
           `motorscooter`, `tanker`, `trailer`, `van`, `anyVehicle`)
    + Mandatory
    
+ `description` : Description about the parking site. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional
    
+ `image` : A URL containing a photo of this parking site.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional
 
+ `layout` : Parking layout.  
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values:  As per the *ParkingLayoutEnum* of DATEX II version 2.3:
        + one Of (`automatedParkingGarage`, `surface`, `multiStorey`, `singleLevel`, `multiLevel`,
        `openSpace`, `covered`, `nested`, `field`, `rooftop`,
        `sheds`, `carports`, `garageBoxes`, `other`). See also [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking). 
        + Or any other value useful for the application and not covered above.
    + Optional
    
+ `usageScenario` : Usage scenario.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the enumeration *ParkingUsageScenarioEnum* of DATEX II version 2.3:
        + (`truckParking`, `parkAndRide`, `parkAndCycle`,	`parkAndWalk`, `kissAndRide`, `	liftshare`, `carSharing`,
            `restArea`, `serviceArea`, `dropOffWithValet`, `dropOffMechanical`, `eventParking`, `automaticParkingGuidance`,
            `staffGuidesToSpace`,  `vehicleLift`, `loadingBay`, `dropOff`, `overnightParking`, `other`)
        + Or any other value useful for the application and not covered above.
    + Optional
    
+ `parkingMode` : Parking mode(s).
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Those defined by the DATEX II version 2.3 *ParkingModeEnum* enumeration:
        + (`perpendicularParking`, `parallelParking`, `echelonParking`)
    + Optional
    
+ `facilities` : Facilities provided by this parking site.
    + Attributes: List of [Text](http://schema.org/Text)
    + Allowed values: The following defined by the *EquipmentTypeEnum* enumeration of DATEX II version 2.3:
        + (`toilet`, `shower`, `informationPoint`, `internetWireless`, `payDesk`, `paymentMachine`, `cashMachine`, `vendingMachine`,
        `faxMachineOrService`, `copyMachineOrService`, `safeDeposit`, `luggageLocker`, `publicPhone`, `elevator`, `dumpingStation`
        `freshWater`, `wasteDisposal`, `refuseBin`, `iceFreeScaffold`, `playground`, `electricChargingStation`, `bikeParking`, `tollTerminal`,
        `defibrillator`, `firstAidEquipment` `fireHose` `fireExtinguisher` `fireHydrant`)
        + Any other application-specific
    + Optional
    
+ `security` : Security aspects provided by this parking site.
    + Attributes: List of [Text](http://schema.org/Text)
    + Allowed values: The following, some of them, defined by *ParkingSecurityEnum* of DATEX II version 2.3:
        + (`patrolled`, `securityStaff`, `externalSecurity`, `cctv`, `dog`, `guard24hours`, `lighting`, `floodLight`, `fences`
        `areaSeperatedFromSurroundings`)
        + Any other application-specific
    + Optional    
    
+ `highestFloor` : For multistorey parking sites, highest floor.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: An integer number. 0 is ground level. Upper floors are positive numbers. Lower floors are negative ones. 
    + Optional
    
+ `lowestFloor` : For multistorey parking sites, lowest floor.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: An integer number.
    + Optional
    
+ `maximumAParkingDuration` : Maximum allowed stay at site encoded as a ISO8601 duration.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional

+ `chargeType` : Type of charge performed by the parking site. If no charge this attribute 
Note that this attribute can change dynamically depending on time of day or day of week.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: Some of those defined by the DATEX II version 2.3 *ChargeTypeEnum* enumeration:
        + (`flat`, `minimum`, `maximum`, `additionalIntervalPrice` `seasonTicket` `temporaryPrice` `firstIntervalPrice`,
        `annualPayment`, `monthlyPayment`, `other`)
        + Any other application-specific
    + Optional
    
+ `acceptedPaymentMethod` : Accepted payment method(s)
    + Normative references: https://schema.org/acceptedPaymentMethod
    + Optional
    
+ `requiredPermit` : This attribute captures what permit(s) are needed to park at this site.
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: The following, defined by the *PermitTypeEnum* enumeration of DATEX II version 2.3.
        + oneOf (`employeePermit`, `fairPermit`, `governmentPermit`,  `residentPermit`, `specificIdentifiedVehiclePermit`,
        `disabledPermit`, `visitorPermit`)
        + Any other application-specific
    + Optional
    
+ `totalSpotNumber` : The total number of spots offered globally by this parking site. 
This number can be difficult to be obtained for those parking locations on which spots are not clearly marked by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: Any positive integer number or 0. 
    + Normative references: DATEX 2 version 2.3 attribute *parkingNumberOfSpaces* of the *ParkingRecord* class.
    + Optional

+ `availableSpotNumber` : The number of spots available globally for the principal allowed vehicle type,
excluding reserved spaces, such as those for disabled people,long term parkers and so on.
This might be harder to estimate at those parking locations on which spots borders are not clearly marked by lines.
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. It must lower or equal than `totalSpotNumber`. 
    + Metadata:
        + `timestamp` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
        
+ `extraSpotNumber` : The number of extra spots *available*, i.e. free. This value must aggregate free spots from all groups mentioned below:
A/ those reserved for special purposes and usually require a permit. Permit details will be found at
parking group level (entity of type `ParkingGroup`).
B/ Those reserved for other vehicle types different than the principal allowed vehicle type.  
    + Attribute type: [Number](http://schema.org/Number)
    + Allowed values: A positive integer number, including 0. `extraSpotNumber` plus `availableSpotNumber` must be lower than or
    equal to `totalSpotNumber`. 
    + Metadata:
        + `timestamp` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Optional
       
+ `openingHours` : Opening hours of the parking site.
    + Normative references:  [http://schema.org/openingHours](http://schema.org/openingHours)
    + Optional
    
+ `firstAvailableFloor` : Number of the floor closest to the ground which currently has available parking spots.
    + Attribute type: [Number](http://schema.org/Number)
    + Metadata:
        + `timestamp` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Allowed values: Stories are numbered between -n and n, being 0 ground floor.
    + Optional
            
+ `specialLocation` : If the parking site is at a special location (airport, depatment store, etc.)
it conveys what is such special location.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: Those defined by *ParkingSpecialLocationEnum* of
    [DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a):
        + (`airportTerminal`, `exhibitonCentre`, `shoppingCentre`, `specificFacility`, `trainStation`,
        `campground`, `themePark`, `ferryTerminal`, `vehicleOnRailTerminal`, `coachStation`, `cableCarStation`, `publicTransportStation`,
        `market`, `religiousCentre`, `conventionCentre`, `cinema`, `skilift`, `hotel`, `other`)
    + Optional
    
+ `occupancyDetectionType` : Occupancy detection method(s).
    + Attribute type: List of [Text](http://schema.org/Text)
    + Allowed values: The following from DATEX II version 2.3 *OccupancyDetectionTypeEnum*:
        + (`none`, `balancing`, `singleSpaceDetection`, `modelBased`, `manual`)
        + Or any other application-specific
    + Optional
    
+ `status` : Status of the parking site. 
    + Attribute type: List of [Text](http://schema.org/Text)
    + Metadata:
        + `timestamp` : Timestamp of the last attribute update
        + Type: [DateTime](https://schema.org/DateTime)
    + Allowed values: The following defined by the following enumerations defined by DATEX II version 2.3 :
        + *ParkingSiteStatusEnum*
        + *OpeningStatusEnum*
        + (`open`, `closed`, `closedAbnormal`,`openingTimesInForce`, `full`,
           `fullAtEntrance`, `spacesAvailable`, `almostFull`)
        + Or any other application-specific
    + Optional

+ `reservationType` : Conditions for reservation.
    + Attribute type: [Text](http://schema.org/Text)
    + Allowed values: The following specified by *ReservationTypeEnum* of DATEX II version 2.3:
        + one Of (`optional`, `mandatory`, `notAvailable`, `partly`).
    + Optional

+ `owner` : Parking site's owner.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional
         
+ `provider` : Parking site service provider.
    + Normative references: [https://schema.org/provider](https://schema.org/provider)
    + Optional
    
+ `contactPoint` : Parking site contact point.
    + Normative references: [https://schema.org/contactPoint](https://schema.org/contactPoint)
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
all the zones.
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional
    
+ `maximumAllowedWidth` : Maximum allowed width for vehicles. If there are multiple zones, it will be the minimum width of
all the zones. 
    + Attribute type: [Number](http://schema.org/Number)
    + Default unit: Meters
    + Optional    

+ `refParkingAccess` : Parking site's access point(s).
    + Attribute type: List of references to [ParkingAccess](../../ParkingAccess/doc/spec.md)
    + Optional
       
+ `refParkingGroup` : Parking site's identified group(s). A group can correspond to a zone, a complete storey, a group of spots, etc. 
    + Attribute type: List of references to [ParkingGroup](../../ParkingGroup/doc/spec.md)
    + Optional
    
+ `refParkingSpot` : Individual parking spots belonging to this offstreet parking site.  
    + Attribute type: List of references to [ParkingSpot](../../ParkingSpot/doc/spec.md)
    + Optional    
    
 + `areaServed` : Area served by this parking site. Precise semantics can depend on the application or target city.
 For instance, it can be a neighbourhood, burough or district.
    + Attribute type: [Text](http://schema.org/Text)
    + Optional
    
+ `aggregateRating` : Aggregated rating for this parking site. 
    + Normative References: [https://schema.org/aggregateRating](https://schema.org/aggregateRating)
    + Optional

## Examples of use

    {
      "type": "OffStreetParking",
      "id": "porto-ParkingLot-23889",
      "name": "Parque de estacionamento Trindade",
      "category": ["underground", "public", "feeCharged", "mediumTerm", "barrierAccess"],
      "chargeType": ["temporaryFee"],
      "layout": ["multiStorey"],
      "maximumParkingDuration": "PT8H",
      "location": {
        "coordinates": [-8.60961198807, 41.150691773],
        "type": "Point"
      },
      "allowedVehicleType": ["car"],
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