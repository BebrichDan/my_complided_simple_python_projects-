#!/bin/sh

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv

tail -n +2 ../ex02/hh_sorted.csv | awk -F, '{
    skill = ($3 ~ /Junior/) ? "\"Junior\"" : (($3 ~ /Middle/) ? "\"Middle\"" : (($3 ~ /Senior/) ? "\"Senior\"" : "\"-\""));
    print $1 "," $2 "," skill "," $4 "," $5;
}' >> hh_positions.csv