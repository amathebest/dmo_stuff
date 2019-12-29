import os
import sys
import csv
import matplotlib.pyplot as plt
import pandas as pd

from modules import Node, Edge
from modules import bool_math, compute_gini_index, compute_gini_impurity

# data input and initialization
base_path = os.path.dirname(__file__)
file_name = "dataset.csv"
df = pd.read_csv(os.path.join(base_path, "/data/" + file_name), sep = ";")
df.head()

# some initialization for the classification tree
tree = []
node_id = 0
edge_id = 0

# creating a new column with a boolean value that will represent a class
df["math"] = df.apply(bool_math, axis = 1)

df_M = df[df.gender == "M"]
df_F = df[df.gender == "F"]













#
#
#
#
#
