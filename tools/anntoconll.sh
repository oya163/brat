#!/bin/bash

# As of now, this script should be in brat/tools/
# How to run
# bash anntoconll.sh ../data/nepsa/Avenues_Khabar/0S8tX4eRa6M/

# Reference : https://stackoverflow.com/questions/9612090/how-to-loop-through-file-names-returned-by-find

# Input data dir
DATA_DIR=$1

# For all *.txt files
# run the script

#find $DATA_DIR -iname '*.txt' -exec echo "Processing {}" \;

# Make sure globstar is enabled
shopt -s globstar
for annfile in $DATA_DIR**/*.ann; do # Whitespace-safe and recursive
	txtfile=${annfile%.*}.txt
	echo "Processing: $txtfile"
	python3 anntoconll.py $txtfile
done
