import csv
import sys
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from modules import Node, Edge
from modules import bool_math, bool_gender, bool_degree, compute_gini_index, compute_gini_impurity

# pandas output settings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# data input and initialization
base_path = Path(__file__).absolute().parent
dataset_loc = str(base_path) + "/data/dataset_shuffled.csv"
df = pd.read_csv(dataset_loc, sep = ";")
print(df.apply(lambda x: x.factorize()[0]).corr())

# creating a new column with a boolean value that will represent a class
df["mat_bool"] = df.apply(bool_math, axis = 1)
df["gen_bool"] = df.apply(bool_gender, axis = 1)
df["deg_bool"] = df.apply(bool_degree, axis = 1)

# shuffle of the dataset and splitting in training and test set
df = df.sample(frac=1).reset_index(drop=True)
split_value = (len(df.index)/10)*8
training, test = train_test_split(df, test_size = 0.2)

# calculating impurity on root node
root_g_idx, count = compute_gini_index(training)

# some initialization for the classification tree
tree = []
edges = []

# correlation matrix of the variables contained in the dataset
print(df.corr())

# split of root: total_cfu
tcfu_sorted = sorted(training.total_cfu.unique())
best_gini = sys.maxsize
df_node_1 = pd.DataFrame()
df_node_2 = pd.DataFrame()
best_val = 0
g_idx_node_1 = 0
g_idx_node_2 = 0

for value in tcfu_sorted:
    df_1 = training[training.total_cfu <= value]
    df_2 = training[training.total_cfu > value]
    g_idx_1, count_1 = compute_gini_index(df_1)
    g_idx_2, count_2 = compute_gini_index(df_2)
    arr_idx = []
    arr_idx.append(g_idx_1)
    arr_idx.append(g_idx_2)
    arr_cnt = []
    arr_cnt.append(count_1)
    arr_cnt.append(count_2)
    len_node = len(training.index)
    g_imp_tcfu = compute_gini_impurity(arr_idx, arr_cnt, len_node)
    if g_imp_tcfu < best_gini:
        best_val = value
        best_gini = g_imp_tcfu
        df_node_1 = df_1
        df_node_2 = df_2
        g_idx_node_1 = g_idx_1
        g_idx_node_2 = g_idx_2

print("Impurity on root: ", root_g_idx)
print("Split impurity: ", best_gini)
print("Node 1: total_cfu <= " + str(best_val) + ", GI: ", g_idx_node_1)
print("Node 2: total_cfu > " + str(best_val) + ", GI: ", g_idx_node_2)

root = Node(len(tree), "total_cfu", training, root_g_idx)
tree.append(root)

node_1 = Node(len(tree), "", df_node_1, g_idx_node_1)
tree.append(node_1)
edge_1 = Edge(len(edges), 0, 1, "<=" + str(best_val))
edges.append(edge_1)
node_2 = Node(len(tree), "", df_node_2, g_idx_node_2)
tree.append(node_2)
edge_2 = Edge(len(edges), 0, 2, ">" + str(best_val))
edges.append(edge_2)

# split of node 1: test
test_sorted = sorted(training.test.unique())
best_gini = sys.maxsize
df_node_3 = pd.DataFrame()
df_node_4 = pd.DataFrame()
best_val = 0
g_idx_node_3 = 0
g_idx_node_4 = 0

for value in test_sorted:
    df_3 = df_node_1[df_node_1.total_cfu <= value]
    df_4 = df_node_1[df_node_1.total_cfu > value]
    g_idx_3, count_3 = compute_gini_index(df_3)
    g_idx_4, count_4 = compute_gini_index(df_4)
    arr_idx = []
    arr_idx.append(g_idx_3)
    arr_idx.append(g_idx_4)
    arr_cnt = []
    arr_cnt.append(count_3)
    arr_cnt.append(count_4)
    len_node = len(df_node_1.index)
    g_imp_tcfu = compute_gini_impurity(arr_idx, arr_cnt, len_node)
    if g_imp_tcfu < best_gini:
        best_val = value
        best_gini = g_imp_tcfu
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
edge_3 = Edge(len(edges), 0, 1, "<=" + str(best_val))
edges.append(edge_3)
node_4 = Node(len(tree), "", df_node_4, g_idx_node_4)
tree.append(node_4)
edge_4 = Edge(len(edges), 0, 2, ">" + str(best_val))
edges.append(edge_4)



#
#
#
#
#
