import os.path
import re
import time

#######Settings for reading the files#######
results_filename = 'extracted_results.txt'
probe_directory = 'probes'
points_files = 'p'
tag_start = '1234_'
tag_end = '.1234'
############################################

#Check if probe data location folder exists ('probe_directory')
print('Checking if %s exists' % probe_directory)
if not os.path.exists(probe_directory):
    print('Probe directory not found!')
    exit

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

#Iterate through the probe data locatio ('probe_directory') and get the last line of each file, clean it from extra spaces, add the delimiter as ',' and write to the result extraction file ('results_filename')
tik=time.time() #Start timer
tikh=time.ctime()
print('Extracting probe data, started at %s ...' % tikh)

for fname in os.listdir(probe_directory):

    f = os.path.join(probe_directory, fname)

    t_step = fname[len(tag_start):-len(tag_end)]

    with open(f, 'r') as points, open(results_filename,'a') as results:
        lines = points.read().splitlines()
        last_line = lines[-1].lstrip()
        cleaned_last_line = re.sub(' +', ",", last_line)
        results.write(cleaned_last_line + t_step + "\n")

tok=time.time() #End Timer
tokh=time.ctime()
length = tok - tik  #Calculate duration

print('Completed at %s' % tokh)
print('Total duration: %s seconds' % length)

