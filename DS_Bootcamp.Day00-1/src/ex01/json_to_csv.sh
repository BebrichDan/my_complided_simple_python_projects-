#!/bin/sh

jq -r -f filter.jq < ../ex00/hh.json > hh.csv
