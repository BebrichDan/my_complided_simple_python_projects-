#!/bin/sh

# Заголовок, который нужно добавить в каждый файл
header='"id","created_at","name","has_test","alternate_url"'

# Обработка данных
tail -n +2 ../ex03/hh_positions.csv | sort -d -t "," -k2 | awk -v header="$header" -F',' '{
    date = substr($2, 0, 11)

    if (date ~ /^"[0-9]{4}-[0-9]{2}-[0-9]{2}$/) {
        filename = "hh_" date ".csv"
        
        # Если файл не существует, добавляем заголовок
        if (!file_created[filename]) {
            print header > filename
            file_created[filename] = 1
        }
        
        # Добавляем строку в соответствующий файл
        print $0 >> filename
    }
}'
