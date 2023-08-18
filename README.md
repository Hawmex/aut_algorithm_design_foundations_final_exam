# AUT Algorithm Design Foundations Final Exam

This repository contains my answers for the final exam of the Algorithm Design
Foundations course at AUT (Tehran Polytechnic).

## Question 1

In this question, we have to implement the k-mean clustering algorithm from
scratch.

### Input

The first line indicates the number of points.

The following lines indicate the `x` and `y` coordinates of the points.

The last line indicates the desired number of clusters (`k`).

### Output

The minimum inter-cluster distance.

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

`7.0710678`

## Question 2

### Input

The first line indicates the number of vertices and edges.

The following lines indicate each edge's starting and ending vertices, and its
length.

The next line indicates the number of tours.

The following lines indicate the number of vertices that should be visited in
each tour followed by the number for each vertex.

### Output

The length of the shortest path for each tour.

## Example

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

In this question we had to implement a program that finds the largest common
substring between two string separated by a space.

### Input

Two strings separated by a space.

### Output

The starting index of the LCS in the first string, the starting index of the LCS
in the second string, and the length of the LCS.

### Example

```
cool toolbox
```

#### Input

```
1 1 3
```

## Question 6

In this question, we had to perform data analysis and implement a linear
regression model from scratch for a dataset containing information about ~20k
houses.

The linear regressor was implemented in an object-oriented manner and used the
closed form solution.

For more information, see [q6_answer.ipynb](./q6_answer.ipynb)
