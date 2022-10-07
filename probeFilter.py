import pandas as pd
import matplotlib.pyplot as plt
import time

results_filename = "extracted_results.txt"

## Full data load
tik=time.time() #Start timer
tikh=time.ctime()
print('Data loading started at %s ...' % tikh)

df = pd.read_csv(results_filename, sep=',', dtype='float64')

print('Dataset Info')
print(df.info(verbose=True))
#print(df.head())   #Data Preview

tok=time.time() #End Timer
tokh=time.ctime()
length = round(tok - tik, 2)  #Calculate duration
print('Data loading completed in %s secs at %s' % (length, tokh))

## Manual conversion (optional)
#df = df['nodenumber'].astype('float64')


## Column Filtering
c1 = 'nodenumber'
c2 = 'pressure'
df2 = df[[c1, c2]]

## Data Filtering
df3 = df2[df2[c1]==4]
df4 = df2[df2[c1]==3]


## Plots (Same Graph)
#Initial Plot
#ax= df2.plot.scatter(x=c1, y =c2, s=10, marker='x', yerr = 0, xerr = 0, label="df2")
ax= df3.plot.scatter(x=c1, y =c2, s=10, marker='x', yerr = 0, xerr = 0, label="df3")
#Subsequent plots
#ax1= df3.plot.scatter(x=c1, y =c2, s=10, marker='x', yerr = 0, xerr = 0, label="df3", ax=ax)
ax2= df4.plot.scatter(x=c1, y =c2, s=10, marker='o', yerr = 0, xerr = 0, label="df4", ax=ax)

## Plot labeling
ax.set_xlabel("Node No.")
ax.set_ylabel("Pressure (Pa)")
ax.set_title(" Node No. vs Pressure")
ax.legend(loc="upper right", frameon=True)

plt.show()
