#!/bin/bash

echo -e "writing my thesis..."

# change path to current working directory
export PATH="$PWD:$PATH"

# make triangle/plot exeutable
chmod +x ./triangle
chmod +x ./plot

# run analysis
cat config.yaml | triangle | plot

# Write report
pdflatex main.tex
