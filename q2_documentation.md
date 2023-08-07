# Principles of Algorithm Design

## Final Exam, Question 2

## Student Name

Hamed Araab

## Student Number

9925003

## Introduction

This documentation provides an overview of the code implementation for solving the Traveling Salesman Problem (TSP). The code uses the principles of Algorithm Design to find the minimum cost of touring a set of nodes in the TSP. The implementation follows a combination of Dijkstra's algorithm and the Heap Queue (Priority Queue) algorithm to efficiently compute the minimum costs.

## Code Structure

The code consists of the following components:

1. `TSPSolver` class: Solves the Traveling Salesman Problem using the provided arcs and nodes count.
2. `main` function: Provides the user interface for input and output handling.

## `TSPSolver` Class

### Class Description

The `TSPSolver` class encapsulates the logic for solving the Traveling Salesman Problem.

### Class Attributes

- `_arcs`: A set of arcs representing connections between nodes.
- `_nodes_count`: The total number of nodes.
- `_graph`: The graph representation of the arcs.
- `_all_min_costs`: A dictionary storing the minimum costs for traveling from a start node to other nodes in the graph.

### Class Methods

#### `_get_graph(self)`

- Description: Returns a graph representation using the provided arcs and nodes count.
- Returns: A dictionary representing the graph, where each node is associated with a set of target nodes and their respective costs.

#### `_get_min_costs(self, start_node)`

- Description: Calculates the minimum costs of traveling from the `start_node` to other nodes using Dijkstra's algorithm.
- Returns: A dictionary containing the minimum costs for traveling from the `start_node` to other nodes.

#### `get_min_cost_of_tour(self, selected_nodes)`

- Description: Calculates the minimum cost of touring the `selected_nodes` in the Traveling Salesman Problem.
- Returns: The minimum cost of touring the selected nodes.

### `main` Function

#### Function Description

The `main` function is the entry point of the program. It handles user input and output.

#### Function Steps

1. Reads the number of nodes and arcs from the user.
2. Reads the arcs and stores them in the `_arcs` attribute.
3. Creates an instance of the `TSPSolver` class with the provided arcs and nodes count.
4. Prints "Ready" to indicate that the solver is ready to process further input.
5. Reads the number of travels from the user.
6. Reads the selected nodes for each travel and calculates the minimum cost of touring them using the `get_min_cost_of_tour` method.
7. Prints the minimum cost for each travel.

## Usage Example

```python
# Start of getting part one of user inputs.
nodes_count, arcs_count = tuple(map(int, input().split(" ")))
arcs = set()

for _ in range(arcs_count):
    user_input = input().split(" ")
    arc = (int(user_input[0]), int(user_input[1]), float(user_input[2]))

    arcs.add(arc)
# End of getting part one of user inputs.

tsp_solver = TSPSolver(arcs, nodes_count)
print("Ready")

# Start of getting part two user inputs.
travels_count = int(input())
travels = [list(map(int, input().split(" ")))[1:] for _ in range(travels_count)]
# End of getting part two user inputs.

for selected_nodes in travels:
    print(tsp_solver.get_min_cost_of_tour(selected_nodes))
```

The user is prompted to provide inputs in two parts. In the first part, they input the number of nodes and arcs, followed by the arcs themselves. In the second part, they input the number of travels and the

selected nodes for each travel. The code then calculates and displays the minimum cost of touring the selected nodes for each travel.

## Conclusion

This documentation provided an overview of the code implementation for solving the Traveling Salesman Problem. It described the class structure, methods, and the main function responsible for user interaction. The code allows users to input arcs and calculate the minimum cost of touring selected nodes using a combination of Dijkstra's algorithm and the Heap Queue algorithm.
