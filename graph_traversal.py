from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def bfs(self, start):
		visited = set()
		queue = [start]
		result = []

		while queue:
			vertex = queue.pop(0)
			if vertex not in visited:
				result.append(vertex)
				visited.add(vertex)
				queue.extend(self.graph[vertex])

		return result

	def dfs(self, start):
		visited = set()
		stack = [start]
		result = []

		while stack:
			vertex = stack.pop()
			if vertex not in visited:
				result.append(vertex)
				visited.add(vertex)
				stack.extend(reversed(self.graph))

		return result


# Example usuage

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal:", g.bfs(2))
print("DFS traversal:", g.dfs(2))
