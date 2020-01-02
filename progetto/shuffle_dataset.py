import os
import csv
import shutil
import pandas as pd
from pathlib import Path

# dataset import
base_path = Path(__file__).absolute().parent
dataset_loc = str(base_path) + "/data/dataset.csv"
df = pd.read_csv(dataset_loc, sep = ";")

# dataset shuffling
df = df.sample(frac=1).reset_index(drop=True)

# dataset output
df.to_csv('dataset_shuffled.csv')

# moving the dataset to the data folder
shutil.move(str(base_path) + "/dataset_shuffled.csv", str(base_path) + "/data/dataset_shuffled.csv")
