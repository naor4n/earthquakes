import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt
from matplotlib import colors, patches


"""
Place, Latitude, Longitude, Country, Continent, Magnitude

"""

column_names =  ['Place', 'Latitude', 'Longitude', 'Country', 'Continent', 'Magnitude']

data = pd.read_csv("earthquakes-main\data\earthquake_dataset.csv", names=column_names, header=None, skiprows=1)

# creating histogram
n_bins = 30
plot = sb.histplot(data['Magnitude'], bins=n_bins, kde=True)

# customizing histogram further
plt.xlabel("magnitudes")
plt.ylabel("number of")
plt.title("Magnitude plot")

N, bins, patches = plot.axes.hist(data['Magnitude'], bins=n_bins)       # N = datapoints, bins = upper and min values for edges, patches = array

# determine color intensity
norm_values = ((N**(1/5))/N.max())
norm = colors.Normalize(norm_values.min(), norm_values.max())

# set color
zip = zip(norm_values, patches)
for value, patch in zip:
    color = plt.cm.viridis(norm(value))
    patch.set_facecolor(color)


plt.show(block=True)
