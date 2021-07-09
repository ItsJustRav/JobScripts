#!/bin/bash

## File Sorter
## File sorting script for CFD cases for execution on a HPC by Ravindu Ranaweera (https://github.com/ItsJustRav)

# Generate a list of files for reference (before any file operations are carried out)
ls -lh *>filelist.log

# Make Directories
mkdir -p  post/animations/videos solutions logs monitors

casename=$(ls *.name | sed -e 's/\.name$//')

# Rename output files
for f in *.out; do
    cp "$f" monitors/"${f%.out}_$casename.out"
done


# Move files
mv *.log *.trn logs/
mv *.h5 *.flprj *.out *.asd *.ard *.index solutions/
mv *.ppm *.cxa post/animations/
mv *.mp4 post/animations/videos
