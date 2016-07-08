# Data models guidelines

This is a set of guidelines for defining new data models. 

## Syntax

+ Use English terms, preferably American English.
+ Use camel case syntax for properties (`camelCase`). 
+ Entity type names must start with a Capital letter, for instance, `WasteContainer`.
+ Use names and not verbs for properties, ex. `name`, qualifying it when necessary, ex. `totalSpotNumber` or `dateCreated`.
+ Avoid plurals in property names, but state clearly when a list of items fits. Ex. `category`. 

## Reuse

+ Check for the existence of the same property on any of the other models and reuse it, if pertinent. 
+ Have a look at [schema.org](http://schema.org) trying to find a similar term with the same semantics.
+ Try to find common used ontologies or existing standards well accepted by the Community, or by goverments, agencies, etc.
For instance, [Open311](http://www.open311.org/) for civic issue tracking or [Datex II](http://www.datex2.eu/) for transport systems. 

## Data types

+ When possible reuse schema.org data types (`Text`, `Number`, `DateTime`, `StructuredValue`, etc.).

## Property definition

+ Enumerate the allowed values for each property. Generally speaking it is a good idea to leave it open for applications
to extend the list, provided the new value is not semantically covered by any of the existing ones.

+ State clearly what properties are mandatory and what are optional. If needed state clearly what is the meaning of a
`null` value. 

## Units

+ Define a default unit for magnitudes. Normally it will be the unit as stated by the international system of units.

+ If a quantity is expressed in a different unit than the default one, use the [unitCode](http://schema.org/unitCode) metadata
property.

## Relative values

+ Use values between `0` and `1` for relative quantities, which represent property values
such as `relativeHumidity`, `precipitationProbability`, etc. 

## Modelling location

+ Use `address` property for civic locations as per [schema.org](http://schema.org/address)

+ Use `location` property for geographical coordinates. Ideally use GeoJSON for codifying geospatial properties. That works
from Orion 1.2 on. If not use, old NGSI version 1 type `coords`.

## Modelling linked data

+ When an entity attribute is used as a link to other entities name
it with the prefix `ref` plus the name of the target (linked) entity type. For instance `refStreetlightModel`, represents an attribute
which contains a reference to an entity of type `StreetlightModel`. 

## Property names for dates

+ Type must be `DateTime`.

+ Use `dateCreated` for creation dates. Be careful that this date can be different than the entity creation date.

+ Use `dateUpdated` for update dates.

+ Use the `date` prefix for naming entity attributes representing dates (or complete timestamps). Ex. `dateLastEmptying`. 

## Dynamic properties

+ Use a metadata attribute named `dateUpdated` for capturing the last update time of a dynamic property.

## Some of the most used properties

In case of doubt check other existing models! 

+ `name`
+ `alternateName`
+ `description`
+ `serialNumber`
+ `category`
+ `features`
+ `source`
+ `relativeHumidity`
+ `temperature`
+ `dateCreated`
+ `dateUpdated`