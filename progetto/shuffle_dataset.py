import os
import csv
import shutil
import pandas as pd
from pathlib import Path

# function that returns 1 whether the row represents a student that passed Analisi Matematica 1
# in the respective first year of career, 0 otherwise
def bool_math(row):
    if row["math_course_g"] == 0:
        return 0
    else:
        return 1

# dataset import
base_path = Path(__file__).absolute().parent
dataset_loc = str(base_path) + "/data/dataset.csv"
df = pd.read_csv(dataset_loc, sep = ";")

# dataset shuffling and class adding
df = df.sample(frac=1).reset_index(drop=True)
df["mat_class"] = df.apply(bool_math, axis = 1)

# dataset output
df.to_csv('dataset_shuffled.csv')

# moving the dataset to the data folder
shutil.move(str(base_path) + "/dataset_shuffled.csv", str(base_path) + "/data/dataset_shuffled.csv")
