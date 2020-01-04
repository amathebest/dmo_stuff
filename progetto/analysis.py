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

# modifying the dataset in order map the categorical columns into numerical or boolean ones.
# this is done purely for visualization of the correlation matrix and to have a class onto which compute
# the classification.
df["cohort"] = df["cohort"].astype(int)
df["gen_bool"] = df.apply(bool_gender, axis = 1)
df["deg_bool"] = df.apply(bool_degree, axis = 1)
df["num_school"] = df.apply(transform_school, axis = 1)
df["mat_bool"] = df.apply(bool_math, axis = 1)

# data visualization: correlation between columns
# print(df.corr())

# shuffle of the dataset and splitting in training and test set
split_value = (len(df.index)/10)*8
training, test = train_test_split(df, test_size = 0.2)

# some initialization for the classification tree
tree = []
edges = []
splits = ["total_cfu", "test", "num_school", "avg_g"]

# calculating impurity on root node
root_g_idx, count = compute_gini_index(training)
root = Node(len(tree), "total_cfu", training, root_g_idx, "")
tree.append(root)
print("Impurity on root: ", root_g_idx)

# split of root: total_cfu
split_impurity, best_value = compute_numerical_split(training, "total_cfu", tree, edges, 0)
print("Impurity on root: ", root_g_idx)
print("Split impurity: ", split_impurity)
for idx in range(len(edges)):
    print("Node " + str(idx+1) + ":", edges[idx].label, ", GI:", tree[idx+1].g_idx, len(tree[idx+1].df.index), tree[idx+1].classif)

# split of node 1: total_cfu
split_impurity, best_value = compute_numerical_split(tree[1].df, "total_cfu", tree, edges, 1)

print("Impurity on node 1: ", tree[1].g_idx)
print("Split impurity: ", split_impurity)
for idx in range(len(edges)):
    print("Node " + str(idx+1) + ":", edges[idx].label, ", GI:", tree[idx+1].g_idx, len(tree[idx+1].df.index), tree[idx+1].classif)

# split of node 2: total_cfu
split_impurity, best_value = compute_numerical_split(tree[2].df, "total_cfu", tree, edges, 2)

print("Impurity on node 2: ", tree[2].g_idx)
print("Split impurity: ", split_impurity)
for idx in range(len(edges)):
    print("Node " + str(idx+1) + ":", edges[idx].label, ", GI:", tree[idx+1].g_idx, len(tree[idx+1].df.index), tree[idx+1].classif)
