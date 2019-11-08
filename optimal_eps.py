# This algorithm aims to find the optimal value for EPS to use in the DBScan algorithm,
# based on the minimum number of points that a cluster should have.
# It is designed to be used for the Data Mining Exercise for DBScan.
# With future adjustments this can me generalized for different datasets.
#
# Dependencies: pandas, numpy, tqdm, matplotlib, scipy.
#
# It works by reading an argument from the command line which represents the number of
# minimum points that can be in a cluster.
# Then it proceeds with the computation of the distance matrix (Euclidean distance)
# and the computation of a Nx2 matrix that contains, for each point, the distance between
# the n-th point and itself.
# After this, it sorts this matrix by the distances from the smallest to the biggest and
# plots the results by using pyplot.
#
# Author: Matteo Amatori

# modules import
import sys
import csv
import pandas as pd
from numpy import empty
from tqdm import tqdm
from matplotlib import pyplot as plt
from scipy.spatial import distance

# method that takes the input dataframe and returns an array of shape a = [[0, n-th_distance]...[k, n-th_distance]]
def compute_dist_matrix (p_df):
    print("Starting the distance matrix computation...")
    dist_matrix = empty([len(p_df.X), len(p_df.Y)])
    for idx1, row1 in tqdm(p_df.iterrows()):
        for idx2, row2 in p_df.iterrows():
            dist_matrix[idx1][idx2] = distance.euclidean([row1.X, row1.Y], [row2.X, row2.Y]) # Euclidean distance between point 1 and 2
    return dist_matrix

# method that takes the distance matrix and the number of minimum points in a cluster and returns,
# for every point, it's other n-th closest point's distance
def closest_dist (dist_matrix, how_many):
    closest_dist_mat = empty([len(dist_matrix), 2])
    for idx, row in enumerate(dist_matrix):
        closest_dist_mat[idx][0] = idx
        closest_dist_mat[idx][1] = sorted(row)[how_many]
    return closest_dist_mat

def main():
    # dataset input
    file_name = "C:/Users/amato/Documents/Uni/11/DMO/DM/Esercizi/Datasets/Coordinates.csv"
    dt = pd.read_csv(file_name, sep = ",")
    how_many = int(sys.argv[1])

    # computation of the distance matrix
    dist_matrix = compute_dist_matrix(dt)

    # calculating the n-smallest distance for every point
    closest_dist_mat = closest_dist(dist_matrix, how_many)
    closest_dist_mat.sort(1)
    closest_dist_mat.sort(0)

    # creating and showing plot
    plt.plot(closest_dist_mat[:,1], closest_dist_mat[:,0])
    plt.xlabel("Point")
    plt.ylabel("Distance to " + str(how_many) + "-th point")
    plt.show()

if __name__ == "__main__":
    main()
