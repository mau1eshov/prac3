def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for nxt in reversed(graph[node]):
                stack.append(path + [nxt])

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])

def ucs(graph, start, goal):
    pq = [(0, start, [start])] 
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return cost, path
        if node not in visited:
            visited.add(node)
            for nxt, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, nxt, path + [nxt]))

def a_star(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return g, path
        if node not in visited:
            visited.add(node)
            for nxt, w in graph[node]:
                new_g = g + w
                heapq.heappush(pq, (new_g + h[nxt], new_g, nxt, path+[nxt]))
