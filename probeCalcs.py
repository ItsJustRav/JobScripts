import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np

#########Settings for Calculations#########

results_filename = "extracted_results.txt"
cols = ["nodenumber", "pressure"]   # Load only the neccessary columns to conserve memory. Use '.' to add more column names encased in "".
P0 = 0.00002 # reference pressure (2 × 10−5 Pa)

## Data load
tik=time.time() #Start timer
tikh=time.ctime()
print('Data loading started at %s ...' % tikh)

df = pd.read_csv(results_filename, sep=',', dtype='float64', usecols=cols)

tok=time.time() #End Timer
tokh=time.ctime()
length = round(tok - tik, 2)  #Calculate duration
print('Data loading completed in %s secs at %s' % (length, tokh))

#p_by_p0 = (df["pressure"]/P0)
spl = 20*np.log(df["pressure"]/P0)
df["accoustin_pressure"] = spl

#print('Dataset Info')
#print(df.info(verbose=True))
print(df.head())   #Data Preview

print(df.info(verbose=True))
