# Streetlight Model

An entity of type `StreetlightModel` encompasses the structure (column, arm(s) and lantern(s) ) and the corresponding lamp(s) of a street light. 

## Data Model

+ `id` : Entity's unique identifier. 

+ `type` : It must be equal to `StreetlightModel`.

+ `name` : Name given to the streetlight model.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Mandatory

+ `alternateName` : Alternate name given to the streetlight model. 
    + Normative References: [https://schema.org/alternateName](https://schema.org/alternateName)
    + Optional

+ `description` : Description of the streetlight model.
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `powerConsumption` : Power consumption(s) supported by the lantern(s).
    + Attribute type: List of [Number](https://schema.org/Number).
    + Default unit: Watts
    + Optional

+ `columnBrandName` : Name of the column's brand.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/brand](https://schema.org/brand)
    + Optional

+ `columnModelName` : Name of the column's model.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/model)
    + Optional

+ `columnManufacturerName` : Name of the column's manufacturer.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/manufacturer)
    + Optional

+ `lanternModelName` : Name of the lantern's model.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/model)
    + Optional

+ `lanternBrandName` : Name of the lantern's brand.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/brand](https://schema.org/brand)
    + Optional

+ `lanternManufacturerName` : Name of the lantern's manufacturer.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/manufacturer)
    + Optional

+ `lampModelName`

+ `lampBrandName`

+ `lampColorTemperature`

+ `compliantWith`

+ `image`

+ `category`


## Examples of Use


## Test it with a real service

## Open issues