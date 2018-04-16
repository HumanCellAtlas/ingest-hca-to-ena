#!/usr/bin/env bash

# sample $F2B_FILE_SET: 'MantonBM4_HiSeq'
if [ -z "$F2B_FILE_SET" ]; then
    echo $'No file set defined in $F2B_FILE_SET'.
    exit 1
fi

if [ -d output ]; then
    rm -rf output
fi

mkdir -p output

for pattern in $@
do
    ls test-files/$F2B_FILE_SET*$pattern*I1*.txt | xargs cat >> output/$F2B_FILE_SET$(echo _)$pattern$(echo _)I1_001.txt
done
