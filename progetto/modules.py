# module file for the analysis script
import sys
import pandas as pd
import matplotlib.pyplot as plt

class Node:
    id = 0
    label = ""
    df = pd.DataFrame()
    g_idx = 0

    def __init__(self, id, label, df, g_idx):
        self.id = id
        self.label = label
        self.df = df
        self.g_idx = g_idx

class Edge:
    id = 0
    id_starting_node = 0
    id_ending_node = 0
    label = ""

    def __init__(self, id, id_starting_node, id_ending_node, label):
        self.id = id
        self.id_starting_node = id_starting_node
        self.id_ending_node = id_ending_node
        self.label = label

# function that returns 1 whether the row represents a student that passed Analisi Matematica 1
# in the respective first year of career, 0 otherwise
def bool_math(row):
    if row["math_course_g"] == 0:
        return 0
    else:
        return 1

# function that encodes the gender column from being a string to a 0/1:
# M -> 0
# F -> 1
def bool_gender(row):
    if row["gender"] == "M":
        return 0
    else:
        return 1

# function that encodes the degree column from being a string to a 0/1:
# CdS3 -> 0
# CdS4 -> 1
def bool_degree(row):
    if row["degree"] == "CdS3":
        return 0
    else:
        return 1

# function that encodes the school string into a numerical value
def transform_school(row):
    if row["school"] == "LS":
        return 0
    elif row["school"] == "LC":
        return 1
    elif row["school"] == "IT":
        return 2
    elif row["school"] == "TC":
        return 3
    elif row["school"] == "IP":
        return 4
    else:
        return 5

# function that finds the best split for a given node on a numerical attribute
def compute_numerical_split(df, attribute, tree, edges, starting_node):
    sorted_values = sorted(df[attribute].unique())
    best_gini = sys.maxsize
    df_node_1 = pd.DataFrame()
    df_node_2 = pd.DataFrame()
    best_val = 0
    g_idx_node_1 = 0
    g_idx_node_2 = 0

    for value in sorted_values:
        df_1 = df[df[attribute] <= value]
        df_2 = df[df[attribute] > value]
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

    node_1 = Node(len(tree), "", df_node_1, g_idx_node_1)
    tree.append(node_1)
    edge_1 = Edge(len(edges), starting_node, len(tree)-1, attribute + "<=" + str(best_val))
    edges.append(edge_1)
    node_2 = Node(len(tree), "", df_node_2, g_idx_node_2)
    tree.append(node_2)
    edge_2 = Edge(len(edges), starting_node, len(tree)-1, attribute + ">" + str(best_val))
    edges.append(edge_2)

    return best_gini, best_val

# function that returns Gini Index of the considered node in a split
def compute_gini_index(df):
    count = len(df.index)
    class_0 = len(df[df.mat_bool == 0].index)
    class_1 = len(df[df.mat_bool == 1].index)
    g_idx = 1 - ((class_0/max(count, 1))**2+(class_1/max(count, 1))**2)
    return g_idx, count

# function that returns the Gini Impurity of a given split
def compute_gini_impurity(idx, cnts, len_node):
    g_imp = 0
    for i in range(len(idx)):
        g_imp += idx[i] * (cnts[i]/len_node)
    return g_imp

# function that outputs some plots
def output_plots(df, base_path):
    df["total_cfu"].value_counts().sort_index().plot.bar(title = "total_cfu")
    plt.savefig(base_path + "/plots/total_cfu.png")
    return
