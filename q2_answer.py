# Principles of Algorithm Design
#
# Final Exam, Question 2
#
# Student Name: Hamed Araab
# Student Number: 9925003


from heapq import heappop, heappush


class TSPSolver:
    def __init__(self, arcs, nodes_count):
        self._arcs = arcs
        self._nodes_count = nodes_count
        self._graph = self._get_graph()
        self._all_min_costs = {node: self._get_min_costs(node) for node in self._graph}

    @property
    def arcs(self):
        return self._arcs

    @property
    def nodes_count(self):
        return self._nodes_count

    @property
    def graph(self):
        return self._graph

    def _get_graph(self):
        """
        Returns a graph using `arcs` and `nodes_count`.

        ### Example:

        Input:

        ```
        arcs = {(1, 2, 1), (3, 1, 1)}
        nodes_count = 3
        ```

        Output:

        ```
        graph = {
            1: {(2, 1), (3, 1)}
            2: {},
            3: {(1, 1)},
        }
        ```
        """

        return {
            node: set(
                (target, cost) for start, target, cost in self._arcs if start == node
            )
            for node in range(1, self._nodes_count + 1)
        }

    def _get_min_costs(self, start_node):
        """
        Returns the minimum cost of traveling from `start_node` to other nodes of the
        `graph` as a `dict`.

        ### Example:

        Input:

        ```
        graph = {
            1: {(2, 1), (3, 3)}
            2: {(3, 1)},
            3: {},
        }

        start_node = 1
        ```

        Output:

        ```
        min_costs = {
            2: 1,
            3: 2,
        }
        ```

        ### Notes:

        - This function uses the Dijkstra and Heap Queue (Priority Queue)
        algorithms.
        """

        min_costs = {
            node: 0.0 if node == start_node else float("inf") for node in self._graph
        }

        visited_nodes = set()
        visiting_queue = [(0.0, start_node)]

        while visiting_queue:
            current_cost, current_node = heappop(visiting_queue)

            if current_node in visited_nodes:
                continue

            for neighbor, cost in self._graph[current_node]:
                new_cost = current_cost + cost

                if new_cost < min_costs[neighbor]:
                    min_costs[neighbor] = new_cost

                    heappush(visiting_queue, (new_cost, neighbor))

            visited_nodes.add(current_node)

        return min_costs

    def get_min_cost_of_tour(self, selected_nodes):
        """
        Returns the minimum cost of touring `selected_nodes`.

        ### Notes:

        - The staring and ending node (aka depot) of the tour is the first node in
        `selected_nodes`.
        """

        def backtrack(current_node, remaining_nodes, total_cost):
            if not remaining_nodes:
                return total_cost + self._all_min_costs[current_node][start_node]

            cost = float("inf")

            for node in remaining_nodes:
                new_cost = backtrack(
                    node,
                    remaining_nodes - {node},
                    total_cost + self._all_min_costs[current_node][node],
                )

                cost = min(cost, new_cost)

            return cost

        start_node = selected_nodes[0]
        remaining_nodes = set(selected_nodes[1:])

        total_cost = backtrack(start_node, remaining_nodes, 0.0)

        if total_cost == float("inf"):
            return -1

        return total_cost


def main():
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


if __name__ == "__main__":
    main()
