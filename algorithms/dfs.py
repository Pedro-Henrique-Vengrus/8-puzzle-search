
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        stack = [(initial, 0)]
        visited = {initial: 0}

        expanded = 0
        generated = 1
        max_frontier = 1

        while stack:
            current, depth = stack.pop()

            if depth > visited[current]:
                continue

            if current.is_goal:
                return SearchResult(
                    current,
                    expanded,
                    generated,
                    max_frontier,
                    depth
                )

            if depth >= self.depth_limit:
                continue

            expanded += 1

            for neighbor in current.neighbors():
                new_depth = depth + 1

                if neighbor not in visited or new_depth < visited[neighbor]:
                    visited[neighbor] = new_depth
                    stack.append((neighbor, new_depth))
                    generated += 1

            max_frontier = max(max_frontier, len(stack))

        return SearchResult(
            None,
            expanded,
            generated,
            max_frontier
        )
