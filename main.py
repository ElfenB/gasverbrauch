import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Gasverbrauch.csv")

x_name = "Gas-Verbrauch"
y_name = "Temperatur"

x = data["verbrauch"]
y = data["temperatur"]

plots = input("Plot graphs? (y/N)") == "y"

r, p = stats.pearsonr(x, y)

print("r:", r, "p:", p)


# Creating the scatter plot
if plots:
  plt.scatter(x, y)
  plt.title("Correlation between " + x_name + " and " + y_name)
  x_name = x_name + "\n" + "r: " + str(r) + " p: " + str(p)
  plt.xlabel(x_name)
  plt.ylabel(y_name)
  plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color="red")
  plt.show()
