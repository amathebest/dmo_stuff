import csv
import sys
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

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

# calculating impurity on root node
root_g_idx, count = compute_gini_index(training)
root = Node(len(tree), "total_cfu", training, root_g_idx)
tree.append(root)

# some initialization for the classification tree
tree = []
edges = []

# correlation matrix of the variables contained in the dataset
print(df.corr())

# split of root: total_cfu
split_impurity = compute_numerical_split(training, "total_cfu", tree, edges)

print("Impurity on root: ", root_g_idx)
print("Split impurity: ", split_impurity)
print("Node 1: total_cfu <= " + str(best_val) + ", GI: ", g_idx_node_1)
print("Node 2: total_cfu > " + str(best_val) + ", GI: ", g_idx_node_2)

if g_idx_node_1 < g_idx_node_2:


# split of node 1: test
test_sorted = sorted(df_node_1.test.unique())
best_gini = sys.maxsize
df_node_3 = pd.DataFrame()
df_node_4 = pd.DataFrame()
best_val = 0
g_idx_node_3 = 0
g_idx_node_4 = 0

for value in test_sorted:
    df_3 = df_node_1[df_node_1.test <= value]
    df_4 = df_node_1[df_node_1.test > value]
    g_idx_3, count_3 = compute_gini_index(df_3)
    g_idx_4, count_4 = compute_gini_index(df_4)
    arr_idx = []
    arr_idx.append(g_idx_3)
    arr_idx.append(g_idx_4)
    arr_cnt = []
    arr_cnt.append(count_3)
    arr_cnt.append(count_4)
    len_node = len(df_node_1.index)
    g_imp_test = compute_gini_impurity(arr_idx, arr_cnt, len_node)
    if g_imp_test < best_gini:
        best_val = value
        best_gini = g_imp_test
        df_node_3 = df_3
        df_node_4 = df_4
        g_idx_node_3 = g_idx_3
        g_idx_node_4 = g_idx_4

print("Impurity on node 1: ", g_idx_node_1)
print("Split impurity: ", best_gini)
print("Node 3: test <= " + str(best_val) + ", GI: ", g_idx_node_3)
print("Node 4: test > " + str(best_val) + ", GI: ", g_idx_node_4)

node_3 = Node(len(tree), "", df_node_3, g_idx_node_3)
tree.append(node_3)
edge_3 = Edge(len(edges), 1, 3, "<=" + str(best_val))
edges.append(edge_3)
node_4 = Node(len(tree), "", df_node_4, g_idx_node_4)
tree.append(node_4)
edge_4 = Edge(len(edges), 1, 4, ">" + str(best_val))
edges.append(edge_4)



#
#
#
#
#
