#!/bin/sh

echo '"name","count"' > hh_uniq_positions.csv

tail -n +2 ../ex03/hh_positions.csv |
 awk -F, '$3 != "\"-\"" {print $3}'|
 sort |
 uniq -c |
 awk '{printf "%s, %d\n", $2, $1}' |
 sort -k2 -rn >> hh_uniq_positions.csv