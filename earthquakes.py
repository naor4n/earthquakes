import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt


"""
Place, Latitude, Longitude, Country, Continent, Magnitude

"""
column_names =  ['Place', 'Latitude', 'Longitude', 'Country', 'Continent', 'Magnitude']

data = pd.read_csv("archive/earthquake_dataset.csv", names=column_names, header=None)

plot = sb.displot(data['Magnitude'], kde=True)
plt.title("Magnitude plot")
plt.show(block=True)
