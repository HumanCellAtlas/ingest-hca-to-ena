#!/usr/bin/env bash

export F2B_FILE_EXT=txt
export F2B_FILE_DIR=$PWD/test-files

../concat.sh $@

echo "Output written in [$F2B_FILE_DIR/output]."
