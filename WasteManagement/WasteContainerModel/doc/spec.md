# Waste Container Model

## Description

A model of waste container which captures the static properties of a class of containers. 

## Data Model

+ `id` : Unique identifier. 

+ `type`: Entity Type. It must be equal to `WasteContainerModel`.

+ `name`. Name given to the container model
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Mandatory

+ `width`. Width of the container.
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: Meters
    + See also: [https://schema.org/width](https://schema.org/width)
    + Optional 

+ `height`. Height of the container. 
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: Meters
    + See also: [https://schema.org/height](https://schema.org/height)
    + Optional 

+ `depth`. Depth of the container.
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: Meters
    + See also: [https://schema.org/depth](https://schema.org/depth)
    + Optional

+ `weight`. Weight of the container.
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: Kilograms
    + See also: [https://schema.org/weight](https://schema.org/weight)
    + Optional

+ `volume`. Total volume the container can hold.
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: cubic meters
    + Optional
       
+ `maximumLoad`. Maximum load the container can hold safely.
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: Kilograms
    + Optional

+ `recommendedLoad`. Manufacturer recommended load for the container.
    + Attribute type: [Number](https://schema.org/Number).
    + Unit: Kilograms
    + Optional

+ `shape`. Container’s shape. TBD. 
    + Attribute type: [Text](https://schema.org/Text).
    + Optional

+ `coverType`
    + Attribute type: [Text](https://schema.org/Text)
    + Allowed values: one Of (`flat`, `round`, `none`)
    + Optional
  
+ `insertHolesNumber`. Number of insert holes the container has.
    + Attribute type: [Number](https://schema.org/Number).
    + Optional

+ `madeOf`. Material the container is made of. 
    + Attribute type: [Text](https://schema.org/Text)
    + Allowed values: one Of (`plastic`, `wood` , `metal`, `other`)
    + Optional
    
+ `madeOfCode`. Material Code as per standard tables. TBD.
    + Attribute type: [Text](https://schema.org/Text)
    + Optional
       
+ `brandName`. Name of the brand.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/brand](https://schema.org/brand)
    + Optional
       
+ `modelName`. Name of the model.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/model)
    + Optional
    
+ `manufacturerName`. Name of the manufacturer.
    + Attribute type: [Text](https://schema.org/Text)
    + See also: [https://schema.org/model](https://schema.org/manufacturer)
    + Optional
    
+ `description`. Description about the waste container model. 
    + Normative References: [https://schema.org/description](https://schema.org/description)
    + Optional

+ `colors`.  Available colors.
    + Attribute type: List of [Text](https://schema.org/Text)
    + Allowed Values:
        + A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords)
        + A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)
    + See also: [https://schema.org/color](https://schema.org/color)
    + Optional

+ `image`. A URL containing a photo of the container model.
    + Normative References: [https://schema.org/image](https://schema.org/image)
    + Optional

    
## Example


## Test it with a real service


## Open issues

