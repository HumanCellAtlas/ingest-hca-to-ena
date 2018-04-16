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

function concat_subgroup {
    ls test-files/$F2B_FILE_SET*$pattern*$1*.txt | xargs cat >> output/$F2B_FILE_SET$(echo _)$pattern$(echo _)$1_001.txt
}

for pattern in $@
do
    concat_subgroup I1
    concat_subgroup R1
    concat_subgroup R2
done
