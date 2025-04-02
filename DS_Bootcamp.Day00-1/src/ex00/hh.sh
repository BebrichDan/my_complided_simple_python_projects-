#!/bin/sh

curl "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20" | jq  'walk(if type == "string" then gsub("\u00a0"; " ") else . end)' > hh.json
