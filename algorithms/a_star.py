import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        distance = 0

        for index, tile in enumerate(state.tiles):
            if tile != 0:
                row, col = divmod(index, 3)
                goal_row, goal_col = divmod(tile - 1, 3)

                distance += abs(row - goal_row)
                distance += abs(col - goal_col)

        return distance

    def search(self, initial: State) -> SearchResult:
        frontier = [(initial.cost + self.heuristic(initial), initial)]
        visited = {initial: initial.cost}

        expanded = 0
        generated = 1
        max_frontier = 1

        while frontier:
            priority, current = heapq.heappop(frontier)

            if current.cost > visited[current]:
                continue

            if current.is_goal:
                return SearchResult(
                    current,
                    expanded,
                    generated,
                    max_frontier,
                    len(current.path()) - 1
                )

            expanded += 1

            for neighbor in current.neighbors():

                if neighbor not in visited or neighbor.cost < visited[neighbor]:
                    visited[neighbor] = neighbor.cost

                    priority = neighbor.cost + self.heuristic(neighbor)

                    heapq.heappush(frontier, (priority, neighbor))
                    generated += 1

            max_frontier = max(max_frontier, len(frontier))

        return SearchResult(
            None,
            expanded,
            generated,
            max_frontier
        )
