import pandas as pd
import matplotlib.pyplot as plt

results_filename = "extracted_results.txt"

df = pd.read_csv(results_filename, sep=',')

#print(df.dtypes)
#print(df.info(verbose=True))

df2 = df[df['nodenumber']==22]


print(df2['pressure'])

plt.axes(df2['pressure'])
