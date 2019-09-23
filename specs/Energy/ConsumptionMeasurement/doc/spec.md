# Consumption measurement

## Description

A `ConsumptionMeasurement` entity represent a instantaneous measurement of
consumption that belongs to an electrical circuit, device. This circuit may be
running under DC or AC energy.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](../schema.json).

-   `id` : Entity's unique identifier.

-   `type` : It must be equal to `ConsumptionMeasurement`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Text or URL
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: URL
    -   Optional

-   `dateObserved` : The date and time of this observation in ISO8601 UTCformat.
     It can be represented by an specific time instant or by an ISO8601 interval.

    -   Attribute type: Property. DateTime or an ISO8601 interval represented as Text.
    -   Mandatory

-   `refDevice` : Device used to obtain the measurement.

    -   Attribute type: List of Reference to entity(ies) of type
        [Device](https://github.com/Fiware/dataModels/blob/master/specs/Device/Device/doc/spec.md)
    -   Mandatory

-   `dcPowerConsumption` A measure of DC power consumption instantaneous by device

    -   Attribute type: [Number](http://schema.org/Number)
    -   Default unit: KWT, The unit code (text) of measurement given using the UN/CEFACT
        Common Code (max. 3 characters).
    -   Optional

-   `acPowerConsumption`

    -   Attribute Type: [StructuredValue](http://schema.org/StructuredValue)
    -   Optional

    -   `frequency` : The frequency of the circuit.

        -   Attribute type: [Number](http://schema.org/Number)
        -   Default unit: Hertz (Hz) The unit code (HTZ) of measurement given using the UN/CEFACT
            Common Code (max. 3 characters).
        -   Mandatory

    -   `phases`: from single, double or triple phase asocciated to devices

        -   Attribute type: [Number](http://schema.org/Number)
        -   Optional

    -   `phi`: The angle of difference (in degrees) between current and voltage

        -   Attribute type: [Number](http://schema.org/Number)
        -   Optional

    -   `powerFactor` : The ratio of the real power absorbed by the load to the apparent power
         flowing in the circuit, and is a dimensionless number in the closed interval of −1 to 1.

        -   Attribute type: [Number](http://schema.org/Number)
        -   Mandatory

    -   `activePower` : Real electrical resistance power consumption in circuit

        -   Default unit: KWT, The unit code (KWT) of measurement given using the UN/CEFACT
            Common Code (max. 3 characters).
        -   Optional

    -   `reactivePower`: Imaginary (refers complex number) inductive and Capacitive power
         consumption in circuit

        -   Default unit: kVAr
        -   Optional

    -   `apparentPower`: The power supplied to the electric circuit.
        -   Default unit: KVA
        -   Optional

-   `dateModified` : Last update timestamp of this entity.

    -   Attribute type: [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `dateCreated` : Entity's creation timestamp.

    -   Attribute type: [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a
[FIWARE NGSI version 2](http://fiware.github.io/specifications/ngsiv2/stable)
API implementation, you need to use the `keyValues` mode (`options=keyValues`).

## Examples

### Normalized Example

Normalized NGSI response for AC

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
  "id": "urn:ngsi-ld:ConsumptionMeasurement:santander:energy:CM-061000A3B83",
  "type": "ConsumptionMeasurement",
  "source": "",
  "dataProvider": "bike-in.com",
  "dataObserved": "2019-09-23T13:13:00.00Z",
  "refBattery": "urn:ngsi-ld:Battery:santander:energy:bat-ac-061000A3B83",
  "acPowerConsumption": {
      "frecuency": 50,
      "phases": 3,
      "phi": 60,
      "powerFactor": 0.8,
      "activePower": 0.35,
      "reactivePower": 0.11,
      "apparentPower": 0.4
  }
}
```

```json
{
  "id": "urn:ngsi-ld:ConsumptionMeasurement:santander:energy:CM-061000A3B83",
  "type": "ConsumptionMeasurement",
  "source": "",
  "dataProvider": "bike-in.com",
  "dataObserved": "2019-09-23T13:13:00.00Z",
  "refBattery": "urn:ngsi-ld:Battery:santander:energy:bat-ac-061000A3B83",
  "dcPowerConsumption": 0.05
}
```

## Test it with a real service

## Open Issues
