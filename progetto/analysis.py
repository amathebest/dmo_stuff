import csv
import matplotlib.pyplot as plt
import pandas as pd

from modules import Node, Edge
from modules import bool_math, compute_gini_index, compute_gini_impurity

# data input and initialization
file_path = "C:/Users/Matteo/Dropbox/University/11/DMO/dmo_stuff/progetto/data/dataset.csv"
df = pd.read_csv(file_path, sep = ";")
df.head()

# creating a new column with a boolean value that will represent a class
df["math"] = df.apply(bool_math, axis = 1)










#
#
#
#
#
