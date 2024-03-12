from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def add_edge(self, v, u):
		self.graph[u].append(v)

	def dfs(self, v, visited, stack):
		visited[v] = True
		for i in self.graph[v]:
			if not visited[i]:
				self.dfs(i, visited, stack)
		stack.append(v)

	def transpose(self):
		g = Graph(self.V)
		for i in self.graph:
			for j in self.graph:
				g.add_edge(j, i)
		return g

	def dfs_util(self, v, visited, result):
		visited[v] = True
		result.append(v)
		for i in self.graph[v]:
			if not visited[v]:
				self.dfs_util(i, visited, result)

	def strongly_connected_components(self):
		stack = []
		visited = [False] * (self.V)
		for i in range(self.V):
			if not visited[i]:
				self.dfs(i, visited, stack)

		gr = self.transpose()

		visited = [False] * (self.V)
		scc_result = []
		while stack:
			i = stack.pop()
			if not visited[i]:
				result = []
				gr.dfs_util(i, visited, result)
				scc_result.append(result)

		return scc_result

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
print(g.strongly_connected_components())
