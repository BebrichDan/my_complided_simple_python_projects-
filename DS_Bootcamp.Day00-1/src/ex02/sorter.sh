#!/bin/sh

{ head -n 1 ../ex01/hh.csv ; tail -n +2 ../ex01/hh.csv | sort -d -t "," -k2 | sort -d -t "," -k1; } > hh_sorted.csv