import csv
import sys
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

from modules import Node, Edge
from modules import bool_math, bool_gender, compute_gini_index, compute_gini_impurity

# data input and initialization
base_path = Path(__file__).absolute().parent
dataset_loc = str(base_path) + "/data/dataset.csv"
df = pd.read_csv(dataset_loc, sep = ";")
df.head()

# creating a new column with a boolean value that will represent a class
df["math"] = df.apply(bool_math, axis = 1)
df["gen_bool"] = df.apply(bool_gender, axis = 1)
root_g_idx, count = compute_gini_index(df) # calculating impurity on root node

# some initialization for the classification tree
tree = []
edges = []

# data analysis and understanding
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(df.corr())

# computation
tcfu_sorted = sorted(df.total_cfu.unique())
best_gini = sys.maxsize
df_node_1 = pd.DataFrame()
df_node_2 = pd.DataFrame()
best_val = 0
g_idx_node_1 = 0
g_idx_node_2 = 0

for value in tcfu_sorted:
    df_1 = df[df.total_cfu <= value]
    df_2 = df[df.total_cfu > value]
    g_idx_1, count_1 = compute_gini_index(df_1)
    g_idx_2, count_2 = compute_gini_index(df_2)
    arr_idx = []
    arr_idx.append(g_idx_1)
    arr_idx.append(g_idx_2)
    arr_cnt = []
    arr_cnt.append(count_1)
    arr_cnt.append(count_2)
    len_node = len(df.index)
    g_imp_tcfu = compute_gini_impurity(arr_idx, arr_cnt, len_node)
    if g_imp_tcfu < best_gini:
        best_val = value
        best_gini = g_imp_tcfu
        df_node_1 = df_1
        df_node_2 = df_2
        g_idx_node_1 = g_idx_1
        g_idx_node_2 = g_idx_2
print("Split on root, Split impurity:", best_gini)
print("Node 1: total_cfu <= 21, GI: ", g_idx_node_1)
print("Node 1: total_cfu > 21, GI: ", g_idx_node_2)

root = Node(len(tree), "total_cfu", df, root_g_idx)
tree.append(root)

node_1 = Node(len(tree), "", df_node_1, g_idx_node_1)
tree.append(node_1)
edge_1 = Edge(len(edges), 0, 1, "<=" + str(best_val))
edges.append(edge_1)
node_2 = Node(len(tree), "", df_node_2, g_idx_node_2)
tree.append(node_2)
edge_2 = Edge(len(edges), 0, 2, ">" + str(best_val))
edges.append(edge_2)







#
#
#
#
#
