import pandas as pd
import matplotlib.pyplot as plt

results_filename = "extracted_results.txt"

df = pd.read_csv(results_filename, sep=',', dtype='float64')


#df = df['nodenumber'].astype('float64')

#print(df.dtypes)
#print(df.info(verbose=True))
#print(df.head())
#list(df.columns)

df2 = df[df['nodenumber']==1]

print(df2)
#print(df2['pressure'])

df.plot.scatter(x="nodenumber", y ='pressure', s=10, marker='x', yerr = 0, xerr = 0, title="Node No. vs Pressure", xlabel="Node No.", ylabel="Pressure (Pa)", legend=True)
df2.plot.scatter(x="nodenumber", y='pressure-coefficient', s=10, marker='x', yerr = 0, xerr = 0, title="Node No. vs Pressure", xlabel="Node No.", ylabel="Pressure (Pa)", legend=True)
#plt.legend(loc='upper left', frameon=False)

plt.show()
