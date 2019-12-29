# module file for the analysis script
import pandas as pd

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

# function that returns Gini Index of the considered node in a split
def compute_gini_index(df):
    g_idx = 0

    return g_idx


def compute_gini_impurity():
    g_imp = 0

    return g_imp
