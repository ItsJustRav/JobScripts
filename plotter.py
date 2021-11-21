# Plot Residuals to Images
# Python script to plot and save residuals as images by Ravindu Ranaweera (https://github.com/ItsJustRav)

# **** Ensure numpy and matplotlib are available. If not install these manually or use the environment.yml file using miniconda.
# Install environment.yml with miniconda>> conda env create -f environment.yml
# ** Place in the parent directory (where the output files are being written to), the files must be in .out format.

# Import required modules
import numpy as np
import matplotlib.pyplot as plt
import glob, os

os.chdir(os.getcwd())   # Get the current working directory

delchar='"'             # Characters to delete

# Check if "monitors" folder exists and if not, create
if not os.path.exists("monitors"):
    os.makedirs("monitors")

#Plotting loop
for fname in glob.glob("*.out"):
    data=np.genfromtxt(fname, dtype=float, delimiter=" ", skip_header=3, deletechars=delchar)                                   # Load data by skipping the first 3 lines and delete characters in "delchar"
    data_leg=np.genfromtxt(fname, dtype=None, encoding=None, delimiter=" ", skip_header=2, max_rows=1, deletechars=delchar)     # Load only the headers line"
    data_l=[s.replace(delchar, "") for s in data_leg]   # Clean headers from additional characters
    data_l=[s.replace("(", "") for s in data_l]         # Clean headers from additional characters
    data_l=[s.replace(")", "") for s in data_l]         # Clean headers from additional characters
    
    x = data[:,0]                                       # Load the first column as x values
    y=data[:,1:-2]                                      # Load rest of the columns as Y values except last 2
    
    plt.title(fname)                                    # Title of the plot (set to data file name)
    #plt.ylim([-4, -0.5])                                # Limits of the y-axis
    #plt.xlim([100, 10000])                              # Limits of the x-axis
    plt.plot(x, y)                                      # Plot the graphs
    plt.legend(data_l[1:-2])                            # Ignore the first column from header line and assign to legend and except last 2
    plt.savefig("monitors/plot_{}.png".format(fname))   # Save plots as images





