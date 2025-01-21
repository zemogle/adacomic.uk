#!/bin/bash

# read -p 'Process files from path: ' fromdir
fromdir=$1

trap "exit" INT
ls "$fromdir"*.md | while read filename; do
    echo "Converting $filename"
    sed -i '' -e 's/+\{2,\}//g' $filename
    sed -i '' -e 's+ =+:+g' $filename
    sed -i '' -e 's+: "+: +g' $filename
    sed -i '' -e 's+Z"++g' $filename
    sed -i '' -e 's+"++g' $filename
    sed -i '' -e '2,$b' -e '/^$/d' $filename
done
