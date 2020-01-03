import csv
import sys
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from modules import Node
from modules import bool_math, bool_gender, bool_degree, transform_school # dataset pre-processing functions
from modules import compute_numerical_split, compute_gini_index, compute_gini_impurity # algorithm functions

# pandas output settings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# data input and initialization
base_path = Path(__file__).absolute().parent
dataset_loc = str(base_path) + "/data/dataset.csv"
df = pd.read_csv(dataset_loc, sep = ";")
print(df.apply(lambda x: x.factorize()[0]).corr())

# creating a new column with a boolean value that will represent a class
df["mat_bool"] = df.apply(bool_math, axis = 1)
df["gen_bool"] = df.apply(bool_gender, axis = 1)
df["deg_bool"] = df.apply(bool_degree, axis = 1)
df["num_school"] = df.apply(transform_school, axis = 1)

# shuffle of the dataset and splitting in training and test set
split_value = (len(df.index)/10)*8
training, test = train_test_split(df, test_size = 0.2)

# some initialization for the classification tree
tree = []
edges = []

# calculating impurity on root node
root_g_idx, count = compute_gini_index(training)
root = Node(len(tree), "total_cfu", training, root_g_idx)
tree.append(root)

# correlation matrix of the variables contained in the dataset
print(df.corr())

# split of root: total_cfu
split_impurity, best_value = compute_numerical_split(training, "total_cfu", tree, edges, len(tree))

print("Impurity on root: ", root_g_idx)
print("Split impurity: ", split_impurity)
for idx in range(len(edges)):
    print("Node " + str(idx+1) + ":", edges[idx].label, ", GI:", tree[idx+1].g_idx, len(tree[idx+1].df.index))

# split of node 2: avg_g
split_impurity, best_value = compute_numerical_split(tree[2].df, "avg_g", tree, edges, len(tree))

print("Impurity on node 2: ", tree[2].g_idx)
print("Split impurity: ", split_impurity)
for idx in range(len(edges)):
    print("Node " + str(idx+1) + ":", edges[idx].label, ", GI:", tree[idx+1].g_idx, len(tree[idx+1].df.index))




#
#
#
#
#
