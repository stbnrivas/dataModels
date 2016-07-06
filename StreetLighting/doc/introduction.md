# Street Lighting Data Models

These data models are intended to model streetlights and all
their controlling equipment towards energy-efficient and effective urban illuminance.
Streetlights, commonly known as 'lamp-posts', are designed to make the streets safer for pedestrians and drivers.

It encompasses the following entity types: 

+ [Streetlight](../Streetlight/doc/spec.md). It represents a particular instance of a streetlight.
A streetlight typically contains a pole with one or more arms and one or more bulbs. 
+ [StreetlightModel](../StreetlightModel/doc/spec.md). It represents a model of streetlight.
Multiple instances of each model will exist as entities of type `Streetlight`. 
+ [StreetlightControlCabinet](../StreetlightControlCabinet/doc/spec.md). It represents equipment, usually on street,
used to control a group of streetlights, i.e. a circuit.
+ [StreetlightControlCabinetModel](../StreetlightControlCabinetModel/doc/spec.md). It represents a model of streetlight control cabinet.
Multiple instances of each model will exist. 