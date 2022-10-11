import pandas as pd
import matplotlib.pyplot as plt
import time


#######Settings for filtering and plotting #######

results_filename = "extracted_results.txt"
cols = ["nodenumber", "pressure"]   # Load only the neccessary columns to conserve memory. Use '.' to add more column names encased in "".
plot_title = "Node No. vs Pressure"
legend_loc = "upper right"
legend_frame = True
xaxis_label = "Node No."
yaxis_label = "Pressure (Pa)"
figure_filename = plot_title + ".jpg"   #plot_title + ".jpg"

##################################################


## Data load
tik=time.time() #Start timer
tikh=time.ctime()
print('Data loading started at %s ...' % tikh)

df = pd.read_csv(results_filename, sep=',', dtype='float64', usecols=cols)

print('Dataset Info')
print(df.info(verbose=True))
#print(df.head())   #Data Preview

tok=time.time() #End Timer
tokh=time.ctime()
length = round(tok - tik, 2)  #Calculate duration
print('Data loading completed in %s secs at %s' % (length, tokh))

## Manual conversion (optional)
#df = df['nodenumber'].astype('float64')


## Additional optional Column Filtering
c1 = 'nodenumber'
c2 = 'pressure'
print('Filtering columns %s and %s' % (c1, c2))
df2 = df[[c1, c2]]

## Data Filtering
d1 = 4
d2 = 3
print('Filtering data ...')
df3 = df2[df2[c1]==d1]
df4 = df2[df2[c1]==d2]


## Plots (Same Graph)
tik=time.time() #Start timer
tikh=time.ctime()
print('Plotting started at %s ...' % tikh)
#Initial Plot
#ax= df2.plot.scatter(x=c1, y =c2, s=10, marker='x', yerr = 0, xerr = 0, label="df2")
ax= df3.plot.scatter(x=c1, y =c2, s=10, marker='x', yerr = 0, xerr = 0, label="df3")

#Subsequent plots
#ax1= df3.plot.scatter(x=c1, y =c2, s=10, marker='x', yerr = 0, xerr = 0, label="df3", ax=ax)
ax2= df4.plot.scatter(x=c1, y =c2, s=10, marker='o', yerr = 0, xerr = 0, label="df4", ax=ax)

## Plot labeling
ax.set_xlabel(xaxis_label)
ax.set_ylabel(yaxis_label)
ax.set_title(plot_title)
ax.legend(loc=legend_loc, frameon=legend_frame)

tok=time.time() #End Timer
tokh=time.ctime()
length = round(tok - tik, 2)  #Calculate duration
print('Plotting completed in %s secs at %s' % (length, tokh))


print('Saving plot(s)...')
plt.savefig(figure_filename)
print('Displaying plot(s)...')
plt.show()
