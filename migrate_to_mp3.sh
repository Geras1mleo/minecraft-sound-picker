#!/bin/bash

files=$(find sounds -type f)

for file in $files; do
    new_name=${file//.ogg/.mp3}
    ffmpeg -i "$file" -f mp3 "$new_name"
done
