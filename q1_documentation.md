# Principles of Algorithm Design

## Final Exam, Question 1

## Student Name

Hamed Araab

## Student Number

9925003

## Introduction

This documentation provides an overview of the code implementation for the K-Means Clustering algorithm. The code performs clustering on a list of points based on the specified number of clusters. The implementation follows the principles of Algorithm Design. The purpose of this code is to find the shortest inter-cluster distance using the K-Means Clustering algorithm.

## Code Structure

The code consists of the following components:

1. `KMeansClustering` class: Performs the K-Means Clustering algorithm on a list of points.
2. `main` function: Provides the user interface for input and output handling.

## `KMeansClustering` Class

### Class Description

The `KMeansClustering` class encapsulates the K-Means Clustering algorithm. It performs clustering on a list of points and calculates the shortest inter-cluster distance.

### Class Attributes

- `_points`: A list of points provided as input.
- `_k`: The specified number of clusters.
- `_means`: The means of each cluster.
- `_clusters`: The clusters formed during the clustering process.

### Class Methods

#### `_get_distance(point1, point2)`

- Description: Returns the Euclidean distance between two points.
- Parameters:
  - `point1`: The first point.
  - `point2`: The second point.
- Returns: The Euclidean distance between the two points.

#### `__init__(self, points, k)`

- Description: Initializes the `KMeansClustering` class with the given points and number of clusters.
- Parameters:
  - `points`: A list of points.
  - `k`: The number of clusters.

#### `points`

- Description: Getter method for the `_points` attribute.
- Returns: The list of points.

#### `k`

- Description: Getter method for the `_k` attribute.
- Returns: The number of clusters.

#### `means`

- Description: Getter method for the `_means` attribute.
- Returns: The means of each cluster.

#### `clusters`

- Description: Getter method for the `_clusters` attribute.
- Returns: The clusters formed during the clustering process.

#### `min_inter_cluster_distance`

- Description: Calculates the shortest inter-cluster distance.
- Returns: The shortest distance between any two points in different clusters.

#### `_get_initial_means()`

- Description: Returns `k` random points as the initial values for means.
- Returns: A list of `k` randomly selected points from the input.

#### `_get_clusters()`

- Description: Assigns each point to its nearest mean and forms clusters.
- Returns: A list of clusters, where each cluster contains at least one point.

#### `_get_means()`

- Description: Calculates the means of all clusters.
- Returns: A list of means for each cluster.

#### `_get_wcss()`

- Description: Calculates the Within-Cluster Sum of Squares (`WCSS`) metric for the current clustering result.
- Returns: The `WCSS` value.

#### `_run()`

- Description: Finds the best clustering result for the given instance.

## `main` Function

### Function Description

The `main` function is the entry point of the program. It handles user input and output.

### Function Steps

1. Reads the number of points from the user.
2. Reads the points from the user.
3. Reads the number of clusters from the user.
4. Creates an instance of the `KMeansClustering` class with the given points and number of clusters.
5. Prints the shortest inter-cluster distance.

## Usage Example

```python
# Start of getting user inputs
points_count = int(input())
points = [list(map(float, input().

split(" "))) for _ in range(points_count)]
clusters_count = int(input())
# End of getting user inputs

clustering = KMeansClustering(points, clusters_count)
print("{:.7f}".format(clustering.min_inter_cluster_distance))
```

The user is prompted to provide the number of points, the coordinates of each point, and the number of clusters. The code then calculates the shortest inter-cluster distance using the K-Means Clustering algorithm and displays the result.

## Conclusion

This documentation provided an overview of the code implementation for the K-Means Clustering algorithm. It described the class structure, methods, and the main function responsible for user interaction. The code allows users to perform clustering on a set of points and obtain the shortest inter-cluster distance.
