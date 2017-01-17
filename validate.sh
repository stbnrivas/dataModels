#!/bin/sh

ajv validate --v5 -s $1 -r schema-common.json -r geometry-schema.json -d $2
