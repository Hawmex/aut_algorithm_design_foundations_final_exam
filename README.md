# AUT Algorithm Design Foundations Final Exam

This repository contains my answers for the final exam of the algorithm design
foundations course at AUT (Tehran Polytechnic).

## Question 1

In this question, we implement the k-means clustering algorithm from scratch.

### Input

- The number of points
- The `x` and `y` coordinates of the points
- The desired number of clusters (`k`)

### Output

- The minimum inter-cluster distance

### Example

#### Input

```
9
3 2
2 2
2 3
7 8
8 8
8 7
22 9
21 8
23 10
3
```

#### Output

```
7.0710678
```

## Question 2

### Input

- The number of vertices and edges
- Each edge's starting and ending vertices and their length
- The number of tours
- The number of vertices that must be visited in each tour, followed by their
  names

### Output

- The length of the shortest path for each tour

### Example

#### Input

```
4 5
1 2 1
2 3 1
3 4 1
4 1 1
2 1 1
3
2 1 2
2 1 3
4 1 2 3 4
```

#### Output

```
Ready
2
4
4
```

## Question 3

In this question, we had to implement a program that finds the largest common
substring between two strings separated by a space.

### Input

- Two strings separated by a space

### Output

- The index of the LCS in the first string
- The index of the LCS in the second string
- The length of the LCS itself

### Example

#### Input

```
cool toolbox
```

#### Output

```
1 1 3
```

## Question 6

In this question, we had to implement a linear regression model from scratch and
apply it to a dataset containing information on ~20k houses.

The linear regressor was implemented utilizing the closed-form solution. For
more information, see [`q6_answer.ipynb`](./q6_answer.ipynb).
