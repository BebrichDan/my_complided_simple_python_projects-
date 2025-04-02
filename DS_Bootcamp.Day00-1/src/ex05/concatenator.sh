#!/bin/sh

output_file="all_hh_data.csv"
temp_file="all_hh_data_temp.csv"

rm -f "$output_file"

for file in hh_*.csv; do
  if [ -f "$file" ]; then
    if [ ! -f "$output_file" ]; then
      cat "$file" >> "$output_file"
    else
      tail -n +2 "$file" >> "$output_file"
    fi
  fi
done

tail -n +2 "$output_file" | sort -d -t "," -k2 | sort -d -t "," -k1 > "$temp_file"

header=$(head -n 1 "$output_file")
echo "$header" > "$output_file"
cat "$temp_file" >> "$output_file"

rm "$temp_file"