# Energy

This folder contains domain specific data models related to energy. Currently
theses entity type has been defined:

-   `Battery`: represent a battery which belongs to an entity. It contains
    identification specifications of battery and use time.

-   `BatteryStatus`: represent a instantaneous of status associated to a
    single entity of `EnergyBattery` entity for historical purposes.

-   `ConsumptionMeasurement`: represent a instantaneous measurement associated to an
    entity, can be IoT device, circuit AC, circuit DC with electric energy consumption.

-   `ThreePhaseMultiCircuitAcMeasurement`: represents a measurement from an electrical
    sub-metering system that monitors three-phase alternating current across multiple
    circuits
