#!/usr/bin/env bash

[ -z "$F2B_FILE_EXT" ] && export F2B_FILE_EXT=fastq.gz
[ -z "$F2B_FILE_DIR" ] && export F2B_FILE_DIR=$PWD

# sample $F2B_FILE_SET: 'MantonBM4_HiSeq'
if [ -z "$F2B_FILE_SET" ]; then
    echo $'No file set defined in $F2B_FILE_SET'.
    exit 1
fi

if [ -d $F2B_FILE_DIR/output ]; then
    rm -rf $F2B_FILE_DIR/output
fi

mkdir -p $F2B_FILE_DIR/output

function concat_subgroup {
    file_name=$F2B_FILE_DIR/output/$F2B_FILE_SET$(echo _)$pattern$(echo _)$1_001.$F2B_FILE_EXT
    ls $F2B_FILE_DIR/$F2B_FILE_SET*$pattern*$1*.$F2B_FILE_EXT |\
	xargs cat >> $file_name
    echo "Output written in [$file_name]."
}

for pattern in $@
do
    concat_subgroup I1
    concat_subgroup R1
    concat_subgroup R2
done


