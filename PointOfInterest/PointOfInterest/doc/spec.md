# Point of interest

## Description

This entity contains a harmonised geographic description of a Point of Interest. This entity is
used in applications that use spatial data and is applicable to Automotive, Environment,
Industry and Smart City vertical segments and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found {{add link to JSON Schema}}

+ `id` : Unique identifier. 

+ `type` : Entity type. It must be equal to `PointOfInterest`.

+ `dateModified` : Last update timestamp of this entity.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional

+ `dateCreated` : Entity's creation timestamp.
    + Attribute type: [DateTime](https://schema.org/DateTime)
    + Optional
    
+ `source` : A sequence of characters giving the source of the entity data.
    + Attribute type: [Text](https://schema.org/Text) or [URL](https://schema.org/URL)
    + Optional    
    
+ `name` : Name of this point of interest.
    + Normative References: [https://schema.org/name](https://schema.org/name)
    + Mandatory

+ `description` : Description of this point of interest.
    + Normative References: [https://schema.org/description](https://schema.org/description]
    + Optional

+ `location` : Location of the point of interest represented by a GeoJSON geometry. 
    + Attribute type: `geo:json`.
    + Normative References: [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    + Mandatory if `address` is not defined. 
    
+ `address` : Civic address of this point of interest.
    + Normative References: [https://schema.org/address](https://schema.org/address)
    + Mandatory if `location` is not present.
    
+ `category` : Category of this point of interest. 
    + Attribute type: List of text [Text](https://schema.org/Text)
    + Allowed values: Those defined by the [Factual taxonomy](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json).
    For instance the value `113` corresponds to beaches, and the value `311` corresponds to museums. 
    + Mandatory
    
+ `refSeeAlso` : Reference to one or more related entities that may provide extra,
specific information about this point of interest.
    + Attribute type: List of References
    + Optional
    
## Examples of use

    {
        "id": "PointOfInterest-A-Concha-123456",
        "type": "PointOfInterest",
        "name": "Playa de a Concha",
        "description": "La Playa de A Concha se presenta como una continuación de la Playa de Compostela, una de las más frecuentadas de Vilagarcía.",
        "address": {
          "addressCountry": "ES",
          "addressLocality": "Vilagarcía de Arousa"
        },
        "category": ["113"],
        "location": {
          "type": "Point",
          "coordinates": [
            -8.768460000000001,
            42.60214472222222
          ]
        },
        "source": "http://www.tourspain.es",
        "refSeeAlso": ["Beach-A-Concha-123456"]
    }

    
## Use it with a real service

Coming soon

## Open Issues

