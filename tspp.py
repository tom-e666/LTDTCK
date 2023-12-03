import sys
from typing import List, Tuple


class TravelingSalesman:
    def __init__(self):
        pass

    @staticmethod
    def is_usable_for_tsp(graph: List[List[int]]) -> bool:
        n = len(graph)

        # Check for completeness and non-negative weights
        for i in range(n):
            if len(graph[i]) != n:
                return False  # Graph is not complete

            for j in range(n):
                if i != j and graph[i][j] == -1:
                    return False  # Missing edge, so not complete
                if graph[i][j] < 0:
                    return False  # Negative weight found

        return True  # Graph is complete and has non-negative weights

    @staticmethod
    def find_min_route(tsp: List[List[int]], start: int) -> Tuple[int, List[int]]:
        sum_value = 0
        counter = 0
        j = 0
        i = start
        min_value = sys.maxsize
        visited_route_list = {start: 1}
        route = [0] * len(tsp)

        while i < len(tsp) and j < len(tsp[i]):
            if counter >= len(tsp[i]) - 1:
                break

            if j != i and visited_route_list.get(j, 0) == 0:
                if tsp[i][j] < min_value:
                    min_value = tsp[i][j]
                    route[counter] = j + 1
            j += 1

            if j == len(tsp[i]):
                sum_value += min_value
                min_value = sys.maxsize
                visited_route_list[route[counter] - 1] = 1
                j = 0
                i = route[counter] - 1
                counter += 1

        i = route[counter - 1] - 1

        for j in range(len(tsp)):
            if i != j and tsp[i][j] < min_value:
                min_value = tsp[i][j]
                route[counter] = j + 1

        sum_value += min_value

        return sum_value, route

    @staticmethod
    def solve_tsp(graph: List[List[int]], start: int) -> Tuple[int, List[int]]:
        if TravelingSalesman.is_usable_for_tsp(graph):
            return TravelingSalesman.find_min_route(graph, start)
        else:
            raise ValueError("The graph is not suitable for TSP.")


# Example usage:
if __name__ == "__main__":
    graph_example = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp_solver = TravelingSalesman()
    distance, route = tsp_solver.solve_tsp(graph_example, start=0)

    print(f"Minimum Distance: {distance}")
    print(f"Route: {route}")
