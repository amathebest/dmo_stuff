# module file for the analysis script
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

# function that returns Gini Index of the considered node in a split
def compute_gini_index(df):
    count = len(df.index)
    class_0 = len(df[df.math == 0].index)
    class_1 = len(df[df.math == 1].index)
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
