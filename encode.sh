#!/bin/bash

# Animation Encoder
# Encode animation files to video using FFMPEG (https://www.ffmpeg.org/), script created by Ravindu Ranaweera (https://github.com/ItsJustRav)
# ***Requires a static build of ffmpeg. This can be downloaded and extracted from https://johnvansickle.com/ffmpeg/ (use "tar xJfv filename.tar.xz" to extract)
# chmod +x <filename> if you get a permission error, then run again

# Creating a list of available animations 
files=$(ls *.cxa | sed -e 's/\.cxa$//')
echo "Animation list: "$files

# ffmpeg settings
loc_ffmpeg=$HOME/utilities/ffmpeg/ffmpeg #ffmpeg static build location

out_format=.mp4 #Output video format

frame_rate=2 #Frame rate of video

# Print ffmpeg settings
echo "ffmpeg location: "$loc_ffmpeg
echo "Output format: "$out_format
echo "Output frame rate: "$frame_rate


# Loop for looping through the available animations
for i in $files
do
	echo ""
	# Creating output filename with animation name and format
	fout=$i$out_format
	# Timestamp
	echo "<--Starting to Encode "$fout"-->"
	date
	
	# Using a static build of ffmpeg to output animations
	$loc_ffmpeg -y -pattern_type glob -framerate $frame_rate -i $i"*.ppm" $fout
	
	echo "<--Encoding Completed "$fout"-->"
	date
	echo ""
done
