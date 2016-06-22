# Parking Harmonized Data Models

These data models are intended to model entities relevant for parking use cases in smart cities scenarios.
When feasible these models reuse types, properties and enumerations from
[DATEX II version 2.3](http://www.datex2.eu/content/parking-publications-extension-v10a).
Nonetheless, these data models are intended to NGSI-based systems and
many simplifications has been made with respect to DATEX II version 2.3. 
 
The main entity types identified are:

+ [OffStreetParking](../OffStreetParking/doc/spec.md). An offstreet parking site with explicit entries and exits.
+ [ParkingAccess](../ParkingAccess/doc/spec.md). An access point to an off street parking site.
+ [OffStreetParkingZone](../OffStreetParkingZone/doc/spec.md). An off street parking zone. Granularity level can vary.
It can be an storey on a parking garage, an specific area belonging to a big parking lot etc or just a group of spots. 
+ [OnStreetParking](../OnStreetParking/doc/spec.md). An on street, free entry (but might be metered) parking zone
which contains at least one ore more adjacent parking spots.
+ [ParkingSpot](../ParkingSpot/doc/spec.md). An individual, usually monitored, parking spot. 