import csv
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from modules import Node, Edge
from modules import bool_math, compute_gini_index, compute_gini_impurity

# data input and initialization
base_path = Path(__file__).absolute().parent
dataset_loc = str(base_path) + "/data/dataset.csv"
df = pd.read_csv(dataset_loc, sep = ";")
df.head()

# creating a new column with a boolean value that will represent a class
df["math"] = df.apply(bool_math, axis = 1)

# some initialization for the classification tree
tree = []
node_id = 0
edge_id = 0

# computation

df_M = df[df.gender == "M"]
df_F = df[df.gender == "F"]

g_idx_M, count_M = compute_gini_index(df_M)
g_idx_F, count_F = compute_gini_index(df_F)

arr_idx = []
arr_idx.append(g_idx_M)
arr_idx.append(g_idx_F)

arr_cnt = []
arr_cnt.append(count_M)
arr_cnt.append(count_F)

len_node = len(df.index)
g_imp_gender = compute_gini_impurity(arr_idx, arr_cnt, len_node)

print(g_idx_M)
print(g_idx_F)
print(g_imp_gender)








#
#
#
#
#
