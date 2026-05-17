from collections import deque

# ─── Graph setup (neighbor list representation) ───────────────────────────────────────
# This defines a simple network of connected nodes from A to H
NETWORK = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['D'],
    'H': ['E'],
}

# ─── BFS Algorithm ─────────────────────────────────────────────────────────────────────
def bfs_search(graph_data, start_node, target_node):
    """
    BFS method: Checks neighboring nodes level by level outward from the start.
    Uses a first-in-first-out queue. Guarantees the shortest route.

    Parameters:
        graph_data: dictionary with each node's connections
        start_node: where we begin searching from
        target_node: what we're trying to find
    Returns:
        List showing the sequence from start to target, or None if unreachable
    """
    # Store (current_position, route_so_far) in the queue
    waiting_queue = deque([(start_node, [start_node])])
    seen_nodes = set([start_node])

    print(f"\n── Running BFS: looking for {target_node} starting from {start_node} ──")
    print(f"  Initial queue contains: [{start_node}]")

    while waiting_queue:
        current, route = waiting_queue.popleft()  # Remove from front (FIFO behavior)
        print(f"  Currently at: {current}  |  Route taken: {' → '.join(route)}")

        if current == target_node:
            print(f"  Success! Target located!")
            return route

        for next_node in graph_data[current]:
            if next_node not in seen_nodes:
                seen_nodes.add(next_node)
                waiting_queue.append((next_node, route + [next_node]))

    print("  Failed - target not reachable.")
    return None

# ─── DFS Algorithm ─────────────────────────────────────────────────────────────────────
def dfs_search(graph_data, current_node, target_node, route=None, visited_set=None, level=0):
    """
    DFS method: Goes down one branch as far as possible before backing up.
    Uses recursion (stack-like behavior). Does not find the shortest path necessarily.

    Parameters:
        graph_data: dictionary with each node's connections
        current_node: where we are right now in the search
        target_node: what we're trying to find
        route: list of nodes visited up to this point
        visited_set: set tracking which nodes we've already processed
        level: how deep we are in the recursion (just for display)
    Returns:
        List showing the sequence from start to target, or None if unreachable
    """
    if route is None:
        route = [current_node]
        visited_set = set([current_node])
        print(f"\n── Running DFS: looking for {target_node} starting from {current_node} ──")

    spacing = "  " + "  " * level
    print(f"{spacing}Now visiting: {current_node}  |  Route so far: {' → '.join(route)}")

    if current_node == target_node:
        print(f"{spacing}Target acquired!")
        return route

    for adjacent in graph_data[current_node]:
        if adjacent not in visited_set:
            visited_set.add(adjacent)
            outcome = dfs_search(graph_data, adjacent, target_node, route + [adjacent], visited_set, level + 1)
            if outcome:
                return outcome
            print(f"{spacing}  ← Backing up from {adjacent}")

    return None

# ─── Execute both searching methods ────────────────────────────────────────────────────────
if __name__ == "__main__":
    START_POINT = 'A'
    TARGET_POINT = 'H'

    bfs_result = bfs_search(NETWORK, START_POINT, TARGET_POINT)
    dfs_result = dfs_search(NETWORK, START_POINT, TARGET_POINT)

    print("\n" + "="*50)
    print("FINAL RESULTS")
    print("="*50)
    print(f"BFS route (optimal shortest): {' → '.join(bfs_result) if bfs_result else 'Not found'}")
    print(f"DFS route (first path discovered): {' → '.join(dfs_result) if dfs_result else 'Not found'}")