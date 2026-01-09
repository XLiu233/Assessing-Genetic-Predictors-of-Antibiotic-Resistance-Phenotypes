#!/bin/bash

for file in output/*.fasta; do
    echo "Processing file: $file"
    docker run -v "$(pwd):/app" genomicepidemiology/resfinder -ifa $file -l 0 -t 0 -o result/$file --acquired
    echo "Completed processing: $file"
done

echo "All .fasta files have been processed."