
from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        queue = deque([initial])
        visited = {initial}

        expanded = 0
        generated = 1
        max_frontier = 1

        while queue:
            current = queue.popleft()

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
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    generated += 1

            max_frontier = max(max_frontier, len(queue))

        return SearchResult(
            None,
            expanded,
            generated,
            max_frontier
        )
