#M##### Merge data from all timesteps ######

import os.path
import re
import time

#######Settings for reading the files#######
results_filename = 'extracted_results2.txt'
probe_directory = 'points'
points_files = 'p'
tag_start = 'AB25x2_Plat_0-'
tag_end = '.5L_S1_URANS_KWSST'
nprobes = 22
nstep = 3280
############################################

#Check if probe data location folder exists ('probe_directory')
print('Checking if %s exists' % probe_directory)
if not os.path.exists(probe_directory):
    print('Probe directory not found!')
    exit

#Get the file list and number of files in the "probe_directory" to report progress when iterating
flist = os.listdir(probe_directory)
nfiles = len(flist)
print('%s timesteps to process' % nfiles)
fcount = 1 #for file counter

#Check if result extraction file exists ('results_filename'), if not create one
print('Checking if %s file exists' % results_filename)
if not os.path.exists(results_filename):
    open(results_filename,'a').close
    print('Results file created: ' + results_filename)

#Get the first file in the 'probe_directory' in preparation for header extraction
print('Getting header information...')
fst_name = os.listdir(probe_directory)[0]
first_file = str(os.path.join(probe_directory, fst_name))

#Get the headers, clean it from extra spaces, add the delimiter as ',' and write to the result extraction file ('results_filename')
with open(first_file, 'r') as ffile, open (results_filename,'a') as results:
    print(first_file)
    first_line = ffile.readline().strip()
    cleaned_first_line = re.sub(' +', ",", first_line)
    print('Writing headers...')
    results.write(cleaned_first_line + "," + "Timestep" + "\n")

#Iterate through each timestep file in the probe data locatio ('probe_directory') extract all probe data, clean it from extra spaces, add the delimiter as ',' and write to the result extraction file ('results_filename')

tik=time.time() #Start timer
tikh=time.ctime()
print('Combining probe data, started at %s ...' % tikh)

for fname in os.listdir(probe_directory):

    print('Proccessing file %s, %s/%s' % (fname, fcount, nfiles))

    f = os.path.join(probe_directory, fname)

    t_step = fname[len(tag_start):-len(tag_end)]

    with open(f, 'r') as points, open(results_filename,'a') as results:
        
        lines = points.read().splitlines()

        for i in range(nprobes):
            current_line = lines[i+1].lstrip()
            cleaned_current_line = re.sub(' +', ",", current_line)
            results.write(t_step + "," + cleaned_current_line + "\n")

    fcount = fcount + 1 #increment counter       
fcount = fcount -1

tok=time.time() #End Timer
tokh=time.ctime()
length = tok - tik  #Calculate duration

print('Processed %s, completed at %s' % (fcount, tokh))
print('Total duration: %s seconds' % length)
print('Processing rate: %s files per second' % (fcount/length))

